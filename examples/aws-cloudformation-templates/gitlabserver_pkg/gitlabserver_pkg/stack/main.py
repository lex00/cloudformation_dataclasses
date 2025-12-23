"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkVPCAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


@cloudformation_dataclass
class NetworkVPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'
    tags = [NetworkVPCAssociationParameter]


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    description = 'Allow HTTP from com.amazonaws.global.cloudfront.origin-facing'
    ip_protocol = 'tcp'
    from_port = 80
    to_port = 80
    source_prefix_list_id = FindInMap("Prefixes", AWS_REGION, 'PrefixList')


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    description = 'Allow all outbound traffic by default'
    ip_protocol = '-1'


@cloudformation_dataclass
class InstanceSecurityGroupAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-isg'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'gitlab-server-isg'
    security_group_ingress = [InstanceSecurityGroupIngress]
    security_group_egress = [InstanceSecurityGroupEgress]
    tags = [InstanceSecurityGroupAssociationParameter]
    vpc_id = ref(NetworkVPC)


@cloudformation_dataclass
class InstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'ec2.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class InstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRoleAllowStatement0]


@cloudformation_dataclass
class InstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = InstanceRoleAssumeRolePolicyDocument
    tags = [{
        'Key': 'Name',
        'Value': 'gitlab-server-instance',
    }]


@cloudformation_dataclass
class InstanceRolePolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        'ec2messages:*',
        'ssm:UpdateInstanceInformation',
        'ssmmessages:*',
        'secretsmanager:GetSecretValue',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class InstanceRolePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRolePolicyAllowStatement0]


@cloudformation_dataclass
class InstanceRolePolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = InstanceRolePolicyPolicyDocument
    policy_name = 'InstanceRolePolicy'
    role_name = ref(InstanceRole)


@cloudformation_dataclass
class InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    roles = [ref(InstanceRole)]


@cloudformation_dataclass
class NetworkPublicSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1'


@cloudformation_dataclass
class NetworkPublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet1AssociationParameter]


@cloudformation_dataclass
class ServerEbs:
    resource: ec2.instance.Ebs
    volume_size = 128


@cloudformation_dataclass
class ServerBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/xvda'
    ebs = ServerEbs


@cloudformation_dataclass
class ServerAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


@cloudformation_dataclass
class Server:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    availability_zone = Select(0, GetAZs())
    block_device_mappings = [ServerBlockDeviceMapping]
    iam_instance_profile = ref(InstanceProfile)
    image_id = ref(LatestAMI)
    instance_type = ref(InstanceType)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    subnet_id = get_att(NetworkPublicSubnet1, "SubnetId")
    tags = [ServerAssociationParameter]
    user_data = Base64(Sub("""#!/bin/bash

set -eou pipefail

local_ip=$(ec2-metadata | grep "^local-ipv4: " | cut -d " " -f 2)

# Install cfn-signal
yum install -y aws-cfn-bootstrap

# Install postfix
yum install -y postfix
systemctl enable postfix
systemctl start postfix

# Get the yum repo
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash

# Install gitlab and run it on the local ip
export EXTERNAL_URL="http://$local_ip" 
yum install -y gitlab-ee

# Tell CloudFormation we're ready to go
# This is a variable for the Sub intrisic function, not a bash variable
cfn-signal -s true --stack ${AWS::StackName} --resource Server --region ${AWS::Region}"""))
    depends_on = ["InstanceRolePolicy", "InstanceRole"]


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-rt'


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet1RouteTableAssociationParameter]


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(NetworkPublicSubnet1RouteTable)
    subnet_id = ref(NetworkPublicSubnet1)


@cloudformation_dataclass
class NetworkInternetGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


@cloudformation_dataclass
class NetworkInternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [NetworkInternetGatewayAssociationParameter]


@cloudformation_dataclass
class NetworkPublicSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(NetworkInternetGateway)
    route_table_id = ref(NetworkPublicSubnet1RouteTable)
    depends_on = ["NetworkVPCGW"]


@cloudformation_dataclass
class NetworkPublicSubnet1EIPAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-eip'


@cloudformation_dataclass
class NetworkPublicSubnet1EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet1EIPAssociationParameter]


@cloudformation_dataclass
class NetworkPublicSubnet1NATGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-ngw'


@cloudformation_dataclass
class NetworkPublicSubnet1NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NetworkPublicSubnet1EIP, "AllocationId")
    subnet_id = ref(NetworkPublicSubnet1)
    tags = [NetworkPublicSubnet1NATGatewayAssociationParameter]
    depends_on = ["NetworkPublicSubnet1DefaultRoute", "NetworkPublicSubnet1RouteTableAssociation"]


@cloudformation_dataclass
class NetworkPublicSubnet2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-2'


@cloudformation_dataclass
class NetworkPublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet2AssociationParameter]


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-2-rt'


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet2RouteTableAssociationParameter]


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(NetworkPublicSubnet2RouteTable)
    subnet_id = ref(NetworkPublicSubnet2)


@cloudformation_dataclass
class NetworkPublicSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(NetworkInternetGateway)
    route_table_id = ref(NetworkPublicSubnet2RouteTable)
    depends_on = ["NetworkVPCGW"]


