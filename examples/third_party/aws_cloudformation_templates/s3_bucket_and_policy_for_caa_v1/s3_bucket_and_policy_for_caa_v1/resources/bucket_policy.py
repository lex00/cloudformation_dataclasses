from __future__ import annotations

"""BucketPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'CrossAccPolicyDoc'
    principal = {
        'AWS': [Sub('arn:${AWS::Partition}:iam::${PublisherAccountID}:root')],
    }
    action = 's3:ListBucket'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${Bucket}')


@cloudformation_dataclass
class BucketPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'CrossAccPolicyDoc'
    principal = {
        'AWS': [Sub('arn:${AWS::Partition}:iam::${PublisherAccountID}:root')],
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${Bucket}/*')


@cloudformation_dataclass
class BucketPolicyDenyStatement2:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${BucketName}'),
        Sub('arn:${AWS::Partition}:s3:::${BucketName}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class BucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [BucketPolicyAllowStatement0, BucketPolicyAllowStatement1, BucketPolicyDenyStatement2]


@cloudformation_dataclass
class BucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(Bucket)
    policy_document = BucketPolicyPolicyDocument
