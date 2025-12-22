"""PropertyTypes for AWS::Kendra::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AdditionalResultAttributeValueType:
    """AdditionalResultAttributeValueType enum values."""

    TEXT_WITH_HIGHLIGHTS_VALUE = "TEXT_WITH_HIGHLIGHTS_VALUE"


class AlfrescoEntity:
    """AlfrescoEntity enum values."""

    WIKI = "wiki"
    BLOG = "blog"
    DOCUMENTLIBRARY = "documentLibrary"


class AttributeSuggestionsMode:
    """AttributeSuggestionsMode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ConditionOperator:
    """ConditionOperator enum values."""

    GREATERTHAN = "GreaterThan"
    GREATERTHANOREQUALS = "GreaterThanOrEquals"
    LESSTHAN = "LessThan"
    LESSTHANOREQUALS = "LessThanOrEquals"
    EQUALS = "Equals"
    NOTEQUALS = "NotEquals"
    CONTAINS = "Contains"
    NOTCONTAINS = "NotContains"
    EXISTS = "Exists"
    NOTEXISTS = "NotExists"
    BEGINSWITH = "BeginsWith"


class ConfluenceAttachmentFieldName:
    """ConfluenceAttachmentFieldName enum values."""

    AUTHOR = "AUTHOR"
    CONTENT_TYPE = "CONTENT_TYPE"
    CREATED_DATE = "CREATED_DATE"
    DISPLAY_URL = "DISPLAY_URL"
    FILE_SIZE = "FILE_SIZE"
    ITEM_TYPE = "ITEM_TYPE"
    PARENT_ID = "PARENT_ID"
    SPACE_KEY = "SPACE_KEY"
    SPACE_NAME = "SPACE_NAME"
    URL = "URL"
    VERSION = "VERSION"


class ConfluenceAuthenticationType:
    """ConfluenceAuthenticationType enum values."""

    HTTP_BASIC = "HTTP_BASIC"
    PAT = "PAT"


class ConfluenceBlogFieldName:
    """ConfluenceBlogFieldName enum values."""

    AUTHOR = "AUTHOR"
    DISPLAY_URL = "DISPLAY_URL"
    ITEM_TYPE = "ITEM_TYPE"
    LABELS = "LABELS"
    PUBLISH_DATE = "PUBLISH_DATE"
    SPACE_KEY = "SPACE_KEY"
    SPACE_NAME = "SPACE_NAME"
    URL = "URL"
    VERSION = "VERSION"


class ConfluencePageFieldName:
    """ConfluencePageFieldName enum values."""

    AUTHOR = "AUTHOR"
    CONTENT_STATUS = "CONTENT_STATUS"
    CREATED_DATE = "CREATED_DATE"
    DISPLAY_URL = "DISPLAY_URL"
    ITEM_TYPE = "ITEM_TYPE"
    LABELS = "LABELS"
    MODIFIED_DATE = "MODIFIED_DATE"
    PARENT_ID = "PARENT_ID"
    SPACE_KEY = "SPACE_KEY"
    SPACE_NAME = "SPACE_NAME"
    URL = "URL"
    VERSION = "VERSION"


class ConfluenceSpaceFieldName:
    """ConfluenceSpaceFieldName enum values."""

    DISPLAY_URL = "DISPLAY_URL"
    ITEM_TYPE = "ITEM_TYPE"
    SPACE_KEY = "SPACE_KEY"
    URL = "URL"


class ConfluenceVersion:
    """ConfluenceVersion enum values."""

    CLOUD = "CLOUD"
    SERVER = "SERVER"


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


