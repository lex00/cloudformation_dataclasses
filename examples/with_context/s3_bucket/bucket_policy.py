"""S3 bucket policy requiring encrypted uploads."""

from . import *  # noqa: F403
from .bucket import MyData
from .context import ctx


@cloudformation_dataclass
class DenyUnencryptedUploadsStatement:
    """Policy statement denying uploads without AES256 encryption."""

    resource: DenyStatement
    sid = "DenyUnencryptedObjectUploads"
    principal = "*"
    action = "s3:PutObject"
    resource_arn = Sub("${MyData.Arn}/*")
    condition = {
        STRING_NOT_EQUALS: {"s3:x-amz-server-side-encryption": "AES256"}
    }


@cloudformation_dataclass
class EncryptionRequiredPolicyDocument:
    """IAM policy document requiring encrypted uploads."""

    resource: PolicyDocument
    statement = [DenyUnencryptedUploadsStatement]


@cloudformation_dataclass
class MyDataPolicy:
    """Bucket policy enforcing server-side encryption."""

    resource: BucketPolicy
    context = ctx
    bucket = ref(MyData)
    policy_document = EncryptionRequiredPolicyDocument
