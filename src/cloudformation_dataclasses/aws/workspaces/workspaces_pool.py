"""PropertyTypes for AWS::WorkSpaces::WorkspacesPool."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AGAModeForDirectoryEnum:
    """AGAModeForDirectoryEnum enum values."""

    ENABLED_AUTO = "ENABLED_AUTO"
    DISABLED = "DISABLED"


class AGAModeForWorkSpaceEnum:
    """AGAModeForWorkSpaceEnum enum values."""

    ENABLED_AUTO = "ENABLED_AUTO"
    DISABLED = "DISABLED"
    INHERITED = "INHERITED"


class AGAPreferredProtocolForDirectory:
    """AGAPreferredProtocolForDirectory enum values."""

    TCP = "TCP"
    NONE = "NONE"


class AGAPreferredProtocolForWorkSpace:
    """AGAPreferredProtocolForWorkSpace enum values."""

    TCP = "TCP"
    NONE = "NONE"
    INHERITED = "INHERITED"


class AccessEndpointType:
    """AccessEndpointType enum values."""

    STREAMING_WSP = "STREAMING_WSP"


class AccessPropertyValue:
    """AccessPropertyValue enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class AccountLinkStatusEnum:
    """AccountLinkStatusEnum enum values."""

    LINKED = "LINKED"
    LINKING_FAILED = "LINKING_FAILED"
    LINK_NOT_FOUND = "LINK_NOT_FOUND"
    PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT = "PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT"
    REJECTED = "REJECTED"


class Application:
    """Application enum values."""

    MICROSOFT_OFFICE_2016 = "Microsoft_Office_2016"
    MICROSOFT_OFFICE_2019 = "Microsoft_Office_2019"


class ApplicationAssociatedResourceType:
    """ApplicationAssociatedResourceType enum values."""

    WORKSPACE = "WORKSPACE"
    BUNDLE = "BUNDLE"
    IMAGE = "IMAGE"


class ApplicationSettingsStatusEnum:
    """ApplicationSettingsStatusEnum enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AssociationErrorCode:
    """AssociationErrorCode enum values."""

    VALIDATIONERROR_INSUFFICIENTDISKSPACE = "ValidationError.InsufficientDiskSpace"
    VALIDATIONERROR_INSUFFICIENTMEMORY = "ValidationError.InsufficientMemory"
    VALIDATIONERROR_UNSUPPORTEDOPERATINGSYSTEM = "ValidationError.UnsupportedOperatingSystem"
    DEPLOYMENTERROR_INTERNALSERVERERROR = "DeploymentError.InternalServerError"
    DEPLOYMENTERROR_WORKSPACEUNREACHABLE = "DeploymentError.WorkspaceUnreachable"


class AssociationState:
    """AssociationState enum values."""

    PENDING_INSTALL = "PENDING_INSTALL"
    PENDING_INSTALL_DEPLOYMENT = "PENDING_INSTALL_DEPLOYMENT"
    PENDING_UNINSTALL = "PENDING_UNINSTALL"
    PENDING_UNINSTALL_DEPLOYMENT = "PENDING_UNINSTALL_DEPLOYMENT"
    INSTALLING = "INSTALLING"
    UNINSTALLING = "UNINSTALLING"
    ERROR = "ERROR"
    COMPLETED = "COMPLETED"
    REMOVED = "REMOVED"


class AssociationStatus:
    """AssociationStatus enum values."""

    NOT_ASSOCIATED = "NOT_ASSOCIATED"
    ASSOCIATED_WITH_OWNER_ACCOUNT = "ASSOCIATED_WITH_OWNER_ACCOUNT"
    ASSOCIATED_WITH_SHARED_ACCOUNT = "ASSOCIATED_WITH_SHARED_ACCOUNT"
    PENDING_ASSOCIATION = "PENDING_ASSOCIATION"
    PENDING_DISASSOCIATION = "PENDING_DISASSOCIATION"


class AuthenticationType:
    """AuthenticationType enum values."""

    SAML = "SAML"


class BundleAssociatedResourceType:
    """BundleAssociatedResourceType enum values."""

    APPLICATION = "APPLICATION"


class BundleType:
    """BundleType enum values."""

    REGULAR = "REGULAR"
    STANDBY = "STANDBY"


class CertificateBasedAuthStatusEnum:
    """CertificateBasedAuthStatusEnum enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ClientDeviceType:
    """ClientDeviceType enum values."""

    DEVICETYPEWINDOWS = "DeviceTypeWindows"
    DEVICETYPEOSX = "DeviceTypeOsx"
    DEVICETYPEANDROID = "DeviceTypeAndroid"
    DEVICETYPEIOS = "DeviceTypeIos"
    DEVICETYPELINUX = "DeviceTypeLinux"
    DEVICETYPEWEB = "DeviceTypeWeb"


