"""
VPC with Managed NAT and Private Subnet.

Inspired by AWS's VPC/VPC_With_Managed_NAT_And_Private_Subnet.yaml template.
Demonstrates:
- VPC with DNS support and hostnames
- Public and private subnets across two AZs
- Internet Gateway with VPC attachment
- NAT Gateways for private subnet internet access
- Route tables for public and private routing
- Network ACLs for subnet security
- Mappings for CIDR configuration
- Select and GetAZs intrinsics for AZ selection
- FindInMap for CIDR lookups
- Export outputs for cross-stack references
"""

from . import *  # noqa: F403


# =============================================================================
# Parameters
# =============================================================================


@cloudformation_dataclass
class VPCName:
    """Name of the VPC being created."""

    resource: Parameter
    type = STRING
    default = "VPC Public and Private with NAT"
    description = "The name of the VPC being created."


# =============================================================================
# Mappings
# =============================================================================


@cloudformation_dataclass
class SubnetConfig:
    """CIDR configuration for VPC and subnets."""

    resource: Mapping
    map_data = {
        "VPC": {"CIDR": "10.0.0.0/16"},
        "Public0": {"CIDR": "10.0.0.0/24"},
        "Public1": {"CIDR": "10.0.1.0/24"},
        "Private0": {"CIDR": "10.0.2.0/24"},
        "Private1": {"CIDR": "10.0.3.0/24"},
    }


# =============================================================================
# Helper functions for intrinsics
# =============================================================================


def az(index: int):
    """Get availability zone at index."""
    return Select(index, GetAZs())


def subnet_cidr(name: str):
    """Get CIDR block from SubnetConfig mapping."""
    return FindInMap("SubnetConfig", name, "CIDR")


def subnet_name(suffix: str, az_index: int):
    """Generate subnet name with VPC name prefix and AZ suffix."""
    return Join("", [ref(VPCName), suffix, az(az_index)])


def resource_name(suffix: str):
    """Generate resource name with VPC name prefix."""
    return Join("", [ref(VPCName), suffix])


# =============================================================================
# Reusable Tag Classes
# =============================================================================


@cloudformation_dataclass
class ApplicationTag:
    """Tag for Application name using stack name."""

    resource: Tag
    key = "Application"
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicNetworkTag:
    """Tag indicating public network."""

    resource: Tag
    key = "Network"
    value = "Public"


@cloudformation_dataclass
class PrivateNetworkTag:
    """Tag indicating private network."""

    resource: Tag
    key = "Network"
    value = "Private"


# =============================================================================
# VPC
# =============================================================================


@cloudformation_dataclass
class MainVPCNameTag:
    """Name tag for VPC."""

    resource: Tag
    key = "Name"
    value = ref(VPCName)


@cloudformation_dataclass
class MainVPC:
    """
    VPC with DNS support and hostnames enabled.

    CIDR block is retrieved from the SubnetConfig mapping.
    """

    resource: VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = subnet_cidr("VPC")
    tags = [ApplicationTag, PublicNetworkTag, MainVPCNameTag]


# =============================================================================
# Internet Gateway
# =============================================================================


@cloudformation_dataclass
class IGWNameTag:
    """Name tag for Internet Gateway."""

    resource: Tag
    key = "Name"
    value = resource_name("-IGW")


@cloudformation_dataclass
class IGW:
    """Internet Gateway for public subnet internet access."""

    resource: InternetGateway
    tags = [ApplicationTag, PublicNetworkTag, IGWNameTag]


@cloudformation_dataclass
class GatewayToInternet:
    """Attach Internet Gateway to VPC."""

    resource: VPCGatewayAttachment
    vpc_id = ref(MainVPC)
    internet_gateway_id = ref(IGW)


# =============================================================================
# Public Subnets
# =============================================================================


@cloudformation_dataclass
class PublicSubnet0NameTag:
    """Name tag for public subnet 0."""

    resource: Tag
    key = "Name"
    value = subnet_name("-public-", 0)


@cloudformation_dataclass
class PublicSubnet0:
    """Public subnet in first availability zone."""

    resource: Subnet
    vpc_id = ref(MainVPC)
    availability_zone = az(0)
    cidr_block = subnet_cidr("Public0")
    map_public_ip_on_launch = True
    tags = [ApplicationTag, PublicNetworkTag, PublicSubnet0NameTag]


@cloudformation_dataclass
class PublicSubnet1NameTag:
    """Name tag for public subnet 1."""

    resource: Tag
    key = "Name"
    value = subnet_name("-public-", 1)


@cloudformation_dataclass
class PublicSubnet1:
    """Public subnet in second availability zone."""

    resource: Subnet
    vpc_id = ref(MainVPC)
    availability_zone = az(1)
    cidr_block = subnet_cidr("Public1")
    map_public_ip_on_launch = True
    tags = [ApplicationTag, PublicNetworkTag, PublicSubnet1NameTag]


# =============================================================================
# Private Subnets
# =============================================================================


@cloudformation_dataclass
class PrivateSubnet0NameTag:
    """Name tag for private subnet 0."""

    resource: Tag
    key = "Name"
    value = subnet_name("-private-", 0)


