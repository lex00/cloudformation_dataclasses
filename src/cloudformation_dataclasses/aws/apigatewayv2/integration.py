"""PropertyTypes for AWS::ApiGatewayV2::Integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResponseParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResponseParameterMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "response_parameters": "ResponseParameters",
    }

    response_parameters: Optional[list[ResponseParameter]] = None


@dataclass
class TlsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "server_name_to_verify": "ServerNameToVerify",
    }

    server_name_to_verify: Optional[Union[str, Ref, GetAtt, Sub]] = None

