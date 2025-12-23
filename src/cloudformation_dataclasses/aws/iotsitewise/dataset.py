"""PropertyTypes for AWS::IoTSiteWise::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DatasetSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_type": "SourceType",
        "source_format": "SourceFormat",
        "source_detail": "SourceDetail",
    }

    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_detail: Optional[SourceDetail] = None


@dataclass
class KendraSourceDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "knowledge_base_arn": "KnowledgeBaseArn",
        "role_arn": "RoleArn",
    }

    knowledge_base_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kendra": "Kendra",
    }

    kendra: Optional[KendraSourceDetail] = None

