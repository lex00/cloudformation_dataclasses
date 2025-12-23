"""Infra resources: TargetAccountLogging."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TargetAccountLogging:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = {
        'Rain::Embed': 'log-setup-target-accounts.yaml',
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
        'ParameterKey': 'CentralEventBusArn',
        'ParameterValue': get_att(CentralEventBus, "Arn"),
    }]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging. It configures logging resources in target accounts.'
    operation_preferences = {
        'FailureToleranceCount': 0,
        'MaxConcurrentCount': 2,
        'RegionConcurrencyType': 'PARALLEL',
    }
    auto_deployment = {
        'Enabled': True,
        'RetainStacksOnAccountRemoval': True,
    }
    stack_set_name = 'log-setup'
    depends_on = ["CentralEventRule", "CentralEventLog", "CentralEventLogPolicy"]
