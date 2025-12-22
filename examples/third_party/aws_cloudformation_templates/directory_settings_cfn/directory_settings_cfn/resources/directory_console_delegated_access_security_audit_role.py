"""DirectoryConsoleDelegatedAccessSecurityAuditRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ds.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0]


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessSecurityAuditRole:
    """AWS::IAM::Role resource."""

    resource: Role
    description = 'IAM Role for Directory Service \'AWS Management Console\' Delegated Access for "Security Audit"'
    assume_role_policy_document = DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/SecurityAudit')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    condition = 'DirectoryConsoleDelegatedAccessRolesCondition'