class DataSourceStatus:
    """DataSourceStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"


class DataSourceSyncJobStatus:
    """DataSourceSyncJobStatus enum values."""

    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    SYNCING = "SYNCING"
    INCOMPLETE = "INCOMPLETE"
    STOPPING = "STOPPING"
    ABORTED = "ABORTED"
    SYNCING_INDEXING = "SYNCING_INDEXING"


class DataSourceType:
    """DataSourceType enum values."""

    S3 = "S3"
    SHAREPOINT = "SHAREPOINT"
    DATABASE = "DATABASE"
    SALESFORCE = "SALESFORCE"
    ONEDRIVE = "ONEDRIVE"
    SERVICENOW = "SERVICENOW"
    CUSTOM = "CUSTOM"
    CONFLUENCE = "CONFLUENCE"
    GOOGLEDRIVE = "GOOGLEDRIVE"
    WEBCRAWLER = "WEBCRAWLER"
    WORKDOCS = "WORKDOCS"
    FSX = "FSX"
    SLACK = "SLACK"
    BOX = "BOX"
    QUIP = "QUIP"
    JIRA = "JIRA"
    GITHUB = "GITHUB"
    ALFRESCO = "ALFRESCO"
    TEMPLATE = "TEMPLATE"


class DatabaseEngineType:
    """DatabaseEngineType enum values."""

    RDS_AURORA_MYSQL = "RDS_AURORA_MYSQL"
    RDS_AURORA_POSTGRESQL = "RDS_AURORA_POSTGRESQL"
    RDS_MYSQL = "RDS_MYSQL"
    RDS_POSTGRESQL = "RDS_POSTGRESQL"


class DocumentAttributeValueType:
    """DocumentAttributeValueType enum values."""

    STRING_VALUE = "STRING_VALUE"
    STRING_LIST_VALUE = "STRING_LIST_VALUE"
    LONG_VALUE = "LONG_VALUE"
    DATE_VALUE = "DATE_VALUE"


class DocumentStatus:
    """DocumentStatus enum values."""

    NOT_FOUND = "NOT_FOUND"
    PROCESSING = "PROCESSING"
    INDEXED = "INDEXED"
    UPDATED = "UPDATED"
    FAILED = "FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"


class EndpointType:
    """EndpointType enum values."""

    HOME = "HOME"


class EntityType:
    """EntityType enum values."""

    USER = "USER"
    GROUP = "GROUP"


class ErrorCode:
    """ErrorCode enum values."""

    INTERNALERROR = "InternalError"
    INVALIDREQUEST = "InvalidRequest"


class ExperienceStatus:
    """ExperienceStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"


class FaqFileFormat:
    """FaqFileFormat enum values."""

    CSV = "CSV"
    CSV_WITH_HEADER = "CSV_WITH_HEADER"
    JSON = "JSON"


class FaqStatus:
    """FaqStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"


class FeaturedResultsSetStatus:
    """FeaturedResultsSetStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class FsxFileSystemType:
    """FsxFileSystemType enum values."""

    WINDOWS = "WINDOWS"


class HighlightType:
    """HighlightType enum values."""

    STANDARD = "STANDARD"
    THESAURUS_SYNONYM = "THESAURUS_SYNONYM"


class IndexEdition:
    """IndexEdition enum values."""

    DEVELOPER_EDITION = "DEVELOPER_EDITION"
    ENTERPRISE_EDITION = "ENTERPRISE_EDITION"
    GEN_AI_ENTERPRISE_EDITION = "GEN_AI_ENTERPRISE_EDITION"


class IndexStatus:
    """IndexStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    SYSTEM_UPDATING = "SYSTEM_UPDATING"


class Interval:
    """Interval enum values."""

    THIS_MONTH = "THIS_MONTH"
    THIS_WEEK = "THIS_WEEK"
    ONE_WEEK_AGO = "ONE_WEEK_AGO"
    TWO_WEEKS_AGO = "TWO_WEEKS_AGO"
    ONE_MONTH_AGO = "ONE_MONTH_AGO"
    TWO_MONTHS_AGO = "TWO_MONTHS_AGO"


class IssueSubEntity:
    """IssueSubEntity enum values."""

    COMMENTS = "COMMENTS"
    ATTACHMENTS = "ATTACHMENTS"
    WORKLOGS = "WORKLOGS"


class KeyLocation:
    """KeyLocation enum values."""

    URL = "URL"
    SECRET_MANAGER = "SECRET_MANAGER"


class MetricType:
    """MetricType enum values."""

    QUERIES_BY_COUNT = "QUERIES_BY_COUNT"
    QUERIES_BY_ZERO_CLICK_RATE = "QUERIES_BY_ZERO_CLICK_RATE"
    QUERIES_BY_ZERO_RESULT_RATE = "QUERIES_BY_ZERO_RESULT_RATE"
    DOCS_BY_CLICK_COUNT = "DOCS_BY_CLICK_COUNT"
    AGG_QUERY_DOC_METRICS = "AGG_QUERY_DOC_METRICS"
    TREND_QUERY_DOC_METRICS = "TREND_QUERY_DOC_METRICS"


class MissingAttributeKeyStrategy:
    """MissingAttributeKeyStrategy enum values."""

    IGNORE = "IGNORE"
    COLLAPSE = "COLLAPSE"
    EXPAND = "EXPAND"


class Mode:
    """Mode enum values."""

    ENABLED = "ENABLED"
    LEARN_ONLY = "LEARN_ONLY"


class Order:
    """Order enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Persona:
    """Persona enum values."""

    OWNER = "OWNER"
    VIEWER = "VIEWER"


class PrincipalMappingStatus:
    """PrincipalMappingStatus enum values."""

    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    PROCESSING = "PROCESSING"
    DELETING = "DELETING"
    DELETED = "DELETED"


class PrincipalType:
    """PrincipalType enum values."""

    USER = "USER"
    GROUP = "GROUP"


class QueryIdentifiersEnclosingOption:
    """QueryIdentifiersEnclosingOption enum values."""

    DOUBLE_QUOTES = "DOUBLE_QUOTES"
    NONE = "NONE"


