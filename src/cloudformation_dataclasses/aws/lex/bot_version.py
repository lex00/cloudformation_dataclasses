"""PropertyTypes for AWS::Lex::BotVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BotVersionLocaleDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_bot_version": "SourceBotVersion",
    }

    source_bot_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BotVersionLocaleSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale_id": "LocaleId",
        "bot_version_locale_details": "BotVersionLocaleDetails",
    }

    locale_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bot_version_locale_details: Optional[BotVersionLocaleDetails] = None

