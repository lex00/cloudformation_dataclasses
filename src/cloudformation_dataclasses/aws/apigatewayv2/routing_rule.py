"""PropertyTypes for AWS::ApiGatewayV2::RoutingRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    INVOKE_API = "InvokeApi"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invoke_api": "InvokeApi",
    }

    invoke_api: Optional[ActionInvokeApi] = None


@dataclass
class ActionInvokeApi(PropertyType):
    STRIP_BASE_PATH = "StripBasePath"
    STAGE = "Stage"
    API_ID = "ApiId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "strip_base_path": "StripBasePath",
        "stage": "Stage",
        "api_id": "ApiId",
    }

    strip_base_path: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    stage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Condition(PropertyType):
    MATCH_BASE_PATHS = "MatchBasePaths"
    MATCH_HEADERS = "MatchHeaders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "match_base_paths": "MatchBasePaths",
        "match_headers": "MatchHeaders",
    }

    match_base_paths: Optional[MatchBasePaths] = None
    match_headers: Optional[MatchHeaders] = None


@dataclass
class MatchBasePaths(PropertyType):
    ANY_OF = "AnyOf"

    _property_mappings: ClassVar[dict[str, str]] = {
        "any_of": "AnyOf",
    }

    any_of: Optional[Union[list[str], Ref]] = None


@dataclass
class MatchHeaderValue(PropertyType):
    VALUE_GLOB = "ValueGlob"
    HEADER = "Header"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_glob": "ValueGlob",
        "header": "Header",
    }

    value_glob: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MatchHeaders(PropertyType):
    ANY_OF = "AnyOf"

    _property_mappings: ClassVar[dict[str, str]] = {
        "any_of": "AnyOf",
    }

    any_of: Optional[list[MatchHeaderValue]] = None

