"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorDomainMembersSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = Sub('${DomainNetBiosName} Domain Members SG via AD Connector')
    vpc_id = ref(VPCID)
    security_group_ingress = [{
        'IpProtocol': '-1',
        'Description': 'LAB - Allow All Private IP Communications',
        'CidrIp': '10.0.0.0/8',
    }, {
        'IpProtocol': '-1',
        'Description': 'LAB - Allow All Private IP Communications',
        'CidrIp': '172.16.0.0/12',
    }, {
        'IpProtocol': '-1',
        'Description': 'LAB - Allow All Private IP Communications',
        'CidrIp': '192.168.0.0/16',
    }]
    security_group_egress = [{
        'Description': 'Allow All Outbound Communications',
        'IpProtocol': '-1',
        'CidrIp': '0.0.0.0/0',
    }]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${DomainNetBiosName}-DomainMembersSG-ADConnector'),
    }]
    condition = 'DomainMembersSGCondition'


@cloudformation_dataclass
class ADConnectorLambdaLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Sub('/aws/lambda/${LambdaFunctionName}')
    retention_in_days = ref(LambdaLogsLogGroupRetention)
    kms_key_id = If("LambdaLogsCloudWatchKMSKeyCondition", ref(LambdaLogsCloudWatchKMSKey), AWS_NO_VALUE)
    deletion_policy = 'Retain'


@cloudformation_dataclass
class ADConnectorServiceAccountSecret:
    """AWS::SecretsManager::Secret resource."""

    resource: secretsmanager.Secret
    name = Sub('ADConnector-ServiceAccount-${DomainNetBiosName}-Domain')
    description = Sub('ADConnector Service Account for ${DomainNetBiosName} Domain')
    secret_string = Sub('{ "username" : "${DomainJoinUser}", "password" : "${DomainJoinUserPassword}" }')
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", ref(SecretsManagerDomainCredentialsSecretsKMSKey), AWS_NO_VALUE)
    deletion_policy = 'Retain'


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class ADConnectorLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0]


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${ADConnectorLambdaLogsLogGroup}')


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${ADConnectorLambdaLogsLogGroup}:log-stream:*')


@cloudformation_dataclass
class ADConnectorLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0_1, ADConnectorLambdaRoleAllowStatement1]


@cloudformation_dataclass
class ADConnectorLambdaRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = ADConnectorLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement0_2:
    resource: PolicyStatement
    sid = 'Directory'
    action = [
        'ds:ConnectDirectory',
        'ds:DeleteDirectory',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement1_1:
    resource: PolicyStatement
    sid = 'CreateAdConnectorEc2Resources'
    action = [
        'ec2:DescribeSubnets',
        'ec2:DescribeVpcs',
        'ec2:CreateSecurityGroup',
        'ec2:CreateNetworkInterface',
        'ec2:DescribeNetworkInterfaces',
        'ec2:AuthorizeSecurityGroupIngress',
        'ec2:AuthorizeSecurityGroupEgress',
        'ec2:CreateTags',
    ]
    resource_arn = '*'
    condition = {
        BOOL: {
            'aws:ViaAWSService': True,
        },
    }


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement2:
    resource: PolicyStatement
    sid = 'DeleteAdConnectorEc2Resources'
    action = [
        'ec2:DeleteSecurityGroup',
        'ec2:DescribeNetworkInterfaces',
        'ec2:DeleteNetworkInterface',
        'ec2:RevokeSecurityGroupIngress',
        'ec2:RevokeSecurityGroupEgress',
        'ec2:DeleteTags',
    ]
    resource_arn = '*'
    condition = {
        BOOL: {
            'aws:ViaAWSService': True,
        },
    }


@cloudformation_dataclass
class ADConnectorLambdaRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0_2, ADConnectorLambdaRoleAllowStatement1_1, ADConnectorLambdaRoleAllowStatement2]


@cloudformation_dataclass
class ADConnectorLambdaRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'ADConnector'
    policy_document = ADConnectorLambdaRolePolicies1PolicyDocument


