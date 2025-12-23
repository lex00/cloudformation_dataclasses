"""PropertyTypes for AWS::ElasticBeanstalk::ConfigurationTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigurationOptionSetting(PropertyType):
    RESOURCE_NAME = "ResourceName"
    VALUE = "Value"
    NAMESPACE = "Namespace"
    OPTION_NAME = "OptionName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_name": "ResourceName",
        "value": "Value",
        "namespace": "Namespace",
        "option_name": "OptionName",
    }

    resource_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    option_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConfiguration(PropertyType):
    APPLICATION_NAME = "ApplicationName"
    TEMPLATE_NAME = "TemplateName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_name": "ApplicationName",
        "template_name": "TemplateName",
    }

    application_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

