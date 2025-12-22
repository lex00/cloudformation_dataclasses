"""PropertyTypes for AWS::SecurityLake::Subscriber."""

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
class AwsLogSource(PropertyType):
    SOURCE_NAME = "SourceName"
    SOURCE_VERSION = "SourceVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_name": "SourceName",
        "source_version": "SourceVersion",
    }

    source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomLogSource(PropertyType):
    SOURCE_NAME = "SourceName"
    SOURCE_VERSION = "SourceVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_name": "SourceName",
        "source_version": "SourceVersion",
    }

    source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    AWS_LOG_SOURCE = "AwsLogSource"
    CUSTOM_LOG_SOURCE = "CustomLogSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_log_source": "AwsLogSource",
        "custom_log_source": "CustomLogSource",
    }

    aws_log_source: Optional[AwsLogSource] = None
    custom_log_source: Optional[CustomLogSource] = None


@dataclass
class SubscriberIdentity(PropertyType):
    EXTERNAL_ID = "ExternalId"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_id": "ExternalId",
        "principal": "Principal",
    }

    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None

