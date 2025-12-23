"""PropertyTypes for AWS::Chatbot::CustomAction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomActionAttachment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "notification_type": "NotificationType",
        "criteria": "Criteria",
        "button_text": "ButtonText",
    }

    variables: Optional[dict[str, str]] = None
    notification_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    criteria: Optional[list[CustomActionAttachmentCriteria]] = None
    button_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomActionAttachmentCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "variable_name": "VariableName",
        "value": "Value",
    }

    operator: Optional[Union[str, CustomActionAttachmentCriteriaOperator, Ref, GetAtt, Sub]] = None
    variable_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomActionDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "command_text": "CommandText",
    }

    command_text: Optional[Union[str, Ref, GetAtt, Sub]] = None

