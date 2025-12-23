"""PropertyTypes for AWS::EVS::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Check(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "impaired_since": "ImpairedSince",
        "result": "Result",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    impaired_since: Optional[Union[str, Ref, GetAtt, Sub]] = None
    result: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectivityInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_route_server_peerings": "PrivateRouteServerPeerings",
    }

    private_route_server_peerings: Optional[Union[list[str], Ref]] = None


@dataclass
class HostInfoForCreate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_name": "KeyName",
        "dedicated_host_id": "DedicatedHostId",
        "placement_group_id": "PlacementGroupId",
        "instance_type": "InstanceType",
        "host_name": "HostName",
    }

    key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dedicated_host_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    placement_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InitialVlanInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InitialVlans(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vmk_management": "VmkManagement",
        "v_tep": "VTep",
        "expansion_vlan2": "ExpansionVlan2",
        "v_san": "VSan",
        "v_motion": "VMotion",
        "is_hcx_public": "IsHcxPublic",
        "hcx": "Hcx",
        "edge_v_tep": "EdgeVTep",
        "hcx_network_acl_id": "HcxNetworkAclId",
        "expansion_vlan1": "ExpansionVlan1",
        "vm_management": "VmManagement",
        "nsx_up_link": "NsxUpLink",
    }

    vmk_management: Optional[InitialVlanInfo] = None
    v_tep: Optional[InitialVlanInfo] = None
    expansion_vlan2: Optional[InitialVlanInfo] = None
    v_san: Optional[InitialVlanInfo] = None
    v_motion: Optional[InitialVlanInfo] = None
    is_hcx_public: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hcx: Optional[InitialVlanInfo] = None
    edge_v_tep: Optional[InitialVlanInfo] = None
    hcx_network_acl_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expansion_vlan1: Optional[InitialVlanInfo] = None
    vm_management: Optional[InitialVlanInfo] = None
    nsx_up_link: Optional[InitialVlanInfo] = None


@dataclass
class LicenseInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "solution_key": "SolutionKey",
        "vsan_key": "VsanKey",
    }

    solution_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vsan_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Secret(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceAccessSecurityGroups(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
    }

    security_groups: Optional[Union[list[str], Ref]] = None


@dataclass
class VcfHostnames(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nsx": "Nsx",
        "v_center": "VCenter",
        "nsx_manager1": "NsxManager1",
        "nsx_edge1": "NsxEdge1",
        "nsx_manager3": "NsxManager3",
        "sddc_manager": "SddcManager",
        "nsx_manager2": "NsxManager2",
        "nsx_edge2": "NsxEdge2",
        "cloud_builder": "CloudBuilder",
    }

    nsx: Optional[Union[str, Ref, GetAtt, Sub]] = None
    v_center: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nsx_manager1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nsx_edge1: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nsx_manager3: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sddc_manager: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nsx_manager2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nsx_edge2: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_builder: Optional[Union[str, Ref, GetAtt, Sub]] = None

