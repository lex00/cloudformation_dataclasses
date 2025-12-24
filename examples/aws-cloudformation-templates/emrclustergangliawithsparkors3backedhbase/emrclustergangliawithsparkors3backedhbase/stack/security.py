"""Security resources: EMRClusterinstanceProfileRole, EMRClusterinstanceProfile, EMRClusterServiceRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EMRClusterinstanceProfileRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EMRClusterinstanceProfileRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EMRClusterinstanceProfileRoleAllowStatement0]


@cloudformation_dataclass
class EMRClusterinstanceProfileRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EMRClusterinstanceProfileRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role']
    path = '/'


@cloudformation_dataclass
class EMRClusterinstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(EMRClusterinstanceProfileRole)]


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
