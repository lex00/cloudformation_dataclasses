"""PropertyTypes for AWS::Config::ConfigurationAggregator."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccountAggregationSource(PropertyType):
    ALL_AWS_REGIONS = "AllAwsRegions"
    AWS_REGIONS = "AwsRegions"
    ACCOUNT_IDS = "AccountIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_aws_regions": "AllAwsRegions",
        "aws_regions": "AwsRegions",
        "account_ids": "AccountIds",
    }

    all_aws_regions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    aws_regions: Optional[Union[list[str], Ref]] = None
    account_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class OrganizationAggregationSource(PropertyType):
    ALL_AWS_REGIONS = "AllAwsRegions"
    AWS_REGIONS = "AwsRegions"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_aws_regions": "AllAwsRegions",
        "aws_regions": "AwsRegions",
        "role_arn": "RoleArn",
    }

    all_aws_regions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    aws_regions: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