class Compute:
    """Compute enum values."""

    VALUE = "VALUE"
    STANDARD = "STANDARD"
    PERFORMANCE = "PERFORMANCE"
    POWER = "POWER"
    GRAPHICS = "GRAPHICS"
    POWERPRO = "POWERPRO"
    GENERALPURPOSE_4XLARGE = "GENERALPURPOSE_4XLARGE"
    GENERALPURPOSE_8XLARGE = "GENERALPURPOSE_8XLARGE"
    GRAPHICSPRO = "GRAPHICSPRO"
    GRAPHICS_G4DN = "GRAPHICS_G4DN"
    GRAPHICSPRO_G4DN = "GRAPHICSPRO_G4DN"


class ConnectionAliasState:
    """ConnectionAliasState enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    DELETING = "DELETING"


class ConnectionState:
    """ConnectionState enum values."""

    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    UNKNOWN = "UNKNOWN"


class CustomImageProtocol:
    """CustomImageProtocol enum values."""

    PCOIP = "PCOIP"
    DCV = "DCV"
    BYOP = "BYOP"


class CustomWorkspaceImageImportState:
    """CustomWorkspaceImageImportState enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"


class DataReplication:
    """DataReplication enum values."""

    NO_REPLICATION = "NO_REPLICATION"
    PRIMARY_AS_SOURCE = "PRIMARY_AS_SOURCE"


class DedicatedTenancyAccountType:
    """DedicatedTenancyAccountType enum values."""

    SOURCE_ACCOUNT = "SOURCE_ACCOUNT"
    TARGET_ACCOUNT = "TARGET_ACCOUNT"


class DedicatedTenancyModificationStateEnum:
    """DedicatedTenancyModificationStateEnum enum values."""

    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DedicatedTenancySupportEnum:
    """DedicatedTenancySupportEnum enum values."""

    ENABLED = "ENABLED"


class DedicatedTenancySupportResultEnum:
    """DedicatedTenancySupportResultEnum enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DeletableCertificateBasedAuthProperty:
    """DeletableCertificateBasedAuthProperty enum values."""

    CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN = "CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"


class DeletableSamlProperty:
    """DeletableSamlProperty enum values."""

    SAML_PROPERTIES_USER_ACCESS_URL = "SAML_PROPERTIES_USER_ACCESS_URL"
    SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME = "SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME"


class DescribeWorkspaceDirectoriesFilterName:
    """DescribeWorkspaceDirectoriesFilterName enum values."""

    USER_IDENTITY_TYPE = "USER_IDENTITY_TYPE"
    WORKSPACE_TYPE = "WORKSPACE_TYPE"


class DescribeWorkspacesPoolsFilterName:
    """DescribeWorkspacesPoolsFilterName enum values."""

    POOLNAME = "PoolName"


class DescribeWorkspacesPoolsFilterOperator:
    """DescribeWorkspacesPoolsFilterOperator enum values."""

    EQUALS = "EQUALS"
    NOTEQUALS = "NOTEQUALS"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOTCONTAINS"


class EndpointEncryptionMode:
    """EndpointEncryptionMode enum values."""

    STANDARD_TLS = "STANDARD_TLS"
    FIPS_VALIDATED = "FIPS_VALIDATED"


class ImageAssociatedResourceType:
    """ImageAssociatedResourceType enum values."""

    APPLICATION = "APPLICATION"


class ImageComputeType:
    """ImageComputeType enum values."""

    BASE = "BASE"
    GRAPHICS_G4DN = "GRAPHICS_G4DN"


class ImageType:
    """ImageType enum values."""

    OWNED = "OWNED"
    SHARED = "SHARED"


class InternetFallbackProtocol:
    """InternetFallbackProtocol enum values."""

    PCOIP = "PCOIP"


class LogUploadEnum:
    """LogUploadEnum enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ModificationResourceEnum:
    """ModificationResourceEnum enum values."""

    ROOT_VOLUME = "ROOT_VOLUME"
    USER_VOLUME = "USER_VOLUME"
    COMPUTE_TYPE = "COMPUTE_TYPE"


