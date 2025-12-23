"""PropertyTypes for AWS::AppStream::Stack."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessEndpoint(PropertyType):
    ENDPOINT_TYPE = "EndpointType"
    VPCE_ID = "VpceId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_type": "EndpointType",
        "vpce_id": "VpceId",
    }

    endpoint_type: Optional[Union[str, AccessEndpointType, Ref, GetAtt, Sub]] = None
    vpce_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationSettings(PropertyType):
    SETTINGS_GROUP = "SettingsGroup"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "settings_group": "SettingsGroup",
        "enabled": "Enabled",
    }

    settings_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class StorageConnector(PropertyType):
    DOMAINS = "Domains"
    RESOURCE_IDENTIFIER = "ResourceIdentifier"
    CONNECTOR_TYPE = "ConnectorType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domains": "Domains",
        "resource_identifier": "ResourceIdentifier",
        "connector_type": "ConnectorType",
    }

    domains: Optional[Union[list[str], Ref]] = None
    resource_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_type: Optional[Union[str, StorageConnectorType, Ref, GetAtt, Sub]] = None


@dataclass
class StreamingExperienceSettings(PropertyType):
    PREFERRED_PROTOCOL = "PreferredProtocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "preferred_protocol": "PreferredProtocol",
    }

    preferred_protocol: Optional[Union[str, PreferredProtocol, Ref, GetAtt, Sub]] = None


@dataclass
class UserSetting(PropertyType):
    ACTION = "Action"
    MAXIMUM_LENGTH = "MaximumLength"
    PERMISSION = "Permission"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "maximum_length": "MaximumLength",
        "permission": "Permission",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    maximum_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    permission: Optional[Union[str, Permission, Ref, GetAtt, Sub]] = None

