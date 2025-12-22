"""PropertyTypes for AWS::ARCRegionSwitch::Plan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ArcRoutingControlConfiguration(PropertyType):
    REGION_AND_ROUTING_CONTROLS = "RegionAndRoutingControls"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    EXTERNAL_ID = "ExternalId"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region_and_routing_controls": "RegionAndRoutingControls",
        "timeout_minutes": "TimeoutMinutes",
        "external_id": "ExternalId",
        "cross_account_role": "CrossAccountRole",
    }

    region_and_routing_controls: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Asg(PropertyType):
    EXTERNAL_ID = "ExternalId"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_id": "ExternalId",
        "cross_account_role": "CrossAccountRole",
        "arn": "Arn",
    }

    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssociatedAlarm(PropertyType):
    RESOURCE_IDENTIFIER = "ResourceIdentifier"
    EXTERNAL_ID = "ExternalId"
    ALARM_TYPE = "AlarmType"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_identifier": "ResourceIdentifier",
        "external_id": "ExternalId",
        "alarm_type": "AlarmType",
        "cross_account_role": "CrossAccountRole",
    }

    resource_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alarm_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomActionLambdaConfiguration(PropertyType):
    LAMBDAS = "Lambdas"
    RETRY_INTERVAL_MINUTES = "RetryIntervalMinutes"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    REGION_TO_RUN = "RegionToRun"
    UNGRACEFUL = "Ungraceful"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambdas": "Lambdas",
        "retry_interval_minutes": "RetryIntervalMinutes",
        "timeout_minutes": "TimeoutMinutes",
        "region_to_run": "RegionToRun",
        "ungraceful": "Ungraceful",
    }

    lambdas: Optional[list[Lambdas]] = None
    retry_interval_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    region_to_run: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ungraceful: Optional[LambdaUngraceful] = None


@dataclass
class Ec2AsgCapacityIncreaseConfiguration(PropertyType):
    ASGS = "Asgs"
    CAPACITY_MONITORING_APPROACH = "CapacityMonitoringApproach"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    UNGRACEFUL = "Ungraceful"
    TARGET_PERCENT = "TargetPercent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "asgs": "Asgs",
        "capacity_monitoring_approach": "CapacityMonitoringApproach",
        "timeout_minutes": "TimeoutMinutes",
        "ungraceful": "Ungraceful",
        "target_percent": "TargetPercent",
    }

    asgs: Optional[list[Asg]] = None
    capacity_monitoring_approach: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ungraceful: Optional[Ec2Ungraceful] = None
    target_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Ec2Ungraceful(PropertyType):
    MINIMUM_SUCCESS_PERCENTAGE = "MinimumSuccessPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_success_percentage": "MinimumSuccessPercentage",
    }

    minimum_success_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class EcsCapacityIncreaseConfiguration(PropertyType):
    SERVICES = "Services"
    CAPACITY_MONITORING_APPROACH = "CapacityMonitoringApproach"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    UNGRACEFUL = "Ungraceful"
    TARGET_PERCENT = "TargetPercent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "services": "Services",
        "capacity_monitoring_approach": "CapacityMonitoringApproach",
        "timeout_minutes": "TimeoutMinutes",
        "ungraceful": "Ungraceful",
        "target_percent": "TargetPercent",
    }

    services: Optional[list[Service]] = None
    capacity_monitoring_approach: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ungraceful: Optional[EcsUngraceful] = None
    target_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class EcsUngraceful(PropertyType):
    MINIMUM_SUCCESS_PERCENTAGE = "MinimumSuccessPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_success_percentage": "MinimumSuccessPercentage",
    }

    minimum_success_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class EksCluster(PropertyType):
    CLUSTER_ARN = "ClusterArn"
    EXTERNAL_ID = "ExternalId"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_arn": "ClusterArn",
        "external_id": "ExternalId",
        "cross_account_role": "CrossAccountRole",
    }

    cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksResourceScalingConfiguration(PropertyType):
    KUBERNETES_RESOURCE_TYPE = "KubernetesResourceType"
    CAPACITY_MONITORING_APPROACH = "CapacityMonitoringApproach"
    EKS_CLUSTERS = "EksClusters"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    SCALING_RESOURCES = "ScalingResources"
    UNGRACEFUL = "Ungraceful"
    TARGET_PERCENT = "TargetPercent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kubernetes_resource_type": "KubernetesResourceType",
        "capacity_monitoring_approach": "CapacityMonitoringApproach",
        "eks_clusters": "EksClusters",
        "timeout_minutes": "TimeoutMinutes",
        "scaling_resources": "ScalingResources",
        "ungraceful": "Ungraceful",
        "target_percent": "TargetPercent",
    }

    kubernetes_resource_type: Optional[KubernetesResourceType] = None
    capacity_monitoring_approach: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    eks_clusters: Optional[list[EksCluster]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    scaling_resources: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    ungraceful: Optional[EksResourceScalingUngraceful] = None
    target_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class EksResourceScalingUngraceful(PropertyType):
    MINIMUM_SUCCESS_PERCENTAGE = "MinimumSuccessPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_success_percentage": "MinimumSuccessPercentage",
    }

    minimum_success_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ExecutionApprovalConfiguration(PropertyType):
    TIMEOUT_MINUTES = "TimeoutMinutes"
    APPROVAL_ROLE = "ApprovalRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_minutes": "TimeoutMinutes",
        "approval_role": "ApprovalRole",
    }

    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    approval_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExecutionBlockConfiguration(PropertyType):
    GLOBAL_AURORA_CONFIG = "GlobalAuroraConfig"
    ROUTE53_HEALTH_CHECK_CONFIG = "Route53HealthCheckConfig"
    ARC_ROUTING_CONTROL_CONFIG = "ArcRoutingControlConfig"
    PARALLEL_CONFIG = "ParallelConfig"
    EKS_RESOURCE_SCALING_CONFIG = "EksResourceScalingConfig"
    ECS_CAPACITY_INCREASE_CONFIG = "EcsCapacityIncreaseConfig"
    CUSTOM_ACTION_LAMBDA_CONFIG = "CustomActionLambdaConfig"
    EXECUTION_APPROVAL_CONFIG = "ExecutionApprovalConfig"
    EC2_ASG_CAPACITY_INCREASE_CONFIG = "Ec2AsgCapacityIncreaseConfig"
    REGION_SWITCH_PLAN_CONFIG = "RegionSwitchPlanConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "global_aurora_config": "GlobalAuroraConfig",
        "route53_health_check_config": "Route53HealthCheckConfig",
        "arc_routing_control_config": "ArcRoutingControlConfig",
        "parallel_config": "ParallelConfig",
        "eks_resource_scaling_config": "EksResourceScalingConfig",
        "ecs_capacity_increase_config": "EcsCapacityIncreaseConfig",
        "custom_action_lambda_config": "CustomActionLambdaConfig",
        "execution_approval_config": "ExecutionApprovalConfig",
        "ec2_asg_capacity_increase_config": "Ec2AsgCapacityIncreaseConfig",
        "region_switch_plan_config": "RegionSwitchPlanConfig",
    }

    global_aurora_config: Optional[GlobalAuroraConfiguration] = None
    route53_health_check_config: Optional[Route53HealthCheckConfiguration] = None
    arc_routing_control_config: Optional[ArcRoutingControlConfiguration] = None
    parallel_config: Optional[ParallelExecutionBlockConfiguration] = None
    eks_resource_scaling_config: Optional[EksResourceScalingConfiguration] = None
    ecs_capacity_increase_config: Optional[EcsCapacityIncreaseConfiguration] = None
    custom_action_lambda_config: Optional[CustomActionLambdaConfiguration] = None
    execution_approval_config: Optional[ExecutionApprovalConfiguration] = None
    ec2_asg_capacity_increase_config: Optional[Ec2AsgCapacityIncreaseConfiguration] = None
    region_switch_plan_config: Optional[RegionSwitchPlanConfiguration] = None


@dataclass
class GlobalAuroraConfiguration(PropertyType):
    DATABASE_CLUSTER_ARNS = "DatabaseClusterArns"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    EXTERNAL_ID = "ExternalId"
    BEHAVIOR = "Behavior"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"
    UNGRACEFUL = "Ungraceful"
    GLOBAL_CLUSTER_IDENTIFIER = "GlobalClusterIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_cluster_arns": "DatabaseClusterArns",
        "timeout_minutes": "TimeoutMinutes",
        "external_id": "ExternalId",
        "behavior": "Behavior",
        "cross_account_role": "CrossAccountRole",
        "ungraceful": "Ungraceful",
        "global_cluster_identifier": "GlobalClusterIdentifier",
    }

    database_cluster_arns: Optional[Union[list[str], Ref]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    behavior: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ungraceful: Optional[GlobalAuroraUngraceful] = None
    global_cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GlobalAuroraUngraceful(PropertyType):
    UNGRACEFUL = "Ungraceful"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ungraceful": "Ungraceful",
    }

    ungraceful: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KubernetesResourceType(PropertyType):
    API_VERSION = "ApiVersion"
    KIND = "Kind"

    _property_mappings: ClassVar[dict[str, str]] = {
        "api_version": "ApiVersion",
        "kind": "Kind",
    }

    api_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kind: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaUngraceful(PropertyType):
    BEHAVIOR = "Behavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "behavior": "Behavior",
    }

    behavior: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class Lambdas(PropertyType):
    EXTERNAL_ID = "ExternalId"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_id": "ExternalId",
        "cross_account_role": "CrossAccountRole",
        "arn": "Arn",
    }

    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParallelExecutionBlockConfiguration(PropertyType):
    STEPS = "Steps"

    _property_mappings: ClassVar[dict[str, str]] = {
        "steps": "Steps",
    }

    steps: Optional[list[Step]] = None


@dataclass
class RegionSwitchPlanConfiguration(PropertyType):
    EXTERNAL_ID = "ExternalId"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_id": "ExternalId",
        "cross_account_role": "CrossAccountRole",
        "arn": "Arn",
    }

    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Route53HealthCheckConfiguration(PropertyType):
    RECORD_NAME = "RecordName"
    TIMEOUT_MINUTES = "TimeoutMinutes"
    EXTERNAL_ID = "ExternalId"
    HOSTED_ZONE_ID = "HostedZoneId"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"
    RECORD_SETS = "RecordSets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "record_name": "RecordName",
        "timeout_minutes": "TimeoutMinutes",
        "external_id": "ExternalId",
        "hosted_zone_id": "HostedZoneId",
        "cross_account_role": "CrossAccountRole",
        "record_sets": "RecordSets",
    }

    record_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_minutes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_sets: Optional[list[Route53ResourceRecordSet]] = None


@dataclass
class Route53ResourceRecordSet(PropertyType):
    REGION = "Region"
    RECORD_SET_IDENTIFIER = "RecordSetIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
        "record_set_identifier": "RecordSetIdentifier",
    }

    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Service(PropertyType):
    CLUSTER_ARN = "ClusterArn"
    EXTERNAL_ID = "ExternalId"
    SERVICE_ARN = "ServiceArn"
    CROSS_ACCOUNT_ROLE = "CrossAccountRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_arn": "ClusterArn",
        "external_id": "ExternalId",
        "service_arn": "ServiceArn",
        "cross_account_role": "CrossAccountRole",
    }

    cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Step(PropertyType):
    DESCRIPTION = "Description"
    EXECUTION_BLOCK_TYPE = "ExecutionBlockType"
    EXECUTION_BLOCK_CONFIGURATION = "ExecutionBlockConfiguration"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "execution_block_type": "ExecutionBlockType",
        "execution_block_configuration": "ExecutionBlockConfiguration",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_block_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_block_configuration: Optional[ExecutionBlockConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Trigger(PropertyType):
    TARGET_REGION = "TargetRegion"
    ACTION = "Action"
    MIN_DELAY_MINUTES_BETWEEN_EXECUTIONS = "MinDelayMinutesBetweenExecutions"
    DESCRIPTION = "Description"
    CONDITIONS = "Conditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_region": "TargetRegion",
        "action": "Action",
        "min_delay_minutes_between_executions": "MinDelayMinutesBetweenExecutions",
        "description": "Description",
        "conditions": "Conditions",
    }

    target_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_delay_minutes_between_executions: Optional[Union[float, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    conditions: Optional[list[TriggerCondition]] = None


@dataclass
class TriggerCondition(PropertyType):
    CONDITION = "Condition"
    ASSOCIATED_ALARM_NAME = "AssociatedAlarmName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "associated_alarm_name": "AssociatedAlarmName",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    associated_alarm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Workflow(PropertyType):
    STEPS = "Steps"
    WORKFLOW_TARGET_ACTION = "WorkflowTargetAction"
    WORKFLOW_DESCRIPTION = "WorkflowDescription"
    WORKFLOW_TARGET_REGION = "WorkflowTargetRegion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "steps": "Steps",
        "workflow_target_action": "WorkflowTargetAction",
        "workflow_description": "WorkflowDescription",
        "workflow_target_region": "WorkflowTargetRegion",
    }

    steps: Optional[list[Step]] = None
    workflow_target_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workflow_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workflow_target_region: Optional[Union[str, Ref, GetAtt, Sub]] = None

