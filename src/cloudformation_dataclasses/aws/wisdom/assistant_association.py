"""PropertyTypes for AWS::Wisdom::AssistantAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AssociationData(PropertyType):
    KNOWLEDGE_BASE_ID = "KnowledgeBaseId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "knowledge_base_id": "KnowledgeBaseId",
    }

    knowledge_base_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

