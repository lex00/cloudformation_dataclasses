"""ADConnectorLambdaRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


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

    resource: Role
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
