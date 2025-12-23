"""PropertyTypes for AWS::ImageBuilder::ContainerRecipe."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComponentConfiguration(PropertyType):
    PARAMETERS = "Parameters"
    COMPONENT_ARN = "ComponentArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "component_arn": "ComponentArn",
    }

    parameters: Optional[list[ComponentParameter]] = None
    component_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentParameter(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EbsInstanceBlockDeviceSpecification(PropertyType):
    SNAPSHOT_ID = "SnapshotId"
    VOLUME_TYPE = "VolumeType"
    KMS_KEY_ID = "KmsKeyId"
    ENCRYPTED = "Encrypted"
    THROUGHPUT = "Throughput"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"
    DELETE_ON_TERMINATION = "DeleteOnTermination"

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
    EBS = "Ebs"
    NO_DEVICE = "NoDevice"
    VIRTUAL_NAME = "VirtualName"
    DEVICE_NAME = "DeviceName"

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
class InstanceConfiguration(PropertyType):
    BLOCK_DEVICE_MAPPINGS = "BlockDeviceMappings"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "block_device_mappings": "BlockDeviceMappings",
        "image": "Image",
    }

    block_device_mappings: Optional[list[InstanceBlockDeviceMapping]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LatestVersion(PropertyType):
    MAJOR = "Major"
    MINOR = "Minor"
    ARN = "Arn"
    PATCH = "Patch"

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
class TargetContainerRepository(PropertyType):
    SERVICE = "Service"
    REPOSITORY_NAME = "RepositoryName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service": "Service",
        "repository_name": "RepositoryName",
    }

    service: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

