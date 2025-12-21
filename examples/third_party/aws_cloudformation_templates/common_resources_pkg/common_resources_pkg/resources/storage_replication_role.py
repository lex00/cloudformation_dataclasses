from __future__ import annotations

"""StorageReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StorageReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class StorageReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [StorageReplicationRoleAllowStatement0]


@cloudformation_dataclass
class StorageReplicationRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = StorageReplicationRoleAssumeRolePolicyDocument
    path = '/'
