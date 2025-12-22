"""DMSVpcRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DMSVpcRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class DMSVpcRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSVpcRoleAllowStatement0]


@cloudformation_dataclass
class DMSVpcRole:
    """AWS::IAM::Role resource."""

    resource: Role
    role_name = 'dms-vpc-role'
    assume_role_policy_document = DMSVpcRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole']
    path = '/'
    condition = 'NotExistsDMSVPCRole'
