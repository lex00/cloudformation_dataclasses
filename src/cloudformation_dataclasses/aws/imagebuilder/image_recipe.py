"""PropertyTypes for AWS::ImageBuilder::ImageRecipe."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalInstanceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "user_data_override": "UserDataOverride",
        "systems_manager_agent": "SystemsManagerAgent",
    }

    user_data_override: Optional[Union[str, Ref, GetAtt, Sub]] = None
    systems_manager_agent: Optional[SystemsManagerAgent] = None


@dataclass
class ComponentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "component_arn": "ComponentArn",
    }

    parameters: Optional[list[ComponentParameter]] = None
    component_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EbsInstanceBlockDeviceSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "iops": "Iops",
        "volume_size": "VolumeSize",
        "delete_on_termination": "DeleteOnTermination",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceBlockDeviceMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs": "Ebs",
        "no_device": "NoDevice",
        "virtual_name": "VirtualName",
        "device_name": "DeviceName",
    }

    ebs: Optional[EbsInstanceBlockDeviceSpecification] = None
    no_device: Optional[Union[str, Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LatestVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "major": "Major",
        "minor": "Minor",
        "arn": "Arn",
        "patch": "Patch",
    }

    major: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minor: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    patch: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SystemsManagerAgent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uninstall_after_build": "UninstallAfterBuild",
    }

    uninstall_after_build: Optional[Union[bool, Ref, GetAtt, Sub]] = None

