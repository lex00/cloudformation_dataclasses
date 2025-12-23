"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class PublicInternetRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicInternetRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(PublicInternetRouteTable)
    depends_on = ["InternetGateway", "PublicInternetRouteTable"]


@cloudformation_dataclass
class VPCGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnetA:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = FindInMap("AWSRegion2AZ", AWS_REGION, 'A')
    cidr_block = '10.0.0.0/25'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnetB:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = FindInMap("AWSRegion2AZ", AWS_REGION, 'B')
    cidr_block = '10.0.0.128/25'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnetARouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicInternetRouteTable)
    subnet_id = ref(PublicSubnetA)


@cloudformation_dataclass
class PublicSubnetBRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicInternetRouteTable)
    subnet_id = ref(PublicSubnetB)


@cloudformation_dataclass
class RedisParameterGroup:
    """AWS::ElastiCache::ParameterGroup resource."""

    resource: elasticache.ParameterGroup
    cache_parameter_group_family = 'redis2.8'
    description = 'RedisParameterGroup'


@cloudformation_dataclass
class RedisSubnetGroup:
    """AWS::ElastiCache::SubnetGroup resource."""

    resource: elasticache.SubnetGroup
    description = 'RedisSubnetGroup'
    subnet_ids = [ref(PublicSubnetA), ref(PublicSubnetB)]


@cloudformation_dataclass
class RedisSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'RedisSecurityGroup'
    vpc_id = ref(VPC)
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '6379',
        'ToPort': '6379',
        'CidrIp': '192.168.1.0/32',
    }]


@cloudformation_dataclass
class RedisReplicationGroup:
    """AWS::ElastiCache::ReplicationGroup resource."""

    resource: elasticache.ReplicationGroup
    automatic_failover_enabled = 'true'
    cache_node_type = ref(RedisNodeType)
    cache_parameter_group_name = ref(RedisParameterGroup)
    cache_subnet_group_name = ref(RedisSubnetGroup)
    engine = 'redis'
    engine_version = '2.8.24'
    num_cache_clusters = '2'
    preferred_cache_cluster_a_zs = [FindInMap("AWSRegion2AZ", AWS_REGION, 'A'), FindInMap("AWSRegion2AZ", AWS_REGION, 'B')]
    replication_group_description = 'RedisReplicationGroup'
    security_group_ids = [ref(RedisSecurityGroup)]


@cloudformation_dataclass
class IamRoleLambdaAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class IamRoleLambdaAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [IamRoleLambdaAllowStatement0]


@cloudformation_dataclass
class IamRoleLambdaAllowStatement0_1:
    resource: PolicyStatement
    action = ['elasticache:ModifyReplicationGroup']
    resource_arn = ref(RedisReplicationGroup)


@cloudformation_dataclass
class IamRoleLambdaPolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [IamRoleLambdaAllowStatement0_1]


@cloudformation_dataclass
class IamRoleLambdaPolicy:
    resource: iam.user.Policy
    policy_name = 'ElastiCacheSnapshotPolicy'
    policy_document = IamRoleLambdaPolicies0PolicyDocument


@cloudformation_dataclass
class IamRoleLambda:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = IamRoleLambdaAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']
    policies = [IamRoleLambdaPolicy]
    condition = 'EnableBackups'


@cloudformation_dataclass
class EnableShapshotCode:
    resource: lambda_.function.Code
    zip_file = {
        'Rain::Embed': 'elastic-code.js',
    }


@cloudformation_dataclass
class EnableShapshot:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = EnableShapshotCode
    handler = 'index.handler'
    memory_size = 128
    role = get_att(IamRoleLambda, "Arn")
    runtime = 'nodejs20.x'
    timeout = 30
    depends_on = ["IamRoleLambda"]
    condition = 'EnableBackups'
    deletion_policy = 'Delete'


@cloudformation_dataclass
class LambdaExecutePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(EnableShapshot, "Arn")
    principal = 'elasticache.amazonaws.com'
    source_account = Sub('${AWS::AccountId}')
    condition = 'EnableBackups'


@cloudformation_dataclass
class EnableShapshotTrigger:
    """Custom::Region resource."""

    # Unknown resource type: Custom::Region
    resource: CloudFormationResource
    service_token = get_att(EnableShapshot, "Arn")
    ss_cluster_id = ref(RedisReplicationGroup)
    ss_window = ref(SnapshotWindow)
    ss_retention_limit = ref(SnapshotRetentionLimit)
    depends_on = ["EnableShapshot", "LambdaExecutePermission", "RedisReplicationGroup"]
    condition = 'EnableBackups'