@cloudformation_dataclass
class PrivateSubnet0:
    """Private subnet in first availability zone."""

    resource: Subnet
    vpc_id = ref(MainVPC)
    availability_zone = az(0)
    cidr_block = subnet_cidr("Private0")
    tags = [ApplicationTag, PrivateNetworkTag, PrivateSubnet0NameTag]


@cloudformation_dataclass
class PrivateSubnet1NameTag:
    """Name tag for private subnet 1."""

    resource: Tag
    key = "Name"
    value = subnet_name("-private-", 1)


@cloudformation_dataclass
class PrivateSubnet1:
    """Private subnet in second availability zone."""

    resource: Subnet
    vpc_id = ref(MainVPC)
    availability_zone = az(1)
    cidr_block = subnet_cidr("Private1")
    tags = [ApplicationTag, PrivateNetworkTag, PrivateSubnet1NameTag]


# =============================================================================
# Public Route Table
# =============================================================================


@cloudformation_dataclass
class PublicRouteTableNameTag:
    """Name tag for public route table."""

    resource: Tag
    key = "Name"
    value = resource_name("-public-route-table")


@cloudformation_dataclass
class PublicRouteTable:
    """Route table for public subnets."""

    resource: RouteTable
    vpc_id = ref(MainVPC)
    tags = [ApplicationTag, PublicNetworkTag, PublicRouteTableNameTag]


@cloudformation_dataclass
class PublicRoute:
    """Route to internet via Internet Gateway."""

    resource: Route
    route_table_id = ref(PublicRouteTable)
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = ref(IGW)
    depends_on = ["GatewayToInternet"]


@cloudformation_dataclass
class PublicSubnetRouteTableAssociation0:
    """Associate public subnet 0 with public route table."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet0)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicSubnetRouteTableAssociation1:
    """Associate public subnet 1 with public route table."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet1)
    route_table_id = ref(PublicRouteTable)


# =============================================================================
# Network ACL
# =============================================================================


@cloudformation_dataclass
class PublicNetworkAclNameTag:
    """Name tag for public network ACL."""

    resource: Tag
    key = "Name"
    value = resource_name("-public-nacl")


@cloudformation_dataclass
class PublicNetworkAcl:
    """Network ACL for public subnets."""

    resource: NetworkAcl
    vpc_id = ref(MainVPC)
    tags = [ApplicationTag, PublicNetworkTag, PublicNetworkAclNameTag]


@cloudformation_dataclass
class InboundPublicNetworkAclEntry:
    """Allow all inbound traffic on public subnets."""

    resource: NetworkAclEntry
    network_acl_id = ref(PublicNetworkAcl)
    rule_number = 100
    protocol = -1  # All protocols
    rule_action = "allow"
    egress = False
    cidr_block = "0.0.0.0/0"


@cloudformation_dataclass
class OutboundPublicNetworkAclEntry:
    """Allow all outbound traffic from public subnets."""

    resource: NetworkAclEntry
    network_acl_id = ref(PublicNetworkAcl)
    rule_number = 100
    protocol = -1  # All protocols
    rule_action = "allow"
    egress = True
    cidr_block = "0.0.0.0/0"


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation0:
    """Associate public subnet 0 with public NACL."""

    resource: SubnetNetworkAclAssociation
    subnet_id = ref(PublicSubnet0)
    network_acl_id = ref(PublicNetworkAcl)


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation1:
    """Associate public subnet 1 with public NACL."""

    resource: SubnetNetworkAclAssociation
    subnet_id = ref(PublicSubnet1)
    network_acl_id = ref(PublicNetworkAcl)


# =============================================================================
# NAT Gateways
# =============================================================================


@cloudformation_dataclass
class ElasticIP0:
    """Elastic IP for NAT Gateway 0."""

    resource: EIP
    domain = "vpc"


@cloudformation_dataclass
class ElasticIP1:
    """Elastic IP for NAT Gateway 1."""

    resource: EIP
    domain = "vpc"


@cloudformation_dataclass
class NATGateway0:
    """NAT Gateway in public subnet 0 for private subnet 0 internet access."""

    resource: NatGateway
    allocation_id = get_att(ElasticIP0, "AllocationId")
    subnet_id = ref(PublicSubnet0)


@cloudformation_dataclass
class NATGateway1:
    """NAT Gateway in public subnet 1 for private subnet 1 internet access."""

    resource: NatGateway
    allocation_id = get_att(ElasticIP1, "AllocationId")
    subnet_id = ref(PublicSubnet1)


# =============================================================================
# Private Route Tables
# =============================================================================


@cloudformation_dataclass
class PrivateRouteTable0NameTag:
    """Name tag for private route table 0."""

    resource: Tag
    key = "Name"
    value = resource_name("-private-route-table-0")


@cloudformation_dataclass
class PrivateRouteTable0:
    """Route table for private subnet 0."""

    resource: RouteTable
    vpc_id = ref(MainVPC)
    tags = [PrivateRouteTable0NameTag]


