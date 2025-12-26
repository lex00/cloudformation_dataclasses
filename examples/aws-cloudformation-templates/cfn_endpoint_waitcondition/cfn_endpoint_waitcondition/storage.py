"""Storage resources: S3BucketDestination, S3BucketDestinationPolicy."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.s3 import BucketVersioningStatus


@cloudformation_dataclass
class S3BucketDestinationServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AWS_KMS
    kms_master_key_id = ref(KmsKey)


@cloudformation_dataclass
class S3BucketDestinationServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketDestinationServerSideEncryptionByDefault
    bucket_key_enabled = True


@cloudformation_dataclass
class S3BucketDestinationBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [S3BucketDestinationServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketDestinationPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3BucketDestinationDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class S3BucketDestination:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-${AWS::AccountId}-bucket')
    bucket_encryption = S3BucketDestinationBucketEncryption
    public_access_block_configuration = S3BucketDestinationPublicAccessBlockConfiguration
    versioning_configuration = S3BucketDestinationDeleteMarkerReplication
    deletion_policy = 'Delete'


@cloudformation_dataclass
class S3BucketDestinationPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'Allow source account access to destination bucket'
    principal = {
        'AWS': ref(AccountIdSource),
    }
    action = [
        's3:ReplicateDelete',
        's3:ReplicateObject',
        's3:ReplicateTags',
        's3:GetObjectVersionTagging',
        's3:ObjectOwnerOverrideToBucketOwner',
    ]
    resource_arn = Sub('${varBucketArn}/*', {
    'varBucketArn': get_att(S3BucketDestination, "Arn"),
})


@cloudformation_dataclass
class S3BucketDestinationPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = Sub('${varBucketArn}/*', {
    'varBucketArn': get_att(S3BucketDestination, "Arn"),
})
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class S3BucketDestinationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [S3BucketDestinationPolicyAllowStatement0, S3BucketDestinationPolicyDenyStatement1]


@cloudformation_dataclass
class S3BucketDestinationPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(S3BucketDestination)
    policy_document = S3BucketDestinationPolicyPolicyDocument
