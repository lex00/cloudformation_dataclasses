"""PropertyTypes for AWS::ApiGateway::RestApi."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EndpointConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "types": "Types",
        "vpc_endpoint_ids": "VpcEndpointIds",
    }

    ip_address_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    types: Optional[Union[list[str], Ref]] = None
    vpc_endpoint_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "e_tag": "ETag",
        "version": "Version",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    e_tag: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

