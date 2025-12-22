"""PropertyTypes for AWS::QBusiness::WebExperience."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class APISchemaType:
    """APISchemaType enum values."""

    OPEN_API_V3 = "OPEN_API_V3"


class ActionPayloadFieldType:
    """ActionPayloadFieldType enum values."""

    STRING = "STRING"
    NUMBER = "NUMBER"
    ARRAY = "ARRAY"
    BOOLEAN = "BOOLEAN"


class ApplicationStatus:
    """ApplicationStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"


class AttachmentStatus:
    """AttachmentStatus enum values."""

    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class AttachmentsControlMode:
    """AttachmentsControlMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AttributeType:
    """AttributeType enum values."""

    STRING = "STRING"
    STRING_LIST = "STRING_LIST"
    NUMBER = "NUMBER"
    DATE = "DATE"


class AttributeValueOperator:
    """AttributeValueOperator enum values."""

    DELETE = "DELETE"


class AudioExtractionStatus:
    """AudioExtractionStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AudioExtractionType:
    """AudioExtractionType enum values."""

    TRANSCRIPT = "TRANSCRIPT"
    SUMMARY = "SUMMARY"


class AutoSubscriptionStatus:
    """AutoSubscriptionStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BrowserExtension:
    """BrowserExtension enum values."""

    FIREFOX = "FIREFOX"
    CHROME = "CHROME"


class ChatMode:
    """ChatMode enum values."""

    RETRIEVAL_MODE = "RETRIEVAL_MODE"
    CREATOR_MODE = "CREATOR_MODE"
    PLUGIN_MODE = "PLUGIN_MODE"


class ChatResponseConfigurationStatus:
    """ChatResponseConfigurationStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    FAILED = "FAILED"
    ACTIVE = "ACTIVE"


class ContentType:
    """ContentType enum values."""

    PDF = "PDF"
    HTML = "HTML"
    MS_WORD = "MS_WORD"
    PLAIN_TEXT = "PLAIN_TEXT"
    PPT = "PPT"
    RTF = "RTF"
    XML = "XML"
    XSLT = "XSLT"
    MS_EXCEL = "MS_EXCEL"
    CSV = "CSV"
    JSON = "JSON"
    MD = "MD"


class CreatorModeControl:
    """CreatorModeControl enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DataAccessorAuthenticationType:
    """DataAccessorAuthenticationType enum values."""

    AWS_IAM_IDC_TTI = "AWS_IAM_IDC_TTI"
    AWS_IAM_IDC_AUTH_CODE = "AWS_IAM_IDC_AUTH_CODE"


class DataSourceStatus:
    """DataSourceStatus enum values."""

    PENDING_CREATION = "PENDING_CREATION"
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"


class DataSourceSyncJobStatus:
    """DataSourceSyncJobStatus enum values."""

    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    SYNCING = "SYNCING"
    INCOMPLETE = "INCOMPLETE"
    STOPPING = "STOPPING"
    ABORTED = "ABORTED"
    SYNCING_INDEXING = "SYNCING_INDEXING"


class DocumentAttributeBoostingLevel:
    """DocumentAttributeBoostingLevel enum values."""

    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"
    ONE = "ONE"
    TWO = "TWO"


class DocumentContentOperator:
    """DocumentContentOperator enum values."""

    DELETE = "DELETE"


class DocumentEnrichmentConditionOperator:
    """DocumentEnrichmentConditionOperator enum values."""

    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUALS = "GREATER_THAN_OR_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUALS = "LESS_THAN_OR_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    EXISTS = "EXISTS"
    NOT_EXISTS = "NOT_EXISTS"
    BEGINS_WITH = "BEGINS_WITH"


class DocumentStatus:
    """DocumentStatus enum values."""

    RECEIVED = "RECEIVED"
    PROCESSING = "PROCESSING"
    INDEXED = "INDEXED"
    UPDATED = "UPDATED"
    FAILED = "FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DOCUMENT_FAILED_TO_INDEX = "DOCUMENT_FAILED_TO_INDEX"


class ErrorCode:
    """ErrorCode enum values."""

    INTERNALERROR = "InternalError"
    INVALIDREQUEST = "InvalidRequest"
    RESOURCEINACTIVE = "ResourceInactive"
    RESOURCENOTFOUND = "ResourceNotFound"


class GroupStatus:
    """GroupStatus enum values."""

    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    PROCESSING = "PROCESSING"
    DELETING = "DELETING"
    DELETED = "DELETED"


class HallucinationReductionControl:
    """HallucinationReductionControl enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class IdentityType:
    """IdentityType enum values."""

    AWS_IAM_IDP_SAML = "AWS_IAM_IDP_SAML"
    AWS_IAM_IDP_OIDC = "AWS_IAM_IDP_OIDC"
    AWS_IAM_IDC = "AWS_IAM_IDC"
    AWS_QUICKSIGHT_IDP = "AWS_QUICKSIGHT_IDP"
    ANONYMOUS = "ANONYMOUS"


