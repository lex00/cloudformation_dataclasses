"""PropertyTypes for AWS::Cloud9::EnvironmentEC2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Repository(PropertyType):
    PATH_COMPONENT = "PathComponent"
    REPOSITORY_URL = "RepositoryUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path_component": "PathComponent",
        "repository_url": "RepositoryUrl",
    }

    path_component: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

