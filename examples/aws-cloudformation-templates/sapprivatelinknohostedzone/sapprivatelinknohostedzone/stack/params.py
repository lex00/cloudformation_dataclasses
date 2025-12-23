"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainName:
    """The fully qualified or wildcard domain name of DNS"""

    resource: Parameter
    type = STRING
    description = 'The fully qualified or wildcard domain name of DNS'


@cloudformation_dataclass
class VpcId:
    """VpcId of your existing Virtual Private Cloud (VPC) where SAP resides"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'VpcId of your existing Virtual Private Cloud (VPC) where SAP resides'


@cloudformation_dataclass
class Subnets:
    """The private subnets (must include one where SAP resides) of above VPC, recommend choose multiple covering different AZs"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'The private subnets (must include one where SAP resides) of above VPC, recommend choose multiple covering different AZs'


@cloudformation_dataclass
class SecurityGroups:
    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID


@cloudformation_dataclass
class IP:
    """SAP Gateway's private IP address within VPC"""

    resource: Parameter
    type = STRING
    description = "SAP Gateway's private IP address within VPC"


@cloudformation_dataclass
class Protocol:
    """SAP Gateway's connect protocol"""

    resource: Parameter
    type = STRING
    description = "SAP Gateway's connect protocol"
    default = 'HTTP'
    allowed_values = [
    'HTTP',
    'HTTPS',
]


@cloudformation_dataclass
class Port:
    """SAP Gateway's HTTP or HTTPS (match with protocol you choose above) port number"""

    resource: Parameter
    type = NUMBER
    description = "SAP Gateway's HTTP or HTTPS (match with protocol you choose above) port number"
    default = 50000


@cloudformation_dataclass
class HealthCheckPath:
    """SAP Gateway's ping path to do health check"""

    resource: Parameter
    type = STRING
    description = "SAP Gateway's ping path to do health check"
    default = '/sap/public/ping'


@cloudformation_dataclass
class InVpc:
    """Choose Yes if SAP resides in above VPC; choose No otherwise (in cases of above VPC just peers with another SAP residing VPC)"""

    resource: Parameter
    type = STRING
    description = 'Choose Yes if SAP resides in above VPC; choose No otherwise (in cases of above VPC just peers with another SAP residing VPC)'
    default = True
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class IpInVpcCondition:
    resource: Condition
    expression = Equals(ref(InVpc), True)


@cloudformation_dataclass
class SapUseHttpsCondition:
    resource: Condition
    expression = Equals(ref(Protocol), 'HTTPS')
