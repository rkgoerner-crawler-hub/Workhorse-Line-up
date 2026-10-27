"""Build data/shared.json: the part of Workhorse Lineup's data that is the same for every league.

Players (from Sleeper), their raw projected stat lines for the rest of the season, their actual stat lines for
finished weeks, injury statuses, trending adds, and this week's kickoff times (from ESPN's public NFL schedule).
Points are NOT computed here: each league's own scoring is applied in the browser.

Usage:  python3 -I tools/build_shared.py --out data/shared.json --work /tmp/whl [--skip-download]

Downloaded files are untrusted data: they are only parsed as JSON. The script exits non-zero and writes nothing
if a safety check fails, so a bad pull never replaces the last good file.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta

SEASON = 2026
LAST_WEEK = 17
SLEEPER = "https://api.sleeper.app"
ESPN_SCHED = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/%d?view=proTeamSchedules_wl" % SEASON
POSITIONS = "position[]=QB&position[]=RB&position[]=WR&position[]=TE&position[]=K&position[]=DEF"

STATUS = {"Questionable": "questionable", "Doubtful": "doubtful", "Out": "out", "IR": "ir", "PUP": "ir", "DNR": "out"}
POSMAP = {"QB": "QB", "RB": "RB", "WR": "WR", "TE": "TE", "K": "K", "DEF": "DST"}

# Stat fields that never score in any league (snap counts, lengths, rates, splits); everything else is kept.
DROP_PREFIX = ("adp", "pos_adp", "pos_rank", "rank_", "fan_pts", "h1_", "q1_", "idp_", "tkl", "tm_")
DROP_SUFFIX = ("_lng", "_pct", "_ypa", "_ypc", "_ypr", "_ypt", "_snp", "_rtg", "_air_yd", "_yar")
DROP = {"pts_ppr", "pts_half_ppr", "pts_std", "cmp_pct", "gs", "penalty", "penalty_yd", "off_snp", "def_snp", "st_snp",
        "pass_rz_att", "rec_rz_tgt", "rush_rz_att", "anytime_tds", "first_td", "kick_pts"}


def keep_field(k):
    return k not in DROP and not k.startswith(DROP_PREFIX) and not k.endswith(DROP_SUFFIX)


def fetch(url, path):
    for _ in range(3):
        r = subprocess.run(["curl", "-sSf", "-m", "120", "-o", path, url], capture_output=True, text=True)
        if r.returncode == 0:
            return
    sys.exit("download failed: %s (%s)" % (url, r.stderr.strip()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--skip-download", action="store_true")
    a = ap.parse_args()
    data = os.path.join(a.work, "data")
    os.makedirs(data, exist_ok=True)
    P = lambda name: os.path.join(data, name)

    if not a.skip_download:
        fetch(SLEEPER + "/v1/state/nfl", P("state.json"))
    week = int(json.load(open(P("state.json"))).get("week") or 1)
    weeks = list(range(week, max(week, LAST_WEEK) + 1))
    past = list(range(1, week))
    if not a.skip_download:
        fetch(SLEEPER + "/v1/players/nfl", P("players.json"))
        for w in weeks + past:
            fetch(SLEEPER + "/projections/nfl/%d/%d?season_type=regular&%s" % (SEASON, w, POSITIONS), P("proj_w%d.json" % w))
        for w in past:
            fetch(SLEEPER + "/stats/nfl/%d/%d?season_type=regular&%s" % (SEASON, w, POSITIONS), P("stats_w%d.json" % w))
        fetch(SLEEPER + "/v1/players/nfl/trending/add?lookback_hours=72&limit=60", P("trending.json"))
        fetch(ESPN_SCHED, P("schedule.json"))

    players = json.load(open(P("players.json")))

    # NFL schedule from ESPN: bye weeks and kickoff times (ms since epoch) for every week.
    sched = json.load(open(P("schedule.json")))
    byes, kick = {}, {}
    for x in sched.get("settings", {}).get("proTeams", []):
        abbr = x.get("abbrev", "").upper().replace("WSH", "WAS")
        if abbr == "FA" or not abbr:
            continue
        byes[abbr] = x.get("byeWeek")
        for w, games in (x.get("proGamesByScoringPeriod") or {}).items():
            if games:
                kick.setdefault(w, {})[abbr] = games[0]["date"]
    problems = []
    if len(byes) != 32:
        problems.append("expected 32 NFL teams in the schedule, got %d" % len(byes))

    def load_lines(name):
        out = {}
        for r in json.load(open(P(name))):
            s = r.get("stats") or {}
            p = players.get(r["player_id"])
            if s and p and p.get("position") in POSMAP:
                out[r["player_id"]] = s
        return out

    proj = {w: load_lines("proj_w%d.json" % w) for w in weeks}
    pproj = {w: load_lines("proj_w%d.json" % w) for w in past}
    stats = {w: load_lines("stats_w%d.json" % w) for w in past}

    # Who to include: anyone with a projection or a game played this season, plus injured players (so they can be found).
    ids = set()
    for d in list(proj.values()) + list(stats.values()):
        ids.update(d)
    for pid, p in players.items():
        if POSMAP.get(p.get("position")) in ("QB", "RB", "WR", "TE") and STATUS.get(p.get("injury_status")) in ("ir", "out", "doubtful") \
                and p.get("team") in byes and p.get("status") == "Inactive":
            ids.add(pid)

    fields, fidx = [], {}

    def enc(s):
        # Sparse line: [fieldIndex, value, fieldIndex, value, ...], zeros dropped.
        out = []
        for k, v in s.items():
            if not isinstance(v, (int, float)) or not v or not keep_field(k):
                continue
            if k not in fidx:
                fidx[k] = len(fields)
                fields.append(k)
            out += [fidx[k], round(float(v), 2)]
        return out

    rows, seen = [], set()
    for pid in ids:
        p = players[pid]
        pos = POSMAP[p["position"]]
        team = p.get("team") or (pid if pos == "DST" else None)
        if team not in byes:
            continue
        name = ((p.get("last_name") or team) + " D/ST") if pos == "DST" else (p.get("full_name") or ((p.get("first_name") or "") + " " + (p.get("last_name") or "")).strip())
        if (name, team) in seen:
            continue
        pj = [enc(proj[w][pid]) if pid in proj[w] else 0 for w in weeks]
        pts_hint = max([float((proj[w].get(pid) or {}).get("pts_ppr") or 0) for w in weeks] + [0])
        status = STATUS.get(p.get("injury_status"), "healthy")
        if pos not in ("K", "DST") and pts_hint < 1.0 and status not in ("ir", "out") and not any(pid in stats[w] for w in past):
            continue
        seen.add((name, team))
        rows.append({
            "r": [name, pos, team, byes[team], status, (p.get("injury_body_part") or "") if status != "healthy" else "", pid],
            "p": pj,
            "pp": [enc(pproj[w][pid]) if pid in pproj[w] else 0 for w in past],
            "s": [enc(stats[w][pid]) if pid in stats[w] else 0 for w in past],
            "o": pts_hint,
        })
    order = {"QB": 0, "RB": 1, "WR": 2, "TE": 3, "K": 4, "DST": 5}
    rows.sort(key=lambda x: (order[x["r"][1]], -x["o"]))

    counts = {}
    for x in rows:
        counts[x["r"][1]] = counts.get(x["r"][1], 0) + 1
    if len(rows) < 300 or counts.get("QB", 0) < 28 or counts.get("DST", 0) < 28 or counts.get("K", 0) < 25:
        problems.append("too few players: %d %s" % (len(rows), counts))
    for team, b in byes.items():
        missing = [w for w in weeks if not any(x["r"][2] == team and x["p"][i] for x in rows for i in [weeks.index(w)])]
        want = [b] if b in weeks else []
        if missing != want:
            problems.append("bye check %s: expected %s, projections missing %s" % (team, want, missing))

    trending = {}
    keys = {(x["r"][0], x["r"][2]) for x in rows}
    for t in json.load(open(P("trending.json"))):
        p = players.get(t["player_id"])
        if not p:
            continue
        pos = POSMAP.get(p.get("position"))
        team = p.get("team")
        name = ((p.get("last_name") or team) + " D/ST") if pos == "DST" else p.get("full_name")
        if (name, team) in keys:
            trending[name + "|" + team] = int(t["count"])

    now = datetime.now(timezone(timedelta(hours=-4)))
    shared = {
        "version": now.isoformat(timespec="minutes"), "asOf": now.strftime("%b %-d, %Y %-I:%M %p ET"),
        "season": SEASON, "week": week, "weeks": weeks, "past": past, "byes": byes, "kickoffs": kick,
        "fields": fields, "players": [x["r"] for x in rows], "proj": [x["p"] for x in rows],
        "pastProj": [x["pp"] for x in rows], "stats": [x["s"] for x in rows], "trending": trending,
    }
    print(json.dumps({"week": week, "players": len(rows), "byPos": counts, "fields": len(fields), "trending": len(trending), "problems": problems}, indent=1))
    if problems:
        sys.exit("stopped: safety checks failed, shared.json not written")
    tmp = a.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(shared, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, a.out)
    print("wrote", a.out, os.path.getsize(a.out), "bytes")


if __name__ == "__main__":
    main()
