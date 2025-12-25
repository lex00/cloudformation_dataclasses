"""Network resources: EIP1, EIP2, loadBalancer, FirstEIP, SecondEIP, TargetGroup, Listener."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EIP1:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class EIP2:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class loadBalancerSubnetMapping:
    resource: elasticloadbalancingv2.load_balancer.SubnetMapping
    allocation_id = get_att(EIP1, "AllocationId")
    subnet_id = Select(0, ref(Subnet1))


@cloudformation_dataclass
class loadBalancerSubnetMapping1:
    resource: elasticloadbalancingv2.load_balancer.SubnetMapping
    allocation_id = get_att(EIP2, "AllocationId")
    subnet_id = Select(0, ref(Subnet2))


@cloudformation_dataclass
class loadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    subnet_mappings = [loadBalancerSubnetMapping, loadBalancerSubnetMapping1]
    type_ = ref(ELBType)
    ip_address_type = ref(ELBIpAddressType)
    depends_on = ["EIP2", "EIP1"]


@cloudformation_dataclass
class FirstEIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class SecondEIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class TargetGroupLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = '20'


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    name = 'MyTargets'
    port = 10
    protocol = 'TCP'
    target_group_attributes = [TargetGroupLoadBalancerAttribute]
    vpc_id = Select(0, ref(VPC))


@cloudformation_dataclass
class ListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(TargetGroup)


@cloudformation_dataclass
class Listener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [ListenerAction]
    load_balancer_arn = ref(loadBalancer)
    port = '80'
    protocol = 'TCP'
