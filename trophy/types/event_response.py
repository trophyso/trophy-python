# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from .event_response_metrics_item import EventResponseMetricsItem
from .streak_response import StreakResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EventResponse(UniversalBaseModel):
    event_id: typing_extensions.Annotated[str, FieldMetadata(alias="eventId")] = (
        pydantic.Field()
    )
    """
    The unique ID of the event.
    """

    metric_id: typing_extensions.Annotated[str, FieldMetadata(alias="metricId")] = (
        pydantic.Field()
    )
    """
    The unique ID of the metric that was updated.
    """

    total: float = pydantic.Field()
    """
    The user's new total progress against the metric.
    """

    achievements: typing.Optional[typing.List[EventResponseMetricsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Changes to achievements as a result of this event.
    """

    current_streak: typing_extensions.Annotated[
        typing.Optional[StreakResponse], FieldMetadata(alias="currentStreak")
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
