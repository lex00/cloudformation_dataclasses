"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADDomainDNSName:
    """Fully qualified domain name for the AWS Managed Microsoft AD directory, such as corp.example.com."""

    resource: Parameter
    type = STRING
    description = 'Fully qualified domain name for the AWS Managed Microsoft AD directory, such as corp.example.com.'
    default = 'awsmad.lab'
    allowed_pattern = '[a-zA-Z0-9-]+\\..+'


@cloudformation_dataclass
class AWSManagedADDomainNetBiosName:
    """NetBIOS name for your domain, such as CORP."""

    resource: Parameter
    type = STRING
    description = 'NetBIOS name for your domain, such as CORP.'
    default = 'AWSMAD'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


@cloudformation_dataclass
class AWSManagedADEdition:
    """AWS Managed AD Edition. Standard supports up to 30,000+ directory objects. Enterprise supports up to 500,000+ directory objects."""

    resource: Parameter
    type = STRING
    description = 'AWS Managed AD Edition. Standard supports up to 30,000+ directory objects. Enterprise supports up to 500,000+ directory objects.'
    default = 'Standard'
    allowed_values = [
    'Standard',
    'Enterprise',
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
class CreateDomainMembersSG:
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
    expression = Equals(ref(CreateDomainMembersSG), True)


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
