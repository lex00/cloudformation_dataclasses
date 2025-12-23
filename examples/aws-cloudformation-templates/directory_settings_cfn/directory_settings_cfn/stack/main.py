"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ds.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0]


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessEC2ReadOnlyRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    description = 'IAM Role for Directory Service \'AWS Management Console\' Delegated Access for "EC2 ReadOnly"'
    assume_role_policy_document = DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ReadOnlyAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    condition = 'DirectoryConsoleDelegatedAccessRolesCondition'


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ds.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0]


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessSecurityAuditRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    description = 'IAM Role for Directory Service \'AWS Management Console\' Delegated Access for "Security Audit"'
    assume_role_policy_document = DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/SecurityAudit')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    condition = 'DirectoryConsoleDelegatedAccessRolesCondition'


@cloudformation_dataclass
class DirectoryMonitoringTopicSubscription:
    resource: sns.topic.Subscription
    endpoint = ref(DirectoryMonitoringEmail)
    protocol = 'email'


@cloudformation_dataclass
class DirectoryMonitoringTopic:
    """AWS::SNS::Topic resource."""

    resource: sns.Topic
    kms_master_key_id = If("DirectoryMonitoringSNSTopicKMSKeyCondition", ref(DirectoryMonitoringSNSTopicKMSKey), 'aws/sns')
    subscription = [DirectoryMonitoringTopicSubscription]
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }, {
        'Key': 'DirectoryID',
        'Value': ref(DirectoryID),
    }]


@cloudformation_dataclass
class DirectorySettingsLambdaLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Sub('/aws/lambda/${LambdaFunctionName}')
    retention_in_days = ref(LambdaLogsLogGroupRetention)
    kms_key_id = If("LambdaLogsCloudWatchKMSKeyCondition", ref(LambdaLogsCloudWatchKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectorySettingsLambdaRoleAllowStatement0]


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${DirectorySettingsLambdaLogsLogGroup}')


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${DirectorySettingsLambdaLogsLogGroup}:log-stream:*')


@cloudformation_dataclass
class DirectorySettingsLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [DirectorySettingsLambdaRoleAllowStatement0_1, DirectorySettingsLambdaRoleAllowStatement1]


@cloudformation_dataclass
class DirectorySettingsLambdaRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = DirectorySettingsLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAllowStatement0_2:
    resource: PolicyStatement
    sid = 'SnsTopic'
    action = [
        'ds:RegisterEventTopic',
        'ds:DeregisterEventTopic',
        'ds:DescribeEventTopics',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ds:${AWS::Region}:${AWS::AccountId}:directory/${DirectoryID}')


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAllowStatement1_1:
    resource: PolicyStatement
    sid = 'DescribeDirectories'
    action = 'ds:DescribeDirectories'
    resource_arn = '*'


@cloudformation_dataclass
class DirectorySettingsLambdaRoleAllowStatement2:
    resource: PolicyStatement
    sid = 'AliasSso'
    action = [
        'ds:CreateAlias',
        'ds:EnableSso',
        'ds:DisableSso',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ds:${AWS::Region}:${AWS::AccountId}:directory/${DirectoryID}')


@cloudformation_dataclass
class DirectorySettingsLambdaRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [DirectorySettingsLambdaRoleAllowStatement0_2, DirectorySettingsLambdaRoleAllowStatement1_1, DirectorySettingsLambdaRoleAllowStatement2]


@cloudformation_dataclass
class DirectorySettingsLambdaRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'DirectorySettings'
    policy_document = DirectorySettingsLambdaRolePolicies1PolicyDocument


@cloudformation_dataclass
class DirectorySettingsLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = Sub('Rights to Setup Directory Settings for Directory ID, ${DirectoryID}')
    assume_role_policy_document = DirectorySettingsLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [DirectorySettingsLambdaRolePolicy, DirectorySettingsLambdaRolePolicy1]


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.capacity_provider.CapacityProviderVpcConfig
    subnet_ids = ref(Subnets)
    security_group_ids = ref(SecurityGroups)


@cloudformation_dataclass
class DirectorySettingsLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = ref(LambdaFunctionName)
    handler = 'directory_settings_custom_resource.lambda_handler'
    role = get_att(DirectorySettingsLambdaRole, "Arn")
    runtime = 'python3.12'
    memory_size = 128
    timeout = 120
    environment = DirectorySettingsLambdaFunctionEnvironment
    code = DirectorySettingsLambdaFunctionContent
    vpc_config = DirectorySettingsLambdaFunctionCapacityProviderVpcConfig


@cloudformation_dataclass
class DirectorySettingsResource:
    """Custom::DirectorySettingsResource resource."""

    # Unknown resource type: Custom::DirectorySettingsResource
    resource: CloudFormationResource
    service_token = get_att(DirectorySettingsLambdaFunction, "Arn")
    directory_id = ref(DirectoryID)
    create_directory_alias = ref(CreateDirectoryAlias)
    enable_directory_sso = ref(EnableDirectorySSO)
    directory_alias = ref(DirectoryAlias)
    directory_monitoring_topic_name = get_att(DirectoryMonitoringTopic, "TopicName")
