"""PropertyTypes for AWS::S3ObjectLambda::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Alias(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "value": "Value",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsLambda(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionArn",
        "function_payload": "FunctionPayload",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    function_payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContentTransformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_lambda": "AwsLambda",
    }

    aws_lambda: Optional[AwsLambda] = None


@dataclass
class ObjectLambdaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supporting_access_point": "SupportingAccessPoint",
        "transformation_configurations": "TransformationConfigurations",
        "allowed_features": "AllowedFeatures",
        "cloud_watch_metrics_enabled": "CloudWatchMetricsEnabled",
    }

    supporting_access_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transformation_configurations: Optional[list[TransformationConfiguration]] = None
    allowed_features: Optional[Union[list[str], Ref]] = None
    cloud_watch_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "restrict_public_buckets": "RestrictPublicBuckets",
        "block_public_policy": "BlockPublicPolicy",
        "block_public_acls": "BlockPublicAcls",
        "ignore_public_acls": "IgnorePublicAcls",
    }

    restrict_public_buckets: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    block_public_policy: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    block_public_acls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ignore_public_acls: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TransformationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "content_transformation": "ContentTransformation",
    }

    actions: Optional[Union[list[str], Ref]] = None
    content_transformation: Optional[ContentTransformation] = None

