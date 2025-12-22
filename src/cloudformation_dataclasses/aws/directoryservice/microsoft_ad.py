"""PropertyTypes for AWS::DirectoryService::MicrosoftAD."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CaEnrollmentPolicyStatus:
    """CaEnrollmentPolicyStatus enum values."""

    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    FAILED = "Failed"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    IMPAIRED = "Impaired"


class CertificateState:
    """CertificateState enum values."""

    REGISTERING = "Registering"
    REGISTERED = "Registered"
    REGISTERFAILED = "RegisterFailed"
    DEREGISTERING = "Deregistering"
    DEREGISTERED = "Deregistered"
    DEREGISTERFAILED = "DeregisterFailed"


class CertificateType:
    """CertificateType enum values."""

    CLIENTCERTAUTH = "ClientCertAuth"
    CLIENTLDAPS = "ClientLDAPS"


class ClientAuthenticationStatus:
    """ClientAuthenticationStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ClientAuthenticationType:
    """ClientAuthenticationType enum values."""

    SMARTCARD = "SmartCard"
    SMARTCARDORPASSWORD = "SmartCardOrPassword"


class DataAccessStatus:
    """DataAccessStatus enum values."""

    DISABLED = "Disabled"
    DISABLING = "Disabling"
    ENABLED = "Enabled"
    ENABLING = "Enabling"
    FAILED = "Failed"


class DirectoryConfigurationStatus:
    """DirectoryConfigurationStatus enum values."""

    REQUESTED = "Requested"
    UPDATING = "Updating"
    UPDATED = "Updated"
    FAILED = "Failed"
    DEFAULT = "Default"


class DirectoryEdition:
    """DirectoryEdition enum values."""

    ENTERPRISE = "Enterprise"
    STANDARD = "Standard"
    HYBRID = "Hybrid"


class DirectorySize:
    """DirectorySize enum values."""

    SMALL = "Small"
    LARGE = "Large"


class DirectoryStage:
    """DirectoryStage enum values."""

    REQUESTED = "Requested"
    CREATING = "Creating"
    CREATED = "Created"
    ACTIVE = "Active"
    INOPERABLE = "Inoperable"
    IMPAIRED = "Impaired"
    RESTORING = "Restoring"
    RESTOREFAILED = "RestoreFailed"
    DELETING = "Deleting"
    DELETED = "Deleted"
    FAILED = "Failed"
    UPDATING = "Updating"


class DirectoryType:
    """DirectoryType enum values."""

    SIMPLEAD = "SimpleAD"
    ADCONNECTOR = "ADConnector"
    MICROSOFTAD = "MicrosoftAD"
    SHAREDMICROSOFTAD = "SharedMicrosoftAD"


class DomainControllerStatus:
    """DomainControllerStatus enum values."""

    CREATING = "Creating"
    ACTIVE = "Active"
    IMPAIRED = "Impaired"
    RESTORING = "Restoring"
    DELETING = "Deleting"
    DELETED = "Deleted"
    FAILED = "Failed"
    UPDATING = "Updating"


class HybridUpdateType:
    """HybridUpdateType enum values."""

    SELFMANAGEDINSTANCES = "SelfManagedInstances"
    HYBRIDADMINISTRATORACCOUNT = "HybridAdministratorAccount"


class IpRouteStatusMsg:
    """IpRouteStatusMsg enum values."""

    ADDING = "Adding"
    ADDED = "Added"
    REMOVING = "Removing"
    REMOVED = "Removed"
    ADDFAILED = "AddFailed"
    REMOVEFAILED = "RemoveFailed"


class LDAPSStatus:
    """LDAPSStatus enum values."""

    ENABLING = "Enabling"
    ENABLED = "Enabled"
    ENABLEFAILED = "EnableFailed"
    DISABLED = "Disabled"


class LDAPSType:
    """LDAPSType enum values."""

    CLIENT = "Client"


