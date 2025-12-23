"""PropertyTypes for AWS::SageMaker::DeviceFleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EdgeOutputConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "s3_output_location": "S3OutputLocation",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_location: Optional[Union[str, Ref, GetAtt, Sub]] = None

