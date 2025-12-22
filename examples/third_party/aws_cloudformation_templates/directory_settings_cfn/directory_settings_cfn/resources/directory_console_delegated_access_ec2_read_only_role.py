"""DirectoryConsoleDelegatedAccessEC2ReadOnlyRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ds.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0]


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessEC2ReadOnlyRole:
    """AWS::IAM::Role resource."""

    resource: Role
    description = 'IAM Role for Directory Service \'AWS Management Console\' Delegated Access for "EC2 ReadOnly"'
    assume_role_policy_document = DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ReadOnlyAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    condition = 'DirectoryConsoleDelegatedAccessRolesCondition'
