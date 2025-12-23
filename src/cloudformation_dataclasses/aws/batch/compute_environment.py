"""PropertyTypes for AWS::Batch::ComputeEnvironment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComputeResources(PropertyType):
    SPOT_IAM_FLEET_ROLE = "SpotIamFleetRole"
    MAXV_CPUS = "MaxvCpus"
    EC2_CONFIGURATION = "Ec2Configuration"
    BID_PERCENTAGE = "BidPercentage"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    ALLOCATION_STRATEGY = "AllocationStrategy"
    SUBNETS = "Subnets"
    TYPE = "Type"
    MINV_CPUS = "MinvCpus"
    UPDATE_TO_LATEST_IMAGE_VERSION = "UpdateToLatestImageVersion"
    LAUNCH_TEMPLATE = "LaunchTemplate"
    IMAGE_ID = "ImageId"
    INSTANCE_ROLE = "InstanceRole"
    INSTANCE_TYPES = "InstanceTypes"
    EC2_KEY_PAIR = "Ec2KeyPair"
    PLACEMENT_GROUP = "PlacementGroup"
    TAGS = "Tags"
    DESIREDV_CPUS = "DesiredvCpus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "spot_iam_fleet_role": "SpotIamFleetRole",
        "maxv_cpus": "MaxvCpus",
        "ec2_configuration": "Ec2Configuration",
        "bid_percentage": "BidPercentage",
        "security_group_ids": "SecurityGroupIds",
        "allocation_strategy": "AllocationStrategy",
        "subnets": "Subnets",
        "type_": "Type",
        "minv_cpus": "MinvCpus",
        "update_to_latest_image_version": "UpdateToLatestImageVersion",
        "launch_template": "LaunchTemplate",
        "image_id": "ImageId",
        "instance_role": "InstanceRole",
        "instance_types": "InstanceTypes",
        "ec2_key_pair": "Ec2KeyPair",
        "placement_group": "PlacementGroup",
        "tags": "Tags",
        "desiredv_cpus": "DesiredvCpus",
    }

    spot_iam_fleet_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maxv_cpus: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ec2_configuration: Optional[list[Ec2ConfigurationObject]] = None
    bid_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    allocation_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnets: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minv_cpus: Optional[Union[int, Ref, GetAtt, Sub]] = None
    update_to_latest_image_version: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    launch_template: Optional[LaunchTemplateSpecification] = None
    image_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_types: Optional[Union[list[str], Ref]] = None
    ec2_key_pair: Optional[Union[str, Ref, GetAtt, Sub]] = None
    placement_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[dict[str, str]] = None
    desiredv_cpus: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Ec2ConfigurationObject(PropertyType):
    IMAGE_ID_OVERRIDE = "ImageIdOverride"
    IMAGE_KUBERNETES_VERSION = "ImageKubernetesVersion"
    IMAGE_TYPE = "ImageType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_id_override": "ImageIdOverride",
        "image_kubernetes_version": "ImageKubernetesVersion",
        "image_type": "ImageType",
    }

    image_id_override: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_kubernetes_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksConfiguration(PropertyType):
    EKS_CLUSTER_ARN = "EksClusterArn"
    KUBERNETES_NAMESPACE = "KubernetesNamespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "eks_cluster_arn": "EksClusterArn",
        "kubernetes_namespace": "KubernetesNamespace",
    }

    eks_cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kubernetes_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    USERDATA_TYPE = "UserdataType"
    LAUNCH_TEMPLATE_NAME = "LaunchTemplateName"
    VERSION = "Version"
    OVERRIDES = "Overrides"
    LAUNCH_TEMPLATE_ID = "LaunchTemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "userdata_type": "UserdataType",
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "overrides": "Overrides",
        "launch_template_id": "LaunchTemplateId",
    }

    userdata_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overrides: Optional[list[LaunchTemplateSpecificationOverride]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchTemplateSpecificationOverride(PropertyType):
    TARGET_INSTANCE_TYPES = "TargetInstanceTypes"
    USERDATA_TYPE = "UserdataType"
    LAUNCH_TEMPLATE_NAME = "LaunchTemplateName"
    VERSION = "Version"
    LAUNCH_TEMPLATE_ID = "LaunchTemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_instance_types": "TargetInstanceTypes",
        "userdata_type": "UserdataType",
        "launch_template_name": "LaunchTemplateName",
        "version": "Version",
        "launch_template_id": "LaunchTemplateId",
    }

    target_instance_types: Optional[Union[list[str], Ref]] = None
    userdata_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdatePolicy(PropertyType):
    JOB_EXECUTION_TIMEOUT_MINUTES = "JobExecutionTimeoutMinutes"
    TERMINATE_JOBS_ON_UPDATE = "TerminateJobsOnUpdate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "job_execution_timeout_minutes": "JobExecutionTimeoutMinutes",
        "terminate_jobs_on_update": "TerminateJobsOnUpdate",
    }

    job_execution_timeout_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    terminate_jobs_on_update: Optional[Union[bool, Ref, GetAtt, Sub]] = None

