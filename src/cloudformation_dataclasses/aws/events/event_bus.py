"""PropertyTypes for AWS::Events::EventBus."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApiDestinationHttpMethod:
    """ApiDestinationHttpMethod enum values."""

    POST = "POST"
    GET = "GET"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ApiDestinationState:
    """ApiDestinationState enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ArchiveState:
    """ArchiveState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"


class AssignPublicIp:
    """AssignPublicIp enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ConnectionAuthorizationType:
    """ConnectionAuthorizationType enum values."""

    BASIC = "BASIC"
    OAUTH_CLIENT_CREDENTIALS = "OAUTH_CLIENT_CREDENTIALS"
    API_KEY = "API_KEY"


class ConnectionOAuthHttpMethod:
    """ConnectionOAuthHttpMethod enum values."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class ConnectionState:
    """ConnectionState enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    AUTHORIZED = "AUTHORIZED"
    DEAUTHORIZED = "DEAUTHORIZED"
    AUTHORIZING = "AUTHORIZING"
    DEAUTHORIZING = "DEAUTHORIZING"
    ACTIVE = "ACTIVE"
    FAILED_CONNECTIVITY = "FAILED_CONNECTIVITY"


class EndpointState:
    """EndpointState enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


class EventSourceState:
    """EventSourceState enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class IncludeDetail:
    """IncludeDetail enum values."""

    NONE = "NONE"
    FULL = "FULL"


class LaunchType:
    """LaunchType enum values."""

    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class Level:
    """Level enum values."""

    OFF = "OFF"
    ERROR = "ERROR"
    INFO = "INFO"
    TRACE = "TRACE"


class PlacementConstraintType:
    """PlacementConstraintType enum values."""

    DISTINCTINSTANCE = "distinctInstance"
    MEMBEROF = "memberOf"


class PlacementStrategyType:
    """PlacementStrategyType enum values."""

    RANDOM = "random"
    SPREAD = "spread"
    BINPACK = "binpack"


class PropagateTags:
    """PropagateTags enum values."""

    TASK_DEFINITION = "TASK_DEFINITION"


class ReplayState:
    """ReplayState enum values."""

    STARTING = "STARTING"
    RUNNING = "RUNNING"
    CANCELLING = "CANCELLING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class ReplicationState:
    """ReplicationState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RuleState:
    """RuleState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS = "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS"


@dataclass
class DeadLetterConfig(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfig(PropertyType):
    INCLUDE_DETAIL = "IncludeDetail"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_detail": "IncludeDetail",
        "level": "Level",
    }

    include_detail: Optional[Union[str, IncludeDetail, Ref, GetAtt, Sub]] = None
    level: Optional[Union[str, Level, Ref, GetAtt, Sub]] = None

