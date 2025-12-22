"""SiteCloudFrontLogsReplicaBucketAccessPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(SiteCloudFrontLogsReplicaBucket)
    policy_document = SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument
