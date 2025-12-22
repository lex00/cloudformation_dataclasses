"""PropertyTypes for AWS::Lex::BotAlias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChannelStatus:
    """ChannelStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CREATED = "CREATED"
    FAILED = "FAILED"


class ChannelType:
    """ChannelType enum values."""

    FACEBOOK = "Facebook"
    SLACK = "Slack"
    TWILIO_SMS = "Twilio-Sms"
    KIK = "Kik"


class ContentType:
    """ContentType enum values."""

    PLAINTEXT = "PlainText"
    SSML = "SSML"
    CUSTOMPAYLOAD = "CustomPayload"


class Destination:
    """Destination enum values."""

    CLOUDWATCH_LOGS = "CLOUDWATCH_LOGS"
    S3 = "S3"


class ExportStatus:
    """ExportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    READY = "READY"
    FAILED = "FAILED"


class ExportType:
    """ExportType enum values."""

    ALEXA_SKILLS_KIT = "ALEXA_SKILLS_KIT"
    LEX = "LEX"


class FulfillmentActivityType:
    """FulfillmentActivityType enum values."""

    RETURNINTENT = "ReturnIntent"
    CODEHOOK = "CodeHook"


class ImportStatus:
    """ImportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class Locale:
    """Locale enum values."""

    DE_DE = "de-DE"
    EN_AU = "en-AU"
    EN_GB = "en-GB"
    EN_IN = "en-IN"
    EN_US = "en-US"
    ES_419 = "es-419"
    ES_ES = "es-ES"
    ES_US = "es-US"
    FR_FR = "fr-FR"
    FR_CA = "fr-CA"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"


class LogType:
    """LogType enum values."""

    AUDIO = "AUDIO"
    TEXT = "TEXT"


class MergeStrategy:
    """MergeStrategy enum values."""

    OVERWRITE_LATEST = "OVERWRITE_LATEST"
    FAIL_ON_CONFLICT = "FAIL_ON_CONFLICT"


class MigrationAlertType:
    """MigrationAlertType enum values."""

    ERROR = "ERROR"
    WARN = "WARN"


class MigrationSortAttribute:
    """MigrationSortAttribute enum values."""

    V1_BOT_NAME = "V1_BOT_NAME"
    MIGRATION_DATE_TIME = "MIGRATION_DATE_TIME"


class MigrationStatus:
    """MigrationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class MigrationStrategy:
    """MigrationStrategy enum values."""

    CREATE_NEW = "CREATE_NEW"
    UPDATE_EXISTING = "UPDATE_EXISTING"


class ObfuscationSetting:
    """ObfuscationSetting enum values."""

    NONE = "NONE"
    DEFAULT_OBFUSCATION = "DEFAULT_OBFUSCATION"


class ProcessBehavior:
    """ProcessBehavior enum values."""

    SAVE = "SAVE"
    BUILD = "BUILD"


class ReferenceType:
    """ReferenceType enum values."""

    INTENT = "Intent"
    BOT = "Bot"
    BOTALIAS = "BotAlias"
    BOTCHANNEL = "BotChannel"


class ResourceType:
    """ResourceType enum values."""

    BOT = "BOT"
    INTENT = "INTENT"
    SLOT_TYPE = "SLOT_TYPE"


class SlotConstraint:
    """SlotConstraint enum values."""

    REQUIRED = "Required"
    OPTIONAL = "Optional"


class SlotValueSelectionStrategy:
    """SlotValueSelectionStrategy enum values."""

    ORIGINAL_VALUE = "ORIGINAL_VALUE"
    TOP_RESOLUTION = "TOP_RESOLUTION"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Status:
    """Status enum values."""

    BUILDING = "BUILDING"
    READY = "READY"
    READY_BASIC_TESTING = "READY_BASIC_TESTING"
    FAILED = "FAILED"
    NOT_BUILT = "NOT_BUILT"


class StatusType:
    """StatusType enum values."""

    DETECTED = "Detected"
    MISSED = "Missed"


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

