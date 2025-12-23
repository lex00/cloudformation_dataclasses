"""PropertyTypes for AWS::SecurityLake::DataLake."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Expiration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days": "Days",
    }

    days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transitions": "Transitions",
        "expiration": "Expiration",
    }

    transitions: Optional[list[Transitions]] = None
    expiration: Optional[Expiration] = None


@dataclass
class ReplicationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "regions": "Regions",
        "role_arn": "RoleArn",
    }

    regions: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transitions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
        "days": "Days",
    }

    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    days: Optional[Union[int, Ref, GetAtt, Sub]] = None

