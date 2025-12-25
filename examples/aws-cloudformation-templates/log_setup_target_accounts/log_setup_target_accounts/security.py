"""Security resources: EventBridgeRole, EventBridgeRolePolicy."""

from . import *  # noqa: F403


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

    resource: iam.Role
    assume_role_policy_document = EventBridgeRoleAssumeRolePolicyDocument


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

    resource: iam.RolePolicy
    policy_name = 'EventBridgeRolePolicy'
    policy_document = EventBridgeRolePolicyPolicyDocument
    role_name = ref(EventBridgeRole)
