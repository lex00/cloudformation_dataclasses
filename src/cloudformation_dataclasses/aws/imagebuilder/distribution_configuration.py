"""PropertyTypes for AWS::ImageBuilder::DistributionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmiDistributionConfiguration(PropertyType):
    AMI_TAGS = "AmiTags"
    DESCRIPTION = "Description"
    KMS_KEY_ID = "KmsKeyId"
    LAUNCH_PERMISSION_CONFIGURATION = "LaunchPermissionConfiguration"
    TARGET_ACCOUNT_IDS = "TargetAccountIds"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ami_tags": "AmiTags",
        "description": "Description",
        "kms_key_id": "KmsKeyId",
        "launch_permission_configuration": "LaunchPermissionConfiguration",
        "target_account_ids": "TargetAccountIds",
        "name": "Name",
    }

    ami_tags: Optional[dict[str, str]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_permission_configuration: Optional[LaunchPermissionConfiguration] = None
    target_account_ids: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerDistributionConfiguration(PropertyType):
    TARGET_REPOSITORY = "TargetRepository"
    CONTAINER_TAGS = "ContainerTags"
    DESCRIPTION = "Description"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_repository": "TargetRepository",
        "container_tags": "ContainerTags",
        "description": "Description",
    }

    target_repository: Optional[TargetContainerRepository] = None
    container_tags: Optional[Union[list[str], Ref]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Distribution(PropertyType):
    AMI_DISTRIBUTION_CONFIGURATION = "AmiDistributionConfiguration"
    CONTAINER_DISTRIBUTION_CONFIGURATION = "ContainerDistributionConfiguration"
    FAST_LAUNCH_CONFIGURATIONS = "FastLaunchConfigurations"
    LAUNCH_TEMPLATE_CONFIGURATIONS = "LaunchTemplateConfigurations"
    LICENSE_CONFIGURATION_ARNS = "LicenseConfigurationArns"
    REGION = "Region"
    SSM_PARAMETER_CONFIGURATIONS = "SsmParameterConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ami_distribution_configuration": "AmiDistributionConfiguration",
        "container_distribution_configuration": "ContainerDistributionConfiguration",
        "fast_launch_configurations": "FastLaunchConfigurations",
        "launch_template_configurations": "LaunchTemplateConfigurations",
        "license_configuration_arns": "LicenseConfigurationArns",
        "region": "Region",
        "ssm_parameter_configurations": "SsmParameterConfigurations",
    }

    ami_distribution_configuration: Optional[AmiDistributionConfiguration] = None
    container_distribution_configuration: Optional[ContainerDistributionConfiguration] = None
    fast_launch_configurations: Optional[list[FastLaunchConfiguration]] = None
    launch_template_configurations: Optional[list[LaunchTemplateConfiguration]] = None
    license_configuration_arns: Optional[Union[list[str], Ref]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssm_parameter_configurations: Optional[list[SsmParameterConfiguration]] = None


@dataclass
class FastLaunchConfiguration(PropertyType):
    ACCOUNT_ID = "AccountId"
    LAUNCH_TEMPLATE = "LaunchTemplate"
    ENABLED = "Enabled"
    MAX_PARALLEL_LAUNCHES = "MaxParallelLaunches"
    SNAPSHOT_CONFIGURATION = "SnapshotConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_id": "AccountId",
        "launch_template": "LaunchTemplate",
        "enabled": "Enabled",
        "max_parallel_launches": "MaxParallelLaunches",
        "snapshot_configuration": "SnapshotConfiguration",
    }

    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template: Optional[FastLaunchLaunchTemplateSpecification] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_parallel_launches: Optional[Union[int, Ref, GetAtt, Sub]] = None
    snapshot_configuration: Optional[FastLaunchSnapshotConfiguration] = None


@dataclass
class FastLaunchLaunchTemplateSpecification(PropertyType):
    LAUNCH_TEMPLATE_NAME = "LaunchTemplateName"
    LAUNCH_TEMPLATE_VERSION = "LaunchTemplateVersion"
    LAUNCH_TEMPLATE_ID = "LaunchTemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "launch_template_name": "LaunchTemplateName",
        "launch_template_version": "LaunchTemplateVersion",
        "launch_template_id": "LaunchTemplateId",
    }

    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FastLaunchSnapshotConfiguration(PropertyType):
    TARGET_RESOURCE_COUNT = "TargetResourceCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_resource_count": "TargetResourceCount",
    }

    target_resource_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchPermissionConfiguration(PropertyType):
    ORGANIZATION_ARNS = "OrganizationArns"
    ORGANIZATIONAL_UNIT_ARNS = "OrganizationalUnitArns"
    USER_IDS = "UserIds"
    USER_GROUPS = "UserGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "organization_arns": "OrganizationArns",
        "organizational_unit_arns": "OrganizationalUnitArns",
        "user_ids": "UserIds",
        "user_groups": "UserGroups",
    }

    organization_arns: Optional[Union[list[str], Ref]] = None
    organizational_unit_arns: Optional[Union[list[str], Ref]] = None
    user_ids: Optional[Union[list[str], Ref]] = None
    user_groups: Optional[Union[list[str], Ref]] = None


@dataclass
class LaunchTemplateConfiguration(PropertyType):
    SET_DEFAULT_VERSION = "SetDefaultVersion"
    ACCOUNT_ID = "AccountId"
    LAUNCH_TEMPLATE_ID = "LaunchTemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "set_default_version": "SetDefaultVersion",
        "account_id": "AccountId",
        "launch_template_id": "LaunchTemplateId",
    }

    set_default_version: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SsmParameterConfiguration(PropertyType):
    DATA_TYPE = "DataType"
    PARAMETER_NAME = "ParameterName"
    AMI_ACCOUNT_ID = "AmiAccountId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_type": "DataType",
        "parameter_name": "ParameterName",
        "ami_account_id": "AmiAccountId",
    }

    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ami_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetContainerRepository(PropertyType):
    SERVICE = "Service"
    REPOSITORY_NAME = "RepositoryName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service": "Service",
        "repository_name": "RepositoryName",
    }

    service: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

