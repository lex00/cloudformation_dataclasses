"""PropertyTypes for AWS::EMRContainers::VirtualCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ContainerInfo(PropertyType):
    EKS_INFO = "EksInfo"

    _property_mappings: ClassVar[dict[str, str]] = {
        "eks_info": "EksInfo",
    }

    eks_info: Optional[EksInfo] = None


@dataclass
class ContainerProvider(PropertyType):
    TYPE = "Type"
    ID = "Id"
    INFO = "Info"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id": "Id",
        "info": "Info",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    info: Optional[ContainerInfo] = None


@dataclass
class EksInfo(PropertyType):
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "namespace": "Namespace",
    }

    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None

