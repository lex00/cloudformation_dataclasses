"""AWSCloudFormationStackSetAdministrationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSCloudFormationStackSetAdministrationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'cloudformation.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetAdministrationRoleAllowStatement0]


@cloudformation_dataclass
class AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'sts:AssumeRole'
    resource_arn = 'arn:aws:iam::*:role/AWSCloudFormationStackSetExecutionRole'


@cloudformation_dataclass
class AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1]


@cloudformation_dataclass
class AWSCloudFormationStackSetAdministrationRolePolicy:
    resource: iam.user.Policy
    policy_name = 'AssumeRole-AWSCloudFormationStackSetExecutionRole'
    policy_document = AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument


@cloudformation_dataclass
class AWSCloudFormationStackSetAdministrationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'AWSCloudFormationStackSetAdministrationRole'
    assume_role_policy_document = AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument
    policies = [AWSCloudFormationStackSetAdministrationRolePolicy]
