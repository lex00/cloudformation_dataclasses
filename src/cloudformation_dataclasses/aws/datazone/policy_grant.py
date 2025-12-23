"""PropertyTypes for AWS::DataZone::PolicyGrant."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AddToProjectMemberPoolPolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CreateAssetTypePolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CreateDomainUnitPolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CreateEnvironmentProfilePolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_unit_id": "DomainUnitId",
    }

    domain_unit_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CreateFormTypePolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CreateGlossaryPolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CreateProjectFromProjectProfilePolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_profiles": "ProjectProfiles",
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    project_profiles: Optional[Union[list[str], Ref]] = None
    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CreateProjectPolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainUnitFilterForProject(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_unit": "DomainUnit",
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    domain_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainUnitGrantFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "all_domain_units_grant_filter": "AllDomainUnitsGrantFilter",
    }

    all_domain_units_grant_filter: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class DomainUnitPolicyGrantPrincipal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_unit_grant_filter": "DomainUnitGrantFilter",
        "domain_unit_designation": "DomainUnitDesignation",
        "domain_unit_identifier": "DomainUnitIdentifier",
    }

    domain_unit_grant_filter: Optional[DomainUnitGrantFilter] = None
    domain_unit_designation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_unit_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GroupPolicyGrantPrincipal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group_identifier": "GroupIdentifier",
    }

    group_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OverrideDomainUnitOwnersPolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OverrideProjectOwnersPolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_child_domain_units": "IncludeChildDomainUnits",
    }

    include_child_domain_units: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyGrantDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "create_environment_from_blueprint": "CreateEnvironmentFromBlueprint",
        "create_glossary": "CreateGlossary",
        "create_asset_type": "CreateAssetType",
        "create_domain_unit": "CreateDomainUnit",
        "create_project": "CreateProject",
        "override_project_owners": "OverrideProjectOwners",
        "add_to_project_member_pool": "AddToProjectMemberPool",
        "delegate_create_environment_profile": "DelegateCreateEnvironmentProfile",
        "create_project_from_project_profile": "CreateProjectFromProjectProfile",
        "create_environment": "CreateEnvironment",
        "create_environment_profile": "CreateEnvironmentProfile",
        "create_form_type": "CreateFormType",
        "override_domain_unit_owners": "OverrideDomainUnitOwners",
    }

    create_environment_from_blueprint: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    create_glossary: Optional[CreateGlossaryPolicyGrantDetail] = None
    create_asset_type: Optional[CreateAssetTypePolicyGrantDetail] = None
    create_domain_unit: Optional[CreateDomainUnitPolicyGrantDetail] = None
    create_project: Optional[CreateProjectPolicyGrantDetail] = None
    override_project_owners: Optional[OverrideProjectOwnersPolicyGrantDetail] = None
    add_to_project_member_pool: Optional[AddToProjectMemberPoolPolicyGrantDetail] = None
    delegate_create_environment_profile: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    create_project_from_project_profile: Optional[CreateProjectFromProjectProfilePolicyGrantDetail] = None
    create_environment: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    create_environment_profile: Optional[CreateEnvironmentProfilePolicyGrantDetail] = None
    create_form_type: Optional[CreateFormTypePolicyGrantDetail] = None
    override_domain_unit_owners: Optional[OverrideDomainUnitOwnersPolicyGrantDetail] = None


@dataclass
class PolicyGrantPrincipal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group": "Group",
        "project": "Project",
        "user": "User",
        "domain_unit": "DomainUnit",
    }

    group: Optional[GroupPolicyGrantPrincipal] = None
    project: Optional[ProjectPolicyGrantPrincipal] = None
    user: Optional[UserPolicyGrantPrincipal] = None
    domain_unit: Optional[DomainUnitPolicyGrantPrincipal] = None


@dataclass
class ProjectGrantFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_unit_filter": "DomainUnitFilter",
    }

    domain_unit_filter: Optional[DomainUnitFilterForProject] = None


@dataclass
class ProjectPolicyGrantPrincipal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_identifier": "ProjectIdentifier",
        "project_designation": "ProjectDesignation",
        "project_grant_filter": "ProjectGrantFilter",
    }

    project_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    project_designation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    project_grant_filter: Optional[ProjectGrantFilter] = None


@dataclass
class UserPolicyGrantPrincipal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "all_users_grant_filter": "AllUsersGrantFilter",
        "user_identifier": "UserIdentifier",
    }

    all_users_grant_filter: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    user_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