class ModificationStateEnum:
    """ModificationStateEnum enum values."""

    UPDATE_INITIATED = "UPDATE_INITIATED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"


class OSVersion:
    """OSVersion enum values."""

    WINDOWS_10 = "Windows_10"
    WINDOWS_11 = "Windows_11"


class OperatingSystemName:
    """OperatingSystemName enum values."""

    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    UBUNTU_18_04 = "UBUNTU_18_04"
    UBUNTU_20_04 = "UBUNTU_20_04"
    UBUNTU_22_04 = "UBUNTU_22_04"
    UNKNOWN = "UNKNOWN"
    WINDOWS_10 = "WINDOWS_10"
    WINDOWS_11 = "WINDOWS_11"
    WINDOWS_7 = "WINDOWS_7"
    WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"
    WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"
    WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"
    RHEL_8 = "RHEL_8"
    ROCKY_8 = "ROCKY_8"


class OperatingSystemType:
    """OperatingSystemType enum values."""

    WINDOWS = "WINDOWS"
    LINUX = "LINUX"


class Platform:
    """Platform enum values."""

    WINDOWS = "WINDOWS"


class PoolsRunningMode:
    """PoolsRunningMode enum values."""

    AUTO_STOP = "AUTO_STOP"
    ALWAYS_ON = "ALWAYS_ON"


class Protocol:
    """Protocol enum values."""

    PCOIP = "PCOIP"
    WSP = "WSP"


class ReconnectEnum:
    """ReconnectEnum enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RunningMode:
    """RunningMode enum values."""

    AUTO_STOP = "AUTO_STOP"
    ALWAYS_ON = "ALWAYS_ON"
    MANUAL = "MANUAL"


class SamlStatusEnum:
    """SamlStatusEnum enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK = "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK"


class SessionConnectionState:
    """SessionConnectionState enum values."""

    CONNECTED = "CONNECTED"
    NOT_CONNECTED = "NOT_CONNECTED"


class StandbyWorkspaceRelationshipType:
    """StandbyWorkspaceRelationshipType enum values."""

    PRIMARY = "PRIMARY"
    STANDBY = "STANDBY"


class StorageConnectorStatusEnum:
    """StorageConnectorStatusEnum enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class StorageConnectorTypeEnum:
    """StorageConnectorTypeEnum enum values."""

    HOME_FOLDER = "HOME_FOLDER"


class StreamingExperiencePreferredProtocolEnum:
    """StreamingExperiencePreferredProtocolEnum enum values."""

    TCP = "TCP"
    UDP = "UDP"


class TargetWorkspaceState:
    """TargetWorkspaceState enum values."""

    AVAILABLE = "AVAILABLE"
    ADMIN_MAINTENANCE = "ADMIN_MAINTENANCE"


class Tenancy:
    """Tenancy enum values."""

    DEDICATED = "DEDICATED"
    SHARED = "SHARED"


class UserIdentityType:
    """UserIdentityType enum values."""

    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    AWS_DIRECTORY_SERVICE = "AWS_DIRECTORY_SERVICE"
    AWS_IAM_IDENTITY_CENTER = "AWS_IAM_IDENTITY_CENTER"


class UserSettingActionEnum:
    """UserSettingActionEnum enum values."""

    CLIPBOARD_COPY_FROM_LOCAL_DEVICE = "CLIPBOARD_COPY_FROM_LOCAL_DEVICE"
    CLIPBOARD_COPY_TO_LOCAL_DEVICE = "CLIPBOARD_COPY_TO_LOCAL_DEVICE"
    PRINTING_TO_LOCAL_DEVICE = "PRINTING_TO_LOCAL_DEVICE"
    SMART_CARD = "SMART_CARD"


class UserSettingPermissionEnum:
    """UserSettingPermissionEnum enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class WorkSpaceApplicationLicenseType:
    """WorkSpaceApplicationLicenseType enum values."""

    LICENSED = "LICENSED"
    UNLICENSED = "UNLICENSED"


