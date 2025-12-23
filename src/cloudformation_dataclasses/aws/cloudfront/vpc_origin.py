"""PropertyTypes for AWS::CloudFront::VpcOrigin."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class VpcOriginEndpointConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
        "arn": "Arn",
        "http_port": "HTTPPort",
        "name": "Name",
        "origin_protocol_policy": "OriginProtocolPolicy",
    }

    https_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_ssl_protocols: Optional[Union[list[str], Ref]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_protocol_policy: Optional[Union[str, OriginProtocolPolicy, Ref, GetAtt, Sub]] = None

