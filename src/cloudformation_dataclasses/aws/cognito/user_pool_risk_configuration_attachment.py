"""PropertyTypes for AWS::Cognito::UserPoolRiskConfigurationAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountTakeoverEventActionType:
    """AccountTakeoverEventActionType enum values."""

    BLOCK = "BLOCK"
    MFA_IF_CONFIGURED = "MFA_IF_CONFIGURED"
    MFA_REQUIRED = "MFA_REQUIRED"
    NO_ACTION = "NO_ACTION"


class AdvancedSecurityEnabledModeType:
    """AdvancedSecurityEnabledModeType enum values."""

    AUDIT = "AUDIT"
    ENFORCED = "ENFORCED"


class AdvancedSecurityModeType:
    """AdvancedSecurityModeType enum values."""

    OFF = "OFF"
    AUDIT = "AUDIT"
    ENFORCED = "ENFORCED"


class AliasAttributeType:
    """AliasAttributeType enum values."""

    PHONE_NUMBER = "phone_number"
    EMAIL = "email"
    PREFERRED_USERNAME = "preferred_username"


class AssetCategoryType:
    """AssetCategoryType enum values."""

    FAVICON_ICO = "FAVICON_ICO"
    FAVICON_SVG = "FAVICON_SVG"
    EMAIL_GRAPHIC = "EMAIL_GRAPHIC"
    SMS_GRAPHIC = "SMS_GRAPHIC"
    AUTH_APP_GRAPHIC = "AUTH_APP_GRAPHIC"
    PASSWORD_GRAPHIC = "PASSWORD_GRAPHIC"
    PASSKEY_GRAPHIC = "PASSKEY_GRAPHIC"
    PAGE_HEADER_LOGO = "PAGE_HEADER_LOGO"
    PAGE_HEADER_BACKGROUND = "PAGE_HEADER_BACKGROUND"
    PAGE_FOOTER_LOGO = "PAGE_FOOTER_LOGO"
    PAGE_FOOTER_BACKGROUND = "PAGE_FOOTER_BACKGROUND"
    PAGE_BACKGROUND = "PAGE_BACKGROUND"
    FORM_BACKGROUND = "FORM_BACKGROUND"
    FORM_LOGO = "FORM_LOGO"
    IDP_BUTTON_ICON = "IDP_BUTTON_ICON"


class AssetExtensionType:
    """AssetExtensionType enum values."""

    ICO = "ICO"
    JPEG = "JPEG"
    PNG = "PNG"
    SVG = "SVG"
    WEBP = "WEBP"


class AttributeDataType:
    """AttributeDataType enum values."""

    STRING = "String"
    NUMBER = "Number"
    DATETIME = "DateTime"
    BOOLEAN = "Boolean"


class AuthFactorType:
    """AuthFactorType enum values."""

    PASSWORD = "PASSWORD"
    EMAIL_OTP = "EMAIL_OTP"
    SMS_OTP = "SMS_OTP"
    WEB_AUTHN = "WEB_AUTHN"


class AuthFlowType:
    """AuthFlowType enum values."""

    USER_SRP_AUTH = "USER_SRP_AUTH"
    REFRESH_TOKEN_AUTH = "REFRESH_TOKEN_AUTH"
    REFRESH_TOKEN = "REFRESH_TOKEN"
    CUSTOM_AUTH = "CUSTOM_AUTH"
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"
    ADMIN_USER_PASSWORD_AUTH = "ADMIN_USER_PASSWORD_AUTH"
    USER_AUTH = "USER_AUTH"


class ChallengeName:
    """ChallengeName enum values."""

    PASSWORD = "Password"
    MFA = "Mfa"


class ChallengeNameType:
    """ChallengeNameType enum values."""

    SMS_MFA = "SMS_MFA"
    EMAIL_OTP = "EMAIL_OTP"
    SOFTWARE_TOKEN_MFA = "SOFTWARE_TOKEN_MFA"
    SELECT_MFA_TYPE = "SELECT_MFA_TYPE"
    MFA_SETUP = "MFA_SETUP"
    PASSWORD_VERIFIER = "PASSWORD_VERIFIER"
    CUSTOM_CHALLENGE = "CUSTOM_CHALLENGE"
    SELECT_CHALLENGE = "SELECT_CHALLENGE"
    DEVICE_SRP_AUTH = "DEVICE_SRP_AUTH"
    DEVICE_PASSWORD_VERIFIER = "DEVICE_PASSWORD_VERIFIER"
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    NEW_PASSWORD_REQUIRED = "NEW_PASSWORD_REQUIRED"
    SMS_OTP = "SMS_OTP"
    PASSWORD = "PASSWORD"
    WEB_AUTHN = "WEB_AUTHN"
    PASSWORD_SRP = "PASSWORD_SRP"


class ChallengeResponse:
    """ChallengeResponse enum values."""

    SUCCESS = "Success"
    FAILURE = "Failure"


class ColorSchemeModeType:
    """ColorSchemeModeType enum values."""

    LIGHT = "LIGHT"
    DARK = "DARK"
    DYNAMIC = "DYNAMIC"


class CompromisedCredentialsEventActionType:
    """CompromisedCredentialsEventActionType enum values."""

    BLOCK = "BLOCK"
    NO_ACTION = "NO_ACTION"


class CustomEmailSenderLambdaVersionType:
    """CustomEmailSenderLambdaVersionType enum values."""

    V1_0 = "V1_0"


class CustomSMSSenderLambdaVersionType:
    """CustomSMSSenderLambdaVersionType enum values."""

    V1_0 = "V1_0"


class DefaultEmailOptionType:
    """DefaultEmailOptionType enum values."""

    CONFIRM_WITH_LINK = "CONFIRM_WITH_LINK"
    CONFIRM_WITH_CODE = "CONFIRM_WITH_CODE"


class DeletionProtectionType:
    """DeletionProtectionType enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class DeliveryMediumType:
    """DeliveryMediumType enum values."""

    SMS = "SMS"
    EMAIL = "EMAIL"


