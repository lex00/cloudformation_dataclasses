"""DMSCloudwatchRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DMSCloudwatchRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class DMSCloudwatchRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSCloudwatchRoleAllowStatement0]


@cloudformation_dataclass
class DMSCloudwatchRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-cloudwatch-logs-role'
    assume_role_policy_document = DMSCloudwatchRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole']
    path = '/'
    condition = 'NotExistsDMSCloudwatchRole'
