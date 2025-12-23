"""PropertyTypes for AWS::DataZone::ProjectProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsAccount(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_account_id": "AwsAccountId",
    }

    aws_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "environment_configuration_id": "EnvironmentConfigurationId",
        "aws_region": "AwsRegion",
        "aws_account": "AwsAccount",
        "deployment_mode": "DeploymentMode",
        "environment_blueprint_id": "EnvironmentBlueprintId",
        "configuration_parameters": "ConfigurationParameters",
        "deployment_order": "DeploymentOrder",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment_configuration_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_region: Optional[Region] = None
    aws_account: Optional[AwsAccount] = None
    deployment_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment_blueprint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_parameters: Optional[EnvironmentConfigurationParametersDetails] = None
    deployment_order: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentConfigurationParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_editable": "IsEditable",
        "value": "Value",
        "name": "Name",
    }

    is_editable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentConfigurationParametersDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_overrides": "ParameterOverrides",
        "resolved_parameters": "ResolvedParameters",
        "ssm_path": "SsmPath",
    }

    parameter_overrides: Optional[list[EnvironmentConfigurationParameter]] = None
    resolved_parameters: Optional[list[EnvironmentConfigurationParameter]] = None
    ssm_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Region(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

