"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainName:
    """FQDN of the domain for this directory"""

    resource: Parameter
    type = STRING
    description = 'FQDN of the domain for this directory'
    default = 'corp.example.com'


@cloudformation_dataclass
class SimpleADShortName:
    """Netbios name of the domain for this directory"""

    resource: Parameter
    type = STRING
    description = 'Netbios name of the domain for this directory'
    default = 'corp'


@cloudformation_dataclass
class CreateAlias:
    """Only required for applications which need a URL to connect to the directory"""

    resource: Parameter
    type = STRING
    description = 'Only required for applications which need a URL to connect to the directory'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


@cloudformation_dataclass
class PrivateSubnet1:
    """Subnet to be used for the Directoty"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'Subnet to be used for the Directoty'


@cloudformation_dataclass
class PrivateSubnet2:
    """Subnet to be used for the Directoty"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'Subnet to be used for the Directoty'


@cloudformation_dataclass
class VPCID:
    """The VPC the directory will be created in"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_VPC_ID
    description = 'The VPC the directory will be created in'


@cloudformation_dataclass
class Size:
    """Size of the Simple AD"""

    resource: Parameter
    type = STRING
    description = 'Size of the Simple AD'
    default = 'Small'
    allowed_values = [
    'Small',
    'Large',
]


@cloudformation_dataclass
class AliasCondition:
    resource: Condition
    expression = Equals(ref(CreateAlias), 'true')
