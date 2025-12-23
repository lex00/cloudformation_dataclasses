"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AMAZONLINUX2:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-ebs'


@cloudformation_dataclass
class DirectoryID:
    """Directory ID"""

    resource: Parameter
    type = STRING
    description = 'Directory ID'
    allowed_pattern = '^d-[0-9a-f]{10}$'


@cloudformation_dataclass
class DirectoryName:
    """Fully qualified name of the on-premises directory, such as corp.example.com"""

    resource: Parameter
    type = STRING
    description = 'Fully qualified name of the on-premises directory, such as corp.example.com'
    allowed_pattern = '[a-zA-Z0-9-]+\\..+'
    min_length = 3
    max_length = 25


@cloudformation_dataclass
class DomainDNSServer1:
    """(Optional) Domain DNS Server 1. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    resource: Parameter
    type = STRING
    description = '(Optional) Domain DNS Server 1. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


@cloudformation_dataclass
class DomainDNSServer2:
    """(Optional) Domain DNS Server 2. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    resource: Parameter
    type = STRING
    description = '(Optional) Domain DNS Server 2. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


@cloudformation_dataclass
class DomainDNSServer3:
    """(Optional) Domain DNS Server 3. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    resource: Parameter
    type = STRING
    description = '(Optional) Domain DNS Server 3. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


@cloudformation_dataclass
class DomainDNSServer4:
    """(Optional) Domain DNS Server 4. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    resource: Parameter
    type = STRING
    description = '(Optional) Domain DNS Server 4. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


@cloudformation_dataclass
class DomainMember1NetBIOSName:
    """NetBIOS name of Domain Member 1 (using inline SSM association). Note, if computer name existed in AD before, delete from AD first."""

    resource: Parameter
    type = STRING
    description = 'NetBIOS name of Domain Member 1 (using inline SSM association). Note, if computer name existed in AD before, delete from AD first.'
    default = 'SERVER1'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


@cloudformation_dataclass
class DomainMember2NetBIOSName:
    """NetBIOS name of Domain Member 2 (using SSM association via instance id). Note, if computer name existed in AD before, delete from AD first."""

    resource: Parameter
    type = STRING
    description = 'NetBIOS name of Domain Member 2 (using SSM association via instance id). Note, if computer name existed in AD before, delete from AD first.'
    default = 'SERVER2'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


@cloudformation_dataclass
class DomainMember3NetBIOSName:
    """NetBIOS name of Domain Member 3 (using SSM association via tag). Note, if computer name existed in AD before, delete from AD first."""

    resource: Parameter
    type = STRING
    description = 'NetBIOS name of Domain Member 3 (using SSM association via tag). Note, if computer name existed in AD before, delete from AD first.'
    default = 'SERVER3'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


@cloudformation_dataclass
class DomainMember4NetBIOSName:
    """NetBIOS name of Domain Member 4 (AmazonLinux2)"""

    resource: Parameter
    type = STRING
    description = 'NetBIOS name of Domain Member 4 (AmazonLinux2)'
    default = 'SERVER4'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


@cloudformation_dataclass
class DomainMembersInstanceType:
    """Amazon EC2 instance type for the AD Server instances"""

    resource: Parameter
    type = STRING
    description = 'Amazon EC2 instance type for the AD Server instances'
    default = 't3.medium'
    allowed_values = [
    't3.medium',
    't3.large',
]


@cloudformation_dataclass
class DomainMembersLinuxInstanceProfile:
    """Existing IAM InstanceProfile with Linux EC2 seamless join domain rights"""

    resource: Parameter
    type = STRING
    description = 'Existing IAM InstanceProfile with Linux EC2 seamless join domain rights'
    allowed_pattern = '[\\w+=,.@-]+'


@cloudformation_dataclass
class DomainMembersWindowsInstanceProfile:
    """Existing IAM InstanceProfile with Windows EC2 seamless join domain rights"""

    resource: Parameter
    type = STRING
    description = 'Existing IAM InstanceProfile with Windows EC2 seamless join domain rights'
    allowed_pattern = '[\\w+=,.@-]+'


@cloudformation_dataclass
class DomainMembersSGID:
    """Security Group ID for Domain Members Security Group"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SECURITY_GROUP_ID
    description = 'Security Group ID for Domain Members Security Group'


@cloudformation_dataclass
class EBSKMSKey:
    """(Optional) KMS Alias, Key ID, Key ID ARN or Alias ARN to use for encrypting the EBS volumes. If empty, the default key for EBS encryption will be used of `alias/aws/ebs` or the CMK set as the default EBS encryption key."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Alias, Key ID, Key ID ARN or Alias ARN to use for encrypting the EBS volumes. If empty, the default key for EBS encryption will be used of `alias/aws/ebs` or the CMK set as the default EBS encryption key.'
    allowed_pattern = '^$|(^alias/[a-zA-Z0-9/-]{1,256}$)|(^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$)|(^arn:(aws[a-z-]*)?:kms:.*:\\d{12}:key/[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$)|(^arn:(aws[a-z-]*)?:kms:.*:\\d{12}:alias/[a-zA-Z0-9/-]{1,256}$)'


@cloudformation_dataclass
class KeyPairName:
    """KeyPair for ONPREMISES INSTANCES"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'KeyPair for ONPREMISES INSTANCES'


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
class SSMLogsBucketName:
    """(Optional) SSM Logs bucket name for where Systems Manager logs should store log files. SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    resource: Parameter
    type = STRING
    description = '(Optional) SSM Logs bucket name for where Systems Manager logs should store log files. SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '^$|(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class WINFULLBASE:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-windows-latest/Windows_Server-2019-English-Full-Base'


@cloudformation_dataclass
class DomainDNSServer1ConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(DomainDNSServer1), ''))


@cloudformation_dataclass
class DomainDNSServer2ConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(DomainDNSServer2), ''))


@cloudformation_dataclass
class DomainDNSServer3ConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(DomainDNSServer3), ''))


@cloudformation_dataclass
class DomainDNSServer4ConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(DomainDNSServer4), ''))


@cloudformation_dataclass
class DomainDNSServersConditionCondition:
    resource: Condition
    expression = Or(conditions=[Condition("DomainDNSServer1Condition"), Condition("DomainDNSServer2Condition"), Condition("DomainDNSServer3Condition"), Condition("DomainDNSServer4Condition")])


@cloudformation_dataclass
class EBSKMSKeyConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(EBSKMSKey), ''))


@cloudformation_dataclass
class SSMLogsBucketConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(SSMLogsBucketName), ''))
