"""Infra resources: StackSet."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StackSetDeploymentTargets:
    resource: cloudformation.stack_set.DeploymentTargets
    organizational_unit_ids = [ref(OUID)]


@cloudformation_dataclass
class StackSetStackInstances:
    resource: cloudformation.stack_set.StackInstances
    deployment_targets = StackSetDeploymentTargets
    regions = ['us-east-1', 'us-west-2']


@cloudformation_dataclass
class StackSetParameter:
    resource: cloudformation.stack_set.Parameter
    parameter_key = 'AppName'
    parameter_value = 'stackset-logging-sample'


@cloudformation_dataclass
class StackSetOperationPreferences:
    resource: cloudformation.stack_set.OperationPreferences
    failure_tolerance_count = 0
    max_concurrent_count = 2
    region_concurrency_type = 'PARALLEL'


@cloudformation_dataclass
class StackSetAutoDeployment:
    resource: cloudformation.stack_set.AutoDeployment
    enabled = True
    retain_stacks_on_account_removal = True


@cloudformation_dataclass
class StackSet:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = {
        'Rain::Embed': 'common-resources-pkg.yaml',
    }
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [StackSetStackInstances]
    parameters = [StackSetParameter]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging'
    operation_preferences = StackSetOperationPreferences
    auto_deployment = StackSetAutoDeployment
    stack_set_name = 'common-resources'
