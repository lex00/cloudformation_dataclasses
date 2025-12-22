"""PropertyTypes for AWS::RefactorSpaces::Route."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DefaultRouteInput(PropertyType):
    ACTIVATION_STATE = "ActivationState"

    _property_mappings: ClassVar[dict[str, str]] = {
        "activation_state": "ActivationState",
    }

    activation_state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UriPathRouteInput(PropertyType):
    SOURCE_PATH = "SourcePath"
    APPEND_SOURCE_PATH = "AppendSourcePath"
    ACTIVATION_STATE = "ActivationState"
    METHODS = "Methods"
    INCLUDE_CHILD_PATHS = "IncludeChildPaths"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_path": "SourcePath",
        "append_source_path": "AppendSourcePath",
        "activation_state": "ActivationState",
        "methods": "Methods",
        "include_child_paths": "IncludeChildPaths",
    }

    source_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    append_source_path: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    activation_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    methods: Optional[Union[list[str], Ref]] = None
    include_child_paths: Optional[Union[bool, Ref, GetAtt, Sub]] = None

