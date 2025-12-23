"""EMRClusterServiceRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EMRClusterServiceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['elasticmapreduce.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EMRClusterServiceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EMRClusterServiceRoleAllowStatement0]


@cloudformation_dataclass
class EMRClusterServiceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EMRClusterServiceRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole']
    path = '/'
