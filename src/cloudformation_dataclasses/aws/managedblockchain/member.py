"""PropertyTypes for AWS::ManagedBlockchain::Member."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApprovalThresholdPolicy(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "admin_username": "AdminUsername",
        "admin_password": "AdminPassword",
    }

    admin_username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    admin_password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MemberFrameworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "member_fabric_configuration": "MemberFabricConfiguration",
    }

    member_fabric_configuration: Optional[MemberFabricConfiguration] = None


@dataclass
class NetworkConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "edition": "Edition",
    }

    edition: Optional[Union[str, Edition, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkFrameworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "network_fabric_configuration": "NetworkFabricConfiguration",
    }

    network_fabric_configuration: Optional[NetworkFabricConfiguration] = None


@dataclass
class VotingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "approval_threshold_policy": "ApprovalThresholdPolicy",
    }

    approval_threshold_policy: Optional[ApprovalThresholdPolicy] = None

