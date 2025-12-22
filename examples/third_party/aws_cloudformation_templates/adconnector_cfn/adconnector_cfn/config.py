"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorDescription:
    """Description for the directory"""

    resource: Parameter
    type = STRING
    description = 'Description for the directory'
    default = 'On-premises AD'
    allowed_pattern = '^[A-Za-z0-9][\\w@#%*+=:?.\\/! -]*$'
    max_length = 128


@cloudformation_dataclass
class ADConnectorSize:
    """Size of the directory"""

    resource: Parameter
    type = STRING
    description = 'Size of the directory'
    default = 'Small'
    allowed_values = [
    'Small',
    'Large',
]


@cloudformation_dataclass
class CreateDHCPOptionSet:
    """Create DHCP Option Set"""

    resource: Parameter
    type = STRING
    description = 'Create DHCP Option Set'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class CreateADConnectorDomainMembersSG:
    """Create Domain Members Security Group. Note, using allow any type rules, restrict accordingly."""

    resource: Parameter
    type = STRING
    description = 'Create Domain Members Security Group. Note, using allow any type rules, restrict accordingly.'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class CreateLinuxEC2DomainJoinResources:
    """Create AWS resources (IAM role, instance profile, & secret) to support seamless domain join Linux EC2 instances"""

    resource: Parameter
    type = STRING
    description = 'Create AWS resources (IAM role, instance profile, & secret) to support seamless domain join Linux EC2 instances'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class CreateWindowsEC2DomainJoinResources:
    """Create AWS resources (IAM role & instnace profile)to support seamless domain join Windows EC2 instances"""

    resource: Parameter
    type = STRING
    description = 'Create AWS resources (IAM role & instnace profile)to support seamless domain join Windows EC2 instances'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class DomainDNSName:
    """Fully qualified name of the on-premises directory, such as corp.example.com"""

    resource: Parameter
    type = STRING
    description = 'Fully qualified name of the on-premises directory, such as corp.example.com'
    allowed_pattern = '[a-zA-Z0-9-]+\\..+'
    min_length = 3
    max_length = 25


@cloudformation_dataclass
class DomainDNSServers:
    """DNS or domain controller servers for the on-premises directory."""

    resource: Parameter
    type = STRING
    description = 'DNS or domain controller servers for the on-premises directory.'
    allowed_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(,|, ))*(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    constraint_description = 'Must be in the form of IP address. Additional IP addresses can be provided, separated by a "comma". (e.g., 10.1.1.1,10.2.2.2) Additional IP addresses can be provided, separated by a "comma".'


@cloudformation_dataclass
class DomainNetBiosName:
    """Short name of your existing directory, such as CORP"""

    resource: Parameter
    type = STRING
    description = 'Short name of your existing directory, such as CORP'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


@cloudformation_dataclass
class DomainJoinUser:
    """Username of a user in the existing directory"""

    resource: Parameter
    type = STRING
    description = 'Username of a user in the existing directory'
    allowed_pattern = '[a-zA-Z0-9]*'
    min_length = 5
    max_length = 25


@cloudformation_dataclass
class DomainJoinUserPassword:
    """Password for the existing user account"""

    resource: Parameter
    type = STRING
    description = 'Password for the existing user account'
    allowed_pattern = '(?=^.{6,255}$)((?=.*\\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\\d)(?=.*[^A-Za-z0-9])(?=.*[a-z])|(?=.*[^A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])|(?=.*\\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9]))^.*'
    min_length = 8
    max_length = 32
    no_echo = True


@cloudformation_dataclass
class LambdaFunctionName:
    """Lambda Function Name for Custom Resource."""

    resource: Parameter
    type = STRING
    description = 'Lambda Function Name for Custom Resource.'
    default = 'CR-ADConnector'
    allowed_pattern = '^[\\w-]{1,64}$'
    constraint_description = 'Max 64 alphanumeric characters. Also special characters supported [_, -]'


@cloudformation_dataclass
class LambdaLogLevel:
    """Lambda logging level"""

    resource: Parameter
    type = STRING
    description = 'Lambda logging level'
    default = 'INFO'
    allowed_values = [
    'INFO',
    'DEBUG',
]


@cloudformation_dataclass
class LambdaLogsLogGroupRetention:
    """Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs"""

    resource: Parameter
    type = STRING
    description = 'Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs'
    default = 14
    allowed_values = [
    1,
    3,
    5,
    7,
    14,
    30,
    60,
    90,
    120,
    150,
    180,
    365,
    400,
    545,
    731,
    1827,
    3653,
]


@cloudformation_dataclass
class LambdaLogsCloudWatchKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*){1}:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class LambdaS3BucketName:
    """Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    resource: Parameter
    type = STRING
    description = 'Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'Lambda S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class LambdaZipFileName:
    """Amazon S3 key of the deployment package."""

    resource: Parameter
    type = STRING
    description = 'Amazon S3 key of the deployment package.'
    default = 'adconnector_custom_resource.zip'
    min_length = 1
    max_length = 1024


@cloudformation_dataclass
class PrivateSubnet1ID:
    """ID of the private subnet 1 in Availability Zone 1 (e.g., subnet-a0246dcd)"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
    description = 'ID of the private subnet 1 in Availability Zone 1 (e.g., subnet-a0246dcd)'


@cloudformation_dataclass
class PrivateSubnet2ID:
    """ID of the private subnet 2 in Availability Zone 2 (e.g., subnet-a0246dcd)"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
    description = 'ID of the private subnet 2 in Availability Zone 2 (e.g., subnet-a0246dcd)'


@cloudformation_dataclass
class SecretsManagerDomainCredentialsSecretsKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the SecretsManager domain credentials secret. If empty, encryption is enabled with SecretsManager managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the SecretsManager domain credentials secret. If empty, encryption is enabled with SecretsManager managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class SSMLogsBucketName:
    """(Optional) SSM Logs bucket name for where Systems Manager logs should store log files. SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    resource: Parameter
    type = STRING
    description = '(Optional) SSM Logs bucket name for where Systems Manager logs should store log files. SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    default = ''
    allowed_pattern = '^$|(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class VPCID:
    """ID of the VPC (e.g., vpc-0343606e)"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'ID of the VPC (e.g., vpc-0343606e)'


@cloudformation_dataclass
class DHCPOptionSetConditionCondition:
    resource: Condition
    expression = Equals(ref(CreateDHCPOptionSet), True)


@cloudformation_dataclass
class DomainMembersSGConditionCondition:
    resource: Condition
    expression = Equals(ref(CreateADConnectorDomainMembersSG), True)


@cloudformation_dataclass
class LambdaLogsCloudWatchKMSKeyConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(LambdaLogsCloudWatchKMSKey), ''))


@cloudformation_dataclass
class LinuxEC2DomainJoinResourcesConditionCondition:
    resource: Condition
    expression = Equals(ref(CreateLinuxEC2DomainJoinResources), True)


@cloudformation_dataclass
class SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(SecretsManagerDomainCredentialsSecretsKMSKey), ''))


@cloudformation_dataclass
class SSMLogsBucketNameConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(SSMLogsBucketName), ''))


@cloudformation_dataclass
class WindowsEC2DomainJoinResourcesConditionCondition:
    resource: Condition
    expression = Equals(ref(CreateWindowsEC2DomainJoinResources), True)
