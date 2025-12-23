"""PropertyTypes for AWS::GameLift::Fleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnywhereConfiguration(PropertyType):
    COST = "Cost"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cost": "Cost",
    }

    cost: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CertificateConfiguration(PropertyType):
    CERTIFICATE_TYPE = "CertificateType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_type": "CertificateType",
    }

    certificate_type: Optional[Union[str, CertificateType, Ref, GetAtt, Sub]] = None


@dataclass
class IpPermission(PropertyType):
    IP_RANGE = "IpRange"
    FROM_PORT = "FromPort"
    TO_PORT = "ToPort"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_range": "IpRange",
        "from_port": "FromPort",
        "to_port": "ToPort",
        "protocol": "Protocol",
    }

    ip_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, IpProtocol, Ref, GetAtt, Sub]] = None


@dataclass
class LocationCapacity(PropertyType):
    MIN_SIZE = "MinSize"
    DESIRED_EC2_INSTANCES = "DesiredEC2Instances"
    MAX_SIZE = "MaxSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_size": "MinSize",
        "desired_ec2_instances": "DesiredEC2Instances",
        "max_size": "MaxSize",
    }

    min_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    desired_ec2_instances: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LocationConfiguration(PropertyType):
    LOCATION_CAPACITY = "LocationCapacity"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "location_capacity": "LocationCapacity",
        "location": "Location",
    }

    location_capacity: Optional[LocationCapacity] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceCreationLimitPolicy(PropertyType):
    POLICY_PERIOD_IN_MINUTES = "PolicyPeriodInMinutes"
    NEW_GAME_SESSIONS_PER_CREATOR = "NewGameSessionsPerCreator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_period_in_minutes": "PolicyPeriodInMinutes",
        "new_game_sessions_per_creator": "NewGameSessionsPerCreator",
    }

    policy_period_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    new_game_sessions_per_creator: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RuntimeConfiguration(PropertyType):
    SERVER_PROCESSES = "ServerProcesses"
    MAX_CONCURRENT_GAME_SESSION_ACTIVATIONS = "MaxConcurrentGameSessionActivations"
    GAME_SESSION_ACTIVATION_TIMEOUT_SECONDS = "GameSessionActivationTimeoutSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_processes": "ServerProcesses",
        "max_concurrent_game_session_activations": "MaxConcurrentGameSessionActivations",
        "game_session_activation_timeout_seconds": "GameSessionActivationTimeoutSeconds",
    }

    server_processes: Optional[list[ServerProcess]] = None
    max_concurrent_game_session_activations: Optional[Union[int, Ref, GetAtt, Sub]] = None
    game_session_activation_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingPolicy(PropertyType):
    STATUS = "Status"
    METRIC_NAME = "MetricName"
    POLICY_TYPE = "PolicyType"
    COMPARISON_OPERATOR = "ComparisonOperator"
    TARGET_CONFIGURATION = "TargetConfiguration"
    UPDATE_STATUS = "UpdateStatus"
    SCALING_ADJUSTMENT = "ScalingAdjustment"
    EVALUATION_PERIODS = "EvaluationPeriods"
    LOCATION = "Location"
    NAME = "Name"
    SCALING_ADJUSTMENT_TYPE = "ScalingAdjustmentType"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "metric_name": "MetricName",
        "policy_type": "PolicyType",
        "comparison_operator": "ComparisonOperator",
        "target_configuration": "TargetConfiguration",
        "update_status": "UpdateStatus",
        "scaling_adjustment": "ScalingAdjustment",
        "evaluation_periods": "EvaluationPeriods",
        "location": "Location",
        "name": "Name",
        "scaling_adjustment_type": "ScalingAdjustmentType",
        "threshold": "Threshold",
    }

    status: Optional[Union[str, ScalingStatusType, Ref, GetAtt, Sub]] = None
    metric_name: Optional[Union[str, MetricName, Ref, GetAtt, Sub]] = None
    policy_type: Optional[Union[str, PolicyType, Ref, GetAtt, Sub]] = None
    comparison_operator: Optional[Union[str, ComparisonOperatorType, Ref, GetAtt, Sub]] = None
    target_configuration: Optional[TargetConfiguration] = None
    update_status: Optional[Union[str, LocationUpdateStatus, Ref, GetAtt, Sub]] = None
    scaling_adjustment: Optional[Union[int, Ref, GetAtt, Sub]] = None
    evaluation_periods: Optional[Union[int, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scaling_adjustment_type: Optional[Union[str, ScalingAdjustmentType, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ServerProcess(PropertyType):
    CONCURRENT_EXECUTIONS = "ConcurrentExecutions"
    PARAMETERS = "Parameters"
    LAUNCH_PATH = "LaunchPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "concurrent_executions": "ConcurrentExecutions",
        "parameters": "Parameters",
        "launch_path": "LaunchPath",
    }

    concurrent_executions: Optional[Union[int, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    launch_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetConfiguration(PropertyType):
    TARGET_VALUE = "TargetValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
    }

    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None

