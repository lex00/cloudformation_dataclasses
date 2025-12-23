"""PropertyTypes for AWS::Timestream::Table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MagneticStoreRejectedDataLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_configuration": "S3Configuration",
    }

    s3_configuration: Optional[S3Configuration] = None


@dataclass
class MagneticStoreWriteProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_magnetic_store_writes": "EnableMagneticStoreWrites",
        "magnetic_store_rejected_data_location": "MagneticStoreRejectedDataLocation",
    }

    enable_magnetic_store_writes: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    magnetic_store_rejected_data_location: Optional[MagneticStoreRejectedDataLocation] = None


@dataclass
class PartitionKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "enforcement_in_record": "EnforcementInRecord",
        "name": "Name",
    }

    type_: Optional[Union[str, PartitionKeyType, Ref, GetAtt, Sub]] = None
    enforcement_in_record: Optional[Union[str, PartitionKeyEnforcementLevel, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "magnetic_store_retention_period_in_days": "MagneticStoreRetentionPeriodInDays",
        "memory_store_retention_period_in_hours": "MemoryStoreRetentionPeriodInHours",
    }

    magnetic_store_retention_period_in_days: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_store_retention_period_in_hours: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "kms_key_id": "KmsKeyId",
        "object_key_prefix": "ObjectKeyPrefix",
        "encryption_option": "EncryptionOption",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_option: Optional[Union[str, S3EncryptionOption, Ref, GetAtt, Sub]] = None


@dataclass
class Schema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "composite_partition_key": "CompositePartitionKey",
    }

    composite_partition_key: Optional[list[PartitionKey]] = None

