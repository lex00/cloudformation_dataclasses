"""PropertyTypes for AWS::Greengrass::ConnectorDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Connector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_arn": "ConnectorArn",
        "parameters": "Parameters",
        "id": "Id",
    }

    connector_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorDefinitionVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connectors": "Connectors",
    }

    connectors: Optional[list[Connector]] = None

