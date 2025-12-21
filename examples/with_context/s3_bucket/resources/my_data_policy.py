from __future__ import annotations

"""MyDataPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyDataPolicyDenyStatement0:
    resource: DenyStatement
    sid = 'DenyUnencryptedObjectUploads'
    principal = '*'
    action = 's3:PutObject'
    resource_arn = Sub('${MyData.Arn}/*')
    condition = {
        STRING_NOT_EQUALS: {
            's3:x-amz-server-side-encryption': 'AES256',
        },
    }


@cloudformation_dataclass
class MyDataPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [MyDataPolicyDenyStatement0]


@cloudformation_dataclass
class MyDataPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket: Ref[MyData] = ref()
    policy_document = MyDataPolicyPolicyDocument
