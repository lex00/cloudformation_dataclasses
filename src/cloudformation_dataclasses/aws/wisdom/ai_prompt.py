"""PropertyTypes for AWS::Wisdom::AIPrompt."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AIPromptTemplateConfiguration(PropertyType):
    TEXT_FULL_AI_PROMPT_EDIT_TEMPLATE_CONFIGURATION = "TextFullAIPromptEditTemplateConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_full_ai_prompt_edit_template_configuration": "TextFullAIPromptEditTemplateConfiguration",
    }

    text_full_ai_prompt_edit_template_configuration: Optional[TextFullAIPromptEditTemplateConfiguration] = None


@dataclass
class TextFullAIPromptEditTemplateConfiguration(PropertyType):
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None

