"""DirectorySettingsLambdaRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


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
    resource: iam.Policy
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
    resource: iam.Policy
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
