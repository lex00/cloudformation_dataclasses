"""PropertyTypes for AWS::Config::ConformancePack."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConformancePackInputParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateSSMDocumentDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "document_version": "DocumentVersion",
        "document_name": "DocumentName",
    }

    document_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    document_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

