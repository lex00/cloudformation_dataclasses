"""PropertyTypes for AWS::Grafana::Workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountAccessType:
    """AccountAccessType enum values."""

    CURRENT_ACCOUNT = "CURRENT_ACCOUNT"
    ORGANIZATION = "ORGANIZATION"


class AuthenticationProviderTypes:
    """AuthenticationProviderTypes enum values."""

    AWS_SSO = "AWS_SSO"
    SAML = "SAML"


class DataSourceType:
    """DataSourceType enum values."""

    AMAZON_OPENSEARCH_SERVICE = "AMAZON_OPENSEARCH_SERVICE"
    CLOUDWATCH = "CLOUDWATCH"
    PROMETHEUS = "PROMETHEUS"
    XRAY = "XRAY"
    TIMESTREAM = "TIMESTREAM"
    SITEWISE = "SITEWISE"
    ATHENA = "ATHENA"
    REDSHIFT = "REDSHIFT"
    TWINMAKER = "TWINMAKER"


class LicenseType:
    """LicenseType enum values."""

    ENTERPRISE = "ENTERPRISE"
    ENTERPRISE_FREE_TRIAL = "ENTERPRISE_FREE_TRIAL"


class NotificationDestinationType:
    """NotificationDestinationType enum values."""

    SNS = "SNS"


class PermissionType:
    """PermissionType enum values."""

    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    SERVICE_MANAGED = "SERVICE_MANAGED"


class Role:
    """Role enum values."""

    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"


class SamlConfigurationStatus:
    """SamlConfigurationStatus enum values."""

    CONFIGURED = "CONFIGURED"
    NOT_CONFIGURED = "NOT_CONFIGURED"


class UpdateAction:
    """UpdateAction enum values."""

    ADD = "ADD"
    REVOKE = "REVOKE"


class UserType:
    """UserType enum values."""

    SSO_USER = "SSO_USER"
    SSO_GROUP = "SSO_GROUP"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


class WorkspaceStatus:
    """WorkspaceStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    UPGRADING = "UPGRADING"
    DELETION_FAILED = "DELETION_FAILED"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPGRADE_FAILED = "UPGRADE_FAILED"
    LICENSE_REMOVAL_FAILED = "LICENSE_REMOVAL_FAILED"
    VERSION_UPDATING = "VERSION_UPDATING"
    VERSION_UPDATE_FAILED = "VERSION_UPDATE_FAILED"


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

