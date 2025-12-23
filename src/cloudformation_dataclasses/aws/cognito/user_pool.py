"""PropertyTypes for AWS::Cognito::UserPool."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccountRecoverySetting(PropertyType):
    RECOVERY_MECHANISMS = "RecoveryMechanisms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recovery_mechanisms": "RecoveryMechanisms",
    }

    recovery_mechanisms: Optional[list[RecoveryOption]] = None


@dataclass
class AdminCreateUserConfig(PropertyType):
    INVITE_MESSAGE_TEMPLATE = "InviteMessageTemplate"
    UNUSED_ACCOUNT_VALIDITY_DAYS = "UnusedAccountValidityDays"
    ALLOW_ADMIN_CREATE_USER_ONLY = "AllowAdminCreateUserOnly"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invite_message_template": "InviteMessageTemplate",
        "unused_account_validity_days": "UnusedAccountValidityDays",
        "allow_admin_create_user_only": "AllowAdminCreateUserOnly",
    }

    invite_message_template: Optional[InviteMessageTemplate] = None
    unused_account_validity_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allow_admin_create_user_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedSecurityAdditionalFlows(PropertyType):
    CUSTOM_AUTH_MODE = "CustomAuthMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_auth_mode": "CustomAuthMode",
    }

    custom_auth_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomEmailSender(PropertyType):
    LAMBDA_ARN = "LambdaArn"
    LAMBDA_VERSION = "LambdaVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "lambda_version": "LambdaVersion",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomSMSSender(PropertyType):
    LAMBDA_ARN = "LambdaArn"
    LAMBDA_VERSION = "LambdaVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "lambda_version": "LambdaVersion",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeviceConfiguration(PropertyType):
    DEVICE_ONLY_REMEMBERED_ON_USER_PROMPT = "DeviceOnlyRememberedOnUserPrompt"
    CHALLENGE_REQUIRED_ON_NEW_DEVICE = "ChallengeRequiredOnNewDevice"

    _property_mappings: ClassVar[dict[str, str]] = {
        "device_only_remembered_on_user_prompt": "DeviceOnlyRememberedOnUserPrompt",
        "challenge_required_on_new_device": "ChallengeRequiredOnNewDevice",
    }

    device_only_remembered_on_user_prompt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    challenge_required_on_new_device: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EmailConfiguration(PropertyType):
    REPLY_TO_EMAIL_ADDRESS = "ReplyToEmailAddress"
    CONFIGURATION_SET = "ConfigurationSet"
    EMAIL_SENDING_ACCOUNT = "EmailSendingAccount"
    SOURCE_ARN = "SourceArn"
    FROM = "From"

    _property_mappings: ClassVar[dict[str, str]] = {
        "reply_to_email_address": "ReplyToEmailAddress",
        "configuration_set": "ConfigurationSet",
        "email_sending_account": "EmailSendingAccount",
        "source_arn": "SourceArn",
        "from_": "From",
    }

    reply_to_email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_set: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_sending_account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    from_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InviteMessageTemplate(PropertyType):
    EMAIL_MESSAGE = "EmailMessage"
    SMS_MESSAGE = "SMSMessage"
    EMAIL_SUBJECT = "EmailSubject"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email_message": "EmailMessage",
        "sms_message": "SMSMessage",
        "email_subject": "EmailSubject",
    }

    email_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sms_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_subject: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaConfig(PropertyType):
    CREATE_AUTH_CHALLENGE = "CreateAuthChallenge"
    PRE_SIGN_UP = "PreSignUp"
    KMS_KEY_ID = "KMSKeyID"
    USER_MIGRATION = "UserMigration"
    POST_AUTHENTICATION = "PostAuthentication"
    VERIFY_AUTH_CHALLENGE_RESPONSE = "VerifyAuthChallengeResponse"
    PRE_AUTHENTICATION = "PreAuthentication"
    DEFINE_AUTH_CHALLENGE = "DefineAuthChallenge"
    PRE_TOKEN_GENERATION = "PreTokenGeneration"
    CUSTOM_SMS_SENDER = "CustomSMSSender"
    POST_CONFIRMATION = "PostConfirmation"
    CUSTOM_MESSAGE = "CustomMessage"
    PRE_TOKEN_GENERATION_CONFIG = "PreTokenGenerationConfig"
    CUSTOM_EMAIL_SENDER = "CustomEmailSender"

    _property_mappings: ClassVar[dict[str, str]] = {
        "create_auth_challenge": "CreateAuthChallenge",
        "pre_sign_up": "PreSignUp",
        "kms_key_id": "KMSKeyID",
        "user_migration": "UserMigration",
        "post_authentication": "PostAuthentication",
        "verify_auth_challenge_response": "VerifyAuthChallengeResponse",
        "pre_authentication": "PreAuthentication",
        "define_auth_challenge": "DefineAuthChallenge",
        "pre_token_generation": "PreTokenGeneration",
        "custom_sms_sender": "CustomSMSSender",
        "post_confirmation": "PostConfirmation",
        "custom_message": "CustomMessage",
        "pre_token_generation_config": "PreTokenGenerationConfig",
        "custom_email_sender": "CustomEmailSender",
    }

    create_auth_challenge: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pre_sign_up: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_migration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    post_authentication: Optional[Union[str, Ref, GetAtt, Sub]] = None
    verify_auth_challenge_response: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pre_authentication: Optional[Union[str, Ref, GetAtt, Sub]] = None
    define_auth_challenge: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pre_token_generation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_sms_sender: Optional[CustomSMSSender] = None
    post_confirmation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pre_token_generation_config: Optional[PreTokenGenerationConfig] = None
    custom_email_sender: Optional[CustomEmailSender] = None


@dataclass
class NumberAttributeConstraints(PropertyType):
    MIN_VALUE = "MinValue"
    MAX_VALUE = "MaxValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_value": "MinValue",
        "max_value": "MaxValue",
    }

    min_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PasswordPolicy(PropertyType):
    REQUIRE_NUMBERS = "RequireNumbers"
    MINIMUM_LENGTH = "MinimumLength"
    TEMPORARY_PASSWORD_VALIDITY_DAYS = "TemporaryPasswordValidityDays"
    REQUIRE_UPPERCASE = "RequireUppercase"
    REQUIRE_LOWERCASE = "RequireLowercase"
    REQUIRE_SYMBOLS = "RequireSymbols"
    PASSWORD_HISTORY_SIZE = "PasswordHistorySize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "require_numbers": "RequireNumbers",
        "minimum_length": "MinimumLength",
        "temporary_password_validity_days": "TemporaryPasswordValidityDays",
        "require_uppercase": "RequireUppercase",
        "require_lowercase": "RequireLowercase",
        "require_symbols": "RequireSymbols",
        "password_history_size": "PasswordHistorySize",
    }

    require_numbers: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    minimum_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    temporary_password_validity_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    require_uppercase: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_lowercase: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_symbols: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password_history_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Policies(PropertyType):
    PASSWORD_POLICY = "PasswordPolicy"
    SIGN_IN_POLICY = "SignInPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "password_policy": "PasswordPolicy",
        "sign_in_policy": "SignInPolicy",
    }

    password_policy: Optional[PasswordPolicy] = None
    sign_in_policy: Optional[SignInPolicy] = None


@dataclass
class PreTokenGenerationConfig(PropertyType):
    LAMBDA_ARN = "LambdaArn"
    LAMBDA_VERSION = "LambdaVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "lambda_version": "LambdaVersion",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecoveryOption(PropertyType):
    PRIORITY = "Priority"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "name": "Name",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaAttribute(PropertyType):
    DEVELOPER_ONLY_ATTRIBUTE = "DeveloperOnlyAttribute"
    MUTABLE = "Mutable"
    ATTRIBUTE_DATA_TYPE = "AttributeDataType"
    STRING_ATTRIBUTE_CONSTRAINTS = "StringAttributeConstraints"
    REQUIRED = "Required"
    NUMBER_ATTRIBUTE_CONSTRAINTS = "NumberAttributeConstraints"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "developer_only_attribute": "DeveloperOnlyAttribute",
        "mutable": "Mutable",
        "attribute_data_type": "AttributeDataType",
        "string_attribute_constraints": "StringAttributeConstraints",
        "required": "Required",
        "number_attribute_constraints": "NumberAttributeConstraints",
        "name": "Name",
    }

    developer_only_attribute: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    mutable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    attribute_data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_attribute_constraints: Optional[StringAttributeConstraints] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    number_attribute_constraints: Optional[NumberAttributeConstraints] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SignInPolicy(PropertyType):
    ALLOWED_FIRST_AUTH_FACTORS = "AllowedFirstAuthFactors"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_first_auth_factors": "AllowedFirstAuthFactors",
    }

    allowed_first_auth_factors: Optional[Union[list[str], Ref]] = None


@dataclass
class SmsConfiguration(PropertyType):
    SNS_REGION = "SnsRegion"
    EXTERNAL_ID = "ExternalId"
    SNS_CALLER_ARN = "SnsCallerArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_region": "SnsRegion",
        "external_id": "ExternalId",
        "sns_caller_arn": "SnsCallerArn",
    }

    sns_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    external_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sns_caller_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StringAttributeConstraints(PropertyType):
    MIN_LENGTH = "MinLength"
    MAX_LENGTH = "MaxLength"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_length": "MinLength",
        "max_length": "MaxLength",
    }

    min_length: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_length: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserAttributeUpdateSettings(PropertyType):
    ATTRIBUTES_REQUIRE_VERIFICATION_BEFORE_UPDATE = "AttributesRequireVerificationBeforeUpdate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes_require_verification_before_update": "AttributesRequireVerificationBeforeUpdate",
    }

    attributes_require_verification_before_update: Optional[Union[list[str], Ref]] = None


@dataclass
class UserPoolAddOns(PropertyType):
    ADVANCED_SECURITY_ADDITIONAL_FLOWS = "AdvancedSecurityAdditionalFlows"
    ADVANCED_SECURITY_MODE = "AdvancedSecurityMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_security_additional_flows": "AdvancedSecurityAdditionalFlows",
        "advanced_security_mode": "AdvancedSecurityMode",
    }

    advanced_security_additional_flows: Optional[AdvancedSecurityAdditionalFlows] = None
    advanced_security_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UsernameConfiguration(PropertyType):
    CASE_SENSITIVE = "CaseSensitive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "case_sensitive": "CaseSensitive",
    }

    case_sensitive: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VerificationMessageTemplate(PropertyType):
    EMAIL_MESSAGE_BY_LINK = "EmailMessageByLink"
    EMAIL_MESSAGE = "EmailMessage"
    SMS_MESSAGE = "SmsMessage"
    EMAIL_SUBJECT = "EmailSubject"
    DEFAULT_EMAIL_OPTION = "DefaultEmailOption"
    EMAIL_SUBJECT_BY_LINK = "EmailSubjectByLink"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email_message_by_link": "EmailMessageByLink",
        "email_message": "EmailMessage",
        "sms_message": "SmsMessage",
        "email_subject": "EmailSubject",
        "default_email_option": "DefaultEmailOption",
        "email_subject_by_link": "EmailSubjectByLink",
    }

    email_message_by_link: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sms_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_subject: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_email_option: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_subject_by_link: Optional[Union[str, Ref, GetAtt, Sub]] = None

