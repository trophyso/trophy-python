# Trophy Python SDK

The Trophy Python SDK provides convenient access to the Trophy API from applications written in the
Python language.

Trophy is the 1:1 customer engagement platform for consumer web and mobile apps. AI lifecycle
marketing agents write and send personalized email and push to every user, alongside in-app
experiences like milestones, streaks, points, and leaderboards. This library gives your app access
to the Trophy API, so you can send the user events that power both.

## Installation

You can install the package via pip:

```bash
pip install trophy
```

## Usage

The package needs to be configured with your account's API key which is available in the Trophy
dashboard.

```python
from trophy import EventRequestUser, TrophyApi

client = TrophyApi(
    api_key="YOUR_API_KEY",
)

client.metrics.event(
    key="words-written",
    user=EventRequestUser(
        id="18",
        email="jk.rowling@harrypotter.com",
        tz="Europe/London",
    ),
    value=750.0,
)
```

## Documentation

See the [Trophy API Docs](https://docs.trophy.so) for more
information on the accessible endpoints.
