"""PropertyTypes for AWS::PinpointEmail::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeliveryOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sending_pool_name": "SendingPoolName",
    }

    sending_pool_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReputationOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "reputation_metrics_enabled": "ReputationMetricsEnabled",
    }

    reputation_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SendingOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sending_enabled": "SendingEnabled",
    }

    sending_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrackingOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_redirect_domain": "CustomRedirectDomain",
    }

    custom_redirect_domain: Optional[Union[str, Ref, GetAtt, Sub]] = None

