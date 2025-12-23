"""PropertyTypes for AWS::Greengrass::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GroupVersion(PropertyType):
    LOGGER_DEFINITION_VERSION_ARN = "LoggerDefinitionVersionArn"
    DEVICE_DEFINITION_VERSION_ARN = "DeviceDefinitionVersionArn"
    FUNCTION_DEFINITION_VERSION_ARN = "FunctionDefinitionVersionArn"
    CORE_DEFINITION_VERSION_ARN = "CoreDefinitionVersionArn"
    RESOURCE_DEFINITION_VERSION_ARN = "ResourceDefinitionVersionArn"
    CONNECTOR_DEFINITION_VERSION_ARN = "ConnectorDefinitionVersionArn"
    SUBSCRIPTION_DEFINITION_VERSION_ARN = "SubscriptionDefinitionVersionArn"

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

