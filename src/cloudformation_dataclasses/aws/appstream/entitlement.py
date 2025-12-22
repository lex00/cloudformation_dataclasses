"""PropertyTypes for AWS::AppStream::Entitlement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessEndpointType:
    """AccessEndpointType enum values."""

    STREAMING = "STREAMING"


class Action:
    """Action enum values."""

    CLIPBOARD_COPY_FROM_LOCAL_DEVICE = "CLIPBOARD_COPY_FROM_LOCAL_DEVICE"
    CLIPBOARD_COPY_TO_LOCAL_DEVICE = "CLIPBOARD_COPY_TO_LOCAL_DEVICE"
    FILE_UPLOAD = "FILE_UPLOAD"
    FILE_DOWNLOAD = "FILE_DOWNLOAD"
    PRINTING_TO_LOCAL_DEVICE = "PRINTING_TO_LOCAL_DEVICE"
    DOMAIN_PASSWORD_SIGNIN = "DOMAIN_PASSWORD_SIGNIN"
    DOMAIN_SMART_CARD_SIGNIN = "DOMAIN_SMART_CARD_SIGNIN"
    AUTO_TIME_ZONE_REDIRECTION = "AUTO_TIME_ZONE_REDIRECTION"


class AgentSoftwareVersion:
    """AgentSoftwareVersion enum values."""

    CURRENT_LATEST = "CURRENT_LATEST"
    ALWAYS_LATEST = "ALWAYS_LATEST"


class AppBlockBuilderAttribute:
    """AppBlockBuilderAttribute enum values."""

    IAM_ROLE_ARN = "IAM_ROLE_ARN"
    ACCESS_ENDPOINTS = "ACCESS_ENDPOINTS"
    VPC_CONFIGURATION_SECURITY_GROUP_IDS = "VPC_CONFIGURATION_SECURITY_GROUP_IDS"


class AppBlockBuilderPlatformType:
    """AppBlockBuilderPlatformType enum values."""

    WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"


class AppBlockBuilderState:
    """AppBlockBuilderState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class AppBlockBuilderStateChangeReasonCode:
    """AppBlockBuilderStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"


class AppBlockState:
    """AppBlockState enum values."""

    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"


class AppVisibility:
    """AppVisibility enum values."""

    ALL = "ALL"
    ASSOCIATED = "ASSOCIATED"


class ApplicationAttribute:
    """ApplicationAttribute enum values."""

    LAUNCH_PARAMETERS = "LAUNCH_PARAMETERS"
    WORKING_DIRECTORY = "WORKING_DIRECTORY"


class AuthenticationType:
    """AuthenticationType enum values."""

    API = "API"
    SAML = "SAML"
    USERPOOL = "USERPOOL"
    AWS_AD = "AWS_AD"


class CertificateBasedAuthStatus:
    """CertificateBasedAuthStatus enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    ENABLED_NO_DIRECTORY_LOGIN_FALLBACK = "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK"


class DynamicAppProvidersEnabled:
    """DynamicAppProvidersEnabled enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ExportImageTaskState:
    """ExportImageTaskState enum values."""

    EXPORTING = "EXPORTING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class FleetAttribute:
    """FleetAttribute enum values."""

    VPC_CONFIGURATION = "VPC_CONFIGURATION"
    VPC_CONFIGURATION_SECURITY_GROUP_IDS = "VPC_CONFIGURATION_SECURITY_GROUP_IDS"
    DOMAIN_JOIN_INFO = "DOMAIN_JOIN_INFO"
    IAM_ROLE_ARN = "IAM_ROLE_ARN"
    USB_DEVICE_FILTER_STRINGS = "USB_DEVICE_FILTER_STRINGS"
    SESSION_SCRIPT_S3_LOCATION = "SESSION_SCRIPT_S3_LOCATION"
    MAX_SESSIONS_PER_INSTANCE = "MAX_SESSIONS_PER_INSTANCE"
    VOLUME_CONFIGURATION = "VOLUME_CONFIGURATION"


class FleetErrorCode:
    """FleetErrorCode enum values."""

    IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION"
    IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION = "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION"
    NETWORK_INTERFACE_LIMIT_EXCEEDED = "NETWORK_INTERFACE_LIMIT_EXCEEDED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"
    IAM_SERVICE_ROLE_IS_MISSING = "IAM_SERVICE_ROLE_IS_MISSING"
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
    FLEET_STOPPED = "FLEET_STOPPED"
    FLEET_INSTANCE_PROVISIONING_FAILURE = "FLEET_INSTANCE_PROVISIONING_FAILURE"
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
    VALIDATION_ERROR = "VALIDATION_ERROR"


class FleetState:
    """FleetState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class FleetType:
    """FleetType enum values."""

    ALWAYS_ON = "ALWAYS_ON"
    ON_DEMAND = "ON_DEMAND"
    ELASTIC = "ELASTIC"


class ImageBuilderState:
    """ImageBuilderState enum values."""

    PENDING = "PENDING"
    UPDATING_AGENT = "UPDATING_AGENT"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    REBOOTING = "REBOOTING"
    SNAPSHOTTING = "SNAPSHOTTING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    PENDING_QUALIFICATION = "PENDING_QUALIFICATION"
    PENDING_SYNCING_APPS = "PENDING_SYNCING_APPS"
    SYNCING_APPS = "SYNCING_APPS"
    PENDING_IMAGE_IMPORT = "PENDING_IMAGE_IMPORT"


