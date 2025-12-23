"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = ref(VPCCidrBlock)
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-vpc'),
    }]


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-ig'),
    }]


@cloudformation_dataclass
class AttachGateway:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-public-route-table'),
    }]


@cloudformation_dataclass
class RouteInternetGateway:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    gateway_id = ref(InternetGateway)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock1)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-public-subnet1'),
    }, {
        'Key': 'kubernetes.io/role/elb',
        'Value': 1,
    }]


@cloudformation_dataclass
class PublicRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock2)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-public-subnet2'),
    }, {
        'Key': 'kubernetes.io/role/elb',
        'Value': 1,
    }]


@cloudformation_dataclass
class PublicRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet2)


@cloudformation_dataclass
class PublicSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock3)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-public-subnet3'),
    }, {
        'Key': 'kubernetes.io/role/elb',
        'Value': 1,
    }]


@cloudformation_dataclass
class PublicRouteTableAssociation3:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet3)


@cloudformation_dataclass
class EIP1:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP1, "AllocationId")
    subnet_id = ref(PublicSubnet1)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-nat-gw1'),
    }]


@cloudformation_dataclass
class EIP2:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP2, "AllocationId")
    subnet_id = ref(PublicSubnet2)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-nat-gw2'),
    }]


@cloudformation_dataclass
class EIP3:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway3:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP3, "AllocationId")
    subnet_id = ref(PublicSubnet3)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-nat-gw3'),
    }]


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock1)
    map_public_ip_on_launch = False
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-subnet1'),
    }]


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-route-table1'),
    }]


@cloudformation_dataclass
class PrivateRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable1)
    subnet_id = ref(PrivateSubnet1)


@cloudformation_dataclass
class PrivateRoute1:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable1)
    nat_gateway_id = ref(NATGateway1)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock2)
    map_public_ip_on_launch = False
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-subnet2'),
    }]


@cloudformation_dataclass
class PrivateRouteTable2:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-route-table2'),
    }]


@cloudformation_dataclass
class PrivateRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)


@cloudformation_dataclass
class PrivateRoute2:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable2)
    nat_gateway_id = ref(NATGateway2)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class PrivateSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock3)
    map_public_ip_on_launch = False
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-subnet3'),
    }]


@cloudformation_dataclass
class PrivateRouteTable3:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-route-table3'),
    }]


@cloudformation_dataclass
class PrivateRouteTableAssociation3:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable3)
    subnet_id = ref(PrivateSubnet3)


@cloudformation_dataclass
class PrivateRoute3:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable3)
    nat_gateway_id = ref(NATGateway3)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class ControlPlaneSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Communication between the control plane and worker nodegroups'
    vpc_id = ref(VPC)
    group_name = Sub('${AWS::StackName}-eks-control-plane-sg')


@cloudformation_dataclass
class EKSClusterRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': FindInMap("ServicePrincipalPartitionMap", AWS_PARTITION, 'EKS'),
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EKSClusterRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EKSClusterRoleAllowStatement0]


@cloudformation_dataclass
class EKSClusterRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EKSClusterRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSClusterPolicy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSVPCResourceController')]


@cloudformation_dataclass
class ControlPlaneResourcesVpcConfig:
    resource: eks.cluster.ResourcesVpcConfig
    security_group_ids = [ref(ControlPlaneSecurityGroup)]
    subnet_ids = [ref(PublicSubnet1), ref(PublicSubnet2), ref(PublicSubnet3), ref(PrivateSubnet1), ref(PrivateSubnet2), ref(PrivateSubnet3)]


@cloudformation_dataclass
class ControlPlane:
    """AWS::EKS::Cluster resource."""

    resource: eks.Cluster
    name = Sub('${AWS::StackName}-cluster')
    resources_vpc_config = ControlPlaneResourcesVpcConfig
    role_arn = get_att(EKSClusterRole, "Arn")
    version = ref(EKSClusterVersion)


@cloudformation_dataclass
class ControlPlaneSecurityGroupIngress:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(ControlPlaneSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = get_att(ControlPlaneSecurityGroup, "GroupId")
    source_security_group_owner_id = AWS_ACCOUNT_ID


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = {
        'BlockDeviceMappings': [{
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'Iops': 3000,
                'Throughput': 125,
                'VolumeSize': 80,
                'VolumeType': 'gp3',
            },
        }],
        'MetadataOptions': {
            'HttpPutResponseHopLimit': 2,
            'HttpTokens': 'optional',
        },
        'SecurityGroupIds': [ref(ControlPlaneSecurityGroup)],
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
            {
                'ResourceType': 'network-interface',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
        ],
    }
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')


@cloudformation_dataclass
class NodeInstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': FindInMap("ServicePrincipalPartitionMap", AWS_PARTITION, 'EC2'),
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class NodeInstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NodeInstanceRoleAllowStatement0]


@cloudformation_dataclass
class NodeInstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${AWS::StackName}-eks-node-role')
    assume_role_policy_document = NodeInstanceRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSWorkerNodePolicy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKS_CNI_Policy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore')]
    path = '/'


@cloudformation_dataclass
class ManagedNodeGroupSsoIdentity:
    resource: eks.capability.SsoIdentity
    id = ref(LaunchTemplate)


@cloudformation_dataclass
class ManagedNodeGroupScalingConfig:
    resource: eks.nodegroup.ScalingConfig
    desired_size = 2
    max_size = 2
    min_size = 2


@cloudformation_dataclass
class ManagedNodeGroup:
    """AWS::EKS::Nodegroup resource."""

    resource: eks.Nodegroup
    ami_type = 'AL2_x86_64'
    cluster_name = ref(ControlPlane)
    instance_types = [ref(NodeGroupInstanceTypes)]
    labels = {
        'alpha.eksctl.io/cluster-name': ref(ControlPlane),
        'alpha.eksctl.io/nodegroup-name': Sub('ng-${AWS::StackName}'),
    }
    launch_template = ManagedNodeGroupSsoIdentity
    node_role = get_att(NodeInstanceRole, "Arn")
    nodegroup_name = Sub('ng-${AWS::StackName}')
    scaling_config = ManagedNodeGroupScalingConfig
    subnets = [ref(PrivateSubnet1), ref(PrivateSubnet2), ref(PrivateSubnet3)]
    tags = {
        'alpha.eksctl.io/nodegroup-name': Sub('ng-${AWS::StackName}'),
        'alpha.eksctl.io/nodegroup-type': 'managed',
    }
