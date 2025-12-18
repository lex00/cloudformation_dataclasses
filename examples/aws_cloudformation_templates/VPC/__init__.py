"""VPC CloudFormation template examples."""

from cloudformation_dataclasses.aws.ec2 import (
    # Resources
    EIP,
    InternetGateway,
    NatGateway,
    NetworkAcl,
    NetworkAclEntry,
    Route,
    RouteTable,
    Subnet,
    SubnetNetworkAclAssociation,
    SubnetRouteTableAssociation,
    VPC,
    VPCGatewayAttachment,
)
from cloudformation_dataclasses.core import (
    # Parameter types
    STRING,
    # Core constructs
    DeploymentContext,
    Mapping,
    Output,
    Parameter,
    Tag,
    Template,
    cloudformation_dataclass,
    ref,
    get_att,
)
from cloudformation_dataclasses.intrinsics import (
    FindInMap,
    GetAZs,
    Join,
    Select,
    Sub,
    AWS_STACK_NAME,
)

__all__ = [
    # Resources
    "EIP",
    "InternetGateway",
    "NatGateway",
    "NetworkAcl",
    "NetworkAclEntry",
    "Route",
    "RouteTable",
    "Subnet",
    "SubnetNetworkAclAssociation",
    "SubnetRouteTableAssociation",
    "VPC",
    "VPCGatewayAttachment",
    # Core
    "DeploymentContext",
    "Mapping",
    "Output",
    "Parameter",
    "STRING",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "get_att",
    "ref",
    # Intrinsics
    "FindInMap",
    "GetAZs",
    "Join",
    "Select",
    "Sub",
    "AWS_STACK_NAME",
]
