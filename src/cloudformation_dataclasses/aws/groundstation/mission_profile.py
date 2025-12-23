"""PropertyTypes for AWS::GroundStation::MissionProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataflowEdge(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamsKmsKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "kms_alias_arn": "KmsAliasArn",
        "kms_alias_name": "KmsAliasName",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_alias_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

