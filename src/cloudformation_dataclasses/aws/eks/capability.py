"""PropertyTypes for AWS::EKS::Capability."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ArgoCd(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "server_url": "ServerUrl",
        "network_access": "NetworkAccess",
        "aws_idc": "AwsIdc",
        "rbac_role_mappings": "RbacRoleMappings",
        "namespace": "Namespace",
    }

    server_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_access: Optional[NetworkAccess] = None
    aws_idc: Optional[AwsIdc] = None
    rbac_role_mappings: Optional[list[ArgoCdRoleMapping]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArgoCdRoleMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "identities": "Identities",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identities: Optional[list[SsoIdentity]] = None


@dataclass
class AwsIdc(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idc_region": "IdcRegion",
        "idc_managed_application_arn": "IdcManagedApplicationArn",
        "idc_instance_arn": "IdcInstanceArn",
    }

    idc_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    idc_managed_application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    idc_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapabilityConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "argo_cd": "ArgoCd",
    }

    argo_cd: Optional[ArgoCd] = None


@dataclass
class NetworkAccess(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpce_ids": "VpceIds",
    }

    vpce_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class SsoIdentity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id": "Id",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

