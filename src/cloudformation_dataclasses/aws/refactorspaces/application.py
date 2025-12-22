"""PropertyTypes for AWS::RefactorSpaces::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApiGatewayProxyInput(PropertyType):
    STAGE_NAME = "StageName"
    ENDPOINT_TYPE = "EndpointType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stage_name": "StageName",
        "endpoint_type": "EndpointType",
    }

    stage_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

