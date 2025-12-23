"""PropertyTypes for AWS::Logs::Integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OpenSearchResourceConfig(PropertyType):
    DASHBOARD_VIEWER_PRINCIPALS = "DashboardViewerPrincipals"
    APPLICATION_ARN = "ApplicationARN"
    KMS_KEY_ARN = "KmsKeyArn"
    RETENTION_DAYS = "RetentionDays"
    DATA_SOURCE_ROLE_ARN = "DataSourceRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dashboard_viewer_principals": "DashboardViewerPrincipals",
        "application_arn": "ApplicationARN",
        "kms_key_arn": "KmsKeyArn",
        "retention_days": "RetentionDays",
        "data_source_role_arn": "DataSourceRoleArn",
    }

    dashboard_viewer_principals: Optional[Union[list[str], Ref]] = None
    application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    data_source_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceConfig(PropertyType):
    OPEN_SEARCH_RESOURCE_CONFIG = "OpenSearchResourceConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "open_search_resource_config": "OpenSearchResourceConfig",
    }

    open_search_resource_config: Optional[OpenSearchResourceConfig] = None