class ImageBuilderStateChangeReasonCode:
    """ImageBuilderStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    IMAGE_UNAVAILABLE = "IMAGE_UNAVAILABLE"


class ImageSharedWithOthers:
    """ImageSharedWithOthers enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"


class ImageState:
    """ImageState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    COPYING = "COPYING"
    DELETING = "DELETING"
    CREATING = "CREATING"
    IMPORTING = "IMPORTING"
    VALIDATING = "VALIDATING"


class ImageStateChangeReasonCode:
    """ImageStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    IMAGE_BUILDER_NOT_AVAILABLE = "IMAGE_BUILDER_NOT_AVAILABLE"
    IMAGE_COPY_FAILURE = "IMAGE_COPY_FAILURE"
    IMAGE_UPDATE_FAILURE = "IMAGE_UPDATE_FAILURE"
    IMAGE_IMPORT_FAILURE = "IMAGE_IMPORT_FAILURE"


class ImageType:
    """ImageType enum values."""

    CUSTOM = "CUSTOM"
    NATIVE = "NATIVE"


class LatestAppstreamAgentVersion:
    """LatestAppstreamAgentVersion enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"


class MessageAction:
    """MessageAction enum values."""

    SUPPRESS = "SUPPRESS"
    RESEND = "RESEND"


class PackagingType:
    """PackagingType enum values."""

    CUSTOM = "CUSTOM"
    APPSTREAM2 = "APPSTREAM2"


class Permission:
    """Permission enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PlatformType:
    """PlatformType enum values."""

    WINDOWS = "WINDOWS"
    WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"
    WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"
    WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"
    AMAZON_LINUX2 = "AMAZON_LINUX2"
    RHEL8 = "RHEL8"
    ROCKY_LINUX8 = "ROCKY_LINUX8"


class PreferredProtocol:
    """PreferredProtocol enum values."""

    TCP = "TCP"
    UDP = "UDP"


class SessionConnectionState:
    """SessionConnectionState enum values."""

    CONNECTED = "CONNECTED"
    NOT_CONNECTED = "NOT_CONNECTED"


class SessionState:
    """SessionState enum values."""

    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"


class SoftwareDeploymentStatus:
    """SoftwareDeploymentStatus enum values."""

    STAGED_FOR_INSTALLATION = "STAGED_FOR_INSTALLATION"
    PENDING_INSTALLATION = "PENDING_INSTALLATION"
    INSTALLED = "INSTALLED"
    STAGED_FOR_UNINSTALLATION = "STAGED_FOR_UNINSTALLATION"
    PENDING_UNINSTALLATION = "PENDING_UNINSTALLATION"
    FAILED_TO_INSTALL = "FAILED_TO_INSTALL"
    FAILED_TO_UNINSTALL = "FAILED_TO_UNINSTALL"


class StackAttribute:
    """StackAttribute enum values."""

    STORAGE_CONNECTORS = "STORAGE_CONNECTORS"
    STORAGE_CONNECTOR_HOMEFOLDERS = "STORAGE_CONNECTOR_HOMEFOLDERS"
    STORAGE_CONNECTOR_GOOGLE_DRIVE = "STORAGE_CONNECTOR_GOOGLE_DRIVE"
    STORAGE_CONNECTOR_ONE_DRIVE = "STORAGE_CONNECTOR_ONE_DRIVE"
    REDIRECT_URL = "REDIRECT_URL"
    FEEDBACK_URL = "FEEDBACK_URL"
    THEME_NAME = "THEME_NAME"
    USER_SETTINGS = "USER_SETTINGS"
    EMBED_HOST_DOMAINS = "EMBED_HOST_DOMAINS"
    IAM_ROLE_ARN = "IAM_ROLE_ARN"
    ACCESS_ENDPOINTS = "ACCESS_ENDPOINTS"
    STREAMING_EXPERIENCE_SETTINGS = "STREAMING_EXPERIENCE_SETTINGS"


class StackErrorCode:
    """StackErrorCode enum values."""

    STORAGE_CONNECTOR_ERROR = "STORAGE_CONNECTOR_ERROR"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"


class StorageConnectorType:
    """StorageConnectorType enum values."""

    HOMEFOLDERS = "HOMEFOLDERS"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    ONE_DRIVE = "ONE_DRIVE"


class StreamView:
    """StreamView enum values."""

    APP = "APP"
    DESKTOP = "DESKTOP"


class ThemeAttribute:
    """ThemeAttribute enum values."""

    FOOTER_LINKS = "FOOTER_LINKS"


class ThemeState:
    """ThemeState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ThemeStyling:
    """ThemeStyling enum values."""

    LIGHT_BLUE = "LIGHT_BLUE"
    BLUE = "BLUE"
    PINK = "PINK"
    RED = "RED"


class UsageReportExecutionErrorCode:
    """UsageReportExecutionErrorCode enum values."""

    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    ACCESS_DENIED = "ACCESS_DENIED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"


class UsageReportSchedule:
    """UsageReportSchedule enum values."""

    DAILY = "DAILY"


class UserStackAssociationErrorCode:
    """UserStackAssociationErrorCode enum values."""

    STACK_NOT_FOUND = "STACK_NOT_FOUND"
    USER_NAME_NOT_FOUND = "USER_NAME_NOT_FOUND"
    DIRECTORY_NOT_FOUND = "DIRECTORY_NOT_FOUND"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class VisibilityType:
    """VisibilityType enum values."""

    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    SHARED = "SHARED"


@dataclass
class Attribute(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

