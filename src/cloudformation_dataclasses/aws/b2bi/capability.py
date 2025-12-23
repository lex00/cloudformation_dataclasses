"""PropertyTypes for AWS::B2BI::Capability."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapabilityConfiguration(PropertyType):
    EDI = "Edi"

    _property_mappings: ClassVar[dict[str, str]] = {
        "edi": "Edi",
    }

    edi: Optional[EdiConfiguration] = None


@dataclass
class EdiConfiguration(PropertyType):
    TYPE = "Type"
    INPUT_LOCATION = "InputLocation"
    TRANSFORMER_ID = "TransformerId"
    OUTPUT_LOCATION = "OutputLocation"
    CAPABILITY_DIRECTION = "CapabilityDirection"

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
    X12_DETAILS = "X12Details"

    _property_mappings: ClassVar[dict[str, str]] = {
        "x12_details": "X12Details",
    }

    x12_details: Optional[X12Details] = None


@dataclass
class S3Location(PropertyType):
    BUCKET_NAME = "BucketName"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "key": "Key",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12Details(PropertyType):
    VERSION = "Version"
    TRANSACTION_SET = "TransactionSet"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "transaction_set": "TransactionSet",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transaction_set: Optional[Union[str, Ref, GetAtt, Sub]] = None

