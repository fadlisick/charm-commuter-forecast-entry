# charm-commuter-forecast-entry

[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/fadlisick/charm-commuter-forecast-entry/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/fadlisick/charm-commuter-forecast-entry/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather forecast, at most 140 characters, for a city that does not exist: name the place, give it weather, and make a bored commuter smile on the way to work. The entry is that single short text, written by `main.py` to `entry.txt`.

> Grumbletown: drizzle till ten, then 21°C and a warm breeze smelling of fresh bread. Visibility high; even the traffic lights are green.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

No dependencies beyond the Python 3 standard library. The program honours `MAKEFUN_OUTPUT_DIR` and defaults to `/output`.
