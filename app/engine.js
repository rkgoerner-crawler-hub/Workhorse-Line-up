/* Workhorse Lineup league engine.
 *
 * Runs in the visitor's browser: loads the shared player data (data/shared.json), fetches the visitor's league
 * straight from ESPN or Sleeper, applies that league's own scoring, and builds the DB object the app renders.
 * Ported from the Python refresh pipeline; both scorers were checked against the sites' recorded points
 * (ESPN 162 of 163 player-weeks exact, Sleeper 720 of 720).
 */
(function (root) {
  'use strict';

  const ESPN_BASE = 'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/';
  const SLEEPER_BASE = 'https://api.sleeper.app/v1/league/';

  // ---------- league links ----------
  // Accepts an ESPN or Sleeper league URL, or a bare ID (ESPN IDs are short, Sleeper IDs are 15+ digits).
  function parseLeagueLink(text) {
    const t = String(text || '').trim();
    let m = t.match(/leagueId=(\d+)/i);
    if (m && /espn/i.test(t)) return { platform: 'espn', id: m[1] };
    m = t.match(/sleeper\.(?:com|app)\/leagues\/(\d+)/i);
    if (m) return { platform: 'sleeper', id: m[1] };
    m = t.match(/leagueId=(\d+)/i);
    if (m) return { platform: 'espn', id: m[1] };
    m = t.match(/^\d+$/);
    if (m) return t.length >= 15 ? { platform: 'sleeper', id: t } : { platform: 'espn', id: t };
    return null;
  }

  // ---------- helpers ----------
  const norm = n => String(n || '').toLowerCase().replace(/-/g, ' ').replace(/[^a-z ]/g, '').split(/\s+/)
    .filter(w => w && !['jr', 'sr', 'ii', 'iii', 'iv', 'v'].includes(w)).join(' ');
  const r2 = v => Math.round(v * 100) / 100;
  const g = (s, k) => Number(s[k]) || 0;
  function decode(fields, line) {
    const s = {};
    if (!line) return s;
    for (let i = 0; i < line.length; i += 2) s[fields[line[i]]] = line[i + 1];
    return s;
  }
  const ncdf = (x, mean, sd) => 0.5 * (1 + erf((x - mean) / (sd * Math.SQRT2)));
  function erf(x) { // Abramowitz-Stegun 7.1.26, |error| < 1.5e-7
    const sgn = x < 0 ? -1 : 1; x = Math.abs(x);
    const t = 1 / (1 + 0.3275911 * x);
    const y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x);
    return sgn * y;
  }
  function pRange(mean, sd, lo, hi, exact) {
    if (exact != null) return lo <= exact && exact <= hi ? 1 : 0;
    if (mean <= 0 && lo > 0) return 0;
    const a = lo <= 0 ? 0 : ncdf(lo - 0.5, mean, sd);
    return Math.max(0, ncdf(hi + 0.5, mean, sd) - a);
  }

  // ---------- ESPN scoring (stat IDs matched to Sleeper fields from real games) ----------
  const ESPN_POS_ID = { QB: 1, RB: 2, WR: 3, TE: 4, K: 5, DST: 16 };
  const E_DIRECT = { 0: 'pass_att', 1: 'pass_cmp', 2: 'pass_inc', 3: 'pass_yd', 4: 'pass_td', 19: 'pass_2pt', 20: 'pass_int', 64: 'pass_sack',
    23: 'rush_att', 24: 'rush_yd', 25: 'rush_td', 26: 'rush_2pt', 41: 'rec', 53: 'rec', 42: 'rec_yd', 43: 'rec_td', 44: 'rec_2pt', 58: 'rec_tgt',
    68: 'fum', 72: 'fum_lost', 83: 'fgm', 84: 'fga', 85: 'fgmiss', 86: 'xpm', 87: 'xpa', 88: 'xpmiss', 74: 'fgm_50p', 77: 'fgm_40_49', 79: 'fgmiss_40_49',
    95: 'int', 96: 'fum_rec', 97: 'blk_kick', 98: 'safe', 99: 'sack' };
  const E_PER = { 5: ['pass_yd', 5], 6: ['pass_yd', 10], 7: ['pass_yd', 20], 8: ['pass_yd', 25], 9: ['pass_yd', 50], 10: ['pass_yd', 100],
    27: ['rush_yd', 5], 28: ['rush_yd', 10], 29: ['rush_yd', 20], 30: ['rush_yd', 25], 31: ['rush_yd', 50], 32: ['rush_yd', 100],
    47: ['rec_yd', 5], 48: ['rec_yd', 10], 49: ['rec_yd', 20], 50: ['rec_yd', 25], 51: ['rec_yd', 50], 52: ['rec_yd', 100] };
  const E_BONUS = { 17: ['pass_yd', 300, 399, 70], 18: ['pass_yd', 400, 9999, 70], 37: ['rush_yd', 100, 199, 0], 38: ['rush_yd', 200, 9999, 0],
    56: ['rec_yd', 100, 199, 0], 57: ['rec_yd', 200, 9999, 0] };
  const E_PA = { 89: [0, 0], 90: [1, 6], 91: [7, 13], 92: [14, 17], 121: [18, 21], 122: [22, 27], 123: [28, 34], 124: [35, 45], 125: [46, 999] };
  const E_YA = { 128: [0, 99], 129: [100, 199], 130: [200, 299], 131: [300, 349], 132: [350, 399], 133: [400, 449], 134: [450, 499], 135: [500, 549], 136: [550, 9999] };
  function espnItemPoints(items, pos) {
    const key = String(ESPN_POS_ID[pos]), out = {};
    items.forEach(it => {
      const o = it.pointsOverrides || {};
      const pts = Object.prototype.hasOwnProperty.call(o, key) ? o[key] : it.points || 0;
      if (pts) out[Number(it.statId)] = Number(pts);
    });
    return out;
  }
  function espnScore(itemPts, pos, s, exact, withCarries) {
    let total = 0;
    for (const k in itemPts) {
      const sid = Number(k), pts = itemPts[k];
      if (sid === 23 && !withCarries) continue;
      let v = null;
      if (sid === 106) v = g(s, 'ff') + g(s, 'def_st_ff');
      else if (E_DIRECT[sid]) v = g(s, E_DIRECT[sid]);
      else if (E_PER[sid]) { const [f, n] = E_PER[sid]; v = exact ? Math.floor(g(s, f) / n) : g(s, f) / n; }
      else if (E_BONUS[sid]) { const [f, lo, hi, sd] = E_BONUS[sid]; const m = g(s, f); v = pRange(m, sd || Math.max(15, 0.45 * m), lo, hi, exact ? m : null); }
      else if (sid === 80) v = g(s, 'fgm_0_19') + g(s, 'fgm_20_29') + g(s, 'fgm_30_39');
      else if (sid === 82) v = g(s, 'fgmiss_0_19') + g(s, 'fgmiss_20_29') + g(s, 'fgmiss_30_39');
      else if (sid === 76 || sid === 200) v = g(s, 'fgmiss_50p');
      else if (sid === 198) v = g(s, 'fgm_50p');
      else if (E_PA[sid] && pos === 'DST' && 'pts_allow' in s) { const [lo, hi] = E_PA[sid]; v = pRange(g(s, 'pts_allow'), 9.5, lo, hi, exact ? g(s, 'pts_allow') : null); }
      else if (E_YA[sid] && pos === 'DST' && 'yds_allow' in s) { const [lo, hi] = E_YA[sid]; v = pRange(g(s, 'yds_allow'), 65, lo, hi, exact ? g(s, 'yds_allow') : null); }
      else if (sid === 93 && pos === 'DST') v = g(s, 'def_td');
      else if (sid === 101 && pos === 'DST') v = g(s, 'def_st_td');
      if (v) total += pts * v;
    }
    return total;
  }

  // ---------- Sleeper scoring (scoring_settings use Sleeper's own stat names) ----------
  const DEF_ONLY = new Set(['sack', 'int', 'ff', 'fum_rec', 'safe', 'blk_kick', 'def_td', 'def_st_td', 'def_st_ff', 'def_st_fum_rec',
    'def_2pt', 'def_pass_def', 'tkl_loss', 'qb_hit', 'def_4_and_stop', 'def_3_and_out', 'def_forced_punts']);
  const SL_PA = { pts_allow_0: [0, 0], pts_allow_1_6: [1, 6], pts_allow_7_13: [7, 13], pts_allow_14_20: [14, 20], pts_allow_21_27: [21, 27], pts_allow_28_34: [28, 34], pts_allow_35p: [35, 999] };
  const SL_YA = { yds_allow_0_100: [0, 99], yds_allow_100_199: [100, 199], yds_allow_200_299: [200, 299], yds_allow_300_349: [300, 349], yds_allow_350_399: [350, 399],
    yds_allow_400_449: [400, 449], yds_allow_450_499: [450, 499], yds_allow_500_549: [500, 549], yds_allow_550p: [550, 9999] };
  const POS_BONUS = { bonus_rec_rb: ['RB', 'rec'], bonus_rec_wr: ['WR', 'rec'], bonus_rec_te: ['TE', 'rec'] };
  function sleeperScore(sc, pos, s, exact, withCarries) {
    let total = 0;
    for (const k in sc) {
      const v = Number(sc[k]);
      if (!v || (k === 'rush_att' && !withCarries)) continue;
      if (SL_PA[k] || SL_YA[k]) {
        if (pos !== 'DST') continue;
        const [lo, hi] = SL_PA[k] || SL_YA[k];
        if (exact) total += v * g(s, k);
        else { const f = SL_PA[k] ? 'pts_allow' : 'yds_allow', sd = SL_PA[k] ? 9.5 : 65; if (f in s) total += v * pRange(g(s, f), sd, lo, hi, null); }
        continue;
      }
      if (DEF_ONLY.has(k) && pos !== 'DST') continue;
      if (POS_BONUS[k]) { const [p, f] = POS_BONUS[k]; if (pos === p) total += v * g(s, f); continue; }
      if (k === 'fgm_50_59' && !('fgm_50_59' in s)) { total += v * Math.max(0, g(s, 'fgm_50p') - g(s, 'fgm_60p')); continue; }
      total += v * g(s, k);
    }
    return total;
  }

  // ---------- fetching ----------
  async function getJson(url, fetchImpl) {
    const res = await (fetchImpl || fetch)(url, { credentials: 'omit' });
    if (!res.ok) {
      const err = new Error('HTTP ' + res.status + ' for ' + url);
      err.status = res.status;
      try { err.body = await res.json(); } catch (e) { /* not json */ }
      throw err;
    }
    return res.json();
  }

  async function fetchLeague(link, week, opts = {}) {
    const f = opts.fetch;
    const season = opts.season || 2026;
    const boxWeeks = opts.boxWeeks || [week - 1, week].filter(w => w >= 1);
    if (link.platform === 'espn') {
      const base = ESPN_BASE + season + '/segments/0/leagues/' + link.id;
      let league;
      try { league = await getJson(base + '?view=mTeam&view=mRoster&view=mSettings', f); }
      catch (e) {
        if (e.status === 401 || (e.body && JSON.stringify(e.body).includes('AUTH_LEAGUE_NOT_VISIBLE'))) {
          const err = new Error('This ESPN league is private.'); err.code = 'private'; throw err;
        }
        if (e.status === 404) { const err = new Error('No ESPN league with that ID.'); err.code = 'notfound'; throw err; }
        throw e;
      }
      const box = {}, tx = {};
      await Promise.all(boxWeeks.map(async w => {
        box[w] = await getJson(base + '?view=mBoxscore&view=mMatchupScore&scoringPeriodId=' + w, f).catch(() => null);
      }));
      if ((league.settings && league.settings.acquisitionSettings || {}).isUsingAcquisitionBudget) {
        await Promise.all((opts.txWeeks || boxWeeks).map(async w => { tx[w] = await getJson(base + '?view=mTransactions2&scoringPeriodId=' + w, f).catch(() => null); }));
      }
      return { platform: 'espn', id: link.id, league, box, tx };
    }
    const base = SLEEPER_BASE + link.id;
    const league = await getJson(base, f).catch(() => null);
    if (!league || !league.scoring_settings) { const err = new Error('No Sleeper league with that ID.'); err.code = 'notfound'; throw err; }
    const [rosters, users] = await Promise.all([getJson(base + '/rosters', f), getJson(base + '/users', f)]);
    const allWeeks = Array.from({ length: week }, (_, i) => i + 1);
    const box = {}, tx = {};
    await Promise.all(allWeeks.map(async w => {
      box[w] = await getJson(base + '/matchups/' + w, f).catch(() => null);
      tx[w] = await getJson(base + '/transactions/' + w, f).catch(() => null);
    }));
    return { platform: 'sleeper', id: link.id, league, rosters, users, box, tx };
  }

  // ---------- building the app's DB ----------
  const EPOS = { 1: 'QB', 2: 'RB', 3: 'WR', 4: 'TE', 5: 'K', 16: 'DST' };
  const PRO = { 1: 'ATL', 2: 'BUF', 3: 'CHI', 4: 'CIN', 5: 'CLE', 6: 'DAL', 7: 'DEN', 8: 'DET', 9: 'GB', 10: 'TEN', 11: 'IND', 12: 'KC', 13: 'LV', 14: 'LAR',
    15: 'MIA', 16: 'MIN', 17: 'NE', 18: 'NO', 19: 'NYG', 20: 'NYJ', 21: 'PHI', 22: 'ARI', 23: 'PIT', 24: 'LAC', 25: 'SF', 26: 'SEA', 27: 'TB', 28: 'WAS', 29: 'CAR', 30: 'JAX', 33: 'BAL', 34: 'HOU' };
  const ESTAT = { QUESTIONABLE: 'questionable', DAY_TO_DAY: 'questionable', DOUBTFUL: 'doubtful', OUT: 'out', INJURY_RESERVE: 'ir' };
  const SLSTAT = { Questionable: 'questionable', Doubtful: 'doubtful', Out: 'out', IR: 'ir', PUP: 'ir', DNR: 'out' };
  const KEEP = { QB: ['pass_yd', 'pass_td', 'pass_int', 'rush_att', 'rush_yd', 'rush_td'], RB: ['rush_att', 'rush_yd', 'rush_td', 'rec_tgt', 'rec', 'rec_yd', 'rec_td'],
    WR: ['rec_tgt', 'rec', 'rec_yd', 'rec_td', 'rush_att', 'rush_yd'], TE: ['rec_tgt', 'rec', 'rec_yd', 'rec_td'], K: ['fgm', 'fga', 'xpm'],
    DST: ['sack', 'int', 'fum_rec', 'def_td', 'pts_allow'] };

  function buildDB(shared, raw) {
    const week = shared.week;
    const F = shared.fields;
    let scorer, carry, slots, bench, recPts, ptd, name, id, bestBall = false, noAdds = false, noTrades = false;
    const unsupported = {};
    if (raw.platform === 'espn') {
      const st = raw.league.settings || {};
      const items = (st.scoringSettings || {}).scoringItems || [];
      const posItems = {};
      ['QB', 'RB', 'WR', 'TE', 'K', 'DST'].forEach(p => { posItems[p] = espnItemPoints(items, p); });
      scorer = (pos, s, exact, wc) => espnScore(posItems[pos], pos, s, exact, wc);
      carry = {};
      ['QB', 'RB', 'WR', 'TE'].forEach(p => { if (posItems[p][23]) carry[p] = posItems[p][23]; });
      const counts = {};
      Object.entries((st.rosterSettings || {}).lineupSlotCounts || {}).forEach(([k, v]) => { if (v) counts[Number(k)] = v; });
      const SLOTMAP = { 0: 'QB', 2: 'RB', 4: 'WR', 6: 'TE', 23: 'FLEX', 17: 'K', 16: 'DST' };
      slots = {};
      Object.entries(SLOTMAP).forEach(([sid, n]) => { slots[n] = counts[sid] || 0; });
      Object.entries(counts).forEach(([sid, n]) => { if (!SLOTMAP[sid] && sid !== '20' && sid !== '21') unsupported[sid] = n; });
      bench = counts[20] || 0;
      recPts = posItems.WR[53] || posItems.WR[41] || 0;
      ptd = posItems.QB[4] || 0;
      name = (st.name || '').trim();
      id = raw.league.id;
    } else {
      const lg = raw.league, st = lg.settings || {}, sc = lg.scoring_settings || {};
      scorer = (pos, s, exact, wc) => sleeperScore(sc, pos, s, exact, wc);
      carry = {};
      if (Number(sc.rush_att)) ['QB', 'RB', 'WR', 'TE'].forEach(p => { carry[p] = Number(sc.rush_att); });
      const SMAP = { QB: 'QB', RB: 'RB', WR: 'WR', TE: 'TE', FLEX: 'FLEX', K: 'K', DEF: 'DST' };
      slots = { QB: 0, RB: 0, WR: 0, TE: 0, FLEX: 0, K: 0, DST: 0 };
      (lg.roster_positions || []).forEach(x => {
        if (SMAP[x]) slots[SMAP[x]]++;
        else if (!['BN', 'IR', 'TAXI'].includes(x)) unsupported[x] = (unsupported[x] || 0) + 1;
      });
      bench = (lg.roster_positions || []).filter(x => x === 'BN').length;
      recPts = Number(sc.rec) || 0;
      ptd = Number(sc.pass_td) || 0;
      name = (lg.name || '').trim();
      id = lg.league_id;
      bestBall = !!st.best_ball;
      noAdds = !!st.disable_adds;
      noTrades = !!st.disable_trades;
    }
    const label = [recPts === 1 ? 'PPR' : recPts === 0.5 ? 'Half PPR' : recPts ? recPts + ' per catch' : 'Standard'];
    if (ptd && ptd !== 4) label.push(ptd + '-pt pass TD');
    const cv = Object.values(carry);
    if (cv.length === 4 && new Set(cv).size === 1) label.push(cv[0] + ' per carry');
    else Object.entries(carry).forEach(([p, v]) => label.push(v + ' per ' + p + ' carry'));
    if (bestBall) label.push('best ball');

    // Players, scored for this league.
    const players = [], season = {}, keyOfPid = {}, byNP = {};
    shared.players.forEach((r, i) => {
      const [nm, pos, team, bye, status, injury, pid] = r;
      const lines = shared.proj[i].map(l => decode(F, l));
      const pts = lines.map(s => (Object.keys(s).length ? r2(scorer(pos, s, false, false)) : 0));
      const att = lines.map(s => Math.round(g(s, 'rush_att') * 10) / 10);
      players.push([nm, pos, team, bye, status, injury, pts, att]);
      const key = nm + '|' + team;
      keyOfPid[pid] = key;
      (byNP[norm(nm) + '|' + pos] = byNP[norm(nm) + '|' + pos] || []).push(key);
      let gp = 0;
      const wk = [], tot = {};
      shared.stats[i].forEach(l => {
        const s = decode(F, l);
        if (!l || !(s.gp || s.gms_active || Object.keys(s).length)) { wk.push(null); return; }
        gp++;
        wk.push(Math.round(scorer(pos, s, true, true) * 10) / 10);
        KEEP[pos].forEach(k => { tot[k] = (tot[k] || 0) + g(s, k); });
      });
      if (gp) {
        Object.keys(tot).forEach(k => { tot[k] = Math.round(tot[k] * 10) / 10; });
        season[key] = { pts: wk, gp, st: tot };
      }
    });
    const pastProjOf = {};
    shared.players.forEach((r, i) => { pastProjOf[r[6]] = (shared.pastProj[i] || []).map(l => (l ? r2(scorer(r[1], decode(F, l), false, false)) : null)); });
    const matchESPN = (fullName, pos) => { const m = byNP[norm(fullName) + '|' + pos] || []; return m.length === 1 ? m[0] : ''; };

    // League: teams, rosters, box scores, FAAB.
    const teams = {}, rostered = {}, rosters = {}, standings = {}, box = {};
    const unmatched = [];
    let faab = null;
    if (raw.platform === 'espn') {
      const lg = raw.league;
      (lg.teams || []).forEach(t => {
        teams[t.id] = (t.name || '').trim() || 'Team ' + t.id;
        const rows = [];
        ((t.roster || {}).entries || []).forEach(e => {
          const p = e.playerPoolEntry.player, pos = EPOS[p.defaultPositionId];
          if (!pos) return;
          const key = matchESPN(p.fullName, pos);
          if (key) rostered[key] = t.id; else unmatched.push(p.fullName);
          const pj = (p.stats || []).filter(x => x.statSourceId === 1 && x.statSplitTypeId === 1 && x.scoringPeriodId === week).map(x => x.appliedTotal || 0);
          rows.push([key, p.fullName, pos, PRO[p.proTeamId] || '', e.lineupSlotId, pj.length ? r2(pj[0]) : null, ESTAT[p.injuryStatus] || 'healthy']);
        });
        rosters[t.id] = rows;
        const rec = (t.record || {}).overall || {};
        standings[t.id] = { w: rec.wins || 0, l: rec.losses || 0, t: rec.ties || 0, pf: r2(rec.pointsFor || 0) };
      });
      Object.entries(raw.box || {}).forEach(([w, bd]) => {
        if (!bd) return;
        w = Number(w);
        const wk = {};
        (bd.schedule || []).forEach(m => {
          if (m.matchupPeriodId !== w) return;
          ['home', 'away'].forEach(side => {
            const t = m[side];
            if (!t) return;
            const rows = [];
            (((t.rosterForCurrentScoringPeriod || {}).entries) || []).forEach(e => {
              const p = e.playerPoolEntry.player, pos = EPOS[p.defaultPositionId];
              if (!pos) return;
              const st = {};
              (p.stats || []).forEach(x => { if (x.statSplitTypeId === 1 && x.scoringPeriodId === w) st[x.statSourceId] = x; });
              const pj = st[1] ? st[1].appliedTotal : null, ac = st[0] ? st[0].appliedTotal : null;
              rows.push([matchESPN(p.fullName, pos), p.fullName, pos, PRO[p.proTeamId] || '', e.lineupSlotId,
                pj != null ? r2(pj) : null, ac != null ? r2(ac) : null, ESTAT[p.injuryStatus] || 'healthy']);
            });
            wk[t.teamId] = rows;
          });
        });
        box[w] = wk;
      });
      const acq = (lg.settings || {}).acquisitionSettings || {};
      if (acq.isUsingAcquisitionBudget) {
        const bids = [];
        Object.values(raw.tx || {}).forEach(d => ((d && d.transactions) || []).forEach(t => {
          if (t.type === 'WAIVER' && t.status === 'EXECUTED' && t.bidAmount != null) bids.push(Number(t.bidAmount));
        }));
        const spent = {};
        (lg.teams || []).forEach(t => { spent[t.id] = (t.transactionCounter || {}).acquisitionBudgetSpent || 0; });
        faab = { budget: acq.acquisitionBudget || 100, minBid: acq.minimumBid || 0, spent, bids: bids.sort((a, b) => a - b) };
      }
    } else {
      const users = {};
      (raw.users || []).forEach(u => { users[u.user_id] = u; });
      const pinfo = {};
      shared.players.forEach(r => { pinfo[r[6]] = r; });
      const slRow = pid => {
        const r = pinfo[pid];
        if (!r) return null;
        return [keyOfPid[pid] || '', r[0], r[1], r[2], r[4]];
      };
      (raw.rosters || []).forEach(ro => {
        const rid = ro.roster_id, u = users[ro.owner_id] || {};
        teams[rid] = (((u.metadata || {}).team_name) || u.display_name || 'Team ' + rid).trim();
        const ss = ro.settings || {};
        standings[rid] = { w: ss.wins || 0, l: ss.losses || 0, t: ss.ties || 0, pf: r2((ss.fpts || 0) + (ss.fpts_decimal || 0) / 100) };
        const starters = new Set(ro.starters || []), reserve = new Set(ro.reserve || []);
        rosters[rid] = (ro.players || []).map(pid => {
          const x = slRow(pid);
          if (!x) { unmatched.push(pid); return null; }
          if (x[0]) rostered[x[0]] = rid;
          return [x[0], x[1], x[2], x[3], reserve.has(pid) ? 21 : starters.has(pid) ? 0 : 20, null, x[4]];
        }).filter(Boolean);
      });
      Object.entries(raw.box || {}).forEach(([w, ms]) => {
        if (!ms) return;
        w = Number(w);
        const wk = {};
        ms.forEach(m => {
          const starters = new Set(m.starters || []), pp = m.players_points || {};
          wk[m.roster_id] = (m.players || []).map(pid => {
            const x = slRow(pid);
            if (!x) return null;
            const idx = shared.players.findIndex(r => r[6] === pid);
            let pj = null;
            if (w < week) pj = (pastProjOf[pid] || [])[w - 1];
            else if (idx >= 0) pj = players[idx][6][shared.weeks.indexOf(w)];
            let ac = pp[pid];
            if (w === week && !ac) ac = null;
            return [x[0], x[1], x[2], x[3], starters.has(pid) ? 0 : 20, pj != null ? r2(pj) : null, ac != null ? r2(ac) : null, x[4]];
          }).filter(Boolean);
        });
        box[w] = wk;
      });
      const st = raw.league.settings || {};
      if (st.waiver_type === 2) {
        const bids = [];
        Object.values(raw.tx || {}).forEach(list => (list || []).forEach(t => {
          if (t.type === 'waiver' && t.status === 'complete') bids.push(Number((t.settings || {}).waiver_bid) || 0);
        }));
        const spent = {};
        (raw.rosters || []).forEach(ro => { spent[ro.roster_id] = (ro.settings || {}).waiver_budget_used || 0; });
        faab = { budget: st.waiver_budget || 100, minBid: 0, spent, bids: bids.sort((a, b) => a - b) };
      }
    }

    const teamIds = Object.keys(teams).map(Number);
    const now = new Date();
    const league = {
      name, id, platform: raw.platform, bestBall, noAdds, noTrades, standings, myTeam: teamIds.length ? Math.min(...teamIds) : 1,
      teams, size: teamIds.length, slots, rosterSize: Object.values(slots).reduce((a, b) => a + b, 0) + bench, carry,
      scoringLabel: label.join(' · '), rostered, rosters, box, faab, week,
      asOf: now.toLocaleString('en-US', { timeZone: 'America/New_York', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }) + ' ET',
      unsupported, unmatched
    };
    return {
      week, weeks: shared.weeks, asOf: shared.asOf, version: shared.version, players, trending: shared.trending || {},
      league, kickoffs: (shared.kickoffs || {})[String(week)] || {}, season: { weeks: shared.past, players: season }, picks: {}
    };
  }

  root.WorkhorseEngine = { parseLeagueLink, fetchLeague, buildDB, espnScore, espnItemPoints, sleeperScore, decode, norm };
})(typeof window !== 'undefined' ? window : globalThis);
