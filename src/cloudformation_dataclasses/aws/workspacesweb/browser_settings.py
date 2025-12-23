"""PropertyTypes for AWS::WorkSpacesWeb::BrowserSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class WebContentFilteringPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "blocked_urls": "BlockedUrls",
        "allowed_urls": "AllowedUrls",
        "blocked_categories": "BlockedCategories",
    }

    blocked_urls: Optional[Union[list[str], Ref]] = None
    allowed_urls: Optional[Union[list[str], Ref]] = None
    blocked_categories: Optional[Union[list[str], Ref]] = None

