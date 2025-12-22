"""PropertyTypes for AWS::SSMIncidents::ReplicationSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class IncidentRecordStatus:
    """IncidentRecordStatus enum values."""

    OPEN = "OPEN"
    RESOLVED = "RESOLVED"


class ItemType:
    """ItemType enum values."""

    ANALYSIS = "ANALYSIS"
    INCIDENT = "INCIDENT"
    METRIC = "METRIC"
    PARENT = "PARENT"
    ATTACHMENT = "ATTACHMENT"
    OTHER = "OTHER"
    AUTOMATION = "AUTOMATION"
    INVOLVED_RESOURCE = "INVOLVED_RESOURCE"
    TASK = "TASK"


class RegionStatus:
    """RegionStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ReplicationSetStatus:
    """ReplicationSetStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ResourceType:
    """ResourceType enum values."""

    RESPONSE_PLAN = "RESPONSE_PLAN"
    INCIDENT_RECORD = "INCIDENT_RECORD"
    TIMELINE_EVENT = "TIMELINE_EVENT"
    REPLICATION_SET = "REPLICATION_SET"
    RESOURCE_POLICY = "RESOURCE_POLICY"


class ServiceCode:
    """ServiceCode enum values."""

    SSM_INCIDENTS = "ssm-incidents"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SsmTargetAccount:
    """SsmTargetAccount enum values."""

    RESPONSE_PLAN_OWNER_ACCOUNT = "RESPONSE_PLAN_OWNER_ACCOUNT"
    IMPACTED_ACCOUNT = "IMPACTED_ACCOUNT"


class TimelineEventSort:
    """TimelineEventSort enum values."""

    EVENT_TIME = "EVENT_TIME"


class VariableType:
    """VariableType enum values."""

    INCIDENT_RECORD_ARN = "INCIDENT_RECORD_ARN"
    INVOLVED_RESOURCES = "INVOLVED_RESOURCES"


@dataclass
class RegionConfiguration(PropertyType):
    SSE_KMS_KEY_ID = "SseKmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_kms_key_id": "SseKmsKeyId",
    }

    sse_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationRegion(PropertyType):
    REGION_CONFIGURATION = "RegionConfiguration"
    REGION_NAME = "RegionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region_configuration": "RegionConfiguration",
        "region_name": "RegionName",
    }

    region_configuration: Optional[RegionConfiguration] = None
    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

