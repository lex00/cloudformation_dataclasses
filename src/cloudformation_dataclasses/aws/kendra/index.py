"""PropertyTypes for AWS::Kendra::Index."""

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
class CapacityUnitsConfiguration(PropertyType):
    QUERY_CAPACITY_UNITS = "QueryCapacityUnits"
    STORAGE_CAPACITY_UNITS = "StorageCapacityUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_capacity_units": "QueryCapacityUnits",
        "storage_capacity_units": "StorageCapacityUnits",
    }

    query_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    storage_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentMetadataConfiguration(PropertyType):
    RELEVANCE = "Relevance"
    TYPE = "Type"
    SEARCH = "Search"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "relevance": "Relevance",
        "type_": "Type",
        "search": "Search",
        "name": "Name",
    }

    relevance: Optional[Relevance] = None
    type_: Optional[Union[str, DocumentAttributeValueType, Ref, GetAtt, Sub]] = None
    search: Optional[Search] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JsonTokenTypeConfiguration(PropertyType):
    GROUP_ATTRIBUTE_FIELD = "GroupAttributeField"
    USER_NAME_ATTRIBUTE_FIELD = "UserNameAttributeField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_attribute_field": "GroupAttributeField",
        "user_name_attribute_field": "UserNameAttributeField",
    }

    group_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_name_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JwtTokenTypeConfiguration(PropertyType):
    CLAIM_REGEX = "ClaimRegex"
    ISSUER = "Issuer"
    KEY_LOCATION = "KeyLocation"
    SECRET_MANAGER_ARN = "SecretManagerArn"
    GROUP_ATTRIBUTE_FIELD = "GroupAttributeField"
    URL = "URL"
    USER_NAME_ATTRIBUTE_FIELD = "UserNameAttributeField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "claim_regex": "ClaimRegex",
        "issuer": "Issuer",
        "key_location": "KeyLocation",
        "secret_manager_arn": "SecretManagerArn",
        "group_attribute_field": "GroupAttributeField",
        "url": "URL",
        "user_name_attribute_field": "UserNameAttributeField",
    }

    claim_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_location: Optional[Union[str, KeyLocation, Ref, GetAtt, Sub]] = None
    secret_manager_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_name_attribute_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Relevance(PropertyType):
    IMPORTANCE = "Importance"
    RANK_ORDER = "RankOrder"
    VALUE_IMPORTANCE_ITEMS = "ValueImportanceItems"
    FRESHNESS = "Freshness"
    DURATION = "Duration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "importance": "Importance",
        "rank_order": "RankOrder",
        "value_importance_items": "ValueImportanceItems",
        "freshness": "Freshness",
        "duration": "Duration",
    }

    importance: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rank_order: Optional[Union[str, Order, Ref, GetAtt, Sub]] = None
    value_importance_items: Optional[list[ValueImportanceItem]] = None
    freshness: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    duration: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Search(PropertyType):
    DISPLAYABLE = "Displayable"
    SORTABLE = "Sortable"
    FACETABLE = "Facetable"
    SEARCHABLE = "Searchable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "displayable": "Displayable",
        "sortable": "Sortable",
        "facetable": "Facetable",
        "searchable": "Searchable",
    }

    displayable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sortable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    facetable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    searchable: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserTokenConfiguration(PropertyType):
    JWT_TOKEN_TYPE_CONFIGURATION = "JwtTokenTypeConfiguration"
    JSON_TOKEN_TYPE_CONFIGURATION = "JsonTokenTypeConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jwt_token_type_configuration": "JwtTokenTypeConfiguration",
        "json_token_type_configuration": "JsonTokenTypeConfiguration",
    }

    jwt_token_type_configuration: Optional[JwtTokenTypeConfiguration] = None
    json_token_type_configuration: Optional[JsonTokenTypeConfiguration] = None


@dataclass
class ValueImportanceItem(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

