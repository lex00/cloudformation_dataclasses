"""AWSManagedADWindowsEC2DomainJoinRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADWindowsEC2DomainJoinRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class AWSManagedADWindowsEC2DomainJoinRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AWSManagedADWindowsEC2DomainJoinRoleAllowStatement0]


@cloudformation_dataclass
class AWSManagedADWindowsEC2DomainJoinRoleAllowStatement0_1:
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
class AWSManagedADWindowsEC2DomainJoinRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AWSManagedADWindowsEC2DomainJoinRoleAllowStatement0_1]


@cloudformation_dataclass
class AWSManagedADWindowsEC2DomainJoinRolePolicy:
    resource: iam.Policy
    policy_name = 'SSMAgent'
    policy_document = AWSManagedADWindowsEC2DomainJoinRolePolicies0PolicyDocument


@cloudformation_dataclass
class AWSManagedADWindowsEC2DomainJoinRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${AWSManagedADDomainNetBiosName}-AWSManagedAD-WindowsEC2DomainJoinRole')
    description = Sub('IAM Role to Seamlessly Join Windows EC2 Instances to ${AWSManagedADDomainDNSName} Domain via AWS Managed Microsoft AD')
    assume_role_policy_document = AWSManagedADWindowsEC2DomainJoinRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMDirectoryServiceAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [AWSManagedADWindowsEC2DomainJoinRolePolicy, If("SSMLogsBucketNameCondition", {
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
