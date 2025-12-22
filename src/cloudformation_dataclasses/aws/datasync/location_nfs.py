"""PropertyTypes for AWS::DataSync::LocationNFS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AgentStatus:
    """AgentStatus enum values."""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


class Atime:
    """Atime enum values."""

    NONE = "NONE"
    BEST_EFFORT = "BEST_EFFORT"


class AzureAccessTier:
    """AzureAccessTier enum values."""

    HOT = "HOT"
    COOL = "COOL"
    ARCHIVE = "ARCHIVE"


class AzureBlobAuthenticationType:
    """AzureBlobAuthenticationType enum values."""

    SAS = "SAS"
    NONE = "NONE"


class AzureBlobType:
    """AzureBlobType enum values."""

    BLOCK = "BLOCK"


class EfsInTransitEncryption:
    """EfsInTransitEncryption enum values."""

    NONE = "NONE"
    TLS1_2 = "TLS1_2"


class EndpointType:
    """EndpointType enum values."""

    PUBLIC = "PUBLIC"
    PRIVATE_LINK = "PRIVATE_LINK"
    FIPS = "FIPS"
    FIPS_PRIVATE_LINK = "FIPS_PRIVATE_LINK"


class FilterType:
    """FilterType enum values."""

    SIMPLE_PATTERN = "SIMPLE_PATTERN"


class Gid:
    """Gid enum values."""

    NONE = "NONE"
    INT_VALUE = "INT_VALUE"
    NAME = "NAME"
    BOTH = "BOTH"


class HdfsAuthenticationType:
    """HdfsAuthenticationType enum values."""

    SIMPLE = "SIMPLE"
    KERBEROS = "KERBEROS"


class HdfsDataTransferProtection:
    """HdfsDataTransferProtection enum values."""

    DISABLED = "DISABLED"
    AUTHENTICATION = "AUTHENTICATION"
    INTEGRITY = "INTEGRITY"
    PRIVACY = "PRIVACY"


class HdfsRpcProtection:
    """HdfsRpcProtection enum values."""

    DISABLED = "DISABLED"
    AUTHENTICATION = "AUTHENTICATION"
    INTEGRITY = "INTEGRITY"
    PRIVACY = "PRIVACY"


class LocationFilterName:
    """LocationFilterName enum values."""

    LOCATIONURI = "LocationUri"
    LOCATIONTYPE = "LocationType"
    CREATIONTIME = "CreationTime"


class LogLevel:
    """LogLevel enum values."""

    OFF = "OFF"
    BASIC = "BASIC"
    TRANSFER = "TRANSFER"


class ManifestAction:
    """ManifestAction enum values."""

    TRANSFER = "TRANSFER"


class ManifestFormat:
    """ManifestFormat enum values."""

    CSV = "CSV"


class Mtime:
    """Mtime enum values."""

    NONE = "NONE"
    PRESERVE = "PRESERVE"


class NfsVersion:
    """NfsVersion enum values."""

    AUTOMATIC = "AUTOMATIC"
    NFS3 = "NFS3"
    NFS4_0 = "NFS4_0"
    NFS4_1 = "NFS4_1"


class ObjectStorageServerProtocol:
    """ObjectStorageServerProtocol enum values."""

    HTTPS = "HTTPS"
    HTTP = "HTTP"


class ObjectTags:
    """ObjectTags enum values."""

    PRESERVE = "PRESERVE"
    NONE = "NONE"


class ObjectVersionIds:
    """ObjectVersionIds enum values."""

    INCLUDE = "INCLUDE"
    NONE = "NONE"


class Operator:
    """Operator enum values."""

    EQUALS = "Equals"
    NOTEQUALS = "NotEquals"
    IN = "In"
    LESSTHANOREQUAL = "LessThanOrEqual"
    LESSTHAN = "LessThan"
    GREATERTHANOREQUAL = "GreaterThanOrEqual"
    GREATERTHAN = "GreaterThan"
    CONTAINS = "Contains"
    NOTCONTAINS = "NotContains"
    BEGINSWITH = "BeginsWith"


class OverwriteMode:
    """OverwriteMode enum values."""

    ALWAYS = "ALWAYS"
    NEVER = "NEVER"


class PhaseStatus:
    """PhaseStatus enum values."""

    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class PosixPermissions:
    """PosixPermissions enum values."""

    NONE = "NONE"
    PRESERVE = "PRESERVE"


class PreserveDeletedFiles:
    """PreserveDeletedFiles enum values."""

    PRESERVE = "PRESERVE"
    REMOVE = "REMOVE"


class PreserveDevices:
    """PreserveDevices enum values."""

    NONE = "NONE"
    PRESERVE = "PRESERVE"


class ReportLevel:
    """ReportLevel enum values."""

    ERRORS_ONLY = "ERRORS_ONLY"
    SUCCESSES_AND_ERRORS = "SUCCESSES_AND_ERRORS"


class ReportOutputType:
    """ReportOutputType enum values."""

    SUMMARY_ONLY = "SUMMARY_ONLY"
    STANDARD = "STANDARD"


class S3StorageClass:
    """S3StorageClass enum values."""

    STANDARD = "STANDARD"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    GLACIER = "GLACIER"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    OUTPOSTS = "OUTPOSTS"
    GLACIER_INSTANT_RETRIEVAL = "GLACIER_INSTANT_RETRIEVAL"


class ScheduleDisabledBy:
    """ScheduleDisabledBy enum values."""

    USER = "USER"
    SERVICE = "SERVICE"


class ScheduleStatus:
    """ScheduleStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SmbAuthenticationType:
    """SmbAuthenticationType enum values."""

    NTLM = "NTLM"
    KERBEROS = "KERBEROS"


