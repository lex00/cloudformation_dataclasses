from __future__ import annotations

"""ObjectStorageReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ObjectStorageReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicationRoleAllowStatement0]


@cloudformation_dataclass
class ObjectStorageReplicationRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = ObjectStorageReplicationRoleAssumeRolePolicyDocument
    path = '/'
