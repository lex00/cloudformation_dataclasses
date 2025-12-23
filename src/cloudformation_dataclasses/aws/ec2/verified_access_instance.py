"""PropertyTypes for AWS::EC2::VerifiedAccessInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLogs(PropertyType):
    LOG_GROUP = "LogGroup"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisDataFirehose(PropertyType):
    DELIVERY_STREAM = "DeliveryStream"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
        "enabled": "Enabled",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3(PropertyType):
    BUCKET_NAME = "BucketName"
    ENABLED = "Enabled"
    PREFIX = "Prefix"
    BUCKET_OWNER = "BucketOwner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "enabled": "Enabled",
        "prefix": "Prefix",
        "bucket_owner": "BucketOwner",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VerifiedAccessLogs(PropertyType):
    S3 = "S3"
    LOG_VERSION = "LogVersion"
    KINESIS_DATA_FIREHOSE = "KinesisDataFirehose"
    CLOUD_WATCH_LOGS = "CloudWatchLogs"
    INCLUDE_TRUST_CONTEXT = "IncludeTrustContext"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "log_version": "LogVersion",
        "kinesis_data_firehose": "KinesisDataFirehose",
        "cloud_watch_logs": "CloudWatchLogs",
        "include_trust_context": "IncludeTrustContext",
    }

    s3: Optional[S3] = None
    log_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kinesis_data_firehose: Optional[KinesisDataFirehose] = None
    cloud_watch_logs: Optional[CloudWatchLogs] = None
    include_trust_context: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VerifiedAccessTrustProvider(PropertyType):
    DESCRIPTION = "Description"
    DEVICE_TRUST_PROVIDER_TYPE = "DeviceTrustProviderType"
    VERIFIED_ACCESS_TRUST_PROVIDER_ID = "VerifiedAccessTrustProviderId"
    TRUST_PROVIDER_TYPE = "TrustProviderType"
    USER_TRUST_PROVIDER_TYPE = "UserTrustProviderType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "device_trust_provider_type": "DeviceTrustProviderType",
        "verified_access_trust_provider_id": "VerifiedAccessTrustProviderId",
        "trust_provider_type": "TrustProviderType",
        "user_trust_provider_type": "UserTrustProviderType",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_trust_provider_type: Optional[Union[str, DeviceTrustProviderType, Ref, GetAtt, Sub]] = None
    verified_access_trust_provider_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trust_provider_type: Optional[Union[str, TrustProviderType, Ref, GetAtt, Sub]] = None
    user_trust_provider_type: Optional[Union[str, UserTrustProviderType, Ref, GetAtt, Sub]] = None

