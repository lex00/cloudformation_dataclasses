"""PropertyTypes for AWS::SecurityLake::Subscriber."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsLogSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_name": "SourceName",
        "source_version": "SourceVersion",
    }

    source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomLogSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_name": "SourceName",
        "source_version": "SourceVersion",
    }

    source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_log_source": "AwsLogSource",
        "custom_log_source": "CustomLogSource",
    }

    aws_log_source: Optional[AwsLogSource] = None
    custom_log_source: Optional[CustomLogSource] = None


@dataclass
class SubscriberIdentity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "external_id": "ExternalId",
        "principal": "Principal",
    }

    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None

