"""OriginALBTG - AWS::ElasticLoadBalancingV2::TargetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginALBTGLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = ref(ALBTargetGroupAttributeDeregistration)


@cloudformation_dataclass
class OriginALBTGTargetDescription:
    resource: elasticloadbalancingv2.target_group.TargetDescription
    id = ref(EC2Instance)
    port = ref(OriginALBTGPort)


@cloudformation_dataclass
class OriginALBTGLoadBalancerAttribute1:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-tg')


@cloudformation_dataclass
class OriginALBTGLoadBalancerAttribute2:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
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
    target_group_attributes = [OriginALBTGLoadBalancerAttribute]
    target_type = 'instance'
    targets = [OriginALBTGTargetDescription]
    port = ref(OriginALBTGPort)
    protocol = 'HTTP'
    vpc_id = ref(VpcId)
    tags = [OriginALBTGLoadBalancerAttribute1, OriginALBTGLoadBalancerAttribute2]
    depends_on = ["OriginALB"]
