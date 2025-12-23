"""PropertyTypes for AWS::CodeGuruProfiler::ProfilingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AgentPermissions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "principals": "Principals",
    }

    principals: Optional[Union[list[str], Ref]] = None


@dataclass
class Channel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_uri": "channelUri",
        "channel_id": "channelId",
    }

    channel_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