class ImageExtractionStatus:
    """ImageExtractionStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class IndexStatus:
    """IndexStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"


class IndexType:
    """IndexType enum values."""

    ENTERPRISE = "ENTERPRISE"
    STARTER = "STARTER"


class MemberRelation:
    """MemberRelation enum values."""

    AND = "AND"
    OR = "OR"


class MembershipType:
    """MembershipType enum values."""

    INDEX = "INDEX"
    DATASOURCE = "DATASOURCE"


class MessageType:
    """MessageType enum values."""

    USER = "USER"
    SYSTEM = "SYSTEM"


class MessageUsefulness:
    """MessageUsefulness enum values."""

    USEFUL = "USEFUL"
    NOT_USEFUL = "NOT_USEFUL"


class MessageUsefulnessReason:
    """MessageUsefulnessReason enum values."""

    NOT_FACTUALLY_CORRECT = "NOT_FACTUALLY_CORRECT"
    HARMFUL_OR_UNSAFE = "HARMFUL_OR_UNSAFE"
    INCORRECT_OR_MISSING_SOURCES = "INCORRECT_OR_MISSING_SOURCES"
    NOT_HELPFUL = "NOT_HELPFUL"
    FACTUALLY_CORRECT = "FACTUALLY_CORRECT"
    COMPLETE = "COMPLETE"
    RELEVANT_SOURCES = "RELEVANT_SOURCES"
    HELPFUL = "HELPFUL"
    NOT_BASED_ON_DOCUMENTS = "NOT_BASED_ON_DOCUMENTS"
    NOT_COMPLETE = "NOT_COMPLETE"
    NOT_CONCISE = "NOT_CONCISE"
    OTHER = "OTHER"


class NumberAttributeBoostingType:
    """NumberAttributeBoostingType enum values."""

    PRIORITIZE_LARGER_VALUES = "PRIORITIZE_LARGER_VALUES"
    PRIORITIZE_SMALLER_VALUES = "PRIORITIZE_SMALLER_VALUES"


class OrchestrationControl:
    """OrchestrationControl enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OutputFormat:
    """OutputFormat enum values."""

    RAW = "RAW"
    EXTRACTED = "EXTRACTED"


class PermissionConditionOperator:
    """PermissionConditionOperator enum values."""

    STRINGEQUALS = "StringEquals"


class PersonalizationControlMode:
    """PersonalizationControlMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PluginBuildStatus:
    """PluginBuildStatus enum values."""

    READY = "READY"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class PluginState:
    """PluginState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PluginType:
    """PluginType enum values."""

    SERVICE_NOW = "SERVICE_NOW"
    SALESFORCE = "SALESFORCE"
    JIRA = "JIRA"
    ZENDESK = "ZENDESK"
    CUSTOM = "CUSTOM"
    QUICKSIGHT = "QUICKSIGHT"
    SERVICENOW_NOW_PLATFORM = "SERVICENOW_NOW_PLATFORM"
    JIRA_CLOUD = "JIRA_CLOUD"
    SALESFORCE_CRM = "SALESFORCE_CRM"
    ZENDESK_SUITE = "ZENDESK_SUITE"
    ATLASSIAN_CONFLUENCE = "ATLASSIAN_CONFLUENCE"
    GOOGLE_CALENDAR = "GOOGLE_CALENDAR"
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    MICROSOFT_EXCHANGE = "MICROSOFT_EXCHANGE"
    PAGERDUTY_ADVANCE = "PAGERDUTY_ADVANCE"
    SMARTSHEET = "SMARTSHEET"
    ASANA = "ASANA"


class PluginTypeCategory:
    """PluginTypeCategory enum values."""

    CUSTOMER_RELATIONSHIP_MANAGEMENT_CRM = "Customer relationship management (CRM)"
    PROJECT_MANAGEMENT = "Project management"
    COMMUNICATION = "Communication"
    PRODUCTIVITY = "Productivity"
    TICKETING_AND_INCIDENT_MANAGEMENT = "Ticketing and incident management"


class QAppsControlMode:
    """QAppsControlMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ReadAccessType:
    """ReadAccessType enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class ResponseConfigurationType:
    """ResponseConfigurationType enum values."""

    ALL = "ALL"


class ResponseScope:
    """ResponseScope enum values."""

    ENTERPRISE_CONTENT_ONLY = "ENTERPRISE_CONTENT_ONLY"
    EXTENDED_KNOWLEDGE_ENABLED = "EXTENDED_KNOWLEDGE_ENABLED"


class RetrieverStatus:
    """RetrieverStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class RetrieverType:
    """RetrieverType enum values."""

    NATIVE_INDEX = "NATIVE_INDEX"
    KENDRA_INDEX = "KENDRA_INDEX"


