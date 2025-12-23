"""PropertyTypes for AWS::Cassandra::Table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoScalingSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_units": "MaximumUnits",
        "scaling_policy": "ScalingPolicy",
        "minimum_units": "MinimumUnits",
        "auto_scaling_disabled": "AutoScalingDisabled",
    }

    maximum_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scaling_policy: Optional[ScalingPolicy] = None
    minimum_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_scaling_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AutoScalingSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "read_capacity_auto_scaling": "ReadCapacityAutoScaling",
        "write_capacity_auto_scaling": "WriteCapacityAutoScaling",
    }

    read_capacity_auto_scaling: Optional[AutoScalingSetting] = None
    write_capacity_auto_scaling: Optional[AutoScalingSetting] = None


@dataclass
class BillingMode(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "provisioned_throughput": "ProvisionedThroughput",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provisioned_throughput: Optional[ProvisionedThroughput] = None


@dataclass
class CdcSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "view_type": "ViewType",
        "tags": "Tags",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    view_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class ClusteringKeyColumn(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "order_by": "OrderBy",
        "column": "Column",
    }

    order_by: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column: Optional[Column] = None


@dataclass
class Column(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "column_type": "ColumnType",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "kms_key_identifier": "KmsKeyIdentifier",
    }

    encryption_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisionedThroughput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "write_capacity_units": "WriteCapacityUnits",
        "read_capacity_units": "ReadCapacityUnits",
    }

    write_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    read_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicaSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "read_capacity_units": "ReadCapacityUnits",
        "region": "Region",
        "read_capacity_auto_scaling": "ReadCapacityAutoScaling",
    }

    read_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    read_capacity_auto_scaling: Optional[AutoScalingSetting] = None


@dataclass
class ScalingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_tracking_scaling_policy_configuration": "TargetTrackingScalingPolicyConfiguration",
    }

    target_tracking_scaling_policy_configuration: Optional[TargetTrackingScalingPolicyConfiguration] = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_out_cooldown": "ScaleOutCooldown",
        "target_value": "TargetValue",
        "disable_scale_in": "DisableScaleIn",
        "scale_in_cooldown": "ScaleInCooldown",
    }

    scale_out_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    disable_scale_in: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    scale_in_cooldown: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WarmThroughput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "read_units_per_second": "ReadUnitsPerSecond",
        "write_units_per_second": "WriteUnitsPerSecond",
    }

    read_units_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    write_units_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None

