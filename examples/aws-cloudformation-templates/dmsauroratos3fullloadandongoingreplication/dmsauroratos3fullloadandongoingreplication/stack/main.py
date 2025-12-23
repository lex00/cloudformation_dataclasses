"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }, {
        'Key': 'Name',
        'Value': AWS_STACK_NAME,
    }]


@cloudformation_dataclass
class DBSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    cidr_block = '10.0.0.0/26'
    availability_zone = Select(0, GetAZs())
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class DBSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    cidr_block = '10.0.0.64/26'
    availability_zone = Select(1, GetAZs())
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class AttachGateway:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class Route:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(RouteTable)
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    depends_on = ["AttachGateway"]


@cloudformation_dataclass
class SubnetRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(DBSubnet1)
    route_table_id = ref(RouteTable)


@cloudformation_dataclass
class SubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(DBSubnet2)
    route_table_id = ref(RouteTable)


@cloudformation_dataclass
class AuroraDBSubnetGroup:
    """AWS::RDS::DBSubnetGroup resource."""

    resource: rds.DBSubnetGroup
    db_subnet_group_description = 'Subnets available for the Aurora SampleDB DB Instance'
    subnet_ids = [ref(DBSubnet1), ref(DBSubnet2)]


@cloudformation_dataclass
class AuroraSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Security group for Aurora SampleDB DB Instance'
    group_name = 'Aurora SampleDB Security Group'
    vpc_id = ref(VPC)
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '3306',
        'ToPort': '3306',
        'CidrIp': ref(ClientIP),
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '3306',
        'ToPort': '3306',
        'CidrIp': '10.0.0.0/24',
    }]


@cloudformation_dataclass
class AuroraCluster:
    """AWS::RDS::DBCluster resource."""

    resource: rds.DBCluster
    database_name = 'dms_sample'
    backup_retention_period = 7
    db_subnet_group_name = ref(AuroraDBSubnetGroup)
    engine = 'aurora-postgresql'
    snapshot_identifier = ref(SnapshotIdentifier)
    vpc_security_group_ids = [ref(AuroraSecurityGroup)]
    storage_encrypted = True
    deletion_policy = 'Retain'


@cloudformation_dataclass
class AuroraDB:
    """AWS::RDS::DBInstance resource."""

    resource: rds.DBInstance
    db_cluster_identifier = ref(AuroraCluster)
    db_instance_class = 'db.t3.medium'
    db_instance_identifier = 'dms-sample'
    db_subnet_group_name = ref(AuroraDBSubnetGroup)
    engine = 'aurora-postgresql'
    multi_az = False
    publicly_accessible = False
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]
    depends_on = ["AuroraCluster"]
    deletion_policy = 'Retain'


@cloudformation_dataclass
class S3BucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class S3BucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class S3BucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [S3BucketServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = S3BucketBucketEncryption
    public_access_block_configuration = S3BucketPublicAccessBlockConfiguration


@cloudformation_dataclass
class DMSCloudwatchRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class DMSCloudwatchRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSCloudwatchRoleAllowStatement0]


@cloudformation_dataclass
class DMSCloudwatchRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-cloudwatch-logs-role'
    assume_role_policy_document = DMSCloudwatchRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole']
    path = '/'
    condition = 'NotExistsDMSCloudwatchRole'


@cloudformation_dataclass
class DMSVpcRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class DMSVpcRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSVpcRoleAllowStatement0]


@cloudformation_dataclass
class DMSVpcRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-vpc-role'
    assume_role_policy_document = DMSVpcRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole']
    path = '/'
    condition = 'NotExistsDMSVPCRole'


@cloudformation_dataclass
class S3TargetDMSRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class S3TargetDMSRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [S3TargetDMSRoleAllowStatement0]


@cloudformation_dataclass
class S3TargetDMSRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'dms-s3-target-role'
    assume_role_policy_document = S3TargetDMSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'S3AccessForDMSPolicy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Action': [
                        's3:PutObject',
                        's3:DeleteObject',
                    ],
                    'Resource': [
                        get_att(S3Bucket, "Arn"),
                        Sub('${S3Bucket.Arn}/*'),
                    ],
                },
                {
                    'Effect': 'Allow',
                    'Action': 's3:ListBucket',
                    'Resource': get_att(S3Bucket, "Arn"),
                },
            ],
        },
    }]
    depends_on = ["S3Bucket"]


@cloudformation_dataclass
class DMSReplicationSubnetGroup:
    """AWS::DMS::ReplicationSubnetGroup resource."""

    resource: dms.ReplicationSubnetGroup
    replication_subnet_group_description = 'Subnets available for DMS'
    subnet_ids = [ref(DBSubnet1), ref(DBSubnet2)]


@cloudformation_dataclass
class DMSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Security group for DMS Instance'
    group_name = 'DMS Demo Security Group'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class DMSReplicationInstance:
    """AWS::DMS::ReplicationInstance resource."""

    resource: dms.ReplicationInstance
    availability_zone = get_att(DBSubnet1, "AvailabilityZone")
    publicly_accessible = False
    replication_instance_class = 'dms.t3.medium'
    replication_instance_identifier = 'aurora-s3-repinstance-sampledb'
    replication_subnet_group_identifier = ref(DMSReplicationSubnetGroup)
    vpc_security_group_ids = [ref(DMSSecurityGroup)]
    depends_on = ["DMSReplicationSubnetGroup", "DMSSecurityGroup"]


@cloudformation_dataclass
class AuroraSourceEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: dms.Endpoint
    endpoint_type = 'source'
    engine_name = 'AURORA'
    password = '{{resolve:secretsmanager:aurora-source-enpoint-password:SecretString:password}}'
    port = 3306
    server_name = get_att(AuroraCluster, "Endpoint.Address")
    username = 'admin'
    depends_on = ["DMSReplicationInstance", "AuroraCluster", "AuroraDB"]


@cloudformation_dataclass
class S3TargetEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: dms.Endpoint
    endpoint_type = 'target'
    engine_name = 'S3'
    extra_connection_attributes = 'addColumnName=true'
    s3_settings = {
        'BucketName': ref(S3Bucket),
        'ServiceAccessRoleArn': get_att(S3TargetDMSRole, "Arn"),
    }
    depends_on = ["DMSReplicationInstance", "S3Bucket", "S3TargetDMSRole"]


@cloudformation_dataclass
class DMSReplicationTask:
    """AWS::DMS::ReplicationTask resource."""

    resource: dms.ReplicationTask
    migration_type = 'full-load-and-cdc'
    replication_instance_arn = ref(DMSReplicationInstance)
    replication_task_settings = '{ "Logging" : { "EnableLogging" : true, "LogComponents": [ { "Id" : "SOURCE_UNLOAD", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "SOURCE_CAPTURE", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "TARGET_LOAD", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "TARGET_APPLY", "Severity" : "LOGGER_SEVERITY_DEFAULT" } ] } }'
    source_endpoint_arn = ref(AuroraSourceEndpoint)
    table_mappings = '{ "rules": [ { "rule-type" : "selection", "rule-id" : "1", "rule-name" : "1", "object-locator" : { "schema-name" : "dms_sample", "table-name" : "%" }, "rule-action" : "include" } ] }'
    target_endpoint_arn = ref(S3TargetEndpoint)
    depends_on = ["AuroraSourceEndpoint", "S3TargetEndpoint", "DMSReplicationInstance"]
