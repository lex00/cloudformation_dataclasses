from __future__ import annotations

"""CloudFrontLogsBucketPolicyPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsBucketPolicyPolicyDenyStatement0, CloudFrontLogsBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket: Ref[CloudFrontLogsBucket] = ref()
    policy_document = CloudFrontLogsBucketPolicyPolicyPolicyDocument
