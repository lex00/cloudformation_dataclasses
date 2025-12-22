"""PropertyTypes for AWS::IoTAnalytics::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChannelStatus:
    """ChannelStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class ComputeType:
    """ComputeType enum values."""

    ACU_1 = "ACU_1"
    ACU_2 = "ACU_2"


class DatasetActionType:
    """DatasetActionType enum values."""

    QUERY = "QUERY"
    CONTAINER = "CONTAINER"


class DatasetContentState:
    """DatasetContentState enum values."""

    CREATING = "CREATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class DatasetStatus:
    """DatasetStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class DatastoreStatus:
    """DatastoreStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class FileFormatType:
    """FileFormatType enum values."""

    JSON = "JSON"
    PARQUET = "PARQUET"


class LoggingLevel:
    """LoggingLevel enum values."""

    ERROR = "ERROR"


class ReprocessingStatus:
    """ReprocessingStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


@dataclass
class ChannelStorage(PropertyType):
    CUSTOMER_MANAGED_S3 = "CustomerManagedS3"
    SERVICE_MANAGED_S3 = "ServiceManagedS3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_s3": "CustomerManagedS3",
        "service_managed_s3": "ServiceManagedS3",
    }

    customer_managed_s3: Optional[CustomerManagedS3] = None
    service_managed_s3: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class CustomerManagedS3(PropertyType):
    BUCKET = "Bucket"
    ROLE_ARN = "RoleArn"
    KEY_PREFIX = "KeyPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "role_arn": "RoleArn",
        "key_prefix": "KeyPrefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionPeriod(PropertyType):
    NUMBER_OF_DAYS = "NumberOfDays"
    UNLIMITED = "Unlimited"

    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_days": "NumberOfDays",
        "unlimited": "Unlimited",
    }

    number_of_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlimited: Optional[Union[bool, Ref, GetAtt, Sub]] = None

