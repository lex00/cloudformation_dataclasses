"""PropertyTypes for AWS::MediaPackage::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HlsIngest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ingest_endpoints": "ingestEndpoints",
    }

    ingest_endpoints: Optional[list[IngestEndpoint]] = None


@dataclass
class IngestEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "id": "Id",
        "url": "Url",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_name": "LogGroupName",
    }

    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

