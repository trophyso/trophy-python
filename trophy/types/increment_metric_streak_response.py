# This file was auto-generated by Fern from our API Definition.

from .base_streak_response import BaseStreakResponse
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class IncrementMetricStreakResponse(BaseStreakResponse):
    """
    An object representing the user's streak after incrementing a metric.
    """

    extended: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this metric event increased the user's streak length.
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
