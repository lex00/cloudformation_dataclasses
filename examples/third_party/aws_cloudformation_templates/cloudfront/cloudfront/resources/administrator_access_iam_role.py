"""AdministratorAccessIAMRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AdministratorAccessIAMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class AdministratorAccessIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AdministratorAccessIAMRoleAllowStatement0]


@cloudformation_dataclass
class AdministratorAccessIAMRole:
    """AWS::IAM::Role resource."""

    resource: Role
    role_name = Sub('AdministratorAccess-${AppName}')
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AdministratorAccess')]
    assume_role_policy_document = AdministratorAccessIAMRoleAssumeRolePolicyDocument
    path = '/'
