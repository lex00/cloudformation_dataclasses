"""ADConnectorLinuxEC2DomainJoinRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


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

    resource: Role
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
