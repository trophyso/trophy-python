# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .streak_frequency import StreakFrequency
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BaseStreakResponse(UniversalBaseModel):
    length: int = pydantic.Field()
    """
    The length of the user's current streak.
    """

    frequency: StreakFrequency = pydantic.Field()
    """
    The frequency of the streak.
    """

    started: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the streak started.
    """

    period_start: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="periodStart")
    ] = pydantic.Field(default=None)
    """
    The start date of the current streak period.
    """

    period_end: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="periodEnd")
    ] = pydantic.Field(default=None)
    """
    The end date of the current streak period.
    """

    expires: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the streak will expire if the user does not increment a metric.
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
