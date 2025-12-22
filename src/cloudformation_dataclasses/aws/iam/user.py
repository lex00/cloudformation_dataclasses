"""PropertyTypes for AWS::IAM::User."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessAdvisorUsageGranularityType:
    """AccessAdvisorUsageGranularityType enum values."""

    SERVICE_LEVEL = "SERVICE_LEVEL"
    ACTION_LEVEL = "ACTION_LEVEL"


class ContextKeyTypeEnum:
    """ContextKeyTypeEnum enum values."""

    STRING = "string"
    STRINGLIST = "stringList"
    NUMERIC = "numeric"
    NUMERICLIST = "numericList"
    BOOLEAN = "boolean"
    BOOLEANLIST = "booleanList"
    IP = "ip"
    IPLIST = "ipList"
    BINARY = "binary"
    BINARYLIST = "binaryList"
    DATE = "date"
    DATELIST = "dateList"


class DeletionTaskStatusType:
    """DeletionTaskStatusType enum values."""

    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"


class EntityType:
    """EntityType enum values."""

    USER = "User"
    ROLE = "Role"
    GROUP = "Group"
    LOCALMANAGEDPOLICY = "LocalManagedPolicy"
    AWSMANAGEDPOLICY = "AWSManagedPolicy"


class FeatureType:
    """FeatureType enum values."""

    ROOTCREDENTIALSMANAGEMENT = "RootCredentialsManagement"
    ROOTSESSIONS = "RootSessions"


class PermissionsBoundaryAttachmentType:
    """PermissionsBoundaryAttachmentType enum values."""

    PERMISSIONSBOUNDARYPOLICY = "PermissionsBoundaryPolicy"


class PolicyEvaluationDecisionType:
    """PolicyEvaluationDecisionType enum values."""

    ALLOWED = "allowed"
    EXPLICITDENY = "explicitDeny"
    IMPLICITDENY = "implicitDeny"


class PolicyParameterTypeEnum:
    """PolicyParameterTypeEnum enum values."""

    STRING = "string"
    STRINGLIST = "stringList"


class PolicySourceType:
    """PolicySourceType enum values."""

    USER = "user"
    GROUP = "group"
    ROLE = "role"
    AWS_MANAGED = "aws-managed"
    USER_MANAGED = "user-managed"
    RESOURCE = "resource"
    NONE = "none"


class PolicyUsageType:
    """PolicyUsageType enum values."""

    PERMISSIONSPOLICY = "PermissionsPolicy"
    PERMISSIONSBOUNDARY = "PermissionsBoundary"


class ReportFormatType:
    """ReportFormatType enum values."""

    TEXT_CSV = "text/csv"


class ReportStateType:
    """ReportStateType enum values."""

    STARTED = "STARTED"
    INPROGRESS = "INPROGRESS"
    COMPLETE = "COMPLETE"


class assertionEncryptionModeType:
    """assertionEncryptionModeType enum values."""

    REQUIRED = "Required"
    ALLOWED = "Allowed"


class assignmentStatusType:
    """assignmentStatusType enum values."""

    ASSIGNED = "Assigned"
    UNASSIGNED = "Unassigned"
    ANY = "Any"


class encodingType:
    """encodingType enum values."""

    SSH = "SSH"
    PEM = "PEM"


class globalEndpointTokenVersion:
    """globalEndpointTokenVersion enum values."""

    V1TOKEN = "v1Token"
    V2TOKEN = "v2Token"


class jobStatusType:
    """jobStatusType enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class permissionCheckResultType:
    """permissionCheckResultType enum values."""

    ALLOWED = "ALLOWED"
    DENIED = "DENIED"
    UNSURE = "UNSURE"


class permissionCheckStatusType:
    """permissionCheckStatusType enum values."""

    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class policyOwnerEntityType:
    """policyOwnerEntityType enum values."""

    USER = "USER"
    ROLE = "ROLE"
    GROUP = "GROUP"


class policyScopeType:
    """policyScopeType enum values."""

    ALL = "All"
    AWS = "AWS"
    LOCAL = "Local"


