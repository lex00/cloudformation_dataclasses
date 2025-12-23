"""PropertyTypes for AWS::Lex::BotAlias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AudioLogDestination(PropertyType):
    S3_BUCKET = "S3Bucket"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
    }

    s3_bucket: Optional[S3BucketLogDestination] = None


@dataclass
class AudioLogSetting(PropertyType):
    DESTINATION = "Destination"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "enabled": "Enabled",
    }

    destination: Optional[AudioLogDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class BotAliasLocaleSettings(PropertyType):
    CODE_HOOK_SPECIFICATION = "CodeHookSpecification"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "code_hook_specification": "CodeHookSpecification",
        "enabled": "Enabled",
    }

    code_hook_specification: Optional[CodeHookSpecification] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class BotAliasLocaleSettingsItem(PropertyType):
    LOCALE_ID = "LocaleId"
    BOT_ALIAS_LOCALE_SETTING = "BotAliasLocaleSetting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "locale_id": "LocaleId",
        "bot_alias_locale_setting": "BotAliasLocaleSetting",
    }

    locale_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bot_alias_locale_setting: Optional[BotAliasLocaleSettings] = None


@dataclass
class CloudWatchLogGroupLogDestination(PropertyType):
    CLOUD_WATCH_LOG_GROUP_ARN = "CloudWatchLogGroupArn"
    LOG_PREFIX = "LogPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_log_group_arn": "CloudWatchLogGroupArn",
        "log_prefix": "LogPrefix",
    }

    cloud_watch_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CodeHookSpecification(PropertyType):
    LAMBDA_CODE_HOOK = "LambdaCodeHook"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_code_hook": "LambdaCodeHook",
    }

    lambda_code_hook: Optional[LambdaCodeHook] = None


@dataclass
class ConversationLogSettings(PropertyType):
    TEXT_LOG_SETTINGS = "TextLogSettings"
    AUDIO_LOG_SETTINGS = "AudioLogSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_log_settings": "TextLogSettings",
        "audio_log_settings": "AudioLogSettings",
    }

    text_log_settings: Optional[list[TextLogSetting]] = None
    audio_log_settings: Optional[list[AudioLogSetting]] = None


@dataclass
class LambdaCodeHook(PropertyType):
    LAMBDA_ARN = "LambdaArn"
    CODE_HOOK_INTERFACE_VERSION = "CodeHookInterfaceVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "code_hook_interface_version": "CodeHookInterfaceVersion",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code_hook_interface_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3BucketLogDestination(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    LOG_PREFIX = "LogPrefix"
    S3_BUCKET_ARN = "S3BucketArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "log_prefix": "LogPrefix",
        "s3_bucket_arn": "S3BucketArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SentimentAnalysisSettings(PropertyType):
    DETECT_SENTIMENT = "DetectSentiment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "detect_sentiment": "DetectSentiment",
    }

    detect_sentiment: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TextLogDestination(PropertyType):
    CLOUD_WATCH = "CloudWatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch": "CloudWatch",
    }

    cloud_watch: Optional[CloudWatchLogGroupLogDestination] = None


@dataclass
class TextLogSetting(PropertyType):
    DESTINATION = "Destination"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "enabled": "Enabled",
    }

    destination: Optional[TextLogDestination] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

