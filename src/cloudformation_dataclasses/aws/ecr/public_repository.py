"""PropertyTypes for AWS::ECR::PublicRepository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RepositoryCatalogData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "about_text": "AboutText",
        "operating_systems": "OperatingSystems",
        "usage_text": "UsageText",
        "repository_description": "RepositoryDescription",
        "architectures": "Architectures",
    }

    about_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    operating_systems: Optional[Union[list[str], Ref]] = None
    usage_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    architectures: Optional[Union[list[str], Ref]] = None