@cloudformation_dataclass
class NetworkPublicSubnet2EIPAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-eip'


@cloudformation_dataclass
class NetworkPublicSubnet2EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet2EIPAssociationParameter]


@cloudformation_dataclass
class NetworkPublicSubnet2NATGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-ngw'


@cloudformation_dataclass
class NetworkPublicSubnet2NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NetworkPublicSubnet2EIP, "AllocationId")
    subnet_id = ref(NetworkPublicSubnet2)
    tags = [NetworkPublicSubnet2NATGatewayAssociationParameter]
    depends_on = ["NetworkPublicSubnet2DefaultRoute", "NetworkPublicSubnet2RouteTableAssociation"]


@cloudformation_dataclass
class NetworkPrivateSubnet1SubnetAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1'


@cloudformation_dataclass
class NetworkPrivateSubnet1Subnet:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet1SubnetAssociationParameter]


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1-rt'


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet1RouteTableAssociationParameter]


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(NetworkPrivateSubnet1RouteTable)
    subnet_id = ref(NetworkPrivateSubnet1Subnet)


@cloudformation_dataclass
class NetworkPrivateSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NetworkPublicSubnet1NATGateway)
    route_table_id = ref(NetworkPrivateSubnet1RouteTable)


@cloudformation_dataclass
class NetworkPrivateSubnet2SubnetAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-2'


@cloudformation_dataclass
class NetworkPrivateSubnet2Subnet:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet2SubnetAssociationParameter]


@cloudformation_dataclass
class NetworkPrivateSubnet2RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-2-rt'


@cloudformation_dataclass
class NetworkPrivateSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet2RouteTableAssociationParameter]


@cloudformation_dataclass
class NetworkPrivateSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(NetworkPrivateSubnet2RouteTable)
    subnet_id = ref(NetworkPrivateSubnet2Subnet)


@cloudformation_dataclass
class NetworkPrivateSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NetworkPublicSubnet2NATGateway)
    route_table_id = ref(NetworkPrivateSubnet2RouteTable)


@cloudformation_dataclass
class NetworkVPCGW:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(NetworkInternetGateway)
    vpc_id = ref(NetworkVPC)


@cloudformation_dataclass
class CloudFrontCachePolicyCookiesConfig:
    resource: cloudfront.cache_policy.CookiesConfig
    cookie_behavior = 'all'


@cloudformation_dataclass
class CloudFrontCachePolicyHeadersConfig:
    resource: cloudfront.cache_policy.HeadersConfig
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


@cloudformation_dataclass
class CloudFrontCachePolicyQueryStringsConfig:
    resource: cloudfront.cache_policy.QueryStringsConfig
    query_string_behavior = 'all'


@cloudformation_dataclass
class CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin:
    resource: cloudfront.cache_policy.ParametersInCacheKeyAndForwardedToOrigin
    cookies_config = CloudFrontCachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CloudFrontCachePolicyHeadersConfig
    query_strings_config = CloudFrontCachePolicyQueryStringsConfig


@cloudformation_dataclass
class CloudFrontCachePolicyCachePolicyConfig:
    resource: cloudfront.cache_policy.CachePolicyConfig
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = 'gitlab-server'
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin


@cloudformation_dataclass
class CloudFrontCachePolicy:
    """AWS::CloudFront::CachePolicy resource."""

    resource: cloudfront.CachePolicy
    cache_policy_config = CloudFrontCachePolicyCachePolicyConfig


@cloudformation_dataclass
class CloudFrontDistributionCacheBehavior:
    resource: cloudfront.distribution.CacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = '4135ea2d-6df8-44a3-9df3-4b5a84be39ad'
    compress = False
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'
    path_pattern = '/proxy/*'


@cloudformation_dataclass
class CloudFrontDistributionDefaultCacheBehavior:
    resource: cloudfront.distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = ref(CloudFrontCachePolicy)
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'


@cloudformation_dataclass
class CloudFrontDistributionCustomOriginConfig:
    resource: cloudfront.distribution.CustomOriginConfig
    http_port = 80
    origin_protocol_policy = 'http-only'


@cloudformation_dataclass
class CloudFrontDistributionOrigin:
    resource: cloudfront.distribution.Origin
    domain_name = get_att(Server, "PublicDnsName")
    id = Sub('CloudFront-${AWS::StackName}')
    custom_origin_config = CloudFrontDistributionCustomOriginConfig


@cloudformation_dataclass
class CloudFrontDistributionDistributionConfig:
    resource: cloudfront.distribution.DistributionConfig
    enabled = True
    http_version = 'http2'
    cache_behaviors = [CloudFrontDistributionCacheBehavior]
    default_cache_behavior = CloudFrontDistributionDefaultCacheBehavior
    origins = [CloudFrontDistributionOrigin]


@cloudformation_dataclass
class CloudFrontDistribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    tags = [{
        'Key': 'Name',
        'Value': 'gitlab-server',
    }, {
        'Key': 'Description',
        'Value': 'gitlab-server',
    }]
    distribution_config = CloudFrontDistributionDistributionConfig
    depends_on = ["Server"]
