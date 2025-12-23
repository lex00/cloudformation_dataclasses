"""PropertyTypes for AWS::ODB::CloudVmCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataCollectionOptions(PropertyType):
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