class RuleType:
    """RuleType enum values."""

    CONTENT_BLOCKER_RULE = "CONTENT_BLOCKER_RULE"
    CONTENT_RETRIEVAL_RULE = "CONTENT_RETRIEVAL_RULE"


class ScoreConfidence:
    """ScoreConfidence enum values."""

    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class Status:
    """Status enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class StringAttributeValueBoostingLevel:
    """StringAttributeValueBoostingLevel enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"


class SubscriptionType:
    """SubscriptionType enum values."""

    Q_LITE = "Q_LITE"
    Q_BUSINESS = "Q_BUSINESS"


class SystemMessageType:
    """SystemMessageType enum values."""

    RESPONSE = "RESPONSE"
    GROUNDED_RESPONSE = "GROUNDED_RESPONSE"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"


class VideoExtractionStatus:
    """VideoExtractionStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class VideoExtractionType:
    """VideoExtractionType enum values."""

    TRANSCRIPT = "TRANSCRIPT"
    SUMMARY = "SUMMARY"


class WebExperienceSamplePromptsControlMode:
    """WebExperienceSamplePromptsControlMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class WebExperienceStatus:
    """WebExperienceStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    PENDING_AUTH_CONFIG = "PENDING_AUTH_CONFIG"


@dataclass
class BrowserExtensionConfiguration(PropertyType):
    ENABLED_BROWSER_EXTENSIONS = "EnabledBrowserExtensions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_browser_extensions": "EnabledBrowserExtensions",
    }

    enabled_browser_extensions: Optional[Union[list[str], Ref]] = None


@dataclass
class CustomizationConfiguration(PropertyType):
    FAVICON_URL = "FaviconUrl"
    FONT_URL = "FontUrl"
    CUSTOM_CSS_URL = "CustomCSSUrl"
    LOGO_URL = "LogoUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "favicon_url": "FaviconUrl",
        "font_url": "FontUrl",
        "custom_css_url": "CustomCSSUrl",
        "logo_url": "LogoUrl",
    }

    favicon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    font_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_css_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logo_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    OPEN_ID_CONNECT_CONFIGURATION = "OpenIDConnectConfiguration"
    SAML_CONFIGURATION = "SamlConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_configuration": "OpenIDConnectConfiguration",
        "saml_configuration": "SamlConfiguration",
    }

    open_id_connect_configuration: Optional[OpenIDConnectProviderConfiguration] = None
    saml_configuration: Optional[SamlProviderConfiguration] = None


@dataclass
class OpenIDConnectProviderConfiguration(PropertyType):
    SECRETS_ARN = "SecretsArn"
    SECRETS_ROLE = "SecretsRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_arn": "SecretsArn",
        "secrets_role": "SecretsRole",
    }

    secrets_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SamlProviderConfiguration(PropertyType):
    AUTHENTICATION_URL = "AuthenticationUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_url": "AuthenticationUrl",
    }

    authentication_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

