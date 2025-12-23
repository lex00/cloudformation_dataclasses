"""Stack resources."""

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
class PrivateSubnetOne:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = ref(VPC)
    cidr_block = FindInMap("SubnetConfig", 'PrivateOne', 'CIDR')


@cloudformation_dataclass
class PrivateSubnetTwo:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = ref(VPC)
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')


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
class NatGatewayOneAttachment:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    depends_on = ["GatewayAttachement"]


@cloudformation_dataclass
class NatGatewayTwoAttachment:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    depends_on = ["GatewayAttachement"]


@cloudformation_dataclass
class NatGatewayOne:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NatGatewayOneAttachment, "AllocationId")
    subnet_id = ref(PublicSubnetOne)


@cloudformation_dataclass
class NatGatewayTwo:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NatGatewayTwoAttachment, "AllocationId")
    subnet_id = ref(PublicSubnetTwo)


@cloudformation_dataclass
class PrivateRouteTableOne:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateRouteOne:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTableOne)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NatGatewayOne)


@cloudformation_dataclass
class PrivateRouteTableOneAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTableOne)
    subnet_id = ref(PrivateSubnetOne)


@cloudformation_dataclass
class PrivateRouteTableTwo:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateRouteTwo:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTableTwo)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NatGatewayTwo)


@cloudformation_dataclass
class PrivateRouteTableTwoAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTableTwo)
    subnet_id = ref(PrivateSubnetTwo)


@cloudformation_dataclass
class DynamoDBEndpointAllowStatement0:
    resource: PolicyStatement
    principal = '*'
    action = '*'
    resource_arn = '*'


@cloudformation_dataclass
class DynamoDBEndpointPolicyDocument:
    resource: PolicyDocument
    statement = [DynamoDBEndpointAllowStatement0]


@cloudformation_dataclass
class DynamoDBEndpoint:
    """AWS::EC2::VPCEndpoint resource."""

    resource: ec2.VPCEndpoint
    policy_document = DynamoDBEndpointPolicyDocument
    route_table_ids = [ref(PrivateRouteTableOne), ref(PrivateRouteTableTwo)]
    service_name = Join('', [
    'com.amazonaws.',
    AWS_REGION,
    '.dynamodb',
])
    vpc_id = ref(VPC)


@cloudformation_dataclass
class ECSCluster:
    """AWS::ECS::Cluster resource."""

    resource: ecs.Cluster


@cloudformation_dataclass
class FargateContainerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the Fargate containers'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = ref(VPC)
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'IpProtocol': '-1',
    }]


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPublicALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(PublicLoadBalancerSG)


@cloudformation_dataclass
class PrivateLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the internal load balancer'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPrivateALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(PrivateLoadBalancerSG)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromSelf:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(FargateContainerSecurityGroup)


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
    depends_on = ["GatewayAttachement"]


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


@cloudformation_dataclass
class PrivateLoadBalancerIngressFromECS:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the fargate container security group'
    group_id = ref(PrivateLoadBalancerSG)
    ip_protocol = '-1'
    source_security_group_id = ref(FargateContainerSecurityGroup)


@cloudformation_dataclass
class PrivateLoadBalancerLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class PrivateLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internal'
    load_balancer_attributes = [PrivateLoadBalancerLoadBalancerAttribute]
    subnets = [ref(PrivateSubnetOne), ref(PrivateSubnetTwo)]
    security_groups = [ref(PrivateLoadBalancerSG)]


@cloudformation_dataclass
class DummyTargetGroupPrivate:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = Join('-', [
    AWS_STACK_NAME,
    'drop-2',
])
    port = 80
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(DummyTargetGroupPrivate)
    type_ = 'forward'


@cloudformation_dataclass
class PrivateLoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [PrivateLoadBalancerListenerAction]
    load_balancer_arn = ref(PrivateLoadBalancer)
    port = 80
    protocol = 'HTTP'


@cloudformation_dataclass
class ECSRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSRoleAllowStatement0]


@cloudformation_dataclass
class ECSRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ec2:AttachNetworkInterface',
        'ec2:CreateNetworkInterface',
        'ec2:CreateNetworkInterfacePermission',
        'ec2:DeleteNetworkInterface',
        'ec2:DeleteNetworkInterfacePermission',
        'ec2:Describe*',
        'ec2:DetachNetworkInterface',
        'elasticloadbalancing:DeregisterInstancesFromLoadBalancer',
        'elasticloadbalancing:DeregisterTargets',
        'elasticloadbalancing:Describe*',
        'elasticloadbalancing:RegisterInstancesWithLoadBalancer',
        'elasticloadbalancing:RegisterTargets',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ECSRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = ECSRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSRolePolicy]


@cloudformation_dataclass
class ECSTaskExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs-tasks.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSTaskExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSTaskExecutionRoleAllowStatement0]


@cloudformation_dataclass
class ECSTaskExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecr:GetAuthorizationToken',
        'ecr:BatchCheckLayerAvailability',
        'ecr:GetDownloadUrlForLayer',
        'ecr:BatchGetImage',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ECSTaskExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSTaskExecutionRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSTaskExecutionRolePolicy:
    resource: iam.user.Policy
    policy_name = 'AmazonECSTaskExecutionRolePolicy'
    policy_document = ECSTaskExecutionRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSTaskExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSTaskExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSTaskExecutionRolePolicy]
