# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .achievement_response_trigger import AchievementResponseTrigger
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from .metric_event_streak_response import MetricEventStreakResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AchievementResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique ID of the achievement.
    """

    name: str = pydantic.Field()
    """
    The name of this achievement.
    """

    trigger: AchievementResponseTrigger = pydantic.Field()
    """
    The trigger of the achievement.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of this achievement.
    """

    badge_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="badgeUrl")
    ] = pydantic.Field(default=None)
    """
    The URL of the badge image for the achievement, if one has been uploaded.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key used to reference this achievement in the API (only applicable if trigger = 'api')
    """

    streak_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="streakLength")
    ] = pydantic.Field(default=None)
    """
    The length of the streak required to complete the achievement (only applicable if trigger = 'streak')
    """

    metric_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metricId")
    ] = pydantic.Field(default=None)
    """
    The ID of the metric associated with this achievement (only applicable if trigger = 'metric')
    """

    metric_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="metricValue")
    ] = pydantic.Field(default=None)
    """
    The value of the metric required to complete the achievement (only applicable if trigger = 'metric')
    """

    metric_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metricName")
    ] = pydantic.Field(default=None)
    """
    The name of the metric associated with this achievement (only applicable if trigger = 'metric')
    """

    current_streak: typing_extensions.Annotated[
        typing.Optional[MetricEventStreakResponse], FieldMetadata(alias="currentStreak")
    ] = pydantic.Field(default=None)
    """
    The user's current streak for the metric, if the metric has streaks enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