@cloudformation_dataclass
class ADConnectorLambdaRoleAllowStatement0_3:
    resource: PolicyStatement
    sid = 'GetSecret'
    action = 'secretsmanager:GetSecretValue'
    resource_arn = ref(ADConnectorServiceAccountSecret)


@cloudformation_dataclass
class ADConnectorLambdaRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0_3]


@cloudformation_dataclass
class ADConnectorLambdaRolePolicy2:
    resource: iam.user.Policy
    policy_name = 'ADConnectorServiceAccountSecret'
    policy_document = ADConnectorLambdaRolePolicies2PolicyDocument


@cloudformation_dataclass
class ADConnectorLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = 'Rights to Setup AD Connector'
    assume_role_policy_document = ADConnectorLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [ADConnectorLambdaRolePolicy, ADConnectorLambdaRolePolicy1, ADConnectorLambdaRolePolicy2, If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", {
    Policy.policy_name: 'KMSKeyForSecret',
    Policy.policy_document: {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': 'kms:Decrypt',
            'Resource': ref(SecretsManagerDomainCredentialsSecretsKMSKey),
        }],
    },
}, AWS_NO_VALUE)]


@cloudformation_dataclass
class ADConnectorLambdaFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class ADConnectorLambdaFunctionContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class ADConnectorLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.capacity_provider.CapacityProviderVpcConfig
    subnet_ids = ['PrivateSubnet1ID', 'PrivateSubnet2ID']
    security_group_ids = [ref(ADConnectorDomainMembersSG)]


@cloudformation_dataclass
class ADConnectorLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = ref(LambdaFunctionName)
    handler = 'adconnector_custom_resource.lambda_handler'
    role = get_att(ADConnectorLambdaRole, "Arn")
    runtime = 'python3.8'
    memory_size = 128
    timeout = 120
    environment = ADConnectorLambdaFunctionEnvironment
    code = ADConnectorLambdaFunctionContent
    vpc_config = ADConnectorLambdaFunctionCapacityProviderVpcConfig


@cloudformation_dataclass
class ADConnectorResource:
    """Custom::ADConnectorResource resource."""

    # Unknown resource type: Custom::ADConnectorResource
    resource: CloudFormationResource
    service_token = get_att(ADConnectorLambdaFunction, "Arn")
    adconnector_description = ref(ADConnectorDescription)
    adconnector_size = ref(ADConnectorSize)
    adconnector_subnet_id1 = ref(PrivateSubnet1ID)
    adconnector_subnet_id2 = ref(PrivateSubnet2ID)
    adconnector_vpcid = ref(VPCID)
    domain_dns_name = ref(DomainDNSName)
    domain_dns_servers = ref(DomainDNSServers)
    domain_netbios_name = ref(DomainNetBiosName)
    domain_join_secret_id = ref(ADConnectorServiceAccountSecret)


