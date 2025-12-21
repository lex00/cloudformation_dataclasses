from __future__ import annotations

"""OpenIoTStarPolicy - AWS::IoT::Policy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OpenIoTStarPolicyAllowStatement0:
    resource: PolicyStatement
    action = 'iot:*'
    resource_arn = '*'


@cloudformation_dataclass
class OpenIoTStarPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [OpenIoTStarPolicyAllowStatement0]


@cloudformation_dataclass
class OpenIoTStarPolicy:
    """AWS::IoT::Policy resource."""

    resource: Policy
    policy_document = OpenIoTStarPolicyPolicyDocument