class QueryResultFormat:
    """QueryResultFormat enum values."""

    TABLE = "TABLE"
    TEXT = "TEXT"


class QueryResultType:
    """QueryResultType enum values."""

    DOCUMENT = "DOCUMENT"
    QUESTION_ANSWER = "QUESTION_ANSWER"
    ANSWER = "ANSWER"


class QuerySuggestionsBlockListStatus:
    """QuerySuggestionsBlockListStatus enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ACTIVE_BUT_UPDATE_FAILED = "ACTIVE_BUT_UPDATE_FAILED"
    FAILED = "FAILED"


class QuerySuggestionsStatus:
    """QuerySuggestionsStatus enum values."""

    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"


class ReadAccessType:
    """ReadAccessType enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class RelevanceType:
    """RelevanceType enum values."""

    RELEVANT = "RELEVANT"
    NOT_RELEVANT = "NOT_RELEVANT"


class SalesforceChatterFeedIncludeFilterType:
    """SalesforceChatterFeedIncludeFilterType enum values."""

    ACTIVE_USER = "ACTIVE_USER"
    STANDARD_USER = "STANDARD_USER"


class SalesforceKnowledgeArticleState:
    """SalesforceKnowledgeArticleState enum values."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"


class SalesforceStandardObjectName:
    """SalesforceStandardObjectName enum values."""

    ACCOUNT = "ACCOUNT"
    CAMPAIGN = "CAMPAIGN"
    CASE = "CASE"
    CONTACT = "CONTACT"
    CONTRACT = "CONTRACT"
    DOCUMENT = "DOCUMENT"
    GROUP = "GROUP"
    IDEA = "IDEA"
    LEAD = "LEAD"
    OPPORTUNITY = "OPPORTUNITY"
    PARTNER = "PARTNER"
    PRICEBOOK = "PRICEBOOK"
    PRODUCT = "PRODUCT"
    PROFILE = "PROFILE"
    SOLUTION = "SOLUTION"
    TASK = "TASK"
    USER = "USER"


class ScoreConfidence:
    """ScoreConfidence enum values."""

    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class ServiceNowAuthenticationType:
    """ServiceNowAuthenticationType enum values."""

    HTTP_BASIC = "HTTP_BASIC"
    OAUTH2 = "OAUTH2"


class ServiceNowBuildVersionType:
    """ServiceNowBuildVersionType enum values."""

    LONDON = "LONDON"
    OTHERS = "OTHERS"


class SharePointOnlineAuthenticationType:
    """SharePointOnlineAuthenticationType enum values."""

    HTTP_BASIC = "HTTP_BASIC"
    OAUTH2 = "OAUTH2"


class SharePointVersion:
    """SharePointVersion enum values."""

    SHAREPOINT_2013 = "SHAREPOINT_2013"
    SHAREPOINT_2016 = "SHAREPOINT_2016"
    SHAREPOINT_ONLINE = "SHAREPOINT_ONLINE"
    SHAREPOINT_2019 = "SHAREPOINT_2019"


class SlackEntity:
    """SlackEntity enum values."""

    PUBLIC_CHANNEL = "PUBLIC_CHANNEL"
    PRIVATE_CHANNEL = "PRIVATE_CHANNEL"
    GROUP_MESSAGE = "GROUP_MESSAGE"
    DIRECT_MESSAGE = "DIRECT_MESSAGE"


class SortOrder:
    """SortOrder enum values."""

    DESC = "DESC"
    ASC = "ASC"


class SuggestionType:
    """SuggestionType enum values."""

    QUERY = "QUERY"
    DOCUMENT_ATTRIBUTES = "DOCUMENT_ATTRIBUTES"


class ThesaurusStatus:
    """ThesaurusStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ACTIVE_BUT_UPDATE_FAILED = "ACTIVE_BUT_UPDATE_FAILED"
    FAILED = "FAILED"


class Type:
    """Type enum values."""

    SAAS = "SAAS"
    ON_PREMISE = "ON_PREMISE"


class UserContextPolicy:
    """UserContextPolicy enum values."""

    ATTRIBUTE_FILTER = "ATTRIBUTE_FILTER"
    USER_TOKEN = "USER_TOKEN"


class UserGroupResolutionMode:
    """UserGroupResolutionMode enum values."""

    AWS_SSO = "AWS_SSO"
    NONE = "NONE"


class WarningCode:
    """WarningCode enum values."""

    QUERY_LANGUAGE_INVALID_SYNTAX = "QUERY_LANGUAGE_INVALID_SYNTAX"


class WebCrawlerMode:
    """WebCrawlerMode enum values."""

    HOST_ONLY = "HOST_ONLY"
    SUBDOMAINS = "SUBDOMAINS"
    EVERYTHING = "EVERYTHING"


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

