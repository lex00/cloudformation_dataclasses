"""PropertyTypes for AWS::MediaPackageV2::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IngestEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
        "url": "Url",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputSwitchConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "preferred_input": "PreferredInput",
        "mqcs_input_switching": "MQCSInputSwitching",
    }

    preferred_input: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mqcs_input_switching: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OutputHeaderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "publish_mqcs": "PublishMQCS",
    }

    publish_mqcs: Optional[Union[bool, Ref, GetAtt, Sub]] = None

