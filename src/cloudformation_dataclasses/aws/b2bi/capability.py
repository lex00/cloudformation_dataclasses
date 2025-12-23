"""PropertyTypes for AWS::B2BI::Capability."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapabilityConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "edi": "Edi",
    }

    edi: Optional[EdiConfiguration] = None


@dataclass
class EdiConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_location": "InputLocation",
        "transformer_id": "TransformerId",
        "output_location": "OutputLocation",
        "capability_direction": "CapabilityDirection",
    }

    type_: Optional[EdiType] = None
    input_location: Optional[S3Location] = None
    transformer_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_location: Optional[S3Location] = None
    capability_direction: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EdiType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "x12_details": "X12Details",
    }

    x12_details: Optional[X12Details] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "key": "Key",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12Details(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "transaction_set": "TransactionSet",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transaction_set: Optional[Union[str, Ref, GetAtt, Sub]] = None

