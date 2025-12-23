"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StackSet:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = {
        'Rain::Embed': 'common-resources-pkg.yaml',
    }
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [{
        'DeploymentTargets': {
            'OrganizationalUnitIds': [ref(OUID)],
        },
        'Regions': [
            'us-east-1',
            'us-west-2',
        ],
    }]
    parameters = [{
        'ParameterKey': 'AppName',
        'ParameterValue': 'stackset-logging-sample',
    }]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging'
    operation_preferences = {
        'FailureToleranceCount': 0,
        'MaxConcurrentCount': 2,
        'RegionConcurrencyType': 'PARALLEL',
    }
    auto_deployment = {
        'Enabled': True,
        'RetainStacksOnAccountRemoval': True,
    }
    stack_set_name = 'common-resources'
