"""PropertyTypes for AWS::DataSync::LocationNFS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MountOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OnPremConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_arns": "AgentArns",
    }

    agent_arns: Optional[Union[list[str], Ref]] = None

