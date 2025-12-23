"""Security resources: IAMAssumeInstanceRole, InstanceProfile."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class IAMAssumeInstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [IAMAssumeInstanceRoleAllowStatement0]


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['ec2:DescribeTags']
    resource_arn = '*'


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement2:
    resource: PolicyStatement
    action = 'logs:*'
    resource_arn = '*'


@cloudformation_dataclass
class IAMAssumeInstanceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [IAMAssumeInstanceRoleAllowStatement0_1, IAMAssumeInstanceRoleAllowStatement1, IAMAssumeInstanceRoleAllowStatement2]


@cloudformation_dataclass
class IAMAssumeInstanceRolePolicy:
    resource: iam.user.Policy
    policy_document = IAMAssumeInstanceRolePolicies0PolicyDocument
    policy_name = Join('-', [
    'IAM',
    'EC2',
    'Policy',
])


@cloudformation_dataclass
class IAMAssumeInstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = IAMAssumeInstanceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [IAMAssumeInstanceRolePolicy]
    role_name = Join('-', [
    'IAM',
    'EC2',
    'Role',
])


@cloudformation_dataclass
class InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    instance_profile_name = Join('-', [
    'IAM',
    'InstanceProfile',
])
    path = '/'
    roles = [ref(IAMAssumeInstanceRole)]
