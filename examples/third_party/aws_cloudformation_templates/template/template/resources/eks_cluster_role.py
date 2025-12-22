from __future__ import annotations

"""EKSClusterRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EKSClusterRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': FindInMap("ServicePrincipalPartitionMap", AWS_PARTITION, 'EKS'),
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EKSClusterRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EKSClusterRoleAllowStatement0]


@cloudformation_dataclass
class EKSClusterRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = EKSClusterRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSClusterPolicy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSVPCResourceController')]
