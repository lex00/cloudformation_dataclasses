"""PropertyTypes for AWS::ECS::ExpressGatewayService."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoScalingArns(PropertyType):
    SCALABLE_TARGET = "ScalableTarget"
    APPLICATION_AUTO_SCALING_POLICIES = "ApplicationAutoScalingPolicies"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scalable_target": "ScalableTarget",
        "application_auto_scaling_policies": "ApplicationAutoScalingPolicies",
    }

    scalable_target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_auto_scaling_policies: Optional[Union[list[str], Ref]] = None


@dataclass
class ECSManagedResourceArns(PropertyType):
    LOG_GROUPS = "LogGroups"
    SERVICE_SECURITY_GROUPS = "ServiceSecurityGroups"
    METRIC_ALARMS = "MetricAlarms"
    INGRESS_PATH = "IngressPath"
    AUTO_SCALING = "AutoScaling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_groups": "LogGroups",
        "service_security_groups": "ServiceSecurityGroups",
        "metric_alarms": "MetricAlarms",
        "ingress_path": "IngressPath",
        "auto_scaling": "AutoScaling",
    }

    log_groups: Optional[Union[list[str], Ref]] = None
    service_security_groups: Optional[Union[list[str], Ref]] = None
    metric_alarms: Optional[Union[list[str], Ref]] = None
    ingress_path: Optional[IngressPathArns] = None
    auto_scaling: Optional[AutoScalingArns] = None


@dataclass
class ExpressGatewayContainer(PropertyType):
    REPOSITORY_CREDENTIALS = "RepositoryCredentials"
    SECRETS = "Secrets"
    COMMAND = "Command"
    AWS_LOGS_CONFIGURATION = "AwsLogsConfiguration"
    CONTAINER_PORT = "ContainerPort"
    ENVIRONMENT = "Environment"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_credentials": "RepositoryCredentials",
        "secrets": "Secrets",
        "command": "Command",
        "aws_logs_configuration": "AwsLogsConfiguration",
        "container_port": "ContainerPort",
        "environment": "Environment",
        "image": "Image",
    }

    repository_credentials: Optional[ExpressGatewayRepositoryCredentials] = None
    secrets: Optional[list[Secret]] = None
    command: Optional[Union[list[str], Ref]] = None
    aws_logs_configuration: Optional[ExpressGatewayServiceAwsLogsConfiguration] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    environment: Optional[list[KeyValuePair]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayRepositoryCredentials(PropertyType):
    CREDENTIALS_PARAMETER = "CredentialsParameter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credentials_parameter": "CredentialsParameter",
    }

    credentials_parameter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayScalingTarget(PropertyType):
    MIN_TASK_COUNT = "MinTaskCount"
    AUTO_SCALING_METRIC = "AutoScalingMetric"
    AUTO_SCALING_TARGET_VALUE = "AutoScalingTargetValue"
    MAX_TASK_COUNT = "MaxTaskCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_task_count": "MinTaskCount",
        "auto_scaling_metric": "AutoScalingMetric",
        "auto_scaling_target_value": "AutoScalingTargetValue",
        "max_task_count": "MaxTaskCount",
    }

    min_task_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_scaling_metric: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_scaling_target_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_task_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayServiceAwsLogsConfiguration(PropertyType):
    LOG_STREAM_PREFIX = "LogStreamPrefix"
    LOG_GROUP = "LogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_prefix": "LogStreamPrefix",
        "log_group": "LogGroup",
    }

    log_stream_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExpressGatewayServiceConfiguration(PropertyType):
    SERVICE_REVISION_ARN = "ServiceRevisionArn"
    EXECUTION_ROLE_ARN = "ExecutionRoleArn"
    TASK_ROLE_ARN = "TaskRoleArn"
    SCALING_TARGET = "ScalingTarget"
    INGRESS_PATHS = "IngressPaths"
    PRIMARY_CONTAINER = "PrimaryContainer"
    MEMORY = "Memory"
    HEALTH_CHECK_PATH = "HealthCheckPath"
    CREATED_AT = "CreatedAt"
    CPU = "Cpu"
    NETWORK_CONFIGURATION = "NetworkConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_revision_arn": "ServiceRevisionArn",
        "execution_role_arn": "ExecutionRoleArn",
        "task_role_arn": "TaskRoleArn",
        "scaling_target": "ScalingTarget",
        "ingress_paths": "IngressPaths",
        "primary_container": "PrimaryContainer",
        "memory": "Memory",
        "health_check_path": "HealthCheckPath",
        "created_at": "CreatedAt",
        "cpu": "Cpu",
        "network_configuration": "NetworkConfiguration",
    }

    service_revision_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scaling_target: Optional[ExpressGatewayScalingTarget] = None
    ingress_paths: Optional[list[IngressPathSummary]] = None
    primary_container: Optional[ExpressGatewayContainer] = None
    memory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    health_check_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_at: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_configuration: Optional[ExpressGatewayServiceNetworkConfiguration] = None


@dataclass
class ExpressGatewayServiceNetworkConfiguration(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None


@dataclass
class ExpressGatewayServiceStatus(PropertyType):
    STATUS_CODE = "StatusCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status_code": "StatusCode",
    }

    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressPathArns(PropertyType):
    LISTENER_ARN = "ListenerArn"
    LOAD_BALANCER_ARN = "LoadBalancerArn"
    TARGET_GROUP_ARNS = "TargetGroupArns"
    LISTENER_RULE_ARN = "ListenerRuleArn"
    LOAD_BALANCER_SECURITY_GROUPS = "LoadBalancerSecurityGroups"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "listener_arn": "ListenerArn",
        "load_balancer_arn": "LoadBalancerArn",
        "target_group_arns": "TargetGroupArns",
        "listener_rule_arn": "ListenerRuleArn",
        "load_balancer_security_groups": "LoadBalancerSecurityGroups",
        "certificate_arn": "CertificateArn",
    }

    listener_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_group_arns: Optional[Union[list[str], Ref]] = None
    listener_rule_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_security_groups: Optional[Union[list[str], Ref]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IngressPathSummary(PropertyType):
    ENDPOINT = "Endpoint"
    ACCESS_TYPE = "AccessType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "access_type": "AccessType",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValuePair(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Secret(PropertyType):
    VALUE_FROM = "ValueFrom"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_from": "ValueFrom",
        "name": "Name",
    }

    value_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

