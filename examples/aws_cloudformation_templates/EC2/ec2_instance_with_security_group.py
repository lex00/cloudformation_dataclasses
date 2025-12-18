"""
EC2 Instance with Security Group.

Inspired by AWS's EC2/EC2InstanceWithSecurityGroupSample.json template.
Demonstrates:
- Parameters with AllowedValues and constraints
- SSM Parameter reference for latest AMI
- SecurityGroup with Ingress rules
- EC2 Instance referencing security group
- GetAtt for outputs (PublicIp, AvailabilityZone, PublicDnsName)
- Select intrinsic for subnet selection
"""

from . import *  # noqa: F403


# =============================================================================
# Parameters
# =============================================================================


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair for SSH access."""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = "Name of an existing EC2 KeyPair to enable SSH access to the instance"
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
    ip_protocol = "tcp"
    from_port = 22
    to_port = 22
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """Security group enabling SSH access."""

    resource: SecurityGroup
    group_description = "Enable SSH access via port 22"
    security_group_ingress = [SSHIngress]


# =============================================================================
# EC2 Instance
# =============================================================================


def first_subnet():
    """Select first subnet from parameter list."""
    return Select(0, ref(Subnets))


@cloudformation_dataclass
class EC2Instance:
    """
    EC2 instance with SSH access.

    Uses SSM Parameter for latest AMI and Security Group for SSH access.
    """

    resource: Instance
    instance_type = ref(InstanceTypeParam)
    subnet_id = first_subnet()
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)


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
class AZOutput:
    """Availability Zone output."""

    resource: Output
    value = get_att(EC2Instance, "AvailabilityZone")
    description = "Availability Zone of the newly created EC2 instance"


@cloudformation_dataclass
class PublicDNSOutput:
    """Public DNS output."""

    resource: Output
    value = get_att(EC2Instance, "PublicDnsName")
    description = "Public DNSName of the newly created EC2 instance"


@cloudformation_dataclass
class PublicIPOutput:
    """Public IP output."""

    resource: Output
    value = get_att(EC2Instance, "PublicIp")
    description = "Public IP address of the newly created EC2 instance"


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class EC2InstanceWithSecurityGroupTemplate:
    """
    EC2 instance with security group template.

    Creates an EC2 instance with SSH access via a security group.
    Uses SSM Parameter for latest AMI lookup.
    """

    resource: Template
    description = (
        "AWS CloudFormation Sample Template: Create an Amazon EC2 instance "
        "with a security group for SSH access."
    )
    parameters = [KeyName, InstanceTypeParam, SSHLocation, LatestAmiId, Subnets]
    resources = [InstanceSecurityGroup, EC2Instance]
    outputs = [InstanceIdOutput, AZOutput, PublicDNSOutput, PublicIPOutput]


def build_template() -> Template:
    """Build the EC2 instance with security group template."""
    return EC2InstanceWithSecurityGroupTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
