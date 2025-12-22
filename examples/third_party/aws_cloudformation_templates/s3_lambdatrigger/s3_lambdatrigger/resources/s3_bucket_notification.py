"""S3BucketNotification - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketNotificationServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class S3BucketNotificationServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketNotificationServerSideEncryptionByDefault


@cloudformation_dataclass
class S3BucketNotificationBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [S3BucketNotificationServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketNotificationPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3BucketNotificationLambdaConfiguration:
    resource: LambdaConfiguration
    event = 's3:ObjectCreated:Put'
    function = get_att(S3TriggerLambdaFunction, "Arn")


@cloudformation_dataclass
class S3BucketNotificationNotificationConfiguration:
    resource: NotificationConfiguration
    lambda_configurations = [S3BucketNotificationLambdaConfiguration]


@cloudformation_dataclass
class S3BucketNotification:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_name = Sub('${NotificationBucket}')
    bucket_encryption = S3BucketNotificationBucketEncryption
    public_access_block_configuration = S3BucketNotificationPublicAccessBlockConfiguration
    notification_configuration = S3BucketNotificationNotificationConfiguration
    depends_on = ["LambdaInvokePermission"]
