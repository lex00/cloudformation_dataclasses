"""PropertyTypes for AWS::OSIS::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChangeProgressStageStatuses:
    """ChangeProgressStageStatuses enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ChangeProgressStatuses:
    """ChangeProgressStatuses enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PipelineEndpointStatus:
    """PipelineEndpointStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    REVOKING = "REVOKING"
    REVOKED = "REVOKED"


class PipelineStatus:
    """PipelineStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    STARTING = "STARTING"
    START_FAILED = "START_FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class VpcEndpointManagement:
    """VpcEndpointManagement enum values."""

    CUSTOMER = "CUSTOMER"
    SERVICE = "SERVICE"


class VpcEndpointServiceName:
    """VpcEndpointServiceName enum values."""

    OPENSEARCH_SERVERLESS = "OPENSEARCH_SERVERLESS"


@dataclass
class BufferOptions(PropertyType):
    PERSISTENT_BUFFER_ENABLED = "PersistentBufferEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "persistent_buffer_enabled": "PersistentBufferEnabled",
    }

    persistent_buffer_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    LOG_GROUP = "LogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogPublishingOptions(PropertyType):
    CLOUD_WATCH_LOG_DESTINATION = "CloudWatchLogDestination"
    IS_LOGGING_ENABLED = "IsLoggingEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_log_destination": "CloudWatchLogDestination",
        "is_logging_enabled": "IsLoggingEnabled",
    }

    cloud_watch_log_destination: Optional[CloudWatchLogDestination] = None
    is_logging_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ResourcePolicy(PropertyType):
    POLICY = "Policy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
    }

    policy: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class VpcAttachmentOptions(PropertyType):
    ATTACH_TO_VPC = "AttachToVpc"
    CIDR_BLOCK = "CidrBlock"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attach_to_vpc": "AttachToVpc",
        "cidr_block": "CidrBlock",
    }

    attach_to_vpc: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cidr_block: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcEndpoint(PropertyType):
    VPC_ID = "VpcId"
    VPC_OPTIONS = "VpcOptions"
    VPC_ENDPOINT_ID = "VpcEndpointId"

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
    VPC_ATTACHMENT_OPTIONS = "VpcAttachmentOptions"
    VPC_ENDPOINT_MANAGEMENT = "VpcEndpointManagement"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

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

