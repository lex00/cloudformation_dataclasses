"""OriginALBTG - AWS::ElasticLoadBalancingV2::TargetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginALBTGTargetGroupAttribute:
    resource: TargetGroupAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = ref(ALBTargetGroupAttributeDeregistration)


@cloudformation_dataclass
class OriginALBTGTargetDescription:
    resource: TargetDescription
    id = ref(EC2Instance)
    port = ref(OriginALBTGPort)


@cloudformation_dataclass
class OriginALBTGListenerAttribute:
    resource: ListenerAttribute
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-tg')


@cloudformation_dataclass
class OriginALBTGListenerAttribute1:
    resource: ListenerAttribute
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class OriginALBTG:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    name = Sub('${AppName}-${Environment}-alb-tg')
    health_check_protocol = ref(HealthCheckProtocol)
    health_check_path = ref(HealthCheckPath)
    health_check_port = Sub('${OriginALBTGPort}')
    health_check_interval_seconds = ref(ALBTargetGroupHealthCheckIntervalSeconds)
    health_check_timeout_seconds = ref(ALBTargetGroupHealthCheckTimeoutSeconds)
    healthy_threshold_count = ref(ALBTargetGroupHealthyThresholdCount)
    unhealthy_threshold_count = ref(ALBTargetGroupUnhealthyThresholdCount)
    target_group_attributes = [OriginALBTGTargetGroupAttribute]
    target_type = 'instance'
    targets = [OriginALBTGTargetDescription]
    port = ref(OriginALBTGPort)
    protocol = 'HTTP'
    vpc_id = ref(VpcId)
    tags = [OriginALBTGListenerAttribute, OriginALBTGListenerAttribute1]
    depends_on = ["OriginALB"]
