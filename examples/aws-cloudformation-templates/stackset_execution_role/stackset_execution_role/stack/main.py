"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSCloudFormationStackSetExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'AWS': Sub('arn:aws:iam::${AdministrationAccountId}:role/AWSCloudFormationStackSetAdministrationRole'),
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetExecutionRoleAllowStatement0]


@cloudformation_dataclass
class AWSCloudFormationStackSetExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'AWSCloudFormationStackSetExecutionRole'
    assume_role_policy_document = AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument
    policies = [{
        'PolicyName': 'ExecutionRolePolicy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Action': [
                        'cloudformation:CreateStack',
                        'cloudformation:UpdateStack',
                        'cloudformation:DeleteStack',
                        'cloudformation:DescribeStacks',
                        'cloudformation:DescribeStackEvents',
                        'cloudformation:DescribeStackResources',
                        'cloudformation:GetTemplate',
                        'cloudformation:ValidateTemplate',
                    ],
                    'Resource': '*',
                },
                {
                    'Effect': 'Allow',
                    'Action': [
                        'cloudwatch:PutDashboard',
                        'cloudwatch:DeleteDashboards',
                        'cloudwatch:PutMetricAlarm',
                        'cloudwatch:DeleteAlarms',
                        'cloudwatch:DescribeAlarms',
                    ],
                    'Resource': '*',
                },
                {
                    'Effect': 'Allow',
                    'Action': [
                        'sns:CreateTopic',
                        'sns:DeleteTopic',
                        'sns:Subscribe',
                        'sns:Unsubscribe',
                        'sns:SetTopicAttributes',
                        'sns:GetTopicAttributes',
                        'sns:ListSubscriptionsByTopic',
                    ],
                    'Resource': '*',
                },
                {
                    'Effect': 'Allow',
                    'Action': [
                        'kms:Decrypt',
                        'kms:DescribeKey',
                    ],
                    'Resource': '*',
                },
                {
                    'Effect': 'Allow',
                    'Action': [
                        'ssm:GetParameter',
                        'ssm:GetParameters',
                        'ssm:GetParametersByPath',
                    ],
                    'Resource': ['arn:aws:ssm:*:*:parameter/cdk-bootstrap/*'],
                },
            ],
        },
    }]
