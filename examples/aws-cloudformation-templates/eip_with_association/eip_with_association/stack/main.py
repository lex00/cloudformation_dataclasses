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

    resource: Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = ref(VPC)
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


@cloudformation_dataclass
class PublicSubnetTwo:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
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

    resource: VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
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

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnetOne)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicSubnetTwoRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnetTwo)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class ECSCluster:
    """AWS::ECS::Cluster resource."""

    resource: ecs.Cluster


@cloudformation_dataclass
class EcsHostSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicLoadBalancerSGEgress:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    ip_protocol = -1


@cloudformation_dataclass
class PublicLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = ref(VPC)
    security_group_ingress = [PublicLoadBalancerSGEgress]


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPublicALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = ref(EcsHostSecurityGroup)
    ip_protocol = -1
    source_security_group_id = ref(PublicLoadBalancerSG)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromSelf:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other hosts in the same security group'
    group_id = ref(EcsHostSecurityGroup)
    ip_protocol = -1
    source_security_group_id = ref(EcsHostSecurityGroup)


@cloudformation_dataclass
class EC2RoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EC2RoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0]


@cloudformation_dataclass
class EC2RoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecs:CreateCluster',
        'ecs:DeregisterContainerInstance',
        'ecs:DiscoverPollEndpoint',
        'ecs:Poll',
        'ecs:RegisterContainerInstance',
        'ecs:StartTelemetrySession',
        'ecs:Submit*',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'ecr:GetAuthorizationToken',
        'ecr:BatchGetImage',
        'ecr:GetDownloadUrlForLayer',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class EC2RolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0_1]


@cloudformation_dataclass
class EC2RolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = EC2RolePolicies0PolicyDocument


@cloudformation_dataclass
class EC2Role:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EC2RoleAssumeRolePolicyDocument
    path = '/'
    policies = [EC2RolePolicy]


@cloudformation_dataclass
class EC2InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(EC2Role)]


@cloudformation_dataclass
class ContainerInstances:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: LaunchConfiguration
    image_id = ref(ECSAMI)
    security_groups = [ref(EcsHostSecurityGroup)]
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(EC2InstanceProfile)
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
"""))


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    vpc_zone_identifier = [ref(PublicSubnetOne), ref(PublicSubnetTwo)]
    launch_configuration_name = ref(ContainerInstances)
    min_size = '1'
    max_size = ref(MaxSize)
    desired_capacity = ref(DesiredCapacity)


@cloudformation_dataclass
class AutoscalingRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['application-autoscaling.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class AutoscalingRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0]


@cloudformation_dataclass
class AutoscalingRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'application-autoscaling:*',
        'cloudwatch:DescribeAlarms',
        'cloudwatch:PutMetricAlarm',
        'ecs:DescribeServices',
        'ecs:UpdateService',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class AutoscalingRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0_1]


@cloudformation_dataclass
class AutoscalingRolePolicy:
    resource: iam.user.Policy
    policy_name = 'service-autoscaling'
    policy_document = AutoscalingRolePolicies0PolicyDocument


@cloudformation_dataclass
class AutoscalingRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = AutoscalingRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AutoscalingRolePolicy]


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
