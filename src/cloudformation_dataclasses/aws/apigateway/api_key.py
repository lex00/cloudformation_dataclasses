"""PropertyTypes for AWS::ApiGateway::ApiKey."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class StageKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stage_name": "StageName",
        "rest_api_id": "RestApiId",
    }

    stage_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rest_api_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

