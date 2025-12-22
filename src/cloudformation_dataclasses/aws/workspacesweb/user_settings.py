"""PropertyTypes for AWS::WorkSpacesWeb::UserSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CookieSpecification(PropertyType):
    PATH = "Path"
    DOMAIN = "Domain"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "domain": "Domain",
        "name": "Name",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CookieSynchronizationConfiguration(PropertyType):
    BLOCKLIST = "Blocklist"
    ALLOWLIST = "Allowlist"

    _property_mappings: ClassVar[dict[str, str]] = {
        "blocklist": "Blocklist",
        "allowlist": "Allowlist",
    }

    blocklist: Optional[list[CookieSpecification]] = None
    allowlist: Optional[list[CookieSpecification]] = None


@dataclass
class ToolbarConfiguration(PropertyType):
    TOOLBAR_TYPE = "ToolbarType"
    HIDDEN_TOOLBAR_ITEMS = "HiddenToolbarItems"
    MAX_DISPLAY_RESOLUTION = "MaxDisplayResolution"
    VISUAL_MODE = "VisualMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "toolbar_type": "ToolbarType",
        "hidden_toolbar_items": "HiddenToolbarItems",
        "max_display_resolution": "MaxDisplayResolution",
        "visual_mode": "VisualMode",
    }

    toolbar_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hidden_toolbar_items: Optional[Union[list[str], Ref]] = None
    max_display_resolution: Optional[Union[str, Ref, GetAtt, Sub]] = None
    visual_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None

