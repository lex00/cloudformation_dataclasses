from __future__ import annotations

"""KmsKey - AWS::KMS::Key resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KmsKeyAllowStatement0:
    resource: PolicyStatement
    sid = 'Allow destination account access to KMS key in destination account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 'kms:*'
    resource_arn = '*'


@cloudformation_dataclass
class KmsKeyAllowStatement1:
    resource: PolicyStatement
    sid = 'Allow source account access to KMS key in destination account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AccountIdSource}:root'),
    }
    action = [
        'kms:Encrypt',
        'kms:ReEncrypt*',
        'kms:GenerateDataKey*',
        'kms:DescribeKey',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class KmsKeyKeyPolicy:
    resource: PolicyDocument
    statement = [KmsKeyAllowStatement0, KmsKeyAllowStatement1]


@cloudformation_dataclass
class KmsKey:
    """AWS::KMS::Key resource."""

    resource: Key
    enable_key_rotation = True
    key_policy = KmsKeyKeyPolicy
