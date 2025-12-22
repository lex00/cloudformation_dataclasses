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
class S3TargetDMSRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        's3:PutObject',
        's3:DeleteObject',
    ]
    resource_arn = [
        get_att(S3Bucket, "Arn"),
        Sub('${S3Bucket.Arn}/*'),
    ]


@cloudformation_dataclass
class S3TargetDMSRoleAllowStatement1:
    resource: PolicyStatement
    action = 's3:ListBucket'
    resource_arn = get_att(S3Bucket, "Arn")


@cloudformation_dataclass
class S3TargetDMSRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [S3TargetDMSRoleAllowStatement0_1, S3TargetDMSRoleAllowStatement1]


@cloudformation_dataclass
class S3TargetDMSRolePolicy:
    resource: iam.user.Policy
    policy_name = 'S3AccessForDMSPolicy'
    policy_document = S3TargetDMSRolePolicies0PolicyDocument


@cloudformation_dataclass
class S3TargetDMSRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-s3-target-role'
    assume_role_policy_document = S3TargetDMSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [S3TargetDMSRolePolicy]
    depends_on = ["S3Bucket"]
