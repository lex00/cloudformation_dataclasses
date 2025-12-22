"""EventBridgeRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EventBridgeRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class EventBridgeRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EventBridgeRoleAllowStatement0]


@cloudformation_dataclass
class EventBridgeRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = EventBridgeRoleAssumeRolePolicyDocument
