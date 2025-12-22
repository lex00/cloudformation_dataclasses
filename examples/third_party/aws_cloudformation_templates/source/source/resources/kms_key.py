"""KmsKey - AWS::KMS::Key resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KmsKeyAllowStatement0:
    resource: PolicyStatement
    sid = 'Allow source account access to KMS key in source account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 'kms:*'
    resource_arn = '*'


@cloudformation_dataclass
class KmsKeyKeyPolicy:
    resource: PolicyDocument
    statement = [KmsKeyAllowStatement0]


@cloudformation_dataclass
class KmsKey:
    """AWS::KMS::Key resource."""

    resource: Key
    enable_key_rotation = True
    key_policy = KmsKeyKeyPolicy