@cloudformation_dataclass
class PrivateRouteTable1NameTag:
    """Name tag for private route table 1."""

    resource: Tag
    key = "Name"
    value = resource_name("-private-route-table-1")


@cloudformation_dataclass
class PrivateRouteTable1:
    """Route table for private subnet 1."""

    resource: RouteTable
    vpc_id = ref(MainVPC)
    tags = [PrivateRouteTable1NameTag]


@cloudformation_dataclass
class PrivateRouteToInternet0:
    """Route to internet via NAT Gateway 0."""

    resource: Route
    route_table_id = ref(PrivateRouteTable0)
    destination_cidr_block = "0.0.0.0/0"
    nat_gateway_id = ref(NATGateway0)


@cloudformation_dataclass
class PrivateRouteToInternet1:
    """Route to internet via NAT Gateway 1."""

    resource: Route
    route_table_id = ref(PrivateRouteTable1)
    destination_cidr_block = "0.0.0.0/0"
    nat_gateway_id = ref(NATGateway1)


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation0:
    """Associate private subnet 0 with private route table 0."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet0)
    route_table_id = ref(PrivateRouteTable0)


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation1:
    """Associate private subnet 1 with private route table 1."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet1)
    route_table_id = ref(PrivateRouteTable1)


# =============================================================================
# Outputs
# =============================================================================


def export_name(suffix: str):
    """Generate export name with region and stack name prefix."""
    return Sub("${AWS::Region}-${AWS::StackName}" + suffix)


@cloudformation_dataclass
class VPCIdOutput:
    """VPC ID output with cross-stack export."""

    resource: Output
    value = ref(MainVPC)
    description = "VPCId of VPC"
    export_name = export_name("-VPC")


@cloudformation_dataclass
class PublicSubnet0Output:
    """Public subnet 0 ID output."""

    resource: Output
    value = ref(PublicSubnet0)
    description = "SubnetId of public subnet 0"
    export_name = export_name("-PublicSubnet0")


@cloudformation_dataclass
class PublicSubnet1Output:
    """Public subnet 1 ID output."""

    resource: Output
    value = ref(PublicSubnet1)
    description = "SubnetId of public subnet 1"
    export_name = export_name("-PublicSubnet1")


@cloudformation_dataclass
class PrivateSubnet0Output:
    """Private subnet 0 ID output."""

    resource: Output
    value = ref(PrivateSubnet0)
    description = "SubnetId of private subnet 0"
    export_name = export_name("-PrivateSubnet0")


@cloudformation_dataclass
class PrivateSubnet1Output:
    """Private subnet 1 ID output."""

    resource: Output
    value = ref(PrivateSubnet1)
    description = "SubnetId of private subnet 1"
    export_name = export_name("-PrivateSubnet1")


@cloudformation_dataclass
class DefaultSecurityGroupOutput:
    """Default security group ID output."""

    resource: Output
    value = get_att(MainVPC, "DefaultSecurityGroup")
    description = "DefaultSecurityGroup Id"
    export_name = export_name("-DefaultSecurityGroup")


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class VPCWithNATTemplate:
    """
    VPC with Managed NAT and Private Subnet template.

    Creates a VPC similar to the VPC Wizard with:
    - 2 public subnets with Internet Gateway
    - 2 private subnets with NAT Gateways
    - Route tables and Network ACLs
    """

    resource: Template
    description = (
        "Creates a VPC with Managed NAT, similar to the VPC Wizard at "
        "https://console.aws.amazon.com/vpc/home#wizardFullpagePublicAndPrivate"
    )
    parameters = [VPCName]
    mappings = [SubnetConfig]
    resources = [
        # VPC
        MainVPC,
        # Internet Gateway
        IGW,
        GatewayToInternet,
        # Public Subnets
        PublicSubnet0,
        PublicSubnet1,
        # Private Subnets
        PrivateSubnet0,
        PrivateSubnet1,
        # Public Route Table
        PublicRouteTable,
        PublicRoute,
        PublicSubnetRouteTableAssociation0,
        PublicSubnetRouteTableAssociation1,
        # Network ACL
        PublicNetworkAcl,
        InboundPublicNetworkAclEntry,
        OutboundPublicNetworkAclEntry,
        PublicSubnetNetworkAclAssociation0,
        PublicSubnetNetworkAclAssociation1,
        # NAT Gateways
        ElasticIP0,
        ElasticIP1,
        NATGateway0,
        NATGateway1,
        # Private Route Tables
        PrivateRouteTable0,
        PrivateRouteTable1,
        PrivateRouteToInternet0,
        PrivateRouteToInternet1,
        PrivateSubnetRouteTableAssociation0,
        PrivateSubnetRouteTableAssociation1,
    ]
    outputs = [
        VPCIdOutput,
        PublicSubnet0Output,
        PublicSubnet1Output,
        PrivateSubnet0Output,
        PrivateSubnet1Output,
        DefaultSecurityGroupOutput,
    ]


def build_template() -> Template:
    """Build the VPC with NAT template."""
    return VPCWithNATTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
