"""PropertyTypes for AWS::SageMaker::App."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourceSpec(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle_config_arn": "LifecycleConfigArn",
        "sage_maker_image_arn": "SageMakerImageArn",
        "instance_type": "InstanceType",
        "sage_maker_image_version_arn": "SageMakerImageVersionArn",
    }

    lifecycle_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sage_maker_image_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, AppInstanceType, Ref, GetAtt, Sub]] = None
    sage_maker_image_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