class NetworkType:
    """NetworkType enum values."""

    DUAL_STACK = "Dual-stack"
    IPV4 = "IPv4"
    IPV6 = "IPv6"


class OSVersion:
    """OSVersion enum values."""

    SERVER_2012 = "SERVER_2012"
    SERVER_2019 = "SERVER_2019"


class RadiusAuthenticationProtocol:
    """RadiusAuthenticationProtocol enum values."""

    PAP = "PAP"
    CHAP = "CHAP"
    MS_CHAPV1 = "MS-CHAPv1"
    MS_CHAPV2 = "MS-CHAPv2"


class RadiusStatus:
    """RadiusStatus enum values."""

    CREATING = "Creating"
    COMPLETED = "Completed"
    FAILED = "Failed"


class RegionType:
    """RegionType enum values."""

    PRIMARY = "Primary"
    ADDITIONAL = "Additional"


class ReplicationScope:
    """ReplicationScope enum values."""

    DOMAIN = "Domain"


class SchemaExtensionStatus:
    """SchemaExtensionStatus enum values."""

    INITIALIZING = "Initializing"
    CREATINGSNAPSHOT = "CreatingSnapshot"
    UPDATINGSCHEMA = "UpdatingSchema"
    REPLICATING = "Replicating"
    CANCELINPROGRESS = "CancelInProgress"
    ROLLBACKINPROGRESS = "RollbackInProgress"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    COMPLETED = "Completed"


class SelectiveAuth:
    """SelectiveAuth enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ShareMethod:
    """ShareMethod enum values."""

    ORGANIZATIONS = "ORGANIZATIONS"
    HANDSHAKE = "HANDSHAKE"


class ShareStatus:
    """ShareStatus enum values."""

    SHARED = "Shared"
    PENDINGACCEPTANCE = "PendingAcceptance"
    REJECTED = "Rejected"
    REJECTING = "Rejecting"
    REJECTFAILED = "RejectFailed"
    SHARING = "Sharing"
    SHAREFAILED = "ShareFailed"
    DELETED = "Deleted"
    DELETING = "Deleting"


class SnapshotStatus:
    """SnapshotStatus enum values."""

    CREATING = "Creating"
    COMPLETED = "Completed"
    FAILED = "Failed"


class SnapshotType:
    """SnapshotType enum values."""

    AUTO = "Auto"
    MANUAL = "Manual"


class TargetType:
    """TargetType enum values."""

    ACCOUNT = "ACCOUNT"


class TopicStatus:
    """TopicStatus enum values."""

    REGISTERED = "Registered"
    TOPIC_NOT_FOUND = "Topic not found"
    FAILED = "Failed"
    DELETED = "Deleted"


class TrustDirection:
    """TrustDirection enum values."""

    ONE_WAY_OUTGOING = "One-Way: Outgoing"
    ONE_WAY_INCOMING = "One-Way: Incoming"
    TWO_WAY = "Two-Way"


class TrustState:
    """TrustState enum values."""

    CREATING = "Creating"
    CREATED = "Created"
    VERIFYING = "Verifying"
    VERIFYFAILED = "VerifyFailed"
    VERIFIED = "Verified"
    UPDATING = "Updating"
    UPDATEFAILED = "UpdateFailed"
    UPDATED = "Updated"
    DELETING = "Deleting"
    DELETED = "Deleted"
    FAILED = "Failed"


class TrustType:
    """TrustType enum values."""

    FOREST = "Forest"
    EXTERNAL = "External"


class UpdateStatus:
    """UpdateStatus enum values."""

    UPDATED = "Updated"
    UPDATING = "Updating"
    UPDATEFAILED = "UpdateFailed"


class UpdateType:
    """UpdateType enum values."""

    OS = "OS"
    NETWORK = "NETWORK"
    SIZE = "SIZE"


@dataclass
class VpcSettings(PropertyType):
    SUBNET_IDS = "SubnetIds"
    VPC_ID = "VpcId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "vpc_id": "VpcId",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

