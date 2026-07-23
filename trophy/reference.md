# Reference
## Achievements
<details><summary><code>client.achievements.<a href="src/trophy/achievements/client.py">all</a>(...) -> typing.List[AchievementWithStatsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all achievements and their completion stats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.achievements.all_(
    user_attributes="plan-type:premium,region:us-east",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_attributes:** `typing.Optional[str]` — Optional colon-delimited user attributes in the format attribute:value,attribute:value. Only achievements accessible to a user with the provided attributes will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.achievements.<a href="src/trophy/achievements/client.py">complete</a>(...) -> AchievementCompletionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark an achievement as completed for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpsertedUser
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.achievements.complete(
    key="finish-onboarding",
    user=UpsertedUser(
        email="user@example.com",
        tz="Europe/London",
        id="user-id",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Unique reference of the achievement as set when created.
    
</dd>
</dl>

<dl>
<dd>

**user:** `UpsertedUser` — The user that completed the achievement.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics
<details><summary><code>client.metrics.<a href="src/trophy/metrics/client.py">event</a>(...) -> EventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Increment or decrement the value of a metric for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpsertedUser
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.metrics.event(
    key="words-written",
    idempotency_key="e4296e4b-8493-4bd1-9c30-5a1a9ac4d78f",
    user=UpsertedUser(
        email="user@example.com",
        tz="Europe/London",
        attributes={
            "department": "engineering",
            "role": "developer"
        },
        id="18",
    ),
    value=750,
    attributes={
        "category": "writing",
        "source": "mobile-app"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Unique reference of the metric as set when created.
    
</dd>
</dl>

<dl>
<dd>

**user:** `UpsertedUser` — The user that triggered the event.
    
</dd>
</dl>

<dl>
<dd>

**value:** `float` — The value to add to the user's current total for the given metric.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The idempotency key for the event.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, str]]` — Event attributes as key-value pairs. Keys must match existing event attributes set up in the Trophy dashboard.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/trophy/users/client.py">create</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.create(
    id="user-id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpsertedUser` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">get</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.get(
    id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">identify</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Identify a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.identify(
    id="id",
    email="user@example.com",
    tz="Europe/London",
    attributes={
        "department": "engineering",
        "role": "developer"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to identify.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdatedUser` — The user object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">update</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.update(
    id="id",
    email="user@example.com",
    tz="Europe/London",
    attributes={
        "department": "engineering",
        "role": "developer"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdatedUser` — The user object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">get_preferences</a>(...) -> UserPreferencesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's notification preferences.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.get_preferences(
    id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The user's ID in your database.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">update_preferences</a>(...) -> UserPreferencesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a user's notification and streak preferences. Streak preferences require streak customization to be enabled in your Trophy dashboard settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, NotificationPreferences
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.update_preferences(
    id="user-123",
    notifications=NotificationPreferences(
        streak_reminder=[
            "email"
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The user's ID in your database.
    
</dd>
</dl>

<dl>
<dd>

**notifications:** `typing.Optional[NotificationPreferences]` 
    
</dd>
</dl>

<dl>
<dd>

**streak:** `typing.Optional[StreakPreferences]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">all_metrics</a>(...) -> typing.List[MetricResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single user's progress against all active metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.all_metrics(
    id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">single_metric</a>(...) -> MetricResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's progress against a single active metric.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.single_metric(
    id="userId",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Unique key of the metric.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">metric_event_summary</a>(...) -> typing.List[UsersMetricEventSummaryResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of metric events over time for a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.metric_event_summary(
    id="userId",
    key="words-written",
    aggregation="daily",
    start_date="2024-01-01",
    end_date="2024-01-31",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Unique key of the metric.
    
</dd>
</dl>

<dl>
<dd>

**aggregation:** `UsersMetricEventSummaryRequestAggregation` — The time period over which to aggregate the event data.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — The start date for the data range in YYYY-MM-DD format. The startDate must be before the endDate, and the date range must not exceed 400 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `str` — The end date for the data range in YYYY-MM-DD format. The endDate must be after the startDate, and the date range must not exceed 400 days.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">achievements</a>(...) -> typing.List[UserAchievementWithStatsResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's achievements.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.achievements(
    id="userId",
    include_incomplete="true",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**include_incomplete:** `typing.Optional[typing.Literal]` — When set to 'true', returns both completed and incomplete achievements for the user. When omitted or set to any other value, returns only completed achievements.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">streak</a>(...) -> StreakResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's streak data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.streak(
    id="userId",
    history_periods=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**history_periods:** `typing.Optional[int]` — The number of past streak periods to include in the streakHistory field of the  response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">points</a>(...) -> GetUserPointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's points for a specific points system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.points(
    id="userId",
    key="points-system-key",
    awards=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**awards:** `typing.Optional[int]` — The number of recent point awards to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">points_boosts</a>(...) -> typing.List[PointsBoost]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get active points boosts for a user in a specific points system. Returns both global boosts the user is eligible for and user-specific boosts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.points_boosts(
    id="userId",
    key="points-system-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">points_event_summary</a>(...) -> typing.List[UsersPointsEventSummaryResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of points awards over time for a user for a specific points system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.points_event_summary(
    id="userId",
    key="points-system-key",
    aggregation="daily",
    start_date="2024-01-01",
    end_date="2024-01-31",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the user.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**aggregation:** `UsersPointsEventSummaryRequestAggregation` — The time period over which to aggregate the event data.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — The start date for the data range in YYYY-MM-DD format. The startDate must be before the endDate, and the date range must not exceed 400 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `str` — The end date for the data range in YYYY-MM-DD format. The endDate must be after the startDate, and the date range must not exceed 400 days.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">leaderboard</a>(...) -> UserLeaderboardResponseWithHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's rank, value, and daily ranking history for a specific leaderboard.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.leaderboard(
    id="user-123",
    key="weekly-words",
    run="2025-01-15",
    num_events=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The user's ID in your database.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Unique key of the leaderboard as set when created.
    
</dd>
</dl>

<dl>
<dd>

**run:** `typing.Optional[str]` — Specific run date in YYYY-MM-DD format. If not provided, returns the current run.
    
</dd>
</dl>

<dl>
<dd>

**num_events:** `typing.Optional[int]` — The number of days to return in the leaderboard history for the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/trophy/users/client.py">wrapped</a>(...) -> WrappedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user's year-in-review wrapped data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.users.wrapped(
    id="user-123",
    year=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The user's ID in your database.
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — The year to get wrapped data for. Defaults to the current year. Must be an integer between 1 and the current year.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Streaks
<details><summary><code>client.streaks.<a href="src/trophy/streaks/client.py">list</a>(...) -> BulkStreakResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the streak lengths of a list of users, ranked by streak length from longest to shortest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.streaks.list(
    user_ids=[
        "userIds"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of up to 100 user IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Points
<details><summary><code>client.points.<a href="src/trophy/points/client.py">summary</a>(...) -> PointsSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a breakdown of the number of users with points in each range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.points.summary(
    key="points-system-key",
    user_attributes="plan-type:premium,region:us-east",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**user_attributes:** `typing.Optional[str]` — Optional colon-delimited user attribute filters in the format attribute:value,attribute:value. Only users matching ALL specified attributes will be included in the points breakdown.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.points.<a href="src/trophy/points/client.py">system</a>(...) -> PointsSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a points system with its triggers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.points.system(
    key="points-system-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.points.<a href="src/trophy/points/client.py">boosts</a>(...) -> typing.List[PointsBoost]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all global boosts for a points system. Finished boosts are excluded by default.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.points.boosts(
    key="points-system-key",
    include_finished=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**include_finished:** `typing.Optional[bool]` — When set to 'true', boosts that have finished (past their end date) will be included in the response. By default, finished boosts are excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.points.<a href="src/trophy/points/client.py">levels</a>(...) -> typing.List[PointsLevel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all levels for a points system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.points.levels(
    key="points-system-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.points.<a href="src/trophy/points/client.py">level_summary</a>(...) -> PointsLevelSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a breakdown of the number of users at each level in a points system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.points.level_summary(
    key="points-system-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Leaderboards
<details><summary><code>client.leaderboards.<a href="src/trophy/leaderboards/client.py">all</a>(...) -> typing.List[LeaderboardsAllResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all leaderboards for your organization. Finished leaderboards are excluded by default.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.leaderboards.all_(
    include_finished=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_finished:** `typing.Optional[bool]` — When set to 'true', leaderboards with status 'finished' will be included in the response. By default, finished leaderboards are excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.leaderboards.<a href="src/trophy/leaderboards/client.py">get</a>(...) -> LeaderboardResponseWithRankings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific leaderboard by its key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.leaderboards.get(
    key="weekly-words",
    offset=1,
    limit=1,
    run="2025-01-15",
    user_id="user-123",
    user_attributes="city:London",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Unique key of the leaderboard as set when created.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of rankings to skip for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of rankings to return. Cannot be greater than the size of the leaderboard.
    
</dd>
</dl>

<dl>
<dd>

**run:** `typing.Optional[str]` — Specific run date in YYYY-MM-DD format. If not provided, returns the current run.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — When provided, offset is relative to this user's position on the leaderboard. If the user is not found in the leaderboard, returns empty rankings array.
    
</dd>
</dl>

<dl>
<dd>

**user_attributes:** `typing.Optional[str]` — Attribute key and value to filter the rankings by, separated by a colon. For example, `city:London`. This parameter is required, and only valid for leaderboards with a breakdown attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Attributes
<details><summary><code>client.admin.attributes.<a href="src/trophy/admin/attributes/client.py">list</a>(...) -> ListAttributesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.attributes.list(
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of records to return.
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of records to skip from the start of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.attributes.<a href="src/trophy/admin/attributes/client.py">create</a>(...) -> CreateAttributesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreateAttributeRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.attributes.create(
    request=[
        CreateAttributeRequestItem(
            name="Plan",
            key="plan",
            type="user",
        ),
        CreateAttributeRequestItem(
            name="Device",
            key="device",
            type="event",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateAttributesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.attributes.<a href="src/trophy/admin/attributes/client.py">delete</a>(...) -> DeleteAttributesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete attributes by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.attributes.delete(
    ids=[
        "550e8400-e29b-41d4-a716-446655440000",
        "550e8400-e29b-41d4-a716-446655440001"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Attribute IDs to delete. Repeat the query param or provide a comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.attributes.<a href="src/trophy/admin/attributes/client.py">update</a>(...) -> UpdateAttributesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update attributes by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpdateAttributeRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.attributes.update(
    request=[
        UpdateAttributeRequestItem(
            id="550e8400-e29b-41d4-a716-446655440000",
            name="Subscription Plan",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateAttributesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.attributes.<a href="src/trophy/admin/attributes/client.py">get</a>(...) -> AdminAttribute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an attribute by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.attributes.get(
    id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID of the attribute to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Metrics
<details><summary><code>client.admin.metrics.<a href="src/trophy/admin/metrics/client.py">list</a>(...) -> ListMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.metrics.list(
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of records to return.
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of records to skip from the start of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.metrics.<a href="src/trophy/admin/metrics/client.py">create</a>(...) -> CreateMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreateMetricRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.metrics.create(
    request=[
        CreateMetricRequestItem(
            name="Invites Sent",
            key="invites-sent",
        ),
        CreateMetricRequestItem(
            name="Revenue",
            key="revenue",
            unit_type="currency",
            units="USD",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMetricsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.metrics.<a href="src/trophy/admin/metrics/client.py">delete</a>(...) -> DeleteMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete metrics by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.metrics.delete(
    ids=[
        "550e8400-e29b-41d4-a716-446655440000",
        "550e8400-e29b-41d4-a716-446655440001"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Metric IDs to delete. Repeat the query param or provide a comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.metrics.<a href="src/trophy/admin/metrics/client.py">update</a>(...) -> UpdateMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update metrics by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpdateMetricRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.metrics.update(
    request=[
        UpdateMetricRequestItem(
            id="550e8400-e29b-41d4-a716-446655440000",
            name="Invites Completed",
            units="invites",
        ),
        UpdateMetricRequestItem(
            id="550e8400-e29b-41d4-a716-446655440001",
            unit_type="number",
            units="dollars",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateMetricsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.metrics.<a href="src/trophy/admin/metrics/client.py">get</a>(...) -> CreatedMetric</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a metric by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.metrics.get(
    id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID of the metric to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Leaderboards
<details><summary><code>client.admin.leaderboards.<a href="src/trophy/admin/leaderboards/client.py">list</a>(...) -> ListLeaderboardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List leaderboards.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.leaderboards.list(
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of records to return.
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of records to skip from the start of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.leaderboards.<a href="src/trophy/admin/leaderboards/client.py">create</a>(...) -> CreateLeaderboardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create leaderboards. Maximum 100 leaderboards per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreateLeaderboardRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.leaderboards.create(
    request=[
        CreateLeaderboardRequestItem(
            name="Revenue Champions",
            key="revenue-champions",
            status="inactive",
            rank_by="metric",
            metric_id="550e8400-e29b-41d4-a716-446655440000",
            max_participants=100,
            start="2026-04-20",
            breakdown_attributes=[
                "550e8400-e29b-41d4-a716-446655440010"
            ],
            run_unit="month",
            run_interval=1,
        ),
        CreateLeaderboardRequestItem(
            name="Streak Legends",
            key="streak-legends",
            status="scheduled",
            rank_by="streak",
            start="2026-04-27",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateLeaderboardsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.leaderboards.<a href="src/trophy/admin/leaderboards/client.py">delete</a>(...) -> DeleteLeaderboardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete leaderboards by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.leaderboards.delete(
    ids=[
        "ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Leaderboard IDs to delete. Repeat the query param or provide a comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.leaderboards.<a href="src/trophy/admin/leaderboards/client.py">update</a>(...) -> UpdateLeaderboardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update leaderboards by ID. Updating `status` behaves the same as activating, scheduling, deactivating, or finishing a leaderboard in the dashboard.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpdateLeaderboardRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.leaderboards.update(
    request=[
        UpdateLeaderboardRequestItem(
            id="550e8400-e29b-41d4-a716-446655440100",
            name="Monthly Revenue Champions",
            description="Ranked by monthly revenue",
            status="active",
        ),
        UpdateLeaderboardRequestItem(
            id="550e8400-e29b-41d4-a716-446655440101",
            status="finished",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateLeaderboardsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.leaderboards.<a href="src/trophy/admin/leaderboards/client.py">get</a>(...) -> AdminLeaderboard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a leaderboard by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.leaderboards.get(
    id="550e8400-e29b-41d4-a716-446655440100",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID of the leaderboard to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Streaks
<details><summary><code>client.admin.streaks.<a href="src/trophy/admin/streaks/client.py">restore</a>(...) -> RestoreStreaksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore streaks for multiple users to the maximum previously achieved streak length found within the current restore window: the last 90 days for daily streaks, weekly periods starting with the week containing the start of the current calendar year for weekly streaks, and monthly periods starting at the beginning of the previous calendar year for monthly streaks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment
from trophy.admin.streaks import RestoreStreaksRequestUsersItem

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.streaks.restore(
    users=[
        RestoreStreaksRequestUsersItem(
            id="user-123",
        ),
        RestoreStreaksRequestUsersItem(
            id="user-456",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**users:** `typing.List[RestoreStreaksRequestUsersItem]` — Array of users to restore streaks for. Maximum 100 users per request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin ApplicationApiKeys
<details><summary><code>client.admin.application_api_keys.<a href="src/trophy/admin/application_api_keys/client.py">create</a>(...) -> CreateApplicationKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create application API keys scoped to specific users. Each key can only perform operations on behalf of the user it was created for.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreateApplicationKeyRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.application_api_keys.create(
    request=[
        CreateApplicationKeyRequestItem(
            user_id="user_123",
        ),
        CreateApplicationKeyRequestItem(
            user_id="user_456",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateApplicationKeysRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.application_api_keys.<a href="src/trophy/admin/application_api_keys/client.py">delete</a>(...) -> DeleteApplicationKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete application API keys by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.application_api_keys.delete(
    ids=[
        "550e8400-e29b-41d4-a716-446655440000"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Application API key IDs (UUIDs returned at creation time). Repeat the query param or provide a comma-separated list. Maximum 100 IDs per request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Tenants
<details><summary><code>client.admin.tenants.<a href="src/trophy/admin/tenants/client.py">list</a>(...) -> ListTenantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List tenants in the current environment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.tenants.list(
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of records to return.
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of records to skip from the start of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.tenants.<a href="src/trophy/admin/tenants/client.py">create</a>(...) -> CreateTenantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create tenants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreateTenantRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.tenants.create(
    request=[
        CreateTenantRequestItem(
            customer_id="customer_12345",
            name="Acme Corp",
        ),
        CreateTenantRequestItem(
            customer_id="customer_67890",
            name="Globex Inc",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateTenantsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.tenants.<a href="src/trophy/admin/tenants/client.py">delete</a>(...) -> DeleteTenantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete tenants by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.tenants.delete(
    ids=[
        "550e8400-e29b-41d4-a716-446655440000",
        "550e8400-e29b-41d4-a716-446655440001"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tenant IDs to delete. Repeat the query param or provide a comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.tenants.<a href="src/trophy/admin/tenants/client.py">update</a>(...) -> UpdateTenantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update tenants by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpdateTenantRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.tenants.update(
    request=[
        UpdateTenantRequestItem(
            id="550e8400-e29b-41d4-a716-446655440000",
            name="Acme Corporation",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateTenantsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.tenants.<a href="src/trophy/admin/tenants/client.py">get</a>(...) -> AdminTenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a tenant by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.tenants.get(
    id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID of the tenant to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Points Systems
<details><summary><code>client.admin.points.systems.<a href="src/trophy/admin/points/systems/client.py">list</a>(...) -> ListPointsSystemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List points systems.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.systems.list(
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of records to return.
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of records to skip from the start of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.systems.<a href="src/trophy/admin/points/systems/client.py">create</a>(...) -> CreatePointsSystemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create points systems. Optionally include sub-entities (levels, boosts, triggers) in each system payload to create them alongside the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreatePointsSystemRequestItem, CreatePointsLevelRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.systems.create(
    request=[
        CreatePointsSystemRequestItem(
            name="XP",
            key="xp",
            description="Experience points",
            levels=[
                CreatePointsLevelRequestItem(
                    name="Bronze",
                    key="bronze",
                    points=100,
                ),
                CreatePointsLevelRequestItem(
                    name="Silver",
                    key="silver",
                    points=500,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreatePointsSystemsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.systems.<a href="src/trophy/admin/points/systems/client.py">delete</a>(...) -> DeletePointsSystemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete (archive) points systems by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.systems.delete(
    ids=[
        "550e8400-e29b-41d4-a716-446655440000"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The IDs of the points systems to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.systems.<a href="src/trophy/admin/points/systems/client.py">update</a>(...) -> UpdatePointsSystemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update points systems by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, UpdatePointsSystemRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.systems.update(
    request=[
        UpdatePointsSystemRequestItem(
            id="550e8400-e29b-41d4-a716-446655440000",
            name="New Name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdatePointsSystemsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.systems.<a href="src/trophy/admin/points/systems/client.py">get</a>(...) -> AdminPointsSystem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a points system by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.systems.get(
    id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Points Boosts
<details><summary><code>client.admin.points.boosts.<a href="src/trophy/admin/points/boosts/client.py">list</a>(...) -> ListPointsBoostsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List points boosts for a system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.boosts.list(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (1-100, default 10).
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of results to skip for pagination (default 0).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.boosts.<a href="src/trophy/admin/points/boosts/client.py">create</a>(...) -> CreatePointsBoostsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create points boosts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreatePointsBoostRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.boosts.create(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    request=[
        CreatePointsBoostRequestItem(
            user_id="user-123",
            name="Double XP Weekend",
            start="2024-01-01",
            end="2024-01-03",
            multiplier=2,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreatePointsBoostsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.boosts.<a href="src/trophy/admin/points/boosts/client.py">delete</a>(...) -> DeletePointsBoostsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete multiple points boosts by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.boosts.delete(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    ids=[
        "ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of up to 100 boost IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.boosts.<a href="src/trophy/admin/points/boosts/client.py">update</a>(...) -> PatchPointsBoostsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update multiple points boosts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, PatchPointsBoostsRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.boosts.update(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    request=[
        PatchPointsBoostsRequestItem(
            id="550e8400-e29b-41d4-a716-446655440000",
            name="Updated Boost Name",
            multiplier=3,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchPointsBoostsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.boosts.<a href="src/trophy/admin/points/boosts/client.py">get</a>(...) -> AdminPointsBoost</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single points boost by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.boosts.get(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    id="660f9500-f30c-42e5-b827-557766550001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The UUID of the points boost.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Points Levels
<details><summary><code>client.admin.points.levels.<a href="src/trophy/admin/points/levels/client.py">list</a>(...) -> ListPointsLevelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List points levels for a system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.levels.list(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of records to return.
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of records to skip from the start of the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.levels.<a href="src/trophy/admin/points/levels/client.py">create</a>(...) -> CreatePointsLevelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create points levels. Maximum 100 levels per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreatePointsLevelRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.levels.create(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    request=[
        CreatePointsLevelRequestItem(
            name="Bronze",
            key="bronze",
            points=100,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreatePointsLevelsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.levels.<a href="src/trophy/admin/points/levels/client.py">delete</a>(...) -> DeletePointsLevelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete multiple points levels by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.levels.delete(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    ids=[
        "ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of level UUIDs to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.levels.<a href="src/trophy/admin/points/levels/client.py">update</a>(...) -> PatchPointsLevelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update multiple points levels. Each item must include an ID. `key` cannot be changed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, PatchPointsLevelsRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.levels.update(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    request=[
        PatchPointsLevelsRequestItem(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchPointsLevelsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.levels.<a href="src/trophy/admin/points/levels/client.py">get</a>(...) -> AdminPointsLevel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single points level by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.levels.get(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    id="660f9500-f30c-42e5-b827-557766550001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The UUID of the points level.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Points Triggers
<details><summary><code>client.admin.points.triggers.<a href="src/trophy/admin/points/triggers/client.py">list</a>(...) -> ListPointsTriggersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List points triggers for a system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.triggers.list(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    limit=1,
    skip=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (1-100, default 10).
    
</dd>
</dl>

<dl>
<dd>

**skip:** `typing.Optional[int]` — Number of results to skip for pagination (default 0).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.triggers.<a href="src/trophy/admin/points/triggers/client.py">create</a>(...) -> CreatePointsTriggersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create points triggers in bulk. Maximum 100 triggers per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, CreatePointsTriggerRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.triggers.create(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    request=[
        CreatePointsTriggerRequestItem(
            type="metric",
            points=10,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreatePointsTriggersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.triggers.<a href="src/trophy/admin/points/triggers/client.py">delete</a>(...) -> DeletePointsTriggersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete (archive) points triggers by ID. Maximum 100 trigger IDs per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.triggers.delete(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    ids=[
        "550e8400-e29b-41d4-a716-446655440000"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Trigger IDs to delete. Can be repeated or comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.triggers.<a href="src/trophy/admin/points/triggers/client.py">update</a>(...) -> PatchPointsTriggersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update points triggers in bulk. Maximum 100 triggers per request. Only provided fields are updated; omitted fields are preserved.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi, PatchPointsTriggersRequestItem
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.triggers.update(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    request=[
        PatchPointsTriggersRequestItem(
            id="id",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchPointsTriggersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.points.triggers.<a href="src/trophy/admin/points/triggers/client.py">get</a>(...) -> AdminPointsTrigger</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single points trigger by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.points.triggers.get(
    system_id="550e8400-e29b-41d4-a716-446655440000",
    id="660f9500-f30c-42e5-b827-557766550001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_id:** `str` — The UUID of the points system.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The UUID of the points trigger.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin Streaks Freezes
<details><summary><code>client.admin.streaks.freezes.<a href="src/trophy/admin/streaks/freezes/client.py">create</a>(...) -> CreateStreakFreezesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create streak freezes for multiple users.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from trophy import TrophyApi
from trophy.environment import TrophyApiEnvironment
from trophy.admin.streaks.freezes import CreateStreakFreezesRequestFreezesItem

client = TrophyApi(
    api_key="<value>",
    sdk_version="<X-SDK-VERSION>",
    environment=TrophyApiEnvironment.PRODUCTION,
)

client.admin.streaks.freezes.create(
    freezes=[
        CreateStreakFreezesRequestFreezesItem(
            user_id="user-123",
        ),
        CreateStreakFreezesRequestFreezesItem(
            user_id="user-456",
        ),
        CreateStreakFreezesRequestFreezesItem(
            user_id="user-123",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**freezes:** `typing.List[CreateStreakFreezesRequestFreezesItem]` — Array of freezes to create. Maximum 100 freezes per request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

