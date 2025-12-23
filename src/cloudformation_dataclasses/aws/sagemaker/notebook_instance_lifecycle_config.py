"""PropertyTypes for AWS::SageMaker::NotebookInstanceLifecycleConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NotebookInstanceLifecycleHook(PropertyType):
    CONTENT = "Content"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
    }

    content: Optional[Union[str, Ref, GetAtt, Sub]] = None

