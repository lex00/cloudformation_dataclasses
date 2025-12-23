"""PropertyTypes for AWS::OpenSearchService::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppConfig(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSource(PropertyType):
    DATA_SOURCE_ARN = "DataSourceArn"
    DATA_SOURCE_DESCRIPTION = "DataSourceDescription"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "data_source_description": "DataSourceDescription",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source_description: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamIdentityCenterOptions(PropertyType):
    IAM_IDENTITY_CENTER_INSTANCE_ARN = "IamIdentityCenterInstanceArn"
    IAM_ROLE_FOR_IDENTITY_CENTER_APPLICATION_ARN = "IamRoleForIdentityCenterApplicationArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_identity_center_instance_arn": "IamIdentityCenterInstanceArn",
        "iam_role_for_identity_center_application_arn": "IamRoleForIdentityCenterApplicationArn",
        "enabled": "Enabled",
    }

    iam_identity_center_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_for_identity_center_application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

