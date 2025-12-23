"""Security resources: DMSCloudwatchRole, DMSVpcRole, S3TargetDMSRole."""

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


@cloudformation_dataclass
class DMSVpcRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class DMSVpcRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSVpcRoleAllowStatement0]


@cloudformation_dataclass
class DMSVpcRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-vpc-role'
    assume_role_policy_document = DMSVpcRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole']
    path = '/'
    condition = 'NotExistsDMSVPCRole'


@cloudformation_dataclass
class S3TargetDMSRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class S3TargetDMSRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [S3TargetDMSRoleAllowStatement0]


@cloudformation_dataclass
class S3TargetDMSRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-s3-target-role'
    assume_role_policy_document = S3TargetDMSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'S3AccessForDMSPolicy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Action': [
                        's3:PutObject',
                        's3:DeleteObject',
                    ],
                    'Resource': [
                        get_att(S3Bucket, "Arn"),
                        Sub('${S3Bucket.Arn}/*'),
                    ],
                },
                {
                    'Effect': 'Allow',
                    'Action': 's3:ListBucket',
                    'Resource': get_att(S3Bucket, "Arn"),
                },
            ],
        },
    }]
    depends_on = ["S3Bucket"]
