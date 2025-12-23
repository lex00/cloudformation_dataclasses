"""PropertyTypes for AWS::OSIS::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BufferOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "persistent_buffer_enabled": "PersistentBufferEnabled",
    }

    persistent_buffer_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogPublishingOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_log_destination": "CloudWatchLogDestination",
        "is_logging_enabled": "IsLoggingEnabled",
    }

    cloud_watch_log_destination: Optional[CloudWatchLogDestination] = None
    is_logging_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ResourcePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
    }

    policy: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class VpcAttachmentOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attach_to_vpc": "AttachToVpc",
        "cidr_block": "CidrBlock",
    }

    attach_to_vpc: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cidr_block: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
        "vpc_options": "VpcOptions",
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_options: Optional[VpcOptions] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_attachment_options": "VpcAttachmentOptions",
        "vpc_endpoint_management": "VpcEndpointManagement",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    vpc_attachment_options: Optional[VpcAttachmentOptions] = None
    vpc_endpoint_management: Optional[Union[str, VpcEndpointManagement, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

