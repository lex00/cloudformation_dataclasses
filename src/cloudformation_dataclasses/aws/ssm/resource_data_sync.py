"""PropertyTypes for AWS::SSM::ResourceDataSync."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsOrganizationsSource(PropertyType):
    ORGANIZATION_SOURCE_TYPE = "OrganizationSourceType"
    ORGANIZATIONAL_UNITS = "OrganizationalUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "organization_source_type": "OrganizationSourceType",
        "organizational_units": "OrganizationalUnits",
    }

    organization_source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organizational_units: Optional[Union[list[str], Ref]] = None


@dataclass
class S3Destination(PropertyType):
    KMS_KEY_ARN = "KMSKeyArn"
    BUCKET_NAME = "BucketName"
    BUCKET_REGION = "BucketRegion"
    SYNC_FORMAT = "SyncFormat"
    BUCKET_PREFIX = "BucketPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
        "bucket_name": "BucketName",
        "bucket_region": "BucketRegion",
        "sync_format": "SyncFormat",
        "bucket_prefix": "BucketPrefix",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sync_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SyncSource(PropertyType):
    SOURCE_TYPE = "SourceType"
    AWS_ORGANIZATIONS_SOURCE = "AwsOrganizationsSource"
    INCLUDE_FUTURE_REGIONS = "IncludeFutureRegions"
    SOURCE_REGIONS = "SourceRegions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_type": "SourceType",
        "aws_organizations_source": "AwsOrganizationsSource",
        "include_future_regions": "IncludeFutureRegions",
        "source_regions": "SourceRegions",
    }

    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_organizations_source: Optional[AwsOrganizationsSource] = None
    include_future_regions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source_regions: Optional[Union[list[str], Ref]] = None

