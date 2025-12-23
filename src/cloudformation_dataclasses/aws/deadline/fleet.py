"""PropertyTypes for AWS::Deadline::Fleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AcceleratorCapabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selections": "Selections",
        "count": "Count",
    }

    selections: Optional[list[AcceleratorSelection]] = None
    count: Optional[AcceleratorCountRange] = None


@dataclass
class AcceleratorCountRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AcceleratorSelection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime": "Runtime",
        "name": "Name",
    }

    runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AcceleratorTotalMemoryMiBRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CustomerManagedFleetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_profile_id": "StorageProfileId",
        "mode": "Mode",
        "worker_capabilities": "WorkerCapabilities",
        "tag_propagation_mode": "TagPropagationMode",
    }

    storage_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    worker_capabilities: Optional[CustomerManagedWorkerCapabilities] = None
    tag_propagation_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomerManagedWorkerCapabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_attributes": "CustomAttributes",
        "accelerator_count": "AcceleratorCount",
        "custom_amounts": "CustomAmounts",
        "accelerator_types": "AcceleratorTypes",
        "accelerator_total_memory_mi_b": "AcceleratorTotalMemoryMiB",
        "v_cpu_count": "VCpuCount",
        "memory_mi_b": "MemoryMiB",
        "os_family": "OsFamily",
        "cpu_architecture_type": "CpuArchitectureType",
    }

    custom_attributes: Optional[list[FleetAttributeCapability]] = None
    accelerator_count: Optional[AcceleratorCountRange] = None
    custom_amounts: Optional[list[FleetAmountCapability]] = None
    accelerator_types: Optional[Union[list[str], Ref]] = None
    accelerator_total_memory_mi_b: Optional[AcceleratorTotalMemoryMiBRange] = None
    v_cpu_count: Optional[VCpuCountRange] = None
    memory_mi_b: Optional[MemoryMiBRange] = None
    os_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu_architecture_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ec2EbsVolume(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_gi_b": "SizeGiB",
        "throughput_mi_b": "ThroughputMiB",
        "iops": "Iops",
    }

    size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    throughput_mi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FleetAmountCapability(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
        "name": "Name",
    }

    min: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FleetAttributeCapability(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FleetCapabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "amounts": "Amounts",
        "attributes": "Attributes",
    }

    amounts: Optional[list[FleetAmountCapability]] = None
    attributes: Optional[list[FleetAttributeCapability]] = None


@dataclass
class FleetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_managed_ec2": "ServiceManagedEc2",
        "customer_managed": "CustomerManaged",
    }

    service_managed_ec2: Optional[ServiceManagedEc2FleetConfiguration] = None
    customer_managed: Optional[CustomerManagedFleetConfiguration] = None


@dataclass
class HostConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "script_timeout_seconds": "ScriptTimeoutSeconds",
        "script_body": "ScriptBody",
    }

    script_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    script_body: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryMiBRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceManagedEc2FleetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_profile_id": "StorageProfileId",
        "instance_market_options": "InstanceMarketOptions",
        "instance_capabilities": "InstanceCapabilities",
        "vpc_configuration": "VpcConfiguration",
    }

    storage_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_market_options: Optional[ServiceManagedEc2InstanceMarketOptions] = None
    instance_capabilities: Optional[ServiceManagedEc2InstanceCapabilities] = None
    vpc_configuration: Optional[VpcConfiguration] = None


@dataclass
class ServiceManagedEc2InstanceCapabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_instance_types": "AllowedInstanceTypes",
        "custom_attributes": "CustomAttributes",
        "accelerator_capabilities": "AcceleratorCapabilities",
        "custom_amounts": "CustomAmounts",
        "v_cpu_count": "VCpuCount",
        "excluded_instance_types": "ExcludedInstanceTypes",
        "memory_mi_b": "MemoryMiB",
        "os_family": "OsFamily",
        "cpu_architecture_type": "CpuArchitectureType",
        "root_ebs_volume": "RootEbsVolume",
    }

    allowed_instance_types: Optional[Union[list[str], Ref]] = None
    custom_attributes: Optional[list[FleetAttributeCapability]] = None
    accelerator_capabilities: Optional[AcceleratorCapabilities] = None
    custom_amounts: Optional[list[FleetAmountCapability]] = None
    v_cpu_count: Optional[VCpuCountRange] = None
    excluded_instance_types: Optional[Union[list[str], Ref]] = None
    memory_mi_b: Optional[MemoryMiBRange] = None
    os_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu_architecture_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    root_ebs_volume: Optional[Ec2EbsVolume] = None


@dataclass
class ServiceManagedEc2InstanceMarketOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VCpuCountRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min": "Min",
        "max": "Max",
    }

    min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_configuration_arns": "ResourceConfigurationArns",
    }

    resource_configuration_arns: Optional[Union[list[str], Ref]] = None

