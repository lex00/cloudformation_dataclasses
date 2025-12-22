"""PropertyTypes for AWS::ManagedBlockchain::Member."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessorNetworkType:
    """AccessorNetworkType enum values."""

    ETHEREUM_GOERLI = "ETHEREUM_GOERLI"
    ETHEREUM_MAINNET = "ETHEREUM_MAINNET"
    ETHEREUM_MAINNET_AND_GOERLI = "ETHEREUM_MAINNET_AND_GOERLI"
    POLYGON_MAINNET = "POLYGON_MAINNET"
    POLYGON_MUMBAI = "POLYGON_MUMBAI"


class AccessorStatus:
    """AccessorStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING_DELETION = "PENDING_DELETION"
    DELETED = "DELETED"


class AccessorType:
    """AccessorType enum values."""

    BILLING_TOKEN = "BILLING_TOKEN"


class Edition:
    """Edition enum values."""

    STARTER = "STARTER"
    STANDARD = "STANDARD"


class Framework:
    """Framework enum values."""

    HYPERLEDGER_FABRIC = "HYPERLEDGER_FABRIC"
    ETHEREUM = "ETHEREUM"


class InvitationStatus:
    """InvitationStatus enum values."""

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    ACCEPTING = "ACCEPTING"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class MemberStatus:
    """MemberStatus enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    INACCESSIBLE_ENCRYPTION_KEY = "INACCESSIBLE_ENCRYPTION_KEY"


class NetworkStatus:
    """NetworkStatus enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class NodeStatus:
    """NodeStatus enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    UNHEALTHY = "UNHEALTHY"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED = "FAILED"
    INACCESSIBLE_ENCRYPTION_KEY = "INACCESSIBLE_ENCRYPTION_KEY"


class ProposalStatus:
    """ProposalStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    ACTION_FAILED = "ACTION_FAILED"


class StateDBType:
    """StateDBType enum values."""

    LEVELDB = "LevelDB"
    COUCHDB = "CouchDB"


class ThresholdComparator:
    """ThresholdComparator enum values."""

    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class VoteValue:
    """VoteValue enum values."""

    YES = "YES"
    NO = "NO"


@dataclass
class ApprovalThresholdPolicy(PropertyType):
    THRESHOLD_COMPARATOR = "ThresholdComparator"
    THRESHOLD_PERCENTAGE = "ThresholdPercentage"
    PROPOSAL_DURATION_IN_HOURS = "ProposalDurationInHours"

    _property_mappings: ClassVar[dict[str, str]] = {
        "threshold_comparator": "ThresholdComparator",
        "threshold_percentage": "ThresholdPercentage",
        "proposal_duration_in_hours": "ProposalDurationInHours",
    }

    threshold_comparator: Optional[Union[str, ThresholdComparator, Ref, GetAtt, Sub]] = None
    threshold_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    proposal_duration_in_hours: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MemberConfiguration(PropertyType):
    DESCRIPTION = "Description"
    MEMBER_FRAMEWORK_CONFIGURATION = "MemberFrameworkConfiguration"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "member_framework_configuration": "MemberFrameworkConfiguration",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    member_framework_configuration: Optional[MemberFrameworkConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemberFabricConfiguration(PropertyType):
    ADMIN_USERNAME = "AdminUsername"
    ADMIN_PASSWORD = "AdminPassword"

    _property_mappings: ClassVar[dict[str, str]] = {
        "admin_username": "AdminUsername",
        "admin_password": "AdminPassword",
    }

    admin_username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    admin_password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemberFrameworkConfiguration(PropertyType):
    MEMBER_FABRIC_CONFIGURATION = "MemberFabricConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "member_fabric_configuration": "MemberFabricConfiguration",
    }

    member_fabric_configuration: Optional[MemberFabricConfiguration] = None


@dataclass
class NetworkConfiguration(PropertyType):
    DESCRIPTION = "Description"
    FRAMEWORK_VERSION = "FrameworkVersion"
    VOTING_POLICY = "VotingPolicy"
    FRAMEWORK = "Framework"
    NAME = "Name"
    NETWORK_FRAMEWORK_CONFIGURATION = "NetworkFrameworkConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "framework_version": "FrameworkVersion",
        "voting_policy": "VotingPolicy",
        "framework": "Framework",
        "name": "Name",
        "network_framework_configuration": "NetworkFrameworkConfiguration",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    framework_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    voting_policy: Optional[VotingPolicy] = None
    framework: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_framework_configuration: Optional[NetworkFrameworkConfiguration] = None


@dataclass
class NetworkFabricConfiguration(PropertyType):
    EDITION = "Edition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "edition": "Edition",
    }

    edition: Optional[Union[str, Edition, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkFrameworkConfiguration(PropertyType):
    NETWORK_FABRIC_CONFIGURATION = "NetworkFabricConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_fabric_configuration": "NetworkFabricConfiguration",
    }

    network_fabric_configuration: Optional[NetworkFabricConfiguration] = None


@dataclass
class VotingPolicy(PropertyType):
    APPROVAL_THRESHOLD_POLICY = "ApprovalThresholdPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "approval_threshold_policy": "ApprovalThresholdPolicy",
    }

    approval_threshold_policy: Optional[ApprovalThresholdPolicy] = None