class SmbSecurityDescriptorCopyFlags:
    """SmbSecurityDescriptorCopyFlags enum values."""

    NONE = "NONE"
    OWNER_DACL = "OWNER_DACL"
    OWNER_DACL_SACL = "OWNER_DACL_SACL"


class SmbVersion:
    """SmbVersion enum values."""

    AUTOMATIC = "AUTOMATIC"
    SMB2 = "SMB2"
    SMB3 = "SMB3"
    SMB1 = "SMB1"
    SMB2_0 = "SMB2_0"


class TaskExecutionStatus:
    """TaskExecutionStatus enum values."""

    QUEUED = "QUEUED"
    CANCELLING = "CANCELLING"
    LAUNCHING = "LAUNCHING"
    PREPARING = "PREPARING"
    TRANSFERRING = "TRANSFERRING"
    VERIFYING = "VERIFYING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class TaskFilterName:
    """TaskFilterName enum values."""

    LOCATIONID = "LocationId"
    CREATIONTIME = "CreationTime"


class TaskMode:
    """TaskMode enum values."""

    BASIC = "BASIC"
    ENHANCED = "ENHANCED"


class TaskQueueing:
    """TaskQueueing enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TaskStatus:
    """TaskStatus enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    UNAVAILABLE = "UNAVAILABLE"


class TransferMode:
    """TransferMode enum values."""

    CHANGED = "CHANGED"
    ALL = "ALL"


class Uid:
    """Uid enum values."""

    NONE = "NONE"
    INT_VALUE = "INT_VALUE"
    NAME = "NAME"
    BOTH = "BOTH"


class VerifyMode:
    """VerifyMode enum values."""

    POINT_IN_TIME_CONSISTENT = "POINT_IN_TIME_CONSISTENT"
    ONLY_FILES_TRANSFERRED = "ONLY_FILES_TRANSFERRED"
    NONE = "NONE"


@dataclass
class MountOptions(PropertyType):
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OnPremConfig(PropertyType):
    AGENT_ARNS = "AgentArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_arns": "AgentArns",
    }

    agent_arns: Optional[Union[list[str], Ref]] = None

