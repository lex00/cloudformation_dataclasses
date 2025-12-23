"""Network resources: VPC, PublicSubnetOne, PublicSubnetTwo, InternetGateway, GatewayAttachement, PublicRouteTable, PublicRoute, PublicSubnetOneRouteTableAssociation, PublicSubnetTwoRouteTableAssociation, EcsHostSecurityGroup, PublicLoadBalancerSG, PublicLoadBalancer, DummyTargetGroupPublic, PublicLoadBalancerListener."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


@cloudformation_dataclass
class PublicSubnetOne:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = ref(VPC)
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


@cloudformation_dataclass
class PublicSubnetTwo:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = ref(VPC)
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class GatewayAttachement:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    depends_on = ["GatewayAttachement"]


@cloudformation_dataclass
class PublicSubnetOneRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnetOne)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicSubnetTwoRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnetTwo)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class EcsHostSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = ref(VPC)
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'IpProtocol': -1,
    }]


@cloudformation_dataclass
class PublicLoadBalancerLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class PublicLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    load_balancer_attributes = [PublicLoadBalancerLoadBalancerAttribute]
    subnets = [ref(PublicSubnetOne), ref(PublicSubnetTwo)]
    security_groups = [ref(PublicLoadBalancerSG)]


@cloudformation_dataclass
class DummyTargetGroupPublic:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = Join('-', [
    AWS_STACK_NAME,
    'drop-1',
])
    port = 80
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(DummyTargetGroupPublic)
    type_ = 'forward'


@cloudformation_dataclass
class PublicLoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [PublicLoadBalancerListenerAction]
    load_balancer_arn = ref(PublicLoadBalancer)
    port = 80
    protocol = 'HTTP'
    depends_on = ["PublicLoadBalancer"]
