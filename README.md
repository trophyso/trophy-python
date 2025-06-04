# Trophy Python SDK

The Trophy Python SDK provides convenient access to the Trophy API from applications written in the
Python language.

Trophy provides APIs and tools for adding gamification to your application, keeping users engaged
through rewards, achievements, streaks, and personalized communication.

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
