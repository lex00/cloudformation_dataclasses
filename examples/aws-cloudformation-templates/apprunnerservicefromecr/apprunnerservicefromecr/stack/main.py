"""Stack resources."""

from .. import *  # noqa: F403


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
