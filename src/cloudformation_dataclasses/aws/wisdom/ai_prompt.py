"""PropertyTypes for AWS::Wisdom::AIPrompt."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AIPromptTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_full_ai_prompt_edit_template_configuration": "TextFullAIPromptEditTemplateConfiguration",
    }

    text_full_ai_prompt_edit_template_configuration: Optional[TextFullAIPromptEditTemplateConfiguration] = None


@dataclass
class TextFullAIPromptEditTemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None

