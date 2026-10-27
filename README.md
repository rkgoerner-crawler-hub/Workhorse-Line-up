# Workhorse Lineup

Lineup, waiver, trade and FAAB help for fantasy football, scored for your own league.
Paste an ESPN or Sleeper league link and the app loads that league's rosters, lineup slots and scoring.

## How it works

- `index.html` is the whole app. It runs in the visitor's browser.
- `app/engine.js` reads a league straight from ESPN or Sleeper and applies that league's scoring.
- `data/shared.json` holds player projections, injuries, weekly stats and kickoff times. A scheduled
  GitHub job (`.github/workflows/refresh-data.yml`) rebuilds it several times a day with `tools/build_shared.py`.
- Nothing is sent anywhere else. Each visitor's league choices and edits stay in their own browser.

## Hosting (free)

The site is plain files, so GitHub Pages hosts it for free:

1. Settings → Pages → Build and deployment → Source: **Deploy from a branch**, Branch: **main**, folder **/ (root)**. Save.
2. Actions tab → enable workflows if asked → **Refresh player data** → **Run workflow** once.
3. The site appears at `https://YOUR-USERNAME.github.io/REPO-NAME/` within a few minutes.

## Sharing a league

In the app, Settings → **Copy a link for your league mates**. Anyone who opens that link gets the league loaded
and picks their team.

## League requirements

- **ESPN:** the league must be viewable to the public (League → Settings → Edit Settings → Basic Settings →
  Make League Viewable to Public). This only lets people see rosters and scores.
- **Sleeper:** works as is.
- Superflex and other special lineup slots are flagged but not handled yet.
