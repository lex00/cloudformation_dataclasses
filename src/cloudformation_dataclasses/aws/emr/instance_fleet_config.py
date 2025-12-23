"""PropertyTypes for AWS::EMR::InstanceFleetConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Configuration(PropertyType):
    CLASSIFICATION = "Classification"
    CONFIGURATION_PROPERTIES = "ConfigurationProperties"
    CONFIGURATIONS = "Configurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "classification": "Classification",
        "configuration_properties": "ConfigurationProperties",
        "configurations": "Configurations",
    }

    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_properties: Optional[dict[str, str]] = None
    configurations: Optional[list[Configuration]] = None


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    VOLUME_SPECIFICATION = "VolumeSpecification"
    VOLUMES_PER_INSTANCE = "VolumesPerInstance"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_specification": "VolumeSpecification",
        "volumes_per_instance": "VolumesPerInstance",
    }

    volume_specification: Optional[VolumeSpecification] = None
    volumes_per_instance: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EbsConfiguration(PropertyType):
    EBS_BLOCK_DEVICE_CONFIGS = "EbsBlockDeviceConfigs"
    EBS_OPTIMIZED = "EbsOptimized"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_block_device_configs": "EbsBlockDeviceConfigs",
        "ebs_optimized": "EbsOptimized",
    }

    ebs_block_device_configs: Optional[list[EbsBlockDeviceConfig]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    ON_DEMAND_SPECIFICATION = "OnDemandSpecification"
    SPOT_SPECIFICATION = "SpotSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_specification": "OnDemandSpecification",
        "spot_specification": "SpotSpecification",
    }

    on_demand_specification: Optional[OnDemandProvisioningSpecification] = None
    spot_specification: Optional[SpotProvisioningSpecification] = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    ON_DEMAND_RESIZE_SPECIFICATION = "OnDemandResizeSpecification"
    SPOT_RESIZE_SPECIFICATION = "SpotResizeSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_resize_specification": "OnDemandResizeSpecification",
        "spot_resize_specification": "SpotResizeSpecification",
    }

    on_demand_resize_specification: Optional[OnDemandResizingSpecification] = None
    spot_resize_specification: Optional[SpotResizingSpecification] = None


@dataclass
class InstanceTypeConfig(PropertyType):
    BID_PRICE = "BidPrice"
    BID_PRICE_AS_PERCENTAGE_OF_ON_DEMAND_PRICE = "BidPriceAsPercentageOfOnDemandPrice"
    CONFIGURATIONS = "Configurations"
    CUSTOM_AMI_ID = "CustomAmiId"
    EBS_CONFIGURATION = "EbsConfiguration"
    INSTANCE_TYPE = "InstanceType"
    PRIORITY = "Priority"
    WEIGHTED_CAPACITY = "WeightedCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bid_price": "BidPrice",
        "bid_price_as_percentage_of_on_demand_price": "BidPriceAsPercentageOfOnDemandPrice",
        "configurations": "Configurations",
        "custom_ami_id": "CustomAmiId",
        "ebs_configuration": "EbsConfiguration",
        "instance_type": "InstanceType",
        "priority": "Priority",
        "weighted_capacity": "WeightedCapacity",
    }

    bid_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bid_price_as_percentage_of_on_demand_price: Optional[Union[float, Ref, GetAtt, Sub]] = None
    configurations: Optional[list[Configuration]] = None
    custom_ami_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_configuration: Optional[EbsConfiguration] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[float, Ref, GetAtt, Sub]] = None
    weighted_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    CAPACITY_RESERVATION_PREFERENCE = "CapacityReservationPreference"
    CAPACITY_RESERVATION_RESOURCE_GROUP_ARN = "CapacityReservationResourceGroupArn"
    USAGE_STRATEGY = "UsageStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_preference": "CapacityReservationPreference",
        "capacity_reservation_resource_group_arn": "CapacityReservationResourceGroupArn",
        "usage_strategy": "UsageStrategy",
    }

    capacity_reservation_preference: Optional[Union[str, OnDemandCapacityReservationPreference, Ref, GetAtt, Sub]] = None
    capacity_reservation_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    usage_strategy: Optional[Union[str, OnDemandCapacityReservationUsageStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    CAPACITY_RESERVATION_OPTIONS = "CapacityReservationOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "capacity_reservation_options": "CapacityReservationOptions",
    }

    allocation_strategy: Optional[Union[str, OnDemandProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[OnDemandCapacityReservationOptions] = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    CAPACITY_RESERVATION_OPTIONS = "CapacityReservationOptions"
    TIMEOUT_DURATION_MINUTES = "TimeoutDurationMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "capacity_reservation_options": "CapacityReservationOptions",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, OnDemandProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[OnDemandCapacityReservationOptions] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    BLOCK_DURATION_MINUTES = "BlockDurationMinutes"
    TIMEOUT_ACTION = "TimeoutAction"
    TIMEOUT_DURATION_MINUTES = "TimeoutDurationMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "block_duration_minutes": "BlockDurationMinutes",
        "timeout_action": "TimeoutAction",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, SpotProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    block_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout_action: Optional[Union[str, SpotProvisioningTimeoutAction, Ref, GetAtt, Sub]] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotResizingSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    TIMEOUT_DURATION_MINUTES = "TimeoutDurationMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, SpotProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeSpecification(PropertyType):
    IOPS = "Iops"
    SIZE_IN_GB = "SizeInGB"
    THROUGHPUT = "Throughput"
    VOLUME_TYPE = "VolumeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iops": "Iops",
        "size_in_gb": "SizeInGB",
        "throughput": "Throughput",
        "volume_type": "VolumeType",
    }

    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