class DeviceRememberedStatusType:
    """DeviceRememberedStatusType enum values."""

    REMEMBERED = "remembered"
    NOT_REMEMBERED = "not_remembered"


class DomainStatusType:
    """DomainStatusType enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class EmailSendingAccountType:
    """EmailSendingAccountType enum values."""

    COGNITO_DEFAULT = "COGNITO_DEFAULT"
    DEVELOPER = "DEVELOPER"


class EventFilterType:
    """EventFilterType enum values."""

    SIGN_IN = "SIGN_IN"
    PASSWORD_CHANGE = "PASSWORD_CHANGE"
    SIGN_UP = "SIGN_UP"


class EventResponseType:
    """EventResponseType enum values."""

    PASS = "Pass"
    FAIL = "Fail"
    INPROGRESS = "InProgress"


class EventSourceName:
    """EventSourceName enum values."""

    USERNOTIFICATION = "userNotification"
    USERAUTHEVENTS = "userAuthEvents"


class EventType:
    """EventType enum values."""

    SIGNIN = "SignIn"
    SIGNUP = "SignUp"
    FORGOTPASSWORD = "ForgotPassword"
    PASSWORDCHANGE = "PasswordChange"
    RESENDCODE = "ResendCode"


class ExplicitAuthFlowsType:
    """ExplicitAuthFlowsType enum values."""

    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    CUSTOM_AUTH_FLOW_ONLY = "CUSTOM_AUTH_FLOW_ONLY"
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"
    ALLOW_ADMIN_USER_PASSWORD_AUTH = "ALLOW_ADMIN_USER_PASSWORD_AUTH"
    ALLOW_CUSTOM_AUTH = "ALLOW_CUSTOM_AUTH"
    ALLOW_USER_PASSWORD_AUTH = "ALLOW_USER_PASSWORD_AUTH"
    ALLOW_USER_SRP_AUTH = "ALLOW_USER_SRP_AUTH"
    ALLOW_REFRESH_TOKEN_AUTH = "ALLOW_REFRESH_TOKEN_AUTH"
    ALLOW_USER_AUTH = "ALLOW_USER_AUTH"


class FeatureType:
    """FeatureType enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FeedbackValueType:
    """FeedbackValueType enum values."""

    VALID = "Valid"
    INVALID = "Invalid"


class IdentityProviderTypeType:
    """IdentityProviderTypeType enum values."""

    SAML = "SAML"
    FACEBOOK = "Facebook"
    GOOGLE = "Google"
    LOGINWITHAMAZON = "LoginWithAmazon"
    SIGNINWITHAPPLE = "SignInWithApple"
    OIDC = "OIDC"


class LogLevel:
    """LogLevel enum values."""

    ERROR = "ERROR"
    INFO = "INFO"


class MessageActionType:
    """MessageActionType enum values."""

    RESEND = "RESEND"
    SUPPRESS = "SUPPRESS"


class OAuthFlowType:
    """OAuthFlowType enum values."""

    CODE = "code"
    IMPLICIT = "implicit"
    CLIENT_CREDENTIALS = "client_credentials"


class PreTokenGenerationLambdaVersionType:
    """PreTokenGenerationLambdaVersionType enum values."""

    V1_0 = "V1_0"
    V2_0 = "V2_0"
    V3_0 = "V3_0"


class PreventUserExistenceErrorTypes:
    """PreventUserExistenceErrorTypes enum values."""

    LEGACY = "LEGACY"
    ENABLED = "ENABLED"


class RecoveryOptionNameType:
    """RecoveryOptionNameType enum values."""

    VERIFIED_EMAIL = "verified_email"
    VERIFIED_PHONE_NUMBER = "verified_phone_number"
    ADMIN_ONLY = "admin_only"


class RiskDecisionType:
    """RiskDecisionType enum values."""

    NORISK = "NoRisk"
    ACCOUNTTAKEOVER = "AccountTakeover"
    BLOCK = "Block"


class RiskLevelType:
    """RiskLevelType enum values."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class StatusType:
    """StatusType enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TermsEnforcementType:
    """TermsEnforcementType enum values."""

    NONE = "NONE"


class TermsSourceType:
    """TermsSourceType enum values."""

    LINK = "LINK"


