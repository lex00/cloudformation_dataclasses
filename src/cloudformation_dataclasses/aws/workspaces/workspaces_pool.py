"""PropertyTypes for AWS::WorkSpaces::WorkspacesPool."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

