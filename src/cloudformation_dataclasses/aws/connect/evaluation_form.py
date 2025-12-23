"""PropertyTypes for AWS::Connect::EvaluationForm."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoEvaluationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AutomaticFailConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_section": "TargetSection",
    }

    target_section: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormBaseItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "section": "Section",
    }

    section: Optional[EvaluationFormSection] = None


@dataclass
class EvaluationFormItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "question": "Question",
        "section": "Section",
    }

    question: Optional[EvaluationFormQuestion] = None
    section: Optional[EvaluationFormSection] = None


@dataclass
class EvaluationFormItemEnablementCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "operands": "Operands",
    }

    operator: Optional[Union[str, EvaluationFormItemEnablementOperator, Ref, GetAtt, Sub]] = None
    operands: Optional[list[EvaluationFormItemEnablementConditionOperand]] = None


@dataclass
class EvaluationFormItemEnablementConditionOperand(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
    }

    expression: Optional[EvaluationFormItemEnablementExpression] = None


@dataclass
class EvaluationFormItemEnablementConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "action": "Action",
        "default_action": "DefaultAction",
    }

    condition: Optional[EvaluationFormItemEnablementCondition] = None
    action: Optional[Union[str, EvaluationFormItemEnablementAction, Ref, GetAtt, Sub]] = None
    default_action: Optional[Union[str, EvaluationFormItemEnablementAction, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormItemEnablementExpression(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "source": "Source",
        "comparator": "Comparator",
    }

    values: Optional[list[EvaluationFormItemEnablementSourceValue]] = None
    source: Optional[EvaluationFormItemEnablementSource] = None
    comparator: Optional[Union[str, EvaluationFormItemSourceValuesComparator, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormItemEnablementSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "ref_id": "RefId",
    }

    type_: Optional[Union[str, EvaluationFormItemEnablementSourceType, Ref, GetAtt, Sub]] = None
    ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormItemEnablementSourceValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "ref_id": "RefId",
    }

    type_: Optional[Union[str, EvaluationFormItemEnablementSourceValueType, Ref, GetAtt, Sub]] = None
    ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormLanguageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "form_language": "FormLanguage",
    }

    form_language: Optional[Union[str, EvaluationFormLanguageCode, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormMultiSelectQuestionAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "answer_source": "AnswerSource",
        "default_option_ref_ids": "DefaultOptionRefIds",
    }

    options: Optional[list[EvaluationFormMultiSelectQuestionAutomationOption]] = None
    answer_source: Optional[EvaluationFormQuestionAutomationAnswerSource] = None
    default_option_ref_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class EvaluationFormMultiSelectQuestionAutomationOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_category": "RuleCategory",
    }

    rule_category: Optional[MultiSelectQuestionRuleCategoryAutomation] = None


@dataclass
class EvaluationFormMultiSelectQuestionOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
        "ref_id": "RefId",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormMultiSelectQuestionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_as": "DisplayAs",
        "options": "Options",
        "automation": "Automation",
    }

    display_as: Optional[Union[str, EvaluationFormMultiSelectQuestionDisplayMode, Ref, GetAtt, Sub]] = None
    options: Optional[list[EvaluationFormMultiSelectQuestionOption]] = None
    automation: Optional[EvaluationFormMultiSelectQuestionAutomation] = None


@dataclass
class EvaluationFormNumericQuestionAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "answer_source": "AnswerSource",
        "property_value": "PropertyValue",
    }

    answer_source: Optional[EvaluationFormQuestionAutomationAnswerSource] = None
    property_value: Optional[NumericQuestionPropertyValueAutomation] = None


@dataclass
class EvaluationFormNumericQuestionOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "score": "Score",
        "automatic_fail_configuration": "AutomaticFailConfiguration",
        "min_value": "MinValue",
        "max_value": "MaxValue",
        "automatic_fail": "AutomaticFail",
    }

    score: Optional[Union[int, Ref, GetAtt, Sub]] = None
    automatic_fail_configuration: Optional[AutomaticFailConfiguration] = None
    min_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    automatic_fail: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormNumericQuestionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "automation": "Automation",
        "min_value": "MinValue",
        "max_value": "MaxValue",
    }

    options: Optional[list[EvaluationFormNumericQuestionOption]] = None
    automation: Optional[EvaluationFormNumericQuestionAutomation] = None
    min_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormQuestion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "not_applicable_enabled": "NotApplicableEnabled",
        "enablement": "Enablement",
        "title": "Title",
        "question_type": "QuestionType",
        "instructions": "Instructions",
        "ref_id": "RefId",
        "question_type_properties": "QuestionTypeProperties",
        "weight": "Weight",
    }

    not_applicable_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enablement: Optional[EvaluationFormItemEnablementConfiguration] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    question_type: Optional[Union[str, EvaluationFormQuestionType, Ref, GetAtt, Sub]] = None
    instructions: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    question_type_properties: Optional[EvaluationFormQuestionTypeProperties] = None
    weight: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormQuestionAutomationAnswerSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_type": "SourceType",
    }

    source_type: Optional[Union[str, EvaluationFormQuestionAutomationAnswerSourceType, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormQuestionTypeProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "numeric": "Numeric",
        "single_select": "SingleSelect",
        "multi_select": "MultiSelect",
        "text": "Text",
    }

    numeric: Optional[EvaluationFormNumericQuestionProperties] = None
    single_select: Optional[EvaluationFormSingleSelectQuestionProperties] = None
    multi_select: Optional[EvaluationFormMultiSelectQuestionProperties] = None
    text: Optional[EvaluationFormTextQuestionProperties] = None


@dataclass
class EvaluationFormSection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "title": "Title",
        "instructions": "Instructions",
        "items": "Items",
        "ref_id": "RefId",
        "weight": "Weight",
    }

    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instructions: Optional[Union[str, Ref, GetAtt, Sub]] = None
    items: Optional[list[EvaluationFormItem]] = None
    ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormSingleSelectQuestionAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "answer_source": "AnswerSource",
        "default_option_ref_id": "DefaultOptionRefId",
    }

    options: Optional[list[EvaluationFormSingleSelectQuestionAutomationOption]] = None
    answer_source: Optional[EvaluationFormQuestionAutomationAnswerSource] = None
    default_option_ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormSingleSelectQuestionAutomationOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_category": "RuleCategory",
    }

    rule_category: Optional[SingleSelectQuestionRuleCategoryAutomation] = None


@dataclass
class EvaluationFormSingleSelectQuestionOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "score": "Score",
        "automatic_fail_configuration": "AutomaticFailConfiguration",
        "text": "Text",
        "ref_id": "RefId",
        "automatic_fail": "AutomaticFail",
    }

    score: Optional[Union[int, Ref, GetAtt, Sub]] = None
    automatic_fail_configuration: Optional[AutomaticFailConfiguration] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    automatic_fail: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormSingleSelectQuestionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "display_as": "DisplayAs",
        "options": "Options",
        "automation": "Automation",
    }

    display_as: Optional[Union[str, EvaluationFormSingleSelectQuestionDisplayMode, Ref, GetAtt, Sub]] = None
    options: Optional[list[EvaluationFormSingleSelectQuestionOption]] = None
    automation: Optional[EvaluationFormSingleSelectQuestionAutomation] = None


@dataclass
class EvaluationFormTargetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_interaction_type": "ContactInteractionType",
    }

    contact_interaction_type: Optional[Union[str, ContactInteractionType, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationFormTextQuestionAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "answer_source": "AnswerSource",
    }

    answer_source: Optional[EvaluationFormQuestionAutomationAnswerSource] = None


@dataclass
class EvaluationFormTextQuestionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "automation": "Automation",
    }

    automation: Optional[EvaluationFormTextQuestionAutomation] = None


@dataclass
class MultiSelectQuestionRuleCategoryAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "category": "Category",
        "option_ref_ids": "OptionRefIds",
    }

    condition: Optional[Union[str, MultiSelectQuestionRuleCategoryAutomationCondition, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, Ref, GetAtt, Sub]] = None
    option_ref_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class NumericQuestionPropertyValueAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "label": "Label",
    }

    label: Optional[Union[str, NumericQuestionPropertyAutomationLabel, Ref, GetAtt, Sub]] = None


@dataclass
class ScoringStrategy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "mode": "Mode",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleSelectQuestionRuleCategoryAutomation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "category": "Category",
        "option_ref_id": "OptionRefId",
    }

    condition: Optional[Union[str, SingleSelectQuestionRuleCategoryAutomationCondition, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, Ref, GetAtt, Sub]] = None
    option_ref_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

