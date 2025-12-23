"""PropertyTypes for AWS::SageMaker::NotebookInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InstanceMetadataServiceConfiguration(PropertyType):
    MINIMUM_INSTANCE_METADATA_SERVICE_VERSION = "MinimumInstanceMetadataServiceVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_instance_metadata_service_version": "MinimumInstanceMetadataServiceVersion",
    }

    minimum_instance_metadata_service_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

