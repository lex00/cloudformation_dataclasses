"""PropertyTypes for AWS::SSMQuickSetup::ConfigurationManager."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigurationDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "parameters": "Parameters",
        "local_deployment_execution_role_name": "LocalDeploymentExecutionRoleName",
        "type_version": "TypeVersion",
        "local_deployment_administration_role_arn": "LocalDeploymentAdministrationRoleArn",
        "id": "id",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[dict[str, str]] = None
    local_deployment_execution_role_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_deployment_administration_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StatusSummary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "last_updated_at": "LastUpdatedAt",
        "status_type": "StatusType",
        "status_details": "StatusDetails",
        "status_message": "StatusMessage",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_details: Optional[dict[str, str]] = None
    status_message: Optional[Union[str, Ref, GetAtt, Sub]] = None

