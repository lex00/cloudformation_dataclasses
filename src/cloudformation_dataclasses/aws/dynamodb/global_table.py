"""PropertyTypes for AWS::DynamoDB::GlobalTable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_type": "AttributeType",
        "attribute_name": "AttributeName",
    }

    attribute_type: Optional[Union[str, AttributeType, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityAutoScalingSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_capacity": "MinCapacity",
        "seed_capacity": "SeedCapacity",
        "target_tracking_scaling_policy_configuration": "TargetTrackingScalingPolicyConfiguration",
        "max_capacity": "MaxCapacity",
    }

    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    seed_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_tracking_scaling_policy_configuration: Optional[TargetTrackingScalingPolicyConfiguration] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ContributorInsightsSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "enabled": "Enabled",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GlobalSecondaryIndex(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "projection": "Projection",
        "key_schema": "KeySchema",
        "warm_throughput": "WarmThroughput",
        "write_provisioned_throughput_settings": "WriteProvisionedThroughputSettings",
        "write_on_demand_throughput_settings": "WriteOnDemandThroughputSettings",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    projection: Optional[Projection] = None
    key_schema: Optional[list[KeySchema]] = None
    warm_throughput: Optional[WarmThroughput] = None
    write_provisioned_throughput_settings: Optional[WriteProvisionedThroughputSettings] = None
    write_on_demand_throughput_settings: Optional[WriteOnDemandThroughputSettings] = None


@dataclass
class GlobalTableWitness(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
    }

    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeySchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_type": "KeyType",
        "attribute_name": "AttributeName",
    }

    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "approximate_creation_date_time_precision": "ApproximateCreationDateTimePrecision",
        "stream_arn": "StreamArn",
    }

    approximate_creation_date_time_precision: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stream_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LocalSecondaryIndex(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "projection": "Projection",
        "key_schema": "KeySchema",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    projection: Optional[Projection] = None
    key_schema: Optional[list[KeySchema]] = None


@dataclass
class PointInTimeRecoverySpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "point_in_time_recovery_enabled": "PointInTimeRecoveryEnabled",
        "recovery_period_in_days": "RecoveryPeriodInDays",
    }

    point_in_time_recovery_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    recovery_period_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Projection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "projection_type": "ProjectionType",
        "non_key_attributes": "NonKeyAttributes",
    }

    projection_type: Optional[Union[str, ProjectionType, Ref, GetAtt, Sub]] = None
    non_key_attributes: Optional[Union[list[str], Ref]] = None


@dataclass
class ReadOnDemandThroughputSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_read_request_units": "MaxReadRequestUnits",
    }

    max_read_request_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ReadProvisionedThroughputSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "read_capacity_units": "ReadCapacityUnits",
        "read_capacity_auto_scaling_settings": "ReadCapacityAutoScalingSettings",
    }

    read_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    read_capacity_auto_scaling_settings: Optional[CapacityAutoScalingSettings] = None


@dataclass
class ReplicaGlobalSecondaryIndexSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "contributor_insights_specification": "ContributorInsightsSpecification",
        "read_provisioned_throughput_settings": "ReadProvisionedThroughputSettings",
        "read_on_demand_throughput_settings": "ReadOnDemandThroughputSettings",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    contributor_insights_specification: Optional[ContributorInsightsSpecification] = None
    read_provisioned_throughput_settings: Optional[ReadProvisionedThroughputSettings] = None
    read_on_demand_throughput_settings: Optional[ReadOnDemandThroughputSettings] = None


@dataclass
class ReplicaSSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyId",
    }

    kms_master_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicaSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_specification": "SSESpecification",
        "kinesis_stream_specification": "KinesisStreamSpecification",
        "contributor_insights_specification": "ContributorInsightsSpecification",
        "point_in_time_recovery_specification": "PointInTimeRecoverySpecification",
        "replica_stream_specification": "ReplicaStreamSpecification",
        "global_secondary_indexes": "GlobalSecondaryIndexes",
        "region": "Region",
        "resource_policy": "ResourcePolicy",
        "read_provisioned_throughput_settings": "ReadProvisionedThroughputSettings",
        "table_class": "TableClass",
        "deletion_protection_enabled": "DeletionProtectionEnabled",
        "tags": "Tags",
        "read_on_demand_throughput_settings": "ReadOnDemandThroughputSettings",
    }

    sse_specification: Optional[ReplicaSSESpecification] = None
    kinesis_stream_specification: Optional[KinesisStreamSpecification] = None
    contributor_insights_specification: Optional[ContributorInsightsSpecification] = None
    point_in_time_recovery_specification: Optional[PointInTimeRecoverySpecification] = None
    replica_stream_specification: Optional[ReplicaStreamSpecification] = None
    global_secondary_indexes: Optional[list[ReplicaGlobalSecondaryIndexSpecification]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_policy: Optional[ResourcePolicy] = None
    read_provisioned_throughput_settings: Optional[ReadProvisionedThroughputSettings] = None
    table_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deletion_protection_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    read_on_demand_throughput_settings: Optional[ReadOnDemandThroughputSettings] = None


@dataclass
class ReplicaStreamSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_policy": "ResourcePolicy",
    }

    resource_policy: Optional[ResourcePolicy] = None


@dataclass
class ResourcePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_document": "PolicyDocument",
    }

    policy_document: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
    }

    sse_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sse_type: Optional[Union[str, SSEType, Ref, GetAtt, Sub]] = None


@dataclass
class StreamSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_view_type": "StreamViewType",
    }

    stream_view_type: Optional[Union[str, StreamViewType, Ref, GetAtt, Sub]] = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_out_cooldown": "ScaleOutCooldown",
        "target_value": "TargetValue",
        "disable_scale_in": "DisableScaleIn",
        "scale_in_cooldown": "ScaleInCooldown",
    }

    scale_out_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    disable_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scale_in_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeToLiveSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "attribute_name": "AttributeName",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WarmThroughput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "read_units_per_second": "ReadUnitsPerSecond",
        "write_units_per_second": "WriteUnitsPerSecond",
    }

    read_units_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    write_units_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WriteOnDemandThroughputSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_write_request_units": "MaxWriteRequestUnits",
    }

    max_write_request_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WriteProvisionedThroughputSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "write_capacity_auto_scaling_settings": "WriteCapacityAutoScalingSettings",
    }

    write_capacity_auto_scaling_settings: Optional[CapacityAutoScalingSettings] = None

