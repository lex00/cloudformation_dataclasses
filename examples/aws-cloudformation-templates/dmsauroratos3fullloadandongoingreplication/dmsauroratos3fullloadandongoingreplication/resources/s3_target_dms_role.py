"""S3TargetDMSRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


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
