"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class BucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class BucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [BucketServerSideEncryptionRule]


@cloudformation_dataclass
class BucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class BucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = ref(BucketName)
    bucket_encryption = BucketBucketEncryption
    versioning_configuration = BucketDeleteMarkerReplication
    public_access_block_configuration = BucketPublicAccessBlockConfiguration


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