class policyType:
    """policyType enum values."""

    INLINE = "INLINE"
    MANAGED = "MANAGED"


class sortKeyType:
    """sortKeyType enum values."""

    SERVICE_NAMESPACE_ASCENDING = "SERVICE_NAMESPACE_ASCENDING"
    SERVICE_NAMESPACE_DESCENDING = "SERVICE_NAMESPACE_DESCENDING"
    LAST_AUTHENTICATED_TIME_ASCENDING = "LAST_AUTHENTICATED_TIME_ASCENDING"
    LAST_AUTHENTICATED_TIME_DESCENDING = "LAST_AUTHENTICATED_TIME_DESCENDING"


class stateType:
    """stateType enum values."""

    UNASSIGNED = "UNASSIGNED"
    ASSIGNED = "ASSIGNED"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    FINALIZED = "FINALIZED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class statusType:
    """statusType enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    EXPIRED = "Expired"


class summaryKeyType:
    """summaryKeyType enum values."""

    USERS = "Users"
    USERSQUOTA = "UsersQuota"
    GROUPS = "Groups"
    GROUPSQUOTA = "GroupsQuota"
    SERVERCERTIFICATES = "ServerCertificates"
    SERVERCERTIFICATESQUOTA = "ServerCertificatesQuota"
    USERPOLICYSIZEQUOTA = "UserPolicySizeQuota"
    GROUPPOLICYSIZEQUOTA = "GroupPolicySizeQuota"
    GROUPSPERUSERQUOTA = "GroupsPerUserQuota"
    SIGNINGCERTIFICATESPERUSERQUOTA = "SigningCertificatesPerUserQuota"
    ACCESSKEYSPERUSERQUOTA = "AccessKeysPerUserQuota"
    MFADEVICES = "MFADevices"
    MFADEVICESINUSE = "MFADevicesInUse"
    ACCOUNTMFAENABLED = "AccountMFAEnabled"
    ACCOUNTACCESSKEYSPRESENT = "AccountAccessKeysPresent"
    ACCOUNTPASSWORDPRESENT = "AccountPasswordPresent"
    ACCOUNTSIGNINGCERTIFICATESPRESENT = "AccountSigningCertificatesPresent"
    ATTACHEDPOLICIESPERGROUPQUOTA = "AttachedPoliciesPerGroupQuota"
    ATTACHEDPOLICIESPERROLEQUOTA = "AttachedPoliciesPerRoleQuota"
    ATTACHEDPOLICIESPERUSERQUOTA = "AttachedPoliciesPerUserQuota"
    POLICIES = "Policies"
    POLICIESQUOTA = "PoliciesQuota"
    POLICYSIZEQUOTA = "PolicySizeQuota"
    POLICYVERSIONSINUSE = "PolicyVersionsInUse"
    POLICYVERSIONSINUSEQUOTA = "PolicyVersionsInUseQuota"
    VERSIONSPERPOLICYQUOTA = "VersionsPerPolicyQuota"
    GLOBALENDPOINTTOKENVERSION = "GlobalEndpointTokenVersion"
    ASSUMEROLEPOLICYSIZEQUOTA = "AssumeRolePolicySizeQuota"
    INSTANCEPROFILES = "InstanceProfiles"
    INSTANCEPROFILESQUOTA = "InstanceProfilesQuota"
    PROVIDERS = "Providers"
    ROLEPOLICYSIZEQUOTA = "RolePolicySizeQuota"
    ROLES = "Roles"
    ROLESQUOTA = "RolesQuota"


class summaryStateType:
    """summaryStateType enum values."""

    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    FAILED = "FAILED"


@dataclass
class LoginProfile(PropertyType):
    PASSWORD_RESET_REQUIRED = "PasswordResetRequired"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "password_reset_required": "PasswordResetRequired",
        "password": "Password",
    }

    password_reset_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Policy(PropertyType):
    POLICY_NAME = "PolicyName"
    POLICY_DOCUMENT = "PolicyDocument"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_name": "PolicyName",
        "policy_document": "PolicyDocument",
    }

    policy_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_document: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

