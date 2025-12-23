"""PropertyTypes for AWS::QBusiness::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AudioExtractionConfiguration(PropertyType):
    AUDIO_EXTRACTION_STATUS = "AudioExtractionStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_extraction_status": "AudioExtractionStatus",
    }

    audio_extraction_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSourceVpcConfiguration(PropertyType):
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class DocumentAttributeCondition(PropertyType):
    OPERATOR = "Operator"
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
        "key": "Key",
    }

    operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[DocumentAttributeValue] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentAttributeTarget(PropertyType):
    VALUE = "Value"
    ATTRIBUTE_VALUE_OPERATOR = "AttributeValueOperator"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "attribute_value_operator": "AttributeValueOperator",
        "key": "Key",
    }

    value: Optional[DocumentAttributeValue] = None
    attribute_value_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
    long_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_list_value: Optional[Union[list[str], Ref]] = None


@dataclass
class DocumentEnrichmentConfiguration(PropertyType):
    INLINE_CONFIGURATIONS = "InlineConfigurations"
    PRE_EXTRACTION_HOOK_CONFIGURATION = "PreExtractionHookConfiguration"
    POST_EXTRACTION_HOOK_CONFIGURATION = "PostExtractionHookConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inline_configurations": "InlineConfigurations",
        "pre_extraction_hook_configuration": "PreExtractionHookConfiguration",
        "post_extraction_hook_configuration": "PostExtractionHookConfiguration",
    }

    inline_configurations: Optional[list[InlineDocumentEnrichmentConfiguration]] = None
    pre_extraction_hook_configuration: Optional[HookConfiguration] = None
    post_extraction_hook_configuration: Optional[HookConfiguration] = None


@dataclass
class HookConfiguration(PropertyType):
    LAMBDA_ARN = "LambdaArn"
    INVOCATION_CONDITION = "InvocationCondition"
    S3_BUCKET_NAME = "S3BucketName"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "invocation_condition": "InvocationCondition",
        "s3_bucket_name": "S3BucketName",
        "role_arn": "RoleArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invocation_condition: Optional[DocumentAttributeCondition] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageExtractionConfiguration(PropertyType):
    IMAGE_EXTRACTION_STATUS = "ImageExtractionStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_extraction_status": "ImageExtractionStatus",
    }

    image_extraction_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InlineDocumentEnrichmentConfiguration(PropertyType):
    CONDITION = "Condition"
    TARGET = "Target"
    DOCUMENT_CONTENT_OPERATOR = "DocumentContentOperator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "target": "Target",
        "document_content_operator": "DocumentContentOperator",
    }

    condition: Optional[DocumentAttributeCondition] = None
    target: Optional[DocumentAttributeTarget] = None
    document_content_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaExtractionConfiguration(PropertyType):
    VIDEO_EXTRACTION_CONFIGURATION = "VideoExtractionConfiguration"
    AUDIO_EXTRACTION_CONFIGURATION = "AudioExtractionConfiguration"
    IMAGE_EXTRACTION_CONFIGURATION = "ImageExtractionConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "video_extraction_configuration": "VideoExtractionConfiguration",
        "audio_extraction_configuration": "AudioExtractionConfiguration",
        "image_extraction_configuration": "ImageExtractionConfiguration",
    }

    video_extraction_configuration: Optional[VideoExtractionConfiguration] = None
    audio_extraction_configuration: Optional[AudioExtractionConfiguration] = None
    image_extraction_configuration: Optional[ImageExtractionConfiguration] = None


@dataclass
class VideoExtractionConfiguration(PropertyType):
    VIDEO_EXTRACTION_STATUS = "VideoExtractionStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "video_extraction_status": "VideoExtractionStatus",
    }

    video_extraction_status: Optional[Union[str, Ref, GetAtt, Sub]] = None

