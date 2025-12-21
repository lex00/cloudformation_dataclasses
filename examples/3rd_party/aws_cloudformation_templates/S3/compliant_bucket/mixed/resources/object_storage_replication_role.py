"""ObjectStorageReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageReplicationRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = PolicyDocument(statement=[PolicyStatement(principal={
                    'Service': ['s3.amazonaws.com'],
                }, action=['sts:AssumeRole'])])
    path = '/'
