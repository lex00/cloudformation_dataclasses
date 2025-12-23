"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppRunnerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['build.apprunner.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class AppRunnerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AppRunnerRoleAllowStatement0]


@cloudformation_dataclass
class AppRunnerRole:
    """AWS::IAM::Role resource."""

    # Unknown resource type: AWS::IAM::Role
    resource: CloudFormationResource
    assume_role_policy_document = AppRunnerRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'root',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Action': [
                    'ecr:GetDownloadUrlForLayer',
                    'ecr:BatchGetImage',
                    'ecr:DescribeImages',
                    'ecr:GetAuthorizationToken',
                    'ecr:BatchCheckLayerAvailability',
                ],
                'Resource': '*',
            }],
        },
    }]


@cloudformation_dataclass
class AppRunner:
    """AWS::AppRunner::Service resource."""

    # Unknown resource type: AWS::AppRunner::Service
    resource: CloudFormationResource
    service_name = Join('', [
    AWS_STACK_NAME,
    '-service',
])
    source_configuration = {
        'AuthenticationConfiguration': {
            'AccessRoleArn': get_att(AppRunnerRole, "Arn"),
        },
        'AutoDeploymentsEnabled': True,
        'ImageRepository': {
            'ImageRepositoryType': 'ECR',
            'ImageIdentifier': ref(ECRURL),
            'ImageConfiguration': {
                'Port': ref(TCPPORT),
            },
        },
    }
