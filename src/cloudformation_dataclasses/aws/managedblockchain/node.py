"""PropertyTypes for AWS::ManagedBlockchain::Node."""

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
class NodeConfiguration(PropertyType):
    AVAILABILITY_ZONE = "AvailabilityZone"
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone": "AvailabilityZone",
        "instance_type": "InstanceType",
    }

    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

