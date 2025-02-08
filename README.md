# Trophy Python SDK

The Trophy Python SDK provides convenient access to the Trophy API from applications written in the
Python language. 

Trophy provides APIs and tools for adding gamification to your application, keeping users engaged 
through rewards, achievements, streaks, and personalized communication.

## Documentation

See the [Trophy API Docs](https://trophy.docs.buildwithfern.com/overview/introduction) for more
information.

## Installation

You can install the package via pip:

```bash
pip install trophy
```

## Usage

The package needs to be configured with your account's API key which is available in the Trophy
dashboard.

```python
from trophy import TrophyApiClient

client = TrophyApiClient(api_key='your-api-key')

# Send a metric event
client.metrics.event("words-written", {
    "user": {
        "id": "18",
        "email": "jk.rowling@harrypotter.com",
        "tz": "Europe/London"
    },
    "value": 750
})
```
