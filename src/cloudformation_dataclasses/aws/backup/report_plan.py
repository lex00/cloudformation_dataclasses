"""PropertyTypes for AWS::Backup::ReportPlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ReportDeliveryChannel(PropertyType):
    S3_KEY_PREFIX = "S3KeyPrefix"
    FORMATS = "Formats"
    S3_BUCKET_NAME = "S3BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_key_prefix": "S3KeyPrefix",
        "formats": "Formats",
        "s3_bucket_name": "S3BucketName",
    }

    s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    formats: Optional[Union[list[str], Ref]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReportSetting(PropertyType):
    FRAMEWORK_ARNS = "FrameworkArns"
    REPORT_TEMPLATE = "ReportTemplate"
    ORGANIZATION_UNITS = "OrganizationUnits"
    REGIONS = "Regions"
    ACCOUNTS = "Accounts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "framework_arns": "FrameworkArns",
        "report_template": "ReportTemplate",
        "organization_units": "OrganizationUnits",
        "regions": "Regions",
        "accounts": "Accounts",
    }

    framework_arns: Optional[Union[list[str], Ref]] = None
    report_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organization_units: Optional[Union[list[str], Ref]] = None
    regions: Optional[Union[list[str], Ref]] = None
    accounts: Optional[Union[list[str], Ref]] = None

