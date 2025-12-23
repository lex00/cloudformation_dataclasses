"""Security resources: AWSCloudFormationStackSetAdministrationRole."""

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
class AWSCloudFormationStackSetAdministrationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'AWSCloudFormationStackSetAdministrationRole'
    assume_role_policy_document = AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument
    policies = [{
        'PolicyName': 'AssumeRole-AWSCloudFormationStackSetExecutionRole',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Action': 'sts:AssumeRole',
                'Resource': 'arn:aws:iam::*:role/AWSCloudFormationStackSetExecutionRole',
            }],
        },
    }]