class TimeUnitsType:
    """TimeUnitsType enum values."""

    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"


class UserImportJobStatusType:
    """UserImportJobStatusType enum values."""

    CREATED = "Created"
    PENDING = "Pending"
    INPROGRESS = "InProgress"
    STOPPING = "Stopping"
    EXPIRED = "Expired"
    STOPPED = "Stopped"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"


class UserPoolMfaType:
    """UserPoolMfaType enum values."""

    OFF = "OFF"
    ON = "ON"
    OPTIONAL = "OPTIONAL"


class UserPoolTierType:
    """UserPoolTierType enum values."""

    LITE = "LITE"
    ESSENTIALS = "ESSENTIALS"
    PLUS = "PLUS"


class UserStatusType:
    """UserStatusType enum values."""

    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"
    ARCHIVED = "ARCHIVED"
    COMPROMISED = "COMPROMISED"
    UNKNOWN = "UNKNOWN"
    RESET_REQUIRED = "RESET_REQUIRED"
    FORCE_CHANGE_PASSWORD = "FORCE_CHANGE_PASSWORD"
    EXTERNAL_PROVIDER = "EXTERNAL_PROVIDER"


class UserVerificationType:
    """UserVerificationType enum values."""

    REQUIRED = "required"
    PREFERRED = "preferred"


class UsernameAttributeType:
    """UsernameAttributeType enum values."""

    PHONE_NUMBER = "phone_number"
    EMAIL = "email"


class VerifiedAttributeType:
    """VerifiedAttributeType enum values."""

    PHONE_NUMBER = "phone_number"
    EMAIL = "email"


class VerifySoftwareTokenResponseType:
    """VerifySoftwareTokenResponseType enum values."""

    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


@dataclass
class AccountTakeoverActionType(PropertyType):
    NOTIFY = "Notify"
    EVENT_ACTION = "EventAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notify": "Notify",
        "event_action": "EventAction",
    }

    notify: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    event_action: Optional[Union[str, AccountTakeoverEventActionType, Ref, GetAtt, Sub]] = None


@dataclass
class AccountTakeoverActionsType(PropertyType):
    HIGH_ACTION = "HighAction"
    LOW_ACTION = "LowAction"
    MEDIUM_ACTION = "MediumAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "high_action": "HighAction",
        "low_action": "LowAction",
        "medium_action": "MediumAction",
    }

    high_action: Optional[AccountTakeoverActionType] = None
    low_action: Optional[AccountTakeoverActionType] = None
    medium_action: Optional[AccountTakeoverActionType] = None


@dataclass
class AccountTakeoverRiskConfigurationType(PropertyType):
    ACTIONS = "Actions"
    NOTIFY_CONFIGURATION = "NotifyConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "notify_configuration": "NotifyConfiguration",
    }

    actions: Optional[AccountTakeoverActionsType] = None
    notify_configuration: Optional[NotifyConfigurationType] = None


@dataclass
class CompromisedCredentialsActionsType(PropertyType):
    EVENT_ACTION = "EventAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_action": "EventAction",
    }

    event_action: Optional[Union[str, CompromisedCredentialsEventActionType, Ref, GetAtt, Sub]] = None


@dataclass
class CompromisedCredentialsRiskConfigurationType(PropertyType):
    ACTIONS = "Actions"
    EVENT_FILTER = "EventFilter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "event_filter": "EventFilter",
    }

    actions: Optional[CompromisedCredentialsActionsType] = None
    event_filter: Optional[Union[list[str], Ref]] = None


@dataclass
class NotifyConfigurationType(PropertyType):
    BLOCK_EMAIL = "BlockEmail"
    REPLY_TO = "ReplyTo"
    SOURCE_ARN = "SourceArn"
    NO_ACTION_EMAIL = "NoActionEmail"
    FROM = "From"
    MFA_EMAIL = "MfaEmail"

    _property_mappings: ClassVar[dict[str, str]] = {
        "block_email": "BlockEmail",
        "reply_to": "ReplyTo",
        "source_arn": "SourceArn",
        "no_action_email": "NoActionEmail",
        "from_": "From",
        "mfa_email": "MfaEmail",
    }

    block_email: Optional[NotifyEmailType] = None
    reply_to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    no_action_email: Optional[NotifyEmailType] = None
    from_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mfa_email: Optional[NotifyEmailType] = None


@dataclass
class NotifyEmailType(PropertyType):
    TEXT_BODY = "TextBody"
    HTML_BODY = "HtmlBody"
    SUBJECT = "Subject"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_body": "TextBody",
        "html_body": "HtmlBody",
        "subject": "Subject",
    }

    text_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    html_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RiskExceptionConfigurationType(PropertyType):
    BLOCKED_IP_RANGE_LIST = "BlockedIPRangeList"
    SKIPPED_IP_RANGE_LIST = "SkippedIPRangeList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "blocked_ip_range_list": "BlockedIPRangeList",
        "skipped_ip_range_list": "SkippedIPRangeList",
    }

    blocked_ip_range_list: Optional[Union[list[str], Ref]] = None
    skipped_ip_range_list: Optional[Union[list[str], Ref]] = None

