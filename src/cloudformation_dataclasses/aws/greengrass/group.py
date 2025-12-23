"""PropertyTypes for AWS::Greengrass::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GroupVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logger_definition_version_arn": "LoggerDefinitionVersionArn",
        "device_definition_version_arn": "DeviceDefinitionVersionArn",
        "function_definition_version_arn": "FunctionDefinitionVersionArn",
        "core_definition_version_arn": "CoreDefinitionVersionArn",
        "resource_definition_version_arn": "ResourceDefinitionVersionArn",
        "connector_definition_version_arn": "ConnectorDefinitionVersionArn",
        "subscription_definition_version_arn": "SubscriptionDefinitionVersionArn",
    }

    logger_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    function_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    core_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subscription_definition_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

