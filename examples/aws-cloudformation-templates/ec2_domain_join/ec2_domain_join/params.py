"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AMI:
    """Windows 2016 AMI available in your region"""

    resource: Parameter
    type = ParameterType.AWS_EC2_IMAGE_ID
    description = 'Windows 2016 AMI available in your region'


@cloudformation_dataclass
class KeyPair:
    """KeyPair for EC2 Instance"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'KeyPair for EC2 Instance'


@cloudformation_dataclass
class PublicSubnet:
    """Subnet to place instance in"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
    description = 'Subnet to place instance in'


@cloudformation_dataclass
class VPC:
    """VPC to place instance in"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'VPC to place instance in'


@cloudformation_dataclass
class InstanceType:
    resource: Parameter
    type = STRING
    default = 't2.small'
    allowed_values = [
    't1.micro',
    't2.micro',
    't2.small',
    't2.medium',
    'm1.small',
    'm1.medium',
    'm1.large',
    'm1.xlarge',
    'm2.xlarge',
    'm2.2xlarge',
    'm2.4xlarge',
    'm3.medium',
    'm3.large',
    'm3.xlarge',
    'm3.2xlarge',
    'c1.medium',
    'c1.xlarge',
    'c3.large',
    'c3.xlarge',
    'c3.2xlarge',
    'c3.4xlarge',
    'c3.8xlarge',
    'c4.large',
    'c4.xlarge',
    'c4.2xlarge',
    'c4.4xlarge',
    'c4.8xlarge',
    'g2.2xlarge',
    'r3.large',
    'r3.xlarge',
    'r3.2xlarge',
    'r3.4xlarge',
    'r3.8xlarge',
    'i2.xlarge',
    'i2.2xlarge',
    'i2.4xlarge',
    'i2.8xlarge',
    'd2.xlarge',
    'd2.2xlarge',
    'd2.4xlarge',
    'd2.8xlarge',
    'hs1.8xlarge',
    'cr1.8xlarge',
    'cc2.8xlarge',
]
    constraint_description = 'Must be a valid EC2 instance type.'


@cloudformation_dataclass
class ADDirectoryId:
    """Active DirectoryId. Eg. d-12345679a"""

    resource: Parameter
    type = STRING
    description = 'Active DirectoryId. Eg. d-12345679a'


@cloudformation_dataclass
class ADDirectoryName:
    """Active Directory Name. Eg. my.ad.com"""

    resource: Parameter
    type = STRING
    description = 'Active Directory Name. Eg. my.ad.com'


@cloudformation_dataclass
class ADDnsIpAddresses1:
    """Active Directory DNS 1. Eg. 10.0.0.142"""

    resource: Parameter
    type = STRING
    description = 'Active Directory DNS 1. Eg. 10.0.0.142'


@cloudformation_dataclass
class ADDnsIpAddresses2:
    """Active Directory DNS 2. Eg. 10.0.0.143"""

    resource: Parameter
    type = STRING
    description = 'Active Directory DNS 2. Eg. 10.0.0.143'
