"""SiteContentBucketAccessPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteContentBucketAccessPolicyAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'cloudfront.amazonaws.com',
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')
    condition = {
        STRING_EQUALS: {
            'AWS:SourceArn': Sub('arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SiteDistribution.Id}'),
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyAllowStatement2:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentBucketAccessPolicyAllowStatement0, SiteContentBucketAccessPolicyDenyStatement1, SiteContentBucketAccessPolicyAllowStatement2]


@cloudformation_dataclass
class SiteContentBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(SiteContentBucket)
    policy_document = SiteContentBucketAccessPolicyPolicyDocument
