from __future__ import annotations

"""EventBridgeRolePolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EventBridgeRolePolicyAllowStatement0:
    resource: PolicyStatement
    action = 'events:PutEvents'
    resource_arn = ref(CentralEventBusArn)


@cloudformation_dataclass
class EventBridgeRolePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [EventBridgeRolePolicyAllowStatement0]


@cloudformation_dataclass
class EventBridgeRolePolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: RolePolicy
    policy_name = 'EventBridgeRolePolicy'
    policy_document = EventBridgeRolePolicyPolicyDocument
    role_name: Ref[EventBridgeRole] = ref()
