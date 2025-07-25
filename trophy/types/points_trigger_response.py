# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .points_trigger_response_type import PointsTriggerResponseType
from .points_trigger_response_status import PointsTriggerResponseStatus
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PointsTriggerResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the trigger.
    """

    type: typing.Optional[PointsTriggerResponseType] = pydantic.Field(default=None)
    """
    The type of trigger.
    """

    points: typing.Optional[float] = pydantic.Field(default=None)
    """
    The points awarded by this trigger.
    """

    status: typing.Optional[PointsTriggerResponseStatus] = pydantic.Field(default=None)
    """
    The status of the trigger.
    """

    achievement_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="achievementId")
    ] = pydantic.Field(default=None)
    """
    The unique ID of the achievement associated with this trigger, if the trigger is an achievement.
    """

    metric_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metricId")
    ] = pydantic.Field(default=None)
    """
    The unique ID of the metric associated with this trigger, if the trigger is a metric.
    """

    metric_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="metricThreshold")
    ] = pydantic.Field(default=None)
    """
    The amount that a user must increase the metric to earn the points, if the trigger is a metric.
    """

    streak_length_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="streakLengthThreshold")
    ] = pydantic.Field(default=None)
    """
    The number of consecutive streak periods that a user must complete to earn the points, if the trigger is a streak.
    """

    metric_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metricName")
    ] = pydantic.Field(default=None)
    """
    The name of the metric associated with this trigger, if the trigger is a metric.
    """

    achievement_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="achievementName")
    ] = pydantic.Field(default=None)
    """
    The name of the achievement associated with this trigger, if the trigger is an achievement.
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the trigger was created, in ISO 8601 format.
    """

    updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the trigger was last updated, in ISO 8601 format.
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
