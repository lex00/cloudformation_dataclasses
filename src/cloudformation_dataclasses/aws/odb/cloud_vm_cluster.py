"""PropertyTypes for AWS::ODB::CloudVmCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Access:
    """Access enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ComputeModel:
    """ComputeModel enum values."""

    ECPU = "ECPU"
    OCPU = "OCPU"


class DayOfWeekName:
    """DayOfWeekName enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DbNodeMaintenanceType:
    """DbNodeMaintenanceType enum values."""

    VMDB_REBOOT_MIGRATION = "VMDB_REBOOT_MIGRATION"


class DbNodeResourceStatus:
    """DbNodeResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    STARTING = "STARTING"


class DbServerPatchingStatus:
    """DbServerPatchingStatus enum values."""

    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"
    SCHEDULED = "SCHEDULED"


class DiskRedundancy:
    """DiskRedundancy enum values."""

    HIGH = "HIGH"
    NORMAL = "NORMAL"


class IamRoleStatus:
    """IamRoleStatus enum values."""

    ASSOCIATING = "ASSOCIATING"
    DISASSOCIATING = "DISASSOCIATING"
    FAILED = "FAILED"
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    PARTIALLY_CONNECTED = "PARTIALLY_CONNECTED"
    UNKNOWN = "UNKNOWN"


class IormLifecycleState:
    """IormLifecycleState enum values."""

    BOOTSTRAPPING = "BOOTSTRAPPING"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    FAILED = "FAILED"
    UPDATING = "UPDATING"


class LicenseModel:
    """LicenseModel enum values."""

    BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"
    LICENSE_INCLUDED = "LICENSE_INCLUDED"


class ManagedResourceStatus:
    """ManagedResourceStatus enum values."""

    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DISABLED = "DISABLED"
    DISABLING = "DISABLING"


class MonthName:
    """MonthName enum values."""

    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"


class Objective:
    """Objective enum values."""

    AUTO = "AUTO"
    BALANCED = "BALANCED"
    BASIC = "BASIC"
    HIGH_THROUGHPUT = "HIGH_THROUGHPUT"
    LOW_LATENCY = "LOW_LATENCY"


class OciOnboardingStatus:
    """OciOnboardingStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    PENDING_LINK_GENERATION = "PENDING_LINK_GENERATION"
    PENDING_CUSTOMER_ACTION = "PENDING_CUSTOMER_ACTION"
    PENDING_INITIALIZATION = "PENDING_INITIALIZATION"
    ACTIVATING = "ACTIVATING"
    ACTIVE_IN_HOME_REGION = "ACTIVE_IN_HOME_REGION"
    ACTIVE = "ACTIVE"
    ACTIVE_LIMITED = "ACTIVE_LIMITED"
    FAILED = "FAILED"
    PUBLIC_OFFER_UNSUPPORTED = "PUBLIC_OFFER_UNSUPPORTED"
    SUSPENDED = "SUSPENDED"
    CANCELED = "CANCELED"


class PatchingModeType:
    """PatchingModeType enum values."""

    ROLLING = "ROLLING"
    NONROLLING = "NONROLLING"


class PreferenceType:
    """PreferenceType enum values."""

    NO_PREFERENCE = "NO_PREFERENCE"
    CUSTOM_PREFERENCE = "CUSTOM_PREFERENCE"


class ResourceStatus:
    """ResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"
    MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"


class ShapeType:
    """ShapeType enum values."""

    AMD = "AMD"
    INTEL = "INTEL"
    INTEL_FLEX_X9 = "INTEL_FLEX_X9"
    AMPERE_FLEX_A1 = "AMPERE_FLEX_A1"


class SupportedAwsIntegration:
    """SupportedAwsIntegration enum values."""

    KMSTDE = "KmsTde"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


class VpcEndpointType:
    """VpcEndpointType enum values."""

    SERVICENETWORK = "SERVICENETWORK"


@dataclass
class DataCollectionOptions(PropertyType):
    IS_INCIDENT_LOGS_ENABLED = "IsIncidentLogsEnabled"
    IS_DIAGNOSTICS_EVENTS_ENABLED = "IsDiagnosticsEventsEnabled"
    IS_HEALTH_MONITORING_ENABLED = "IsHealthMonitoringEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_incident_logs_enabled": "IsIncidentLogsEnabled",
        "is_diagnostics_events_enabled": "IsDiagnosticsEventsEnabled",
        "is_health_monitoring_enabled": "IsHealthMonitoringEnabled",
    }

    is_incident_logs_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_diagnostics_events_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_health_monitoring_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DbNode(PropertyType):
    STATUS = "Status"
    HOST_IP_ID = "HostIpId"
    MEMORY_SIZE_IN_G_BS = "MemorySizeInGBs"
    CPU_CORE_COUNT = "CpuCoreCount"
    BACKUP_IP_ID = "BackupIpId"
    HOSTNAME = "Hostname"
    OCID = "Ocid"
    DB_NODE_ID = "DbNodeId"
    VNIC_ID = "VnicId"
    DB_NODE_STORAGE_SIZE_IN_G_BS = "DbNodeStorageSizeInGBs"
    VNIC2_ID = "Vnic2Id"
    DB_NODE_ARN = "DbNodeArn"
    DB_SERVER_ID = "DbServerId"
    BACKUP_VNIC2_ID = "BackupVnic2Id"
    TAGS = "Tags"
    DB_SYSTEM_ID = "DbSystemId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "host_ip_id": "HostIpId",
        "memory_size_in_g_bs": "MemorySizeInGBs",
        "cpu_core_count": "CpuCoreCount",
        "backup_ip_id": "BackupIpId",
        "hostname": "Hostname",
        "ocid": "Ocid",
        "db_node_id": "DbNodeId",
        "vnic_id": "VnicId",
        "db_node_storage_size_in_g_bs": "DbNodeStorageSizeInGBs",
        "vnic2_id": "Vnic2Id",
        "db_node_arn": "DbNodeArn",
        "db_server_id": "DbServerId",
        "backup_vnic2_id": "BackupVnic2Id",
        "tags": "Tags",
        "db_system_id": "DbSystemId",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_ip_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory_size_in_g_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cpu_core_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    backup_ip_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ocid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_node_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vnic_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_node_storage_size_in_g_bs: Optional[Union[int, Ref, GetAtt, Sub]] = None
    vnic2_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_node_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_server_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    backup_vnic2_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    db_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

