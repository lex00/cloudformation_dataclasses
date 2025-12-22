"""PropertyTypes for AWS::AmazonMQ::Broker."""

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


@dataclass
class EncryptionOptions(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    USE_AWS_OWNED_KEY = "UseAwsOwnedKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "use_aws_owned_key": "UseAwsOwnedKey",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_aws_owned_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LdapServerMetadata(PropertyType):
    HOSTS = "Hosts"
    USER_ROLE_NAME = "UserRoleName"
    USER_SEARCH_MATCHING = "UserSearchMatching"
    ROLE_NAME = "RoleName"
    USER_BASE = "UserBase"
    USER_SEARCH_SUBTREE = "UserSearchSubtree"
    ROLE_SEARCH_MATCHING = "RoleSearchMatching"
    SERVICE_ACCOUNT_USERNAME = "ServiceAccountUsername"
    ROLE_BASE = "RoleBase"
    SERVICE_ACCOUNT_PASSWORD = "ServiceAccountPassword"
    ROLE_SEARCH_SUBTREE = "RoleSearchSubtree"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hosts": "Hosts",
        "user_role_name": "UserRoleName",
        "user_search_matching": "UserSearchMatching",
        "role_name": "RoleName",
        "user_base": "UserBase",
        "user_search_subtree": "UserSearchSubtree",
        "role_search_matching": "RoleSearchMatching",
        "service_account_username": "ServiceAccountUsername",
        "role_base": "RoleBase",
        "service_account_password": "ServiceAccountPassword",
        "role_search_subtree": "RoleSearchSubtree",
    }

    hosts: Optional[Union[list[str], Ref]] = None
    user_role_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_search_matching: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_base: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_search_subtree: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    role_search_matching: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_account_username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_base: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_account_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_search_subtree: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LogList(PropertyType):
    AUDIT = "Audit"
    GENERAL = "General"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audit": "Audit",
        "general": "General",
    }

    audit: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    general: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindow(PropertyType):
    DAY_OF_WEEK = "DayOfWeek"
    TIME_OF_DAY = "TimeOfDay"
    TIME_ZONE = "TimeZone"

    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_week": "DayOfWeek",
        "time_of_day": "TimeOfDay",
        "time_zone": "TimeZone",
    }

    day_of_week: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_of_day: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagsEntry(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class User(PropertyType):
    REPLICATION_USER = "ReplicationUser"
    USERNAME = "Username"
    GROUPS = "Groups"
    CONSOLE_ACCESS = "ConsoleAccess"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "replication_user": "ReplicationUser",
        "username": "Username",
        "groups": "Groups",
        "console_access": "ConsoleAccess",
        "password": "Password",
    }

    replication_user: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[list[str], Ref]] = None
    console_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None