class WorkSpaceApplicationState:
    """WorkSpaceApplicationState enum values."""

    PENDING = "PENDING"
    ERROR = "ERROR"
    AVAILABLE = "AVAILABLE"
    UNINSTALL_ONLY = "UNINSTALL_ONLY"


class WorkSpaceAssociatedResourceType:
    """WorkSpaceAssociatedResourceType enum values."""

    APPLICATION = "APPLICATION"


class WorkspaceBundleState:
    """WorkspaceBundleState enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    ERROR = "ERROR"


class WorkspaceDirectoryState:
    """WorkspaceDirectoryState enum values."""

    REGISTERING = "REGISTERING"
    REGISTERED = "REGISTERED"
    DEREGISTERING = "DEREGISTERING"
    DEREGISTERED = "DEREGISTERED"
    ERROR = "ERROR"


class WorkspaceDirectoryType:
    """WorkspaceDirectoryType enum values."""

    SIMPLE_AD = "SIMPLE_AD"
    AD_CONNECTOR = "AD_CONNECTOR"
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    AWS_IAM_IDENTITY_CENTER = "AWS_IAM_IDENTITY_CENTER"


class WorkspaceImageErrorDetailCode:
    """WorkspaceImageErrorDetailCode enum values."""

    OUTDATEDPOWERSHELLVERSION = "OutdatedPowershellVersion"
    OFFICEINSTALLED = "OfficeInstalled"
    PCOIPAGENTINSTALLED = "PCoIPAgentInstalled"
    WINDOWSUPDATESENABLED = "WindowsUpdatesEnabled"
    AUTOMOUNTDISABLED = "AutoMountDisabled"
    WORKSPACESBYOLACCOUNTNOTFOUND = "WorkspacesBYOLAccountNotFound"
    WORKSPACESBYOLACCOUNTDISABLED = "WorkspacesBYOLAccountDisabled"
    DHCPDISABLED = "DHCPDisabled"
    DISKFREESPACE = "DiskFreeSpace"
    ADDITIONALDRIVESATTACHED = "AdditionalDrivesAttached"
    OSNOTSUPPORTED = "OSNotSupported"
    DOMAINJOINED = "DomainJoined"
    AZUREDOMAINJOINED = "AzureDomainJoined"
    FIREWALLENABLED = "FirewallEnabled"
    VMWARETOOLSINSTALLED = "VMWareToolsInstalled"
    DISKSIZEEXCEEDED = "DiskSizeExceeded"
    INCOMPATIBLEPARTITIONING = "IncompatiblePartitioning"
    PENDINGREBOOT = "PendingReboot"
    AUTOLOGONENABLED = "AutoLogonEnabled"
    REALTIMEUNIVERSALDISABLED = "RealTimeUniversalDisabled"
    MULTIPLEBOOTPARTITION = "MultipleBootPartition"
    REQUIRES64BITOS = "Requires64BitOS"
    ZEROREARMCOUNT = "ZeroRearmCount"
    INPLACEUPGRADE = "InPlaceUpgrade"
    ANTIVIRUSINSTALLED = "AntiVirusInstalled"
    UEFINOTSUPPORTED = "UEFINotSupported"
    UNKNOWNERROR = "UnknownError"
    APPXPACKAGESINSTALLED = "AppXPackagesInstalled"
    RESERVEDSTORAGEINUSE = "ReservedStorageInUse"
    ADDITIONALDRIVESPRESENT = "AdditionalDrivesPresent"
    WINDOWSUPDATESREQUIRED = "WindowsUpdatesRequired"
    SYSPREPFILEMISSING = "SysPrepFileMissing"
    USERPROFILEMISSING = "UserProfileMissing"
    INSUFFICIENTDISKSPACE = "InsufficientDiskSpace"
    ENVIRONMENTVARIABLESPATHMISSINGENTRIES = "EnvironmentVariablesPathMissingEntries"
    DOMAINACCOUNTSERVICESFOUND = "DomainAccountServicesFound"
    INVALIDIP = "InvalidIp"
    REMOTEDESKTOPSERVICESDISABLED = "RemoteDesktopServicesDisabled"
    WINDOWSMODULESINSTALLERDISABLED = "WindowsModulesInstallerDisabled"
    AMAZONSSMAGENTENABLED = "AmazonSsmAgentEnabled"
    UNSUPPORTEDSECURITYPROTOCOL = "UnsupportedSecurityProtocol"
    MULTIPLEUSERPROFILES = "MultipleUserProfiles"
    STAGEDAPPXPACKAGE = "StagedAppxPackage"
    UNSUPPORTEDOSUPGRADE = "UnsupportedOsUpgrade"
    INSUFFICIENTREARMCOUNT = "InsufficientRearmCount"
    PROTOCOLOSINCOMPATIBILITY = "ProtocolOSIncompatibility"
    MEMORYINTEGRITYINCOMPATIBILITY = "MemoryIntegrityIncompatibility"
    RESTRICTEDDRIVELETTERINUSE = "RestrictedDriveLetterInUse"


class WorkspaceImageIngestionProcess:
    """WorkspaceImageIngestionProcess enum values."""

    BYOL_REGULAR = "BYOL_REGULAR"
    BYOL_GRAPHICS = "BYOL_GRAPHICS"
    BYOL_GRAPHICSPRO = "BYOL_GRAPHICSPRO"
    BYOL_GRAPHICS_G4DN = "BYOL_GRAPHICS_G4DN"
    BYOL_REGULAR_WSP = "BYOL_REGULAR_WSP"
    BYOL_GRAPHICS_G4DN_WSP = "BYOL_GRAPHICS_G4DN_WSP"
    BYOL_REGULAR_BYOP = "BYOL_REGULAR_BYOP"
    BYOL_GRAPHICS_G4DN_BYOP = "BYOL_GRAPHICS_G4DN_BYOP"


class WorkspaceImageRequiredTenancy:
    """WorkspaceImageRequiredTenancy enum values."""

    DEFAULT = "DEFAULT"
    DEDICATED = "DEDICATED"


class WorkspaceImageState:
    """WorkspaceImageState enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    ERROR = "ERROR"


