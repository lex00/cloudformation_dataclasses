"""Security resources: ASCPrivateLinkLambdaRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ASCPrivateLinkLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ASCPrivateLinkLambdaRoleAllowStatement0]


@cloudformation_dataclass
class ASCPrivateLinkLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'ec2:DescribeVpcEndpointServiceConfigurations',
        'ec2:ModifyVpcEndpointServiceConfiguration',
        'route53:ChangeResourceRecordSets',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ASCPrivateLinkLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ASCPrivateLinkLambdaRoleAllowStatement0_1]


@cloudformation_dataclass
class ASCPrivateLinkLambdaRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ASCPrivateLinkLambdaPolicy'
    policy_document = ASCPrivateLinkLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class ASCPrivateLinkLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ASCPrivateLinkLambdaRolePolicy]
