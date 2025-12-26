"""Network resources: EcsSecurityGroup, ECSALB, ECSTG, ALBListener, ECSALBListenerRule."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'ECS Security Group'
    vpc_id = ref(VpcId)


@cloudformation_dataclass
class ECSALBLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class ECSALB:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    name = 'ECSALB'
    scheme = 'internet-facing'
    load_balancer_attributes = [ECSALBLoadBalancerAttribute]
    subnets = ref(SubnetId)
    security_groups = [ref(EcsSecurityGroup)]


@cloudformation_dataclass
class ECSTG:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 10
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = 'ECSTG'
    port = 80
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ref(VpcId)
    depends_on = [ECSALB]


@cloudformation_dataclass
class ALBListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class ALBListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [ALBListenerAction]
    load_balancer_arn = ref(ECSALB)
    port = '80'
    protocol = 'HTTP'
    depends_on = [ECSServiceRole]


@cloudformation_dataclass
class ECSALBListenerRuleAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class ECSALBListenerRuleRuleCondition:
    resource: elasticloadbalancingv2.listener_rule.RuleCondition
    field = 'path-pattern'
    values = ['/']


@cloudformation_dataclass
class ECSALBListenerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: elasticloadbalancingv2.ListenerRule
    actions = [ECSALBListenerRuleAction]
    conditions = [ECSALBListenerRuleRuleCondition]
    listener_arn = ref(ALBListener)
    priority = 1
    depends_on = [ALBListener]
