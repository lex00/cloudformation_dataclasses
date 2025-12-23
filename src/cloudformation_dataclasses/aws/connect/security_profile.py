"""PropertyTypes for AWS::Connect::SecurityProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Application(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_permissions": "ApplicationPermissions",
        "namespace": "Namespace",
    }

    application_permissions: Optional[Union[list[str], Ref]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataTableAccessControlConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_attribute_access_control_configuration": "PrimaryAttributeAccessControlConfiguration",
    }

    primary_attribute_access_control_configuration: Optional[PrimaryAttributeAccessControlConfigurationItem] = None


@dataclass
class GranularAccessControlConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_table_access_control_configuration": "DataTableAccessControlConfiguration",
    }

    data_table_access_control_configuration: Optional[DataTableAccessControlConfiguration] = None


@dataclass
class PrimaryAttributeAccessControlConfigurationItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_attribute_values": "PrimaryAttributeValues",
    }

    primary_attribute_values: Optional[list[PrimaryAttributeValue]] = None


@dataclass
class PrimaryAttributeValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "attribute_name": "AttributeName",
        "access_type": "AccessType",
    }

    values: Optional[Union[list[str], Ref]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_type: Optional[Union[str, AccessType, Ref, GetAtt, Sub]] = None

