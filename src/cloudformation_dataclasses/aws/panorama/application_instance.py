"""PropertyTypes for AWS::Panorama::ApplicationInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationInstanceHealthStatus:
    """ApplicationInstanceHealthStatus enum values."""

    RUNNING = "RUNNING"
    ERROR = "ERROR"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class ApplicationInstanceStatus:
    """ApplicationInstanceStatus enum values."""

    DEPLOYMENT_PENDING = "DEPLOYMENT_PENDING"
    DEPLOYMENT_REQUESTED = "DEPLOYMENT_REQUESTED"
    DEPLOYMENT_IN_PROGRESS = "DEPLOYMENT_IN_PROGRESS"
    DEPLOYMENT_ERROR = "DEPLOYMENT_ERROR"
    DEPLOYMENT_SUCCEEDED = "DEPLOYMENT_SUCCEEDED"
    REMOVAL_PENDING = "REMOVAL_PENDING"
    REMOVAL_REQUESTED = "REMOVAL_REQUESTED"
    REMOVAL_IN_PROGRESS = "REMOVAL_IN_PROGRESS"
    REMOVAL_FAILED = "REMOVAL_FAILED"
    REMOVAL_SUCCEEDED = "REMOVAL_SUCCEEDED"
    DEPLOYMENT_FAILED = "DEPLOYMENT_FAILED"


class ConnectionType:
    """ConnectionType enum values."""

    STATIC_IP = "STATIC_IP"
    DHCP = "DHCP"


class DesiredState:
    """DesiredState enum values."""

    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    REMOVED = "REMOVED"


class DeviceAggregatedStatus:
    """DeviceAggregatedStatus enum values."""

    ERROR = "ERROR"
    AWAITING_PROVISIONING = "AWAITING_PROVISIONING"
    PENDING = "PENDING"
    FAILED = "FAILED"
    DELETING = "DELETING"
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    LEASE_EXPIRED = "LEASE_EXPIRED"
    UPDATE_NEEDED = "UPDATE_NEEDED"
    REBOOTING = "REBOOTING"


class DeviceBrand:
    """DeviceBrand enum values."""

    AWS_PANORAMA = "AWS_PANORAMA"
    LENOVO = "LENOVO"


class DeviceConnectionStatus:
    """DeviceConnectionStatus enum values."""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    AWAITING_CREDENTIALS = "AWAITING_CREDENTIALS"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    ERROR = "ERROR"


class DeviceReportedStatus:
    """DeviceReportedStatus enum values."""

    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    STOP_ERROR = "STOP_ERROR"
    REMOVAL_FAILED = "REMOVAL_FAILED"
    REMOVAL_IN_PROGRESS = "REMOVAL_IN_PROGRESS"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    INSTALL_ERROR = "INSTALL_ERROR"
    LAUNCHED = "LAUNCHED"
    LAUNCH_ERROR = "LAUNCH_ERROR"
    INSTALL_IN_PROGRESS = "INSTALL_IN_PROGRESS"


class DeviceStatus:
    """DeviceStatus enum values."""

    AWAITING_PROVISIONING = "AWAITING_PROVISIONING"
    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    ERROR = "ERROR"
    DELETING = "DELETING"


class DeviceType:
    """DeviceType enum values."""

    PANORAMA_APPLIANCE_DEVELOPER_KIT = "PANORAMA_APPLIANCE_DEVELOPER_KIT"
    PANORAMA_APPLIANCE = "PANORAMA_APPLIANCE"


class JobResourceType:
    """JobResourceType enum values."""

    PACKAGE = "PACKAGE"


class JobType:
    """JobType enum values."""

    OTA = "OTA"
    REBOOT = "REBOOT"


class ListDevicesSortBy:
    """ListDevicesSortBy enum values."""

    DEVICE_ID = "DEVICE_ID"
    CREATED_TIME = "CREATED_TIME"
    NAME = "NAME"
    DEVICE_AGGREGATED_STATUS = "DEVICE_AGGREGATED_STATUS"


class NetworkConnectionStatus:
    """NetworkConnectionStatus enum values."""

    CONNECTED = "CONNECTED"
    NOT_CONNECTED = "NOT_CONNECTED"
    CONNECTING = "CONNECTING"


class NodeCategory:
    """NodeCategory enum values."""

    BUSINESS_LOGIC = "BUSINESS_LOGIC"
    ML_MODEL = "ML_MODEL"
    MEDIA_SOURCE = "MEDIA_SOURCE"
    MEDIA_SINK = "MEDIA_SINK"


class NodeFromTemplateJobStatus:
    """NodeFromTemplateJobStatus enum values."""

    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class NodeInstanceStatus:
    """NodeInstanceStatus enum values."""

    RUNNING = "RUNNING"
    ERROR = "ERROR"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    PAUSED = "PAUSED"


class NodeSignalValue:
    """NodeSignalValue enum values."""

    PAUSE = "PAUSE"
    RESUME = "RESUME"


class PackageImportJobStatus:
    """PackageImportJobStatus enum values."""

    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class PackageImportJobType:
    """PackageImportJobType enum values."""

    NODE_PACKAGE_VERSION = "NODE_PACKAGE_VERSION"
    MARKETPLACE_NODE_PACKAGE_VERSION = "MARKETPLACE_NODE_PACKAGE_VERSION"


class PackageVersionStatus:
    """PackageVersionStatus enum values."""

    REGISTER_PENDING = "REGISTER_PENDING"
    REGISTER_COMPLETED = "REGISTER_COMPLETED"
    FAILED = "FAILED"
    DELETING = "DELETING"


class PortType:
    """PortType enum values."""

    BOOLEAN = "BOOLEAN"
    STRING = "STRING"
    INT32 = "INT32"
    FLOAT32 = "FLOAT32"
    MEDIA = "MEDIA"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class StatusFilter:
    """StatusFilter enum values."""

    DEPLOYMENT_SUCCEEDED = "DEPLOYMENT_SUCCEEDED"
    DEPLOYMENT_ERROR = "DEPLOYMENT_ERROR"
    REMOVAL_SUCCEEDED = "REMOVAL_SUCCEEDED"
    REMOVAL_FAILED = "REMOVAL_FAILED"
    PROCESSING_DEPLOYMENT = "PROCESSING_DEPLOYMENT"
    PROCESSING_REMOVAL = "PROCESSING_REMOVAL"
    DEPLOYMENT_FAILED = "DEPLOYMENT_FAILED"


class TemplateType:
    """TemplateType enum values."""

    RTSP_CAMERA_STREAM = "RTSP_CAMERA_STREAM"


class UpdateProgress:
    """UpdateProgress enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    VERIFYING = "VERIFYING"
    REBOOTING = "REBOOTING"
    DOWNLOADING = "DOWNLOADING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


@dataclass
class ManifestOverridesPayload(PropertyType):
    PAYLOAD_DATA = "PayloadData"

    _property_mappings: ClassVar[dict[str, str]] = {
        "payload_data": "PayloadData",
    }

    payload_data: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManifestPayload(PropertyType):
    PAYLOAD_DATA = "PayloadData"

    _property_mappings: ClassVar[dict[str, str]] = {
        "payload_data": "PayloadData",
    }

    payload_data: Optional[Union[str, Ref, GetAtt, Sub]] = None

