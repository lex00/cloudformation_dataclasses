"""S3BucketDestinationPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


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
