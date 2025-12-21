from __future__ import annotations

"""NeptuneS3Policy - AWS::IAM::ManagedPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneS3PolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowNeptuneAccessToS3'
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::*')]


@cloudformation_dataclass
class NeptuneS3PolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneS3PolicyAllowStatement0]


@cloudformation_dataclass
class NeptuneS3Policy:
    """AWS::IAM::ManagedPolicy resource."""

    resource: ManagedPolicy
    description = 'Neptune default policy for S3 access for data load'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-s3-policy-${AWS::Region}')
    policy_document = NeptuneS3PolicyPolicyDocument
