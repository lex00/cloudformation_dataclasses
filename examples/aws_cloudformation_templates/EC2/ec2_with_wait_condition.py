"""
EC2 with WaitCondition.

Inspired by AWS's EC2/ec2_with_waitcondition_template.json template.
Demonstrates:
- WaitConditionHandle resource
- WaitCondition with timeout for signaling
- UserData script that signals completion via cfn-signal
- SecurityGroup with multiple ingress rules
- Tags using parameter references
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
    default = "my-key"
    constraint_description = "must be the name of an existing EC2 KeyPair."


@cloudformation_dataclass
class InstanceName:
    """Name tag for the EC2 instance."""

    resource: Parameter
    type = STRING
    description = "Name of EC2 instance"
    constraint_description = "must be a valid EC2 instance string name."


@cloudformation_dataclass
class InstanceTypeParam:
    """EC2 instance type with allowed values."""

    resource: Parameter
    type = STRING
    description = "EC2 instance type"
    default = "t3.small"
    allowed_values = [
        "t2.micro",
        "t2.small",
        "t2.medium",
        "t2.large",
        "t3.micro",
        "t3.small",
        "t3.medium",
        "t3.large",
        "m5.large",
        "m5.xlarge",
    ]
    constraint_description = "must be a valid EC2 instance type."


@cloudformation_dataclass
class ImageId:
    """AMI ID for the instance."""

    resource: Parameter
    type = "AWS::EC2::Image::Id"
    description = "AMI ID for the instance"


@cloudformation_dataclass
class VpcId:
    """VPC ID for security group."""

    resource: Parameter
    type = STRING
    description = "VpcId of your existing Virtual Private Cloud (VPC)"


@cloudformation_dataclass
class SubnetId:
    """Subnet ID for the instance."""

    resource: Parameter
    type = STRING
    description = "SubnetId of an existing subnet in your Virtual Private Cloud (VPC)"


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


# =============================================================================
# Security Group
# =============================================================================


@cloudformation_dataclass
class HTTPIngress:
    """Ingress rule for HTTP access."""

    resource: Ingress
    ip_protocol = "tcp"
    from_port = 80
    to_port = 80
    cidr_ip = "0.0.0.0/0"


@cloudformation_dataclass
class HTTPSIngress:
    """Ingress rule for HTTPS access."""

    resource: Ingress
    ip_protocol = "tcp"
    from_port = 443
    to_port = 443
    cidr_ip = "0.0.0.0/0"


@cloudformation_dataclass
class ICMPIngress:
    """Ingress rule for ICMP (ping) access."""

    resource: Ingress
    ip_protocol = "icmp"
    from_port = -1
    to_port = -1
    cidr_ip = "0.0.0.0/0"


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
    """Security group enabling HTTP, HTTPS, ICMP, and SSH access."""

    resource: SecurityGroup
    vpc_id = ref(VpcId)
    group_description = "Enable HTTP access via port 80/443, ICMP, and SSH via port 22"
    security_group_ingress = [HTTPIngress, HTTPSIngress, ICMPIngress, SSHIngress]


# =============================================================================
# Wait Condition
# =============================================================================


@cloudformation_dataclass
class InstanceWaitHandle:
    """Wait condition handle for instance signaling."""

    resource: WaitConditionHandle


@cloudformation_dataclass
class InstanceWaitCondition:
    """Wait condition that waits for instance setup to complete."""

    resource: WaitCondition
    handle = ref(InstanceWaitHandle)
    timeout = "300"


# =============================================================================
# EC2 Instance
# =============================================================================


def user_data_script():
    """
    UserData script that installs cfn tools and signals completion.

    The script:
    1. Installs python-pip and aws-cfn-bootstrap
    2. Runs cfn-init for instance configuration
    3. Signals success or failure via the WaitConditionHandle
    """
    return Base64(
        Join(
            "",
            [
                "#!/bin/bash\n",
                "apt-get -y install python-pip\n",
                "pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz\n",
                "# Helper function\n",
                "function error_exit\n",
                "{\n",
                '  /usr/local/bin/cfn-signal -e 1 -r "$1" \'',
                ref(InstanceWaitHandle),
                "'\n",
                "  exit 1\n",
                "}\n",
                "# Install the basic system configuration\n",
                "/usr/local/bin/cfn-init -s ",
                AWS_STACK_ID,
                " -r WebInstance ",
                "         --region ",
                AWS_REGION,
                " || error_exit 'Failed to run cfn-init'\n",
                "# All done so signal success\n",
                '/usr/local/bin/cfn-signal -e 0 -r "Setup complete" \'',
                ref(InstanceWaitHandle),
                "'\n",
            ],
        )
    )


@cloudformation_dataclass
class WebInstance:
    """
    EC2 instance with WaitCondition signaling.

    The instance runs a UserData script that signals completion
    via the WaitConditionHandle, allowing CloudFormation to wait
    for instance setup before proceeding.
    """

    resource: Instance
    image_id = ref(ImageId)
    instance_type = ref(InstanceTypeParam)
    subnet_id = ref(SubnetId)
    security_group_ids = [ref(InstanceSecurityGroup)]
    key_name = ref(KeyName)
    monitoring = False
    user_data = user_data_script()
    tags = [
        Tag(key="Name", value=ref(InstanceName)),
    ]


# =============================================================================
# Outputs
# =============================================================================


@cloudformation_dataclass
class WebsiteURLOutput:
    """URL for the deployed instance."""

    resource: Output
    description = "URL for newly created instance"
    value = Join("", ["http://", get_att(WebInstance, "PublicDnsName")])


@cloudformation_dataclass
class InstanceIdOutput:
    """Instance ID output."""

    resource: Output
    description = "Instance Id of newly created instance"
    value = ref(WebInstance)


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class EC2WithWaitConditionTemplate:
    """
    EC2 with WaitCondition template.

    Creates an EC2 instance that signals CloudFormation when setup is complete.
    Uses WaitCondition to block stack creation until the instance signals success.
    """

    resource: Template
    description = "Create an EC2 instance with WaitCondition for setup signaling."
    parameters = [
        KeyName,
        InstanceName,
        InstanceTypeParam,
        ImageId,
        VpcId,
        SubnetId,
        SSHLocation,
    ]
    resources = [
        InstanceSecurityGroup,
        InstanceWaitHandle,
        InstanceWaitCondition,
        WebInstance,
    ]
    outputs = [WebsiteURLOutput, InstanceIdOutput]


def build_template() -> Template:
    """Build the EC2 with WaitCondition template."""
    return EC2WithWaitConditionTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