class WorkspaceState:
    """WorkspaceState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    IMPAIRED = "IMPAIRED"
    UNHEALTHY = "UNHEALTHY"
    REBOOTING = "REBOOTING"
    STARTING = "STARTING"
    REBUILDING = "REBUILDING"
    RESTORING = "RESTORING"
    MAINTENANCE = "MAINTENANCE"
    ADMIN_MAINTENANCE = "ADMIN_MAINTENANCE"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    SUSPENDED = "SUSPENDED"
    UPDATING = "UPDATING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


class WorkspaceType:
    """WorkspaceType enum values."""

    PERSONAL = "PERSONAL"
    POOLS = "POOLS"


class WorkspacesPoolErrorCode:
    """WorkspacesPoolErrorCode enum values."""

    IAM_SERVICE_ROLE_IS_MISSING = "IAM_SERVICE_ROLE_IS_MISSING"
    IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION"
    NETWORK_INTERFACE_LIMIT_EXCEEDED = "NETWORK_INTERFACE_LIMIT_EXCEEDED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"
    MACHINE_ROLE_IS_MISSING = "MACHINE_ROLE_IS_MISSING"
    STS_DISABLED_IN_REGION = "STS_DISABLED_IN_REGION"
    SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES = "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES"
    IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION = "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION"
    SUBNET_NOT_FOUND = "SUBNET_NOT_FOUND"
    IMAGE_NOT_FOUND = "IMAGE_NOT_FOUND"
    INVALID_SUBNET_CONFIGURATION = "INVALID_SUBNET_CONFIGURATION"
    SECURITY_GROUPS_NOT_FOUND = "SECURITY_GROUPS_NOT_FOUND"
    IGW_NOT_ATTACHED = "IGW_NOT_ATTACHED"
    IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION = "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION"
    WORKSPACES_POOL_STOPPED = "WORKSPACES_POOL_STOPPED"
    WORKSPACES_POOL_INSTANCE_PROVISIONING_FAILURE = "WORKSPACES_POOL_INSTANCE_PROVISIONING_FAILURE"
    DOMAIN_JOIN_ERROR_FILE_NOT_FOUND = "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND"
    DOMAIN_JOIN_ERROR_ACCESS_DENIED = "DOMAIN_JOIN_ERROR_ACCESS_DENIED"
    DOMAIN_JOIN_ERROR_LOGON_FAILURE = "DOMAIN_JOIN_ERROR_LOGON_FAILURE"
    DOMAIN_JOIN_ERROR_INVALID_PARAMETER = "DOMAIN_JOIN_ERROR_INVALID_PARAMETER"
    DOMAIN_JOIN_ERROR_MORE_DATA = "DOMAIN_JOIN_ERROR_MORE_DATA"
    DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN = "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN"
    DOMAIN_JOIN_ERROR_NOT_SUPPORTED = "DOMAIN_JOIN_ERROR_NOT_SUPPORTED"
    DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME = "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME"
    DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED = "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED"
    DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED = "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED"
    DOMAIN_JOIN_NERR_PASSWORD_EXPIRED = "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED"
    DOMAIN_JOIN_INTERNAL_SERVICE_ERROR = "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR"
    DOMAIN_JOIN_ERROR_SECRET_ACTION_PERMISSION_IS_MISSING = "DOMAIN_JOIN_ERROR_SECRET_ACTION_PERMISSION_IS_MISSING"
    DOMAIN_JOIN_ERROR_SECRET_DECRYPTION_FAILURE = "DOMAIN_JOIN_ERROR_SECRET_DECRYPTION_FAILURE"
    DOMAIN_JOIN_ERROR_SECRET_STATE_INVALID = "DOMAIN_JOIN_ERROR_SECRET_STATE_INVALID"
    DOMAIN_JOIN_ERROR_SECRET_NOT_FOUND = "DOMAIN_JOIN_ERROR_SECRET_NOT_FOUND"
    DOMAIN_JOIN_ERROR_SECRET_VALUE_KEY_NOT_FOUND = "DOMAIN_JOIN_ERROR_SECRET_VALUE_KEY_NOT_FOUND"
    DOMAIN_JOIN_ERROR_SECRET_INVALID = "DOMAIN_JOIN_ERROR_SECRET_INVALID"
    BUNDLE_NOT_FOUND = "BUNDLE_NOT_FOUND"
    DIRECTORY_NOT_FOUND = "DIRECTORY_NOT_FOUND"
    INSUFFICIENT_PERMISSIONS_ERROR = "INSUFFICIENT_PERMISSIONS_ERROR"
    DEFAULT_OU_IS_MISSING = "DEFAULT_OU_IS_MISSING"


class WorkspacesPoolState:
    """WorkspacesPoolState enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    RUNNING = "RUNNING"
    STARTING = "STARTING"
    STOPPED = "STOPPED"
    STOPPING = "STOPPING"
    UPDATING = "UPDATING"


@dataclass
class ApplicationSettings(PropertyType):
    STATUS = "Status"
    SETTINGS_GROUP = "SettingsGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "settings_group": "SettingsGroup",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    settings_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Capacity(PropertyType):
    DESIRED_USER_SESSIONS = "DesiredUserSessions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "desired_user_sessions": "DesiredUserSessions",
    }

    desired_user_sessions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeoutSettings(PropertyType):
    MAX_USER_DURATION_IN_SECONDS = "MaxUserDurationInSeconds"
    IDLE_DISCONNECT_TIMEOUT_IN_SECONDS = "IdleDisconnectTimeoutInSeconds"
    DISCONNECT_TIMEOUT_IN_SECONDS = "DisconnectTimeoutInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_user_duration_in_seconds": "MaxUserDurationInSeconds",
        "idle_disconnect_timeout_in_seconds": "IdleDisconnectTimeoutInSeconds",
        "disconnect_timeout_in_seconds": "DisconnectTimeoutInSeconds",
    }

    max_user_duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    idle_disconnect_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    disconnect_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None

