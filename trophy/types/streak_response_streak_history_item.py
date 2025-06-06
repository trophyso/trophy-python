# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class StreakResponseStreakHistoryItem(UniversalBaseModel):
    """
    An object representing a past streak period.
    """

    period_start: typing_extensions.Annotated[
        str, FieldMetadata(alias="periodStart")
    ] = pydantic.Field()
    """
    The date this streak period started.
    """

    period_end: typing_extensions.Annotated[str, FieldMetadata(alias="periodEnd")] = (
        pydantic.Field()
    )
    """
    The date this streak period ended.
    """

    length: int = pydantic.Field()
    """
    The length of the user's streak during this period.
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
