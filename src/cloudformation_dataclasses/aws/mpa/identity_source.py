"""PropertyTypes for AWS::MPA::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionCompletionStrategy:
    """ActionCompletionStrategy enum values."""

    AUTO_COMPLETION_UPON_APPROVAL = "AUTO_COMPLETION_UPON_APPROVAL"


class ApprovalTeamStatus:
    """ApprovalTeamStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETING = "DELETING"
    PENDING = "PENDING"


class ApprovalTeamStatusCode:
    """ApprovalTeamStatusCode enum values."""

    VALIDATING = "VALIDATING"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    FAILED_VALIDATION = "FAILED_VALIDATION"
    FAILED_ACTIVATION = "FAILED_ACTIVATION"
    UPDATE_PENDING_APPROVAL = "UPDATE_PENDING_APPROVAL"
    UPDATE_PENDING_ACTIVATION = "UPDATE_PENDING_ACTIVATION"
    UPDATE_FAILED_APPROVAL = "UPDATE_FAILED_APPROVAL"
    UPDATE_FAILED_ACTIVATION = "UPDATE_FAILED_ACTIVATION"
    UPDATE_FAILED_VALIDATION = "UPDATE_FAILED_VALIDATION"
    DELETE_PENDING_APPROVAL = "DELETE_PENDING_APPROVAL"
    DELETE_FAILED_APPROVAL = "DELETE_FAILED_APPROVAL"
    DELETE_FAILED_VALIDATION = "DELETE_FAILED_VALIDATION"


class FilterField:
    """FilterField enum values."""

    ACTIONNAME = "ActionName"
    APPROVALTEAMNAME = "ApprovalTeamName"
    VOTINGTIME = "VotingTime"
    VOTE = "Vote"
    SESSIONSTATUS = "SessionStatus"
    INITIATIONTIME = "InitiationTime"


class IdentitySourceStatus:
    """IdentitySourceStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    ERROR = "ERROR"


class IdentitySourceStatusCode:
    """IdentitySourceStatusCode enum values."""

    ACCESS_DENIED = "ACCESS_DENIED"
    DELETION_FAILED = "DELETION_FAILED"
    IDC_INSTANCE_NOT_FOUND = "IDC_INSTANCE_NOT_FOUND"
    IDC_INSTANCE_NOT_VALID = "IDC_INSTANCE_NOT_VALID"


class IdentitySourceType:
    """IdentitySourceType enum values."""

    IAM_IDENTITY_CENTER = "IAM_IDENTITY_CENTER"


class IdentityStatus:
    """IdentityStatus enum values."""

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    INVALID = "INVALID"


class Operator:
    """Operator enum values."""

    EQ = "EQ"
    NE = "NE"
    GT = "GT"
    LT = "LT"
    GTE = "GTE"
    LTE = "LTE"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    BETWEEN = "BETWEEN"


class PolicyStatus:
    """PolicyStatus enum values."""

    ATTACHABLE = "ATTACHABLE"
    DEPRECATED = "DEPRECATED"


class PolicyType:
    """PolicyType enum values."""

    AWS_MANAGED = "AWS_MANAGED"
    AWS_RAM = "AWS_RAM"


class SessionExecutionStatus:
    """SessionExecutionStatus enum values."""

    EXECUTED = "EXECUTED"
    FAILED = "FAILED"
    PENDING = "PENDING"


class SessionResponse:
    """SessionResponse enum values."""

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    NO_RESPONSE = "NO_RESPONSE"


class SessionStatus:
    """SessionStatus enum values."""

    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    CREATING = "CREATING"


class SessionStatusCode:
    """SessionStatusCode enum values."""

    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    CONFIGURATION_CHANGED = "CONFIGURATION_CHANGED"


@dataclass
class IamIdentityCenter(PropertyType):
    APPROVAL_PORTAL_URL = "ApprovalPortalUrl"
    INSTANCE_ARN = "InstanceArn"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "approval_portal_url": "ApprovalPortalUrl",
        "instance_arn": "InstanceArn",
        "region": "Region",
    }

    approval_portal_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdentitySourceParameters(PropertyType):
    IAM_IDENTITY_CENTER = "IamIdentityCenter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_identity_center": "IamIdentityCenter",
    }

    iam_identity_center: Optional[IamIdentityCenter] = None

