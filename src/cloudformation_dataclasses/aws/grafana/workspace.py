"""PropertyTypes for AWS::Grafana::Workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssertionAttributes(PropertyType):
    ROLE = "Role"
    EMAIL = "Email"
    ORG = "Org"
    GROUPS = "Groups"
    LOGIN = "Login"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "email": "Email",
        "org": "Org",
        "groups": "Groups",
        "login": "Login",
        "name": "Name",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email: Optional[Union[str, Ref, GetAtt, Sub]] = None
    org: Optional[Union[str, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[str, Ref, GetAtt, Sub]] = None
    login: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdpMetadata(PropertyType):
    XML = "Xml"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "xml": "Xml",
        "url": "Url",
    }

    xml: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkAccessControl(PropertyType):
    PREFIX_LIST_IDS = "PrefixListIds"
    VPCE_IDS = "VpceIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix_list_ids": "PrefixListIds",
        "vpce_ids": "VpceIds",
    }

    prefix_list_ids: Optional[Union[list[str], Ref]] = None
    vpce_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class RoleValues(PropertyType):
    EDITOR = "Editor"
    ADMIN = "Admin"

    _property_mappings: ClassVar[dict[str, str]] = {
        "editor": "Editor",
        "admin": "Admin",
    }

    editor: Optional[Union[list[str], Ref]] = None
    admin: Optional[Union[list[str], Ref]] = None


@dataclass
class SamlConfiguration(PropertyType):
    LOGIN_VALIDITY_DURATION = "LoginValidityDuration"
    ROLE_VALUES = "RoleValues"
    IDP_METADATA = "IdpMetadata"
    ASSERTION_ATTRIBUTES = "AssertionAttributes"
    ALLOWED_ORGANIZATIONS = "AllowedOrganizations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "login_validity_duration": "LoginValidityDuration",
        "role_values": "RoleValues",
        "idp_metadata": "IdpMetadata",
        "assertion_attributes": "AssertionAttributes",
        "allowed_organizations": "AllowedOrganizations",
    }

    login_validity_duration: Optional[Union[float, Ref, GetAtt, Sub]] = None
    role_values: Optional[RoleValues] = None
    idp_metadata: Optional[IdpMetadata] = None
    assertion_attributes: Optional[AssertionAttributes] = None
    allowed_organizations: Optional[Union[list[str], Ref]] = None


@dataclass
class VpcConfiguration(PropertyType):
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

