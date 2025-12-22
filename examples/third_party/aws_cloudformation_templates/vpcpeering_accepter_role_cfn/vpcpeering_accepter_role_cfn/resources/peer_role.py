"""PeerRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'AWS': Split(',', ref(PeerOwnerIds)),
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class PeerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [PeerRoleAllowStatement0]


@cloudformation_dataclass
class PeerRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'ec2:AcceptVpcPeeringConnection'
    resource_arn = '*'


@cloudformation_dataclass
class PeerRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [PeerRoleAllowStatement0_1]


@cloudformation_dataclass
class PeerRolePolicy:
    resource: iam.user.Policy
    policy_name = 'AcceptVPCPeering'
    policy_document = PeerRolePolicies0PolicyDocument


@cloudformation_dataclass
class PeerRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = PeerRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [PeerRolePolicy]
