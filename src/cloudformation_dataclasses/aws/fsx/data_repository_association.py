"""PropertyTypes for AWS::FSx::DataRepositoryAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoExportPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
    }

    events: Optional[Union[list[str], Ref]] = None


@dataclass
class AutoImportPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
    }

    events: Optional[Union[list[str], Ref]] = None


@dataclass
class S3(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_import_policy": "AutoImportPolicy",
        "auto_export_policy": "AutoExportPolicy",
    }

    auto_import_policy: Optional[AutoImportPolicy] = None
    auto_export_policy: Optional[AutoExportPolicy] = None

