"""PropertyTypes for AWS::QBusiness::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AudioExtractionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_extraction_status": "AudioExtractionStatus",
    }

    audio_extraction_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSourceVpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class DocumentAttributeCondition(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "image_extraction_status": "ImageExtractionStatus",
    }

    image_extraction_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InlineDocumentEnrichmentConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "video_extraction_status": "VideoExtractionStatus",
    }

    video_extraction_status: Optional[Union[str, Ref, GetAtt, Sub]] = None

