"""PropertyTypes for AWS::Kendra::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomDocumentEnrichmentConfiguration(PropertyType):
    INLINE_CONFIGURATIONS = "InlineConfigurations"
    PRE_EXTRACTION_HOOK_CONFIGURATION = "PreExtractionHookConfiguration"
    POST_EXTRACTION_HOOK_CONFIGURATION = "PostExtractionHookConfiguration"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inline_configurations": "InlineConfigurations",
        "pre_extraction_hook_configuration": "PreExtractionHookConfiguration",
        "post_extraction_hook_configuration": "PostExtractionHookConfiguration",
        "role_arn": "RoleArn",
    }

    inline_configurations: Optional[list[InlineCustomDocumentEnrichmentConfiguration]] = None
    pre_extraction_hook_configuration: Optional[HookConfiguration] = None
    post_extraction_hook_configuration: Optional[HookConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSourceConfiguration(PropertyType):
    TEMPLATE_CONFIGURATION = "TemplateConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template_configuration": "TemplateConfiguration",
    }

    template_configuration: Optional[TemplateConfiguration] = None


@dataclass
class DocumentAttributeCondition(PropertyType):
    OPERATOR = "Operator"
    CONDITION_DOCUMENT_ATTRIBUTE_KEY = "ConditionDocumentAttributeKey"
    CONDITION_ON_VALUE = "ConditionOnValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "condition_document_attribute_key": "ConditionDocumentAttributeKey",
        "condition_on_value": "ConditionOnValue",
    }

    operator: Optional[Union[str, ConditionOperator, Ref, GetAtt, Sub]] = None
    condition_document_attribute_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_on_value: Optional[DocumentAttributeValue] = None


@dataclass
class DocumentAttributeTarget(PropertyType):
    TARGET_DOCUMENT_ATTRIBUTE_KEY = "TargetDocumentAttributeKey"
    TARGET_DOCUMENT_ATTRIBUTE_VALUE_DELETION = "TargetDocumentAttributeValueDeletion"
    TARGET_DOCUMENT_ATTRIBUTE_VALUE = "TargetDocumentAttributeValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_document_attribute_key": "TargetDocumentAttributeKey",
        "target_document_attribute_value_deletion": "TargetDocumentAttributeValueDeletion",
        "target_document_attribute_value": "TargetDocumentAttributeValue",
    }

    target_document_attribute_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_document_attribute_value_deletion: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    target_document_attribute_value: Optional[DocumentAttributeValue] = None


@dataclass
class DocumentAttributeValue(PropertyType):
    DATE_VALUE = "DateValue"
    LONG_VALUE = "LongValue"
    STRING_VALUE = "StringValue"
    STRING_LIST_VALUE = "StringListValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "date_value": "DateValue",
        "long_value": "LongValue",
        "string_value": "StringValue",
        "string_list_value": "StringListValue",
    }

    date_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    long_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_list_value: Optional[Union[list[str], Ref]] = None


@dataclass
class HookConfiguration(PropertyType):
    S3_BUCKET = "S3Bucket"
    LAMBDA_ARN = "LambdaArn"
    INVOCATION_CONDITION = "InvocationCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "lambda_arn": "LambdaArn",
        "invocation_condition": "InvocationCondition",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invocation_condition: Optional[DocumentAttributeCondition] = None


@dataclass
class InlineCustomDocumentEnrichmentConfiguration(PropertyType):
    CONDITION = "Condition"
    TARGET = "Target"
    DOCUMENT_CONTENT_DELETION = "DocumentContentDeletion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "target": "Target",
        "document_content_deletion": "DocumentContentDeletion",
    }

    condition: Optional[DocumentAttributeCondition] = None
    target: Optional[DocumentAttributeTarget] = None
    document_content_deletion: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateConfiguration(PropertyType):
    TEMPLATE = "Template"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template": "Template",
    }

    template: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

