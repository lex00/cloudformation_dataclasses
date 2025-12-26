"""Infra resources: TargetAccountLogging."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TargetAccountLoggingDeploymentTargets:
    resource: cloudformation.stack_set.DeploymentTargets
    organizational_unit_ids = [ref(OUID)]


@cloudformation_dataclass
class TargetAccountLoggingStackInstances:
    resource: cloudformation.stack_set.StackInstances
    deployment_targets = TargetAccountLoggingDeploymentTargets
    regions = ['us-east-1', 'us-west-2']


@cloudformation_dataclass
class TargetAccountLoggingParameter:
    resource: cloudformation.stack_set.Parameter
    parameter_key = 'CentralEventBusArn'
    parameter_value = get_att(CentralEventBus, "Arn")


@cloudformation_dataclass
class TargetAccountLoggingOperationPreferences:
    resource: cloudformation.stack_set.OperationPreferences
    failure_tolerance_count = 0
    max_concurrent_count = 2
    region_concurrency_type = 'PARALLEL'


@cloudformation_dataclass
class TargetAccountLoggingAutoDeployment:
    resource: cloudformation.stack_set.AutoDeployment
    enabled = True
    retain_stacks_on_account_removal = True


@cloudformation_dataclass
class TargetAccountLogging:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = {
        'Rain::Embed': 'log-setup-target-accounts.yaml',
    }
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [TargetAccountLoggingStackInstances]
    parameters = [TargetAccountLoggingParameter]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging. It configures logging resources in target accounts.'
    operation_preferences = TargetAccountLoggingOperationPreferences
    auto_deployment = TargetAccountLoggingAutoDeployment
    stack_set_name = 'log-setup'
    depends_on = [CentralEventRule, CentralEventLog, CentralEventLogPolicy]