@cloudformation_dataclass
class ADConnectorLinuxEC2SeamlessDomainJoinSecret:
    """AWS::SecretsManager::Secret resource."""

    resource: secretsmanager.Secret
    name = Sub('aws/directory-services/${ADConnectorResource}/seamless-domain-join')
    description = Sub('AD Credentials for Seamless Domain Join Windows/Linux EC2 instances to ${DomainNetBiosName} Domain via AD Connector')
    secret_string = Sub('{ "awsSeamlessDomainUsername" : "${DomainJoinUser}", "awsSeamlessDomainPassword" : "${DomainJoinUserPassword}" }')
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", ref(SecretsManagerDomainCredentialsSecretsKMSKey), AWS_NO_VALUE)
    condition = 'LinuxEC2DomainJoinResourcesCondition'
    deletion_policy = 'Retain'


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLinuxEC2DomainJoinRoleAllowStatement0]


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 's3:GetObject'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-windows-downloads-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-packages-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::Region}-birdwatcher-prod/*'),
        Sub('arn:${AWS::Partition}:s3:::patch-baseline-snapshot-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-distributor-file-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-document-attachments-${AWS::Region}/*'),
    ]


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1]


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRolePolicy:
    resource: iam.user.Policy
    policy_name = 'SSMAgent'
    policy_document = ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2:
    resource: PolicyStatement
    action = [
        'secretsmanager:GetSecretValue',
        'secretsmanager:DescribeSecret',
    ]
    resource_arn = ref(ADConnectorLinuxEC2SeamlessDomainJoinSecret)


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2]


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'ADConnectorLinuxEC2SeamlessDomainJoinSecret'
    policy_document = ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${DomainNetBiosName}-LinuxEC2DomainJoinRole-ADConnector')
    description = Sub('IAM Role to Seamlessly Join Linux EC2 Instances to ${DomainNetBiosName} Domain via AD Connector')
    assume_role_policy_document = ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMDirectoryServiceAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [ADConnectorLinuxEC2DomainJoinRolePolicy, If("SSMLogsBucketNameCondition", {
    Policy.policy_name: 'SsmLogs',
    Policy.policy_document: {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': [
                's3:GetObject',
                's3:PutObject',
                's3:PutObjectAcl',
                's3:GetEncryptionConfiguration',
            ],
            'Resource': [
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}'),
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}/*'),
            ],
        }],
    },
}, AWS_NO_VALUE), ADConnectorLinuxEC2DomainJoinRolePolicy1, If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", {
    Policy.policy_name: 'KMSKeyForSecret',
    Policy.policy_document: {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': 'kms:Decrypt',
            'Resource': ref(SecretsManagerDomainCredentialsSecretsKMSKey),
        }],
    },
}, AWS_NO_VALUE)]
    condition = 'LinuxEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    instance_profile_name = ref(ADConnectorLinuxEC2DomainJoinRole)
    path = '/'
    roles = [ref(ADConnectorLinuxEC2DomainJoinRole)]
    condition = 'LinuxEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorWindowsEC2DomainJoinRoleAllowStatement0]


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 's3:GetObject'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-windows-downloads-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-packages-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::Region}-birdwatcher-prod/*'),
        Sub('arn:${AWS::Partition}:s3:::patch-baseline-snapshot-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-distributor-file-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-document-attachments-${AWS::Region}/*'),
    ]


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1]


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinRolePolicy:
    resource: iam.user.Policy
    policy_name = 'SSMAgent'
    policy_document = ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${DomainNetBiosName}-ADConnector-WindowsEC2DomainJoinRole')
    description = Sub('IAM Role to Seamlessly Join Windows EC2 Instances to ${DomainDNSName} Domain via AD Connector')
    assume_role_policy_document = ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMDirectoryServiceAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [ADConnectorWindowsEC2DomainJoinRolePolicy, If("SSMLogsBucketNameCondition", {
    Policy.policy_name: 'SsmLogs',
    Policy.policy_document: {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': [
                's3:GetObject',
                's3:PutObject',
                's3:PutObjectAcl',
                's3:GetEncryptionConfiguration',
            ],
            'Resource': [
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}'),
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}/*'),
            ],
        }],
    },
}, AWS_NO_VALUE)]
    condition = 'WindowsEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    instance_profile_name = ref(ADConnectorWindowsEC2DomainJoinRole)
    path = '/'
    roles = [ref(ADConnectorWindowsEC2DomainJoinRole)]
    condition = 'WindowsEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class DHCPOptions:
    """AWS::EC2::DHCPOptions resource."""

    resource: ec2.DHCPOptions
    domain_name = ref(DomainDNSName)
    domain_name_servers = [ref(DomainDNSServers)]
    tags = [{
        'Key': 'Name',
        'Value': ref(DomainDNSName),
    }]
    condition = 'DHCPOptionSetCondition'


@cloudformation_dataclass
class DHCPOptionsVPCAssociation:
    """AWS::EC2::VPCDHCPOptionsAssociation resource."""

    resource: ec2.VPCDHCPOptionsAssociation
    vpc_id = ref(VPCID)
    dhcp_options_id = ref(DHCPOptions)
    condition = 'DHCPOptionSetCondition'
