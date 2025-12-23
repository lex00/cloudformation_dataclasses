"""PropertyTypes for AWS::GameLift::ContainerFleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionPortRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protection_strategy": "ProtectionStrategy",
        "impairment_strategy": "ImpairmentStrategy",
        "minimum_healthy_percentage": "MinimumHealthyPercentage",
    }

    protection_strategy: Optional[Union[str, DeploymentProtectionStrategy, Ref, GetAtt, Sub]] = None
    impairment_strategy: Optional[Union[str, DeploymentImpairmentStrategy, Ref, GetAtt, Sub]] = None
    minimum_healthy_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "latest_deployment_id": "LatestDeploymentId",
    }

    latest_deployment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GameSessionCreationLimitPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_period_in_minutes": "PolicyPeriodInMinutes",
        "new_game_sessions_per_creator": "NewGameSessionsPerCreator",
    }

    policy_period_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    new_game_sessions_per_creator: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IpPermission(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "location_capacity": "LocationCapacity",
        "stopped_actions": "StoppedActions",
        "location": "Location",
    }

    location_capacity: Optional[LocationCapacity] = None
    stopped_actions: Optional[Union[list[str], Ref]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_destination": "LogDestination",
        "s3_bucket_name": "S3BucketName",
        "log_group_arn": "LogGroupArn",
    }

    log_destination: Optional[Union[str, LogDestination, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "policy_type": "PolicyType",
        "comparison_operator": "ComparisonOperator",
        "target_configuration": "TargetConfiguration",
        "scaling_adjustment": "ScalingAdjustment",
        "evaluation_periods": "EvaluationPeriods",
        "name": "Name",
        "scaling_adjustment_type": "ScalingAdjustmentType",
        "threshold": "Threshold",
    }

    metric_name: Optional[Union[str, MetricName, Ref, GetAtt, Sub]] = None
    policy_type: Optional[Union[str, PolicyType, Ref, GetAtt, Sub]] = None
    comparison_operator: Optional[Union[str, ComparisonOperatorType, Ref, GetAtt, Sub]] = None
    target_configuration: Optional[TargetConfiguration] = None
    scaling_adjustment: Optional[Union[int, Ref, GetAtt, Sub]] = None
    evaluation_periods: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scaling_adjustment_type: Optional[Union[str, ScalingAdjustmentType, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TargetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_value": "TargetValue",
    }

    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None

