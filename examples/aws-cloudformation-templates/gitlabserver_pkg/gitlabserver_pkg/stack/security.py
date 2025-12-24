"""Security resources: InstanceRole, InstanceRolePolicy, InstanceProfile."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'ec2.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class InstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRoleAllowStatement0]


@cloudformation_dataclass
class InstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = InstanceRoleAssumeRolePolicyDocument
    tags = [{
        'Key': 'Name',
        'Value': 'gitlab-server-instance',
    }]


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


@cloudformation_dataclass
class InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    roles = [ref(InstanceRole)]
