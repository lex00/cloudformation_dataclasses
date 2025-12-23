"""PropertyTypes for AWS::EC2::VPCEncryptionControl."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourceExclusions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "elastic_file_system": "ElasticFileSystem",
        "vpc_lattice": "VpcLattice",
        "vpc_peering": "VpcPeering",
        "internet_gateway": "InternetGateway",
        "egress_only_internet_gateway": "EgressOnlyInternetGateway",
        "virtual_private_gateway": "VirtualPrivateGateway",
        "nat_gateway": "NatGateway",
        "lambda_": "Lambda",
    }

    elastic_file_system: Optional[VpcEncryptionControlExclusion] = None
    vpc_lattice: Optional[VpcEncryptionControlExclusion] = None
    vpc_peering: Optional[VpcEncryptionControlExclusion] = None
    internet_gateway: Optional[VpcEncryptionControlExclusion] = None
    egress_only_internet_gateway: Optional[VpcEncryptionControlExclusion] = None
    virtual_private_gateway: Optional[VpcEncryptionControlExclusion] = None
    nat_gateway: Optional[VpcEncryptionControlExclusion] = None
    lambda_: Optional[VpcEncryptionControlExclusion] = None


@dataclass
class VpcEncryptionControlExclusion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "state_message": "StateMessage",
    }

    state: Optional[Union[str, VpcEncryptionControlExclusionState, Ref, GetAtt, Sub]] = None
    state_message: Optional[Union[str, Ref, GetAtt, Sub]] = None

