"""
EIP with Association.

Inspired by AWS's EC2/EIP_With_Association.json template.
Demonstrates:
- EIP (Elastic IP) resource creation
- EIPAssociation linking EIP to instance
- GetAtt for AllocationId
- Base64 + Join for UserData
"""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


# =============================================================================
# Parameters
# =============================================================================


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair for SSH access."""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = "Name of an existing EC2 KeyPair to enable SSH access to the instances"
    constraint_description = "must be the name of an existing EC2 KeyPair."


@cloudformation_dataclass
class InstanceTypeParam:
    """EC2 instance type with allowed values."""

    resource: Parameter
    type = STRING
    description = "WebServer EC2 instance type"
    default = "t3.small"
    allowed_values = [
        "t2.nano",
        "t2.micro",
        "t2.small",
        "t2.medium",
        "t2.large",
        "t3.nano",
        "t3.micro",
        "t3.small",
        "t3.medium",
        "t3.large",
        "m5.large",
        "m5.xlarge",
    ]
    constraint_description = "must be a valid EC2 instance type."


@cloudformation_dataclass
class SSHLocation:
    """IP address range for SSH access."""

    resource: Parameter
    type = STRING
    description = "The IP address range that can be used to SSH to the EC2 instances"
    default = "0.0.0.0/0"
    min_length = 9
    max_length = 18
    allowed_pattern = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})"
    constraint_description = "must be a valid IP CIDR range of the form x.x.x.x/x."


@cloudformation_dataclass
class LatestAmiId:
    """SSM Parameter for latest Amazon Linux 2 AMI."""

    resource: Parameter
    type = "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"
    default = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"


@cloudformation_dataclass
class Subnets:
    """List of subnets to deploy into."""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = "List of subnets to deploy the instance into"


# =============================================================================
# Security Group
# =============================================================================


@cloudformation_dataclass
class SSHIngress:
    """Ingress rule for SSH access."""

    resource: Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 22
    to_port = 22
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """Security group enabling SSH access."""

    resource: SecurityGroup
    group_description = "Enable SSH access"
    security_group_ingress = [SSHIngress]


# =============================================================================
# Elastic IP
# =============================================================================


@cloudformation_dataclass
class IPAddress:
    """Elastic IP address."""

    resource: EIP


# =============================================================================
# EC2 Instance
# =============================================================================


def first_subnet():
    """Select first subnet from parameter list."""
    return Select(0, ref(Subnets))


def user_data():
    """Generate UserData that displays the EIP address."""
    return Base64(Join("", ["IPAddress=", ref(IPAddress)]))


@cloudformation_dataclass
class EC2Instance:
    """
    EC2 instance with Elastic IP.

    UserData script displays the assigned Elastic IP.
    """

    resource: Instance
    user_data = user_data()
    instance_type = ref(InstanceTypeParam)
    subnet_id = first_subnet()
    security_groups = [ref(InstanceSecurityGroup)]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)


# =============================================================================
# EIP Association
# =============================================================================


@cloudformation_dataclass
class IPAssoc:
    """Associate Elastic IP with EC2 instance."""

    resource: EIPAssociation
    instance_id = ref(EC2Instance)
    allocation_id = get_att(IPAddress, "AllocationId")


# =============================================================================
# Outputs
# =============================================================================


@cloudformation_dataclass
class InstanceIdOutput:
    """Instance ID output."""

    resource: Output
    value = ref(EC2Instance)
    description = "InstanceId of the newly created EC2 instance"


@cloudformation_dataclass
class InstanceIPAddressOutput:
    """Elastic IP address output."""

    resource: Output
    value = ref(IPAddress)
    description = "IP address of the newly created EC2 instance"


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class EIPWithAssociationTemplate:
    """
    EIP with Association template.

    Creates an EC2 instance and associates an Elastic IP address with it.
    Demonstrates how to link an EIP to an instance using EIPAssociation.
    """

    resource: Template
    description = (
        "AWS CloudFormation Sample Template: This template shows how to associate "
        "an Elastic IP address with an Amazon EC2 instance."
    )
    parameters = [KeyName, InstanceTypeParam, SSHLocation, LatestAmiId, Subnets]
    resources = [InstanceSecurityGroup, IPAddress, EC2Instance, IPAssoc]
    outputs = [InstanceIdOutput, InstanceIPAddressOutput]


def build_template() -> Template:
    """Build the EIP with association template."""
    return EIPWithAssociationTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
