"""PropertyTypes for AWS::AmazonMQ::ConfigurationAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AuthenticationStrategy:
    """AuthenticationStrategy enum values."""

    SIMPLE = "SIMPLE"
    LDAP = "LDAP"
    CONFIG_MANAGED = "CONFIG_MANAGED"


class BrokerState:
    """BrokerState enum values."""

    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_FAILED = "CREATION_FAILED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    RUNNING = "RUNNING"
    REBOOT_IN_PROGRESS = "REBOOT_IN_PROGRESS"
    CRITICAL_ACTION_REQUIRED = "CRITICAL_ACTION_REQUIRED"
    REPLICA = "REPLICA"


class BrokerStorageType:
    """BrokerStorageType enum values."""

    EBS = "EBS"
    EFS = "EFS"


class ChangeType:
    """ChangeType enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class DataReplicationMode:
    """DataReplicationMode enum values."""

    NONE = "NONE"
    CRDR = "CRDR"


class DayOfWeek:
    """DayOfWeek enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DeploymentMode:
    """DeploymentMode enum values."""

    SINGLE_INSTANCE = "SINGLE_INSTANCE"
    ACTIVE_STANDBY_MULTI_AZ = "ACTIVE_STANDBY_MULTI_AZ"
    CLUSTER_MULTI_AZ = "CLUSTER_MULTI_AZ"


class EngineType:
    """EngineType enum values."""

    ACTIVEMQ = "ACTIVEMQ"
    RABBITMQ = "RABBITMQ"


class PromoteMode:
    """PromoteMode enum values."""

    SWITCHOVER = "SWITCHOVER"
    FAILOVER = "FAILOVER"


class SanitizationWarningReason:
    """SanitizationWarningReason enum values."""

    DISALLOWED_ELEMENT_REMOVED = "DISALLOWED_ELEMENT_REMOVED"
    DISALLOWED_ATTRIBUTE_REMOVED = "DISALLOWED_ATTRIBUTE_REMOVED"
    INVALID_ATTRIBUTE_VALUE_REMOVED = "INVALID_ATTRIBUTE_VALUE_REMOVED"


@dataclass
class ConfigurationId(PropertyType):
    REVISION = "Revision"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "revision": "Revision",
        "id": "Id",
    }

    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

