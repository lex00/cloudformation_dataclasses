"""PropertyTypes for AWS::ImageBuilder::InfrastructureConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InstanceMetadataOptions(PropertyType):
    HTTP_PUT_RESPONSE_HOP_LIMIT = "HttpPutResponseHopLimit"
    HTTP_TOKENS = "HttpTokens"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_put_response_hop_limit": "HttpPutResponseHopLimit",
        "http_tokens": "HttpTokens",
    }

    http_put_response_hop_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_tokens: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Logging(PropertyType):
    S3_LOGS = "S3Logs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_logs": "S3Logs",
    }

    s3_logs: Optional[S3Logs] = None


@dataclass
class Placement(PropertyType):
    TENANCY = "Tenancy"
    AVAILABILITY_ZONE = "AvailabilityZone"
    HOST_ID = "HostId"
    HOST_RESOURCE_GROUP_ARN = "HostResourceGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tenancy": "Tenancy",
        "availability_zone": "AvailabilityZone",
        "host_id": "HostId",
        "host_resource_group_arn": "HostResourceGroupArn",
    }

    tenancy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Logs(PropertyType):
    S3_KEY_PREFIX = "S3KeyPrefix"
    S3_BUCKET_NAME = "S3BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_key_prefix": "S3KeyPrefix",
        "s3_bucket_name": "S3BucketName",
    }

    s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

