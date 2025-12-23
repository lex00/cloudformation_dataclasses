"""PropertyTypes for AWS::SMSVOICE::ProtectConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CountryRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protect_status": "ProtectStatus",
        "country_code": "CountryCode",
    }

    protect_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    country_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CountryRuleSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "voice": "VOICE",
        "mms": "MMS",
        "sms": "SMS",
    }

    voice: Optional[list[CountryRule]] = None
    mms: Optional[list[CountryRule]] = None
    sms: Optional[list[CountryRule]] = None

