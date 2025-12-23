"""ServiceScalingPolicy - AWS::ApplicationAutoScaling::ScalingPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceScalingPolicyStepAdjustment:
    resource: applicationautoscaling.scaling_policy.StepAdjustment
    metric_interval_lower_bound = 0
    scaling_adjustment = 200


@cloudformation_dataclass
class ServiceScalingPolicyStepScalingPolicyConfiguration:
    resource: applicationautoscaling.scaling_policy.StepScalingPolicyConfiguration
    adjustment_type = 'PercentChangeInCapacity'
    cooldown = 60
    metric_aggregation_type = 'Average'
    step_adjustments = [ServiceScalingPolicyStepAdjustment]


@cloudformation_dataclass
class ServiceScalingPolicy:
    """AWS::ApplicationAutoScaling::ScalingPolicy resource."""

    resource: applicationautoscaling.ScalingPolicy
    policy_name = 'AStepPolicy'
    policy_type = 'StepScaling'
    scaling_target_id = ref(ServiceScalingTarget)
    step_scaling_policy_configuration = ServiceScalingPolicyStepScalingPolicyConfiguration
