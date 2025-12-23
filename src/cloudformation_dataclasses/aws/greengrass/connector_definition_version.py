"""PropertyTypes for AWS::Greengrass::ConnectorDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Connector(PropertyType):
    CONNECTOR_ARN = "ConnectorArn"
    PARAMETERS = "Parameters"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_arn": "ConnectorArn",
        "parameters": "Parameters",
        "id": "Id",
    }

    connector_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

