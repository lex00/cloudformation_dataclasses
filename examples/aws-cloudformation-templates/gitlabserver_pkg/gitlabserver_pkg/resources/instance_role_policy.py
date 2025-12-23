"""InstanceRolePolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceRolePolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        'ec2messages:*',
        'ssm:UpdateInstanceInformation',
        'ssmmessages:*',
        'secretsmanager:GetSecretValue',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class InstanceRolePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRolePolicyAllowStatement0]


@cloudformation_dataclass
class InstanceRolePolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = InstanceRolePolicyPolicyDocument
    policy_name = 'InstanceRolePolicy'
    role_name = ref(InstanceRole)
