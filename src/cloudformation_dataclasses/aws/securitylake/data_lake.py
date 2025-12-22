"""PropertyTypes for AWS::SecurityLake::DataLake."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessType:
    """AccessType enum values."""

    LAKEFORMATION = "LAKEFORMATION"
    S3 = "S3"


class AwsLogSourceName:
    """AwsLogSourceName enum values."""

    ROUTE53 = "ROUTE53"
    VPC_FLOW = "VPC_FLOW"
    SH_FINDINGS = "SH_FINDINGS"
    CLOUD_TRAIL_MGMT = "CLOUD_TRAIL_MGMT"
    LAMBDA_EXECUTION = "LAMBDA_EXECUTION"
    S3_DATA = "S3_DATA"
    EKS_AUDIT = "EKS_AUDIT"
    WAF = "WAF"


class DataLakeStatus:
    """DataLakeStatus enum values."""

    INITIALIZED = "INITIALIZED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class HttpMethod:
    """HttpMethod enum values."""

    POST = "POST"
    PUT = "PUT"


class SourceCollectionStatus:
    """SourceCollectionStatus enum values."""

    COLLECTING = "COLLECTING"
    MISCONFIGURED = "MISCONFIGURED"
    NOT_COLLECTING = "NOT_COLLECTING"


class SubscriberStatus:
    """SubscriberStatus enum values."""

    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"
    PENDING = "PENDING"
    READY = "READY"


@dataclass
class EncryptionConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Expiration(PropertyType):
    DAYS = "Days"

    _property_mappings: ClassVar[dict[str, str]] = {
        "days": "Days",
    }

    days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    TRANSITIONS = "Transitions"
    EXPIRATION = "Expiration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transitions": "Transitions",
        "expiration": "Expiration",
    }

    transitions: Optional[list[Transitions]] = None
    expiration: Optional[Expiration] = None


@dataclass
class ReplicationConfiguration(PropertyType):
    REGIONS = "Regions"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regions": "Regions",
        "role_arn": "RoleArn",
    }

    regions: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transitions(PropertyType):
    STORAGE_CLASS = "StorageClass"
    DAYS = "Days"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
        "days": "Days",
    }

    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    days: Optional[Union[int, Ref, GetAtt, Sub]] = None

