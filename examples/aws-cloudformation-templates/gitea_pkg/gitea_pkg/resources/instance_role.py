"""InstanceRole - AWS::IAM::Role resource."""

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
        'Value': 'gitea-server-instance',
    }]
