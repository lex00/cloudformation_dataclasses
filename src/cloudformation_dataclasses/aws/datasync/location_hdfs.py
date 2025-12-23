"""PropertyTypes for AWS::DataSync::LocationHDFS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NameNode(PropertyType):
    PORT = "Port"
    HOSTNAME = "Hostname"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "hostname": "Hostname",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QopConfiguration(PropertyType):
    RPC_PROTECTION = "RpcProtection"
    DATA_TRANSFER_PROTECTION = "DataTransferProtection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rpc_protection": "RpcProtection",
        "data_transfer_protection": "DataTransferProtection",
    }

    rpc_protection: Optional[Union[str, HdfsRpcProtection, Ref, GetAtt, Sub]] = None
    data_transfer_protection: Optional[Union[str, HdfsDataTransferProtection, Ref, GetAtt, Sub]] = None

