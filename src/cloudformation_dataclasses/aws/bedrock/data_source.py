"""PropertyTypes for AWS::Bedrock::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AgreementStatus:
    """AgreementStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    ERROR = "ERROR"


class ApplicationType:
    """ApplicationType enum values."""

    MODELEVALUATION = "ModelEvaluation"
    RAGEVALUATION = "RagEvaluation"


class AttributeType:
    """AttributeType enum values."""

    STRING = "STRING"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    STRING_LIST = "STRING_LIST"


class AuthorizationStatus:
    """AuthorizationStatus enum values."""

    AUTHORIZED = "AUTHORIZED"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"


class AutomatedReasoningCheckLogicWarningType:
    """AutomatedReasoningCheckLogicWarningType enum values."""

    ALWAYS_TRUE = "ALWAYS_TRUE"
    ALWAYS_FALSE = "ALWAYS_FALSE"


class AutomatedReasoningCheckResult:
    """AutomatedReasoningCheckResult enum values."""

    VALID = "VALID"
    INVALID = "INVALID"
    SATISFIABLE = "SATISFIABLE"
    IMPOSSIBLE = "IMPOSSIBLE"
    TRANSLATION_AMBIGUOUS = "TRANSLATION_AMBIGUOUS"
    TOO_COMPLEX = "TOO_COMPLEX"
    NO_TRANSLATION = "NO_TRANSLATION"


class AutomatedReasoningPolicyAnnotationStatus:
    """AutomatedReasoningPolicyAnnotationStatus enum values."""

    APPLIED = "APPLIED"
    FAILED = "FAILED"


class AutomatedReasoningPolicyBuildDocumentContentType:
    """AutomatedReasoningPolicyBuildDocumentContentType enum values."""

    PDF = "pdf"
    TXT = "txt"


class AutomatedReasoningPolicyBuildMessageType:
    """AutomatedReasoningPolicyBuildMessageType enum values."""

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class AutomatedReasoningPolicyBuildResultAssetType:
    """AutomatedReasoningPolicyBuildResultAssetType enum values."""

    BUILD_LOG = "BUILD_LOG"
    QUALITY_REPORT = "QUALITY_REPORT"
    POLICY_DEFINITION = "POLICY_DEFINITION"
    GENERATED_TEST_CASES = "GENERATED_TEST_CASES"
    POLICY_SCENARIOS = "POLICY_SCENARIOS"


class AutomatedReasoningPolicyBuildWorkflowStatus:
    """AutomatedReasoningPolicyBuildWorkflowStatus enum values."""

    SCHEDULED = "SCHEDULED"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    PREPROCESSING = "PREPROCESSING"
    BUILDING = "BUILDING"
    TESTING = "TESTING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class AutomatedReasoningPolicyBuildWorkflowType:
    """AutomatedReasoningPolicyBuildWorkflowType enum values."""

    INGEST_CONTENT = "INGEST_CONTENT"
    REFINE_POLICY = "REFINE_POLICY"
    IMPORT_POLICY = "IMPORT_POLICY"


class AutomatedReasoningPolicyTestRunResult:
    """AutomatedReasoningPolicyTestRunResult enum values."""

    PASSED = "PASSED"
    FAILED = "FAILED"


class AutomatedReasoningPolicyTestRunStatus:
    """AutomatedReasoningPolicyTestRunStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class CommitmentDuration:
    """CommitmentDuration enum values."""

    ONEMONTH = "OneMonth"
    SIXMONTHS = "SixMonths"


class ConfigurationOwner:
    """ConfigurationOwner enum values."""

    ACCOUNT = "ACCOUNT"


class CustomModelDeploymentStatus:
    """CustomModelDeploymentStatus enum values."""

    CREATING = "Creating"
    ACTIVE = "Active"
    FAILED = "Failed"


class CustomModelDeploymentUpdateStatus:
    """CustomModelDeploymentUpdateStatus enum values."""

    UPDATING = "Updating"
    UPDATECOMPLETED = "UpdateCompleted"
    UPDATEFAILED = "UpdateFailed"


class CustomizationType:
    """CustomizationType enum values."""

    FINE_TUNING = "FINE_TUNING"
    CONTINUED_PRE_TRAINING = "CONTINUED_PRE_TRAINING"
    DISTILLATION = "DISTILLATION"
    REINFORCEMENT_FINE_TUNING = "REINFORCEMENT_FINE_TUNING"
    IMPORTED = "IMPORTED"


class EntitlementAvailability:
    """EntitlementAvailability enum values."""

    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class EvaluationJobStatus:
    """EvaluationJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    DELETING = "Deleting"


class EvaluationJobType:
    """EvaluationJobType enum values."""

    HUMAN = "Human"
    AUTOMATED = "Automated"


class EvaluationTaskType:
    """EvaluationTaskType enum values."""

    SUMMARIZATION = "Summarization"
    CLASSIFICATION = "Classification"
    QUESTIONANDANSWER = "QuestionAndAnswer"
    GENERATION = "Generation"
    CUSTOM = "Custom"


class ExternalSourceType:
    """ExternalSourceType enum values."""

    S3 = "S3"
    BYTE_CONTENT = "BYTE_CONTENT"


class FineTuningJobStatus:
    """FineTuningJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class FoundationModelLifecycleStatus:
    """FoundationModelLifecycleStatus enum values."""

    ACTIVE = "ACTIVE"
    LEGACY = "LEGACY"


class GuardrailContentFilterAction:
    """GuardrailContentFilterAction enum values."""

    BLOCK = "BLOCK"
    NONE = "NONE"


class GuardrailContentFilterType:
    """GuardrailContentFilterType enum values."""

    SEXUAL = "SEXUAL"
    VIOLENCE = "VIOLENCE"
    HATE = "HATE"
    INSULTS = "INSULTS"
    MISCONDUCT = "MISCONDUCT"
    PROMPT_ATTACK = "PROMPT_ATTACK"


class GuardrailContentFiltersTierName:
    """GuardrailContentFiltersTierName enum values."""

    CLASSIC = "CLASSIC"
    STANDARD = "STANDARD"


class GuardrailContextualGroundingAction:
    """GuardrailContextualGroundingAction enum values."""

    BLOCK = "BLOCK"
    NONE = "NONE"


class GuardrailContextualGroundingFilterType:
    """GuardrailContextualGroundingFilterType enum values."""

    GROUNDING = "GROUNDING"
    RELEVANCE = "RELEVANCE"


class GuardrailFilterStrength:
    """GuardrailFilterStrength enum values."""

    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class GuardrailManagedWordsType:
    """GuardrailManagedWordsType enum values."""

    PROFANITY = "PROFANITY"


class GuardrailModality:
    """GuardrailModality enum values."""

    TEXT = "TEXT"
    IMAGE = "IMAGE"


class GuardrailPiiEntityType:
    """GuardrailPiiEntityType enum values."""

    ADDRESS = "ADDRESS"
    AGE = "AGE"
    AWS_ACCESS_KEY = "AWS_ACCESS_KEY"
    AWS_SECRET_KEY = "AWS_SECRET_KEY"
    CA_HEALTH_NUMBER = "CA_HEALTH_NUMBER"
    CA_SOCIAL_INSURANCE_NUMBER = "CA_SOCIAL_INSURANCE_NUMBER"
    CREDIT_DEBIT_CARD_CVV = "CREDIT_DEBIT_CARD_CVV"
    CREDIT_DEBIT_CARD_EXPIRY = "CREDIT_DEBIT_CARD_EXPIRY"
    CREDIT_DEBIT_CARD_NUMBER = "CREDIT_DEBIT_CARD_NUMBER"
    DRIVER_ID = "DRIVER_ID"
    EMAIL = "EMAIL"
    INTERNATIONAL_BANK_ACCOUNT_NUMBER = "INTERNATIONAL_BANK_ACCOUNT_NUMBER"
    IP_ADDRESS = "IP_ADDRESS"
    LICENSE_PLATE = "LICENSE_PLATE"
    MAC_ADDRESS = "MAC_ADDRESS"
    NAME = "NAME"
    PASSWORD = "PASSWORD"
    PHONE = "PHONE"
    PIN = "PIN"
    SWIFT_CODE = "SWIFT_CODE"
    UK_NATIONAL_HEALTH_SERVICE_NUMBER = "UK_NATIONAL_HEALTH_SERVICE_NUMBER"
    UK_NATIONAL_INSURANCE_NUMBER = "UK_NATIONAL_INSURANCE_NUMBER"
    UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER = "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER"
    URL = "URL"
    USERNAME = "USERNAME"
    US_BANK_ACCOUNT_NUMBER = "US_BANK_ACCOUNT_NUMBER"
    US_BANK_ROUTING_NUMBER = "US_BANK_ROUTING_NUMBER"
    US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER = "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER"
    US_PASSPORT_NUMBER = "US_PASSPORT_NUMBER"
    US_SOCIAL_SECURITY_NUMBER = "US_SOCIAL_SECURITY_NUMBER"
    VEHICLE_IDENTIFICATION_NUMBER = "VEHICLE_IDENTIFICATION_NUMBER"


class GuardrailSensitiveInformationAction:
    """GuardrailSensitiveInformationAction enum values."""

    BLOCK = "BLOCK"
    ANONYMIZE = "ANONYMIZE"
    NONE = "NONE"


class GuardrailStatus:
    """GuardrailStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    VERSIONING = "VERSIONING"
    READY = "READY"
    FAILED = "FAILED"
    DELETING = "DELETING"


class GuardrailTopicAction:
    """GuardrailTopicAction enum values."""

    BLOCK = "BLOCK"
    NONE = "NONE"


class GuardrailTopicType:
    """GuardrailTopicType enum values."""

    DENY = "DENY"


class GuardrailTopicsTierName:
    """GuardrailTopicsTierName enum values."""

    CLASSIC = "CLASSIC"
    STANDARD = "STANDARD"


class GuardrailWordAction:
    """GuardrailWordAction enum values."""

    BLOCK = "BLOCK"
    NONE = "NONE"


class InferenceProfileStatus:
    """InferenceProfileStatus enum values."""

    ACTIVE = "ACTIVE"


class InferenceProfileType:
    """InferenceProfileType enum values."""

    SYSTEM_DEFINED = "SYSTEM_DEFINED"
    APPLICATION = "APPLICATION"


class InferenceType:
    """InferenceType enum values."""

    ON_DEMAND = "ON_DEMAND"
    PROVISIONED = "PROVISIONED"


class InputTags:
    """InputTags enum values."""

    HONOR = "HONOR"
    IGNORE = "IGNORE"


class JobStatusDetails:
    """JobStatusDetails enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"
    NOTSTARTED = "NotStarted"


class ModelCopyJobStatus:
    """ModelCopyJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class ModelCustomization:
    """ModelCustomization enum values."""

    FINE_TUNING = "FINE_TUNING"
    CONTINUED_PRE_TRAINING = "CONTINUED_PRE_TRAINING"
    DISTILLATION = "DISTILLATION"


class ModelCustomizationJobStatus:
    """ModelCustomizationJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class ModelImportJobStatus:
    """ModelImportJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class ModelInvocationJobStatus:
    """ModelInvocationJobStatus enum values."""

    SUBMITTED = "Submitted"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    PARTIALLYCOMPLETED = "PartiallyCompleted"
    EXPIRED = "Expired"
    VALIDATING = "Validating"
    SCHEDULED = "Scheduled"


class ModelModality:
    """ModelModality enum values."""

    TEXT = "TEXT"
    IMAGE = "IMAGE"
    EMBEDDING = "EMBEDDING"


class ModelStatus:
    """ModelStatus enum values."""

    ACTIVE = "Active"
    CREATING = "Creating"
    FAILED = "Failed"


class OfferType:
    """OfferType enum values."""

    ALL = "ALL"
    PUBLIC = "PUBLIC"


class PerformanceConfigLatency:
    """PerformanceConfigLatency enum values."""

    STANDARD = "standard"
    OPTIMIZED = "optimized"


class PromptRouterStatus:
    """PromptRouterStatus enum values."""

    AVAILABLE = "AVAILABLE"


class PromptRouterType:
    """PromptRouterType enum values."""

    CUSTOM = "custom"
    DEFAULT = "default"


class ProvisionedModelStatus:
    """ProvisionedModelStatus enum values."""

    CREATING = "Creating"
    INSERVICE = "InService"
    UPDATING = "Updating"
    FAILED = "Failed"


class QueryTransformationType:
    """QueryTransformationType enum values."""

    QUERY_DECOMPOSITION = "QUERY_DECOMPOSITION"


class ReasoningEffort:
    """ReasoningEffort enum values."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RegionAvailability:
    """RegionAvailability enum values."""

    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class RerankingMetadataSelectionMode:
    """RerankingMetadataSelectionMode enum values."""

    SELECTIVE = "SELECTIVE"
    ALL = "ALL"


class RetrieveAndGenerateType:
    """RetrieveAndGenerateType enum values."""

    KNOWLEDGE_BASE = "KNOWLEDGE_BASE"
    EXTERNAL_SOURCES = "EXTERNAL_SOURCES"


class S3InputFormat:
    """S3InputFormat enum values."""

    JSONL = "JSONL"


class SearchType:
    """SearchType enum values."""

    HYBRID = "HYBRID"
    SEMANTIC = "SEMANTIC"


class SortByProvisionedModels:
    """SortByProvisionedModels enum values."""

    CREATIONTIME = "CreationTime"


class SortJobsBy:
    """SortJobsBy enum values."""

    CREATIONTIME = "CreationTime"


class SortModelsBy:
    """SortModelsBy enum values."""

    CREATIONTIME = "CreationTime"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class Status:
    """Status enum values."""

    REGISTERED = "REGISTERED"
    INCOMPATIBLE_ENDPOINT = "INCOMPATIBLE_ENDPOINT"


class VectorSearchRerankingConfigurationType:
    """VectorSearchRerankingConfigurationType enum values."""

    BEDROCK_RERANKING_MODEL = "BEDROCK_RERANKING_MODEL"


@dataclass
class BedrockDataAutomationConfiguration(PropertyType):
    PARSING_MODALITY = "ParsingModality"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_modality": "ParsingModality",
    }

    parsing_modality: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    MODEL_ARN = "ModelArn"
    PARSING_MODALITY = "ParsingModality"
    PARSING_PROMPT = "ParsingPrompt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
        "parsing_modality": "ParsingModality",
        "parsing_prompt": "ParsingPrompt",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parsing_modality: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parsing_prompt: Optional[ParsingPrompt] = None


@dataclass
class BedrockFoundationModelContextEnrichmentConfiguration(PropertyType):
    ENRICHMENT_STRATEGY_CONFIGURATION = "EnrichmentStrategyConfiguration"
    MODEL_ARN = "ModelArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enrichment_strategy_configuration": "EnrichmentStrategyConfiguration",
        "model_arn": "ModelArn",
    }

    enrichment_strategy_configuration: Optional[EnrichmentStrategyConfiguration] = None
    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ChunkingConfiguration(PropertyType):
    CHUNKING_STRATEGY = "ChunkingStrategy"
    FIXED_SIZE_CHUNKING_CONFIGURATION = "FixedSizeChunkingConfiguration"
    SEMANTIC_CHUNKING_CONFIGURATION = "SemanticChunkingConfiguration"
    HIERARCHICAL_CHUNKING_CONFIGURATION = "HierarchicalChunkingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "chunking_strategy": "ChunkingStrategy",
        "fixed_size_chunking_configuration": "FixedSizeChunkingConfiguration",
        "semantic_chunking_configuration": "SemanticChunkingConfiguration",
        "hierarchical_chunking_configuration": "HierarchicalChunkingConfiguration",
    }

    chunking_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fixed_size_chunking_configuration: Optional[FixedSizeChunkingConfiguration] = None
    semantic_chunking_configuration: Optional[SemanticChunkingConfiguration] = None
    hierarchical_chunking_configuration: Optional[HierarchicalChunkingConfiguration] = None


@dataclass
class ConfluenceCrawlerConfiguration(PropertyType):
    FILTER_CONFIGURATION = "FilterConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_configuration": "FilterConfiguration",
    }

    filter_configuration: Optional[CrawlFilterConfiguration] = None


@dataclass
class ConfluenceDataSourceConfiguration(PropertyType):
    SOURCE_CONFIGURATION = "SourceConfiguration"
    CRAWLER_CONFIGURATION = "CrawlerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[ConfluenceSourceConfiguration] = None
    crawler_configuration: Optional[ConfluenceCrawlerConfiguration] = None


@dataclass
class ConfluenceSourceConfiguration(PropertyType):
    HOST_URL = "HostUrl"
    HOST_TYPE = "HostType"
    AUTH_TYPE = "AuthType"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "host_url": "HostUrl",
        "host_type": "HostType",
        "auth_type": "AuthType",
        "credentials_secret_arn": "CredentialsSecretArn",
    }

    host_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContextEnrichmentConfiguration(PropertyType):
    TYPE = "Type"
    BEDROCK_FOUNDATION_MODEL_CONFIGURATION = "BedrockFoundationModelConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "bedrock_foundation_model_configuration": "BedrockFoundationModelConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_foundation_model_configuration: Optional[BedrockFoundationModelContextEnrichmentConfiguration] = None


@dataclass
class CrawlFilterConfiguration(PropertyType):
    TYPE = "Type"
    PATTERN_OBJECT_FILTER = "PatternObjectFilter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "pattern_object_filter": "PatternObjectFilter",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_object_filter: Optional[PatternObjectFilterConfiguration] = None


@dataclass
class CustomTransformationConfiguration(PropertyType):
    INTERMEDIATE_STORAGE = "IntermediateStorage"
    TRANSFORMATIONS = "Transformations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "intermediate_storage": "IntermediateStorage",
        "transformations": "Transformations",
    }

    intermediate_storage: Optional[IntermediateStorage] = None
    transformations: Optional[list[Transformation]] = None


@dataclass
class DataSourceConfiguration(PropertyType):
    TYPE = "Type"
    S3_CONFIGURATION = "S3Configuration"
    SALESFORCE_CONFIGURATION = "SalesforceConfiguration"
    CONFLUENCE_CONFIGURATION = "ConfluenceConfiguration"
    SHARE_POINT_CONFIGURATION = "SharePointConfiguration"
    WEB_CONFIGURATION = "WebConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "s3_configuration": "S3Configuration",
        "salesforce_configuration": "SalesforceConfiguration",
        "confluence_configuration": "ConfluenceConfiguration",
        "share_point_configuration": "SharePointConfiguration",
        "web_configuration": "WebConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_configuration: Optional[S3DataSourceConfiguration] = None
    salesforce_configuration: Optional[SalesforceDataSourceConfiguration] = None
    confluence_configuration: Optional[ConfluenceDataSourceConfiguration] = None
    share_point_configuration: Optional[SharePointDataSourceConfiguration] = None
    web_configuration: Optional[WebDataSourceConfiguration] = None


@dataclass
class EnrichmentStrategyConfiguration(PropertyType):
    METHOD = "Method"

    _property_mappings: ClassVar[dict[str, str]] = {
        "method": "Method",
    }

    method: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    OVERLAP_PERCENTAGE = "OverlapPercentage"
    MAX_TOKENS = "MaxTokens"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overlap_percentage": "OverlapPercentage",
        "max_tokens": "MaxTokens",
    }

    overlap_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    OVERLAP_TOKENS = "OverlapTokens"
    LEVEL_CONFIGURATIONS = "LevelConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overlap_tokens": "OverlapTokens",
        "level_configurations": "LevelConfigurations",
    }

    overlap_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None
    level_configurations: Optional[list[HierarchicalChunkingLevelConfiguration]] = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    MAX_TOKENS = "MaxTokens"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_tokens": "MaxTokens",
    }

    max_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IntermediateStorage(PropertyType):
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_location": "S3Location",
    }

    s3_location: Optional[S3Location] = None


@dataclass
class ParsingConfiguration(PropertyType):
    BEDROCK_DATA_AUTOMATION_CONFIGURATION = "BedrockDataAutomationConfiguration"
    BEDROCK_FOUNDATION_MODEL_CONFIGURATION = "BedrockFoundationModelConfiguration"
    PARSING_STRATEGY = "ParsingStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_data_automation_configuration": "BedrockDataAutomationConfiguration",
        "bedrock_foundation_model_configuration": "BedrockFoundationModelConfiguration",
        "parsing_strategy": "ParsingStrategy",
    }

    bedrock_data_automation_configuration: Optional[BedrockDataAutomationConfiguration] = None
    bedrock_foundation_model_configuration: Optional[BedrockFoundationModelConfiguration] = None
    parsing_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParsingPrompt(PropertyType):
    PARSING_PROMPT_TEXT = "ParsingPromptText"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_prompt_text": "ParsingPromptText",
    }

    parsing_prompt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PatternObjectFilter(PropertyType):
    OBJECT_TYPE = "ObjectType"
    INCLUSION_FILTERS = "InclusionFilters"
    EXCLUSION_FILTERS = "ExclusionFilters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_type": "ObjectType",
        "inclusion_filters": "InclusionFilters",
        "exclusion_filters": "ExclusionFilters",
    }

    object_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion_filters: Optional[Union[list[str], Ref]] = None
    exclusion_filters: Optional[Union[list[str], Ref]] = None


@dataclass
class PatternObjectFilterConfiguration(PropertyType):
    FILTERS = "Filters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
    }

    filters: Optional[list[PatternObjectFilter]] = None


@dataclass
class S3DataSourceConfiguration(PropertyType):
    BUCKET_ARN = "BucketArn"
    BUCKET_OWNER_ACCOUNT_ID = "BucketOwnerAccountId"
    INCLUSION_PREFIXES = "InclusionPrefixes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "bucket_owner_account_id": "BucketOwnerAccountId",
        "inclusion_prefixes": "InclusionPrefixes",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion_prefixes: Optional[Union[list[str], Ref]] = None


@dataclass
class S3Location(PropertyType):
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceCrawlerConfiguration(PropertyType):
    FILTER_CONFIGURATION = "FilterConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_configuration": "FilterConfiguration",
    }

    filter_configuration: Optional[CrawlFilterConfiguration] = None


@dataclass
class SalesforceDataSourceConfiguration(PropertyType):
    SOURCE_CONFIGURATION = "SourceConfiguration"
    CRAWLER_CONFIGURATION = "CrawlerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[SalesforceSourceConfiguration] = None
    crawler_configuration: Optional[SalesforceCrawlerConfiguration] = None


@dataclass
class SalesforceSourceConfiguration(PropertyType):
    HOST_URL = "HostUrl"
    AUTH_TYPE = "AuthType"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "host_url": "HostUrl",
        "auth_type": "AuthType",
        "credentials_secret_arn": "CredentialsSecretArn",
    }

    host_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SeedUrl(PropertyType):
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "url": "Url",
    }

    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    BUFFER_SIZE = "BufferSize"
    MAX_TOKENS = "MaxTokens"
    BREAKPOINT_PERCENTILE_THRESHOLD = "BreakpointPercentileThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "buffer_size": "BufferSize",
        "max_tokens": "MaxTokens",
        "breakpoint_percentile_threshold": "BreakpointPercentileThreshold",
    }

    buffer_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None
    breakpoint_percentile_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SharePointCrawlerConfiguration(PropertyType):
    FILTER_CONFIGURATION = "FilterConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_configuration": "FilterConfiguration",
    }

    filter_configuration: Optional[CrawlFilterConfiguration] = None


@dataclass
class SharePointDataSourceConfiguration(PropertyType):
    SOURCE_CONFIGURATION = "SourceConfiguration"
    CRAWLER_CONFIGURATION = "CrawlerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[SharePointSourceConfiguration] = None
    crawler_configuration: Optional[SharePointCrawlerConfiguration] = None


@dataclass
class SharePointSourceConfiguration(PropertyType):
    SITE_URLS = "SiteUrls"
    HOST_TYPE = "HostType"
    TENANT_ID = "TenantId"
    AUTH_TYPE = "AuthType"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"
    DOMAIN = "Domain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "site_urls": "SiteUrls",
        "host_type": "HostType",
        "tenant_id": "TenantId",
        "auth_type": "AuthType",
        "credentials_secret_arn": "CredentialsSecretArn",
        "domain": "Domain",
    }

    site_urls: Optional[Union[list[str], Ref]] = None
    host_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tenant_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transformation(PropertyType):
    STEP_TO_APPLY = "StepToApply"
    TRANSFORMATION_FUNCTION = "TransformationFunction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "step_to_apply": "StepToApply",
        "transformation_function": "TransformationFunction",
    }

    step_to_apply: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transformation_function: Optional[TransformationFunction] = None


@dataclass
class TransformationFunction(PropertyType):
    TRANSFORMATION_LAMBDA_CONFIGURATION = "TransformationLambdaConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transformation_lambda_configuration": "TransformationLambdaConfiguration",
    }

    transformation_lambda_configuration: Optional[TransformationLambdaConfiguration] = None


@dataclass
class TransformationLambdaConfiguration(PropertyType):
    LAMBDA_ARN = "LambdaArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UrlConfiguration(PropertyType):
    SEED_URLS = "SeedUrls"

    _property_mappings: ClassVar[dict[str, str]] = {
        "seed_urls": "SeedUrls",
    }

    seed_urls: Optional[list[SeedUrl]] = None


@dataclass
class VectorIngestionConfiguration(PropertyType):
    PARSING_CONFIGURATION = "ParsingConfiguration"
    CONTEXT_ENRICHMENT_CONFIGURATION = "ContextEnrichmentConfiguration"
    CUSTOM_TRANSFORMATION_CONFIGURATION = "CustomTransformationConfiguration"
    CHUNKING_CONFIGURATION = "ChunkingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_configuration": "ParsingConfiguration",
        "context_enrichment_configuration": "ContextEnrichmentConfiguration",
        "custom_transformation_configuration": "CustomTransformationConfiguration",
        "chunking_configuration": "ChunkingConfiguration",
    }

    parsing_configuration: Optional[ParsingConfiguration] = None
    context_enrichment_configuration: Optional[ContextEnrichmentConfiguration] = None
    custom_transformation_configuration: Optional[CustomTransformationConfiguration] = None
    chunking_configuration: Optional[ChunkingConfiguration] = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    INCLUSION_FILTERS = "InclusionFilters"
    USER_AGENT_HEADER = "UserAgentHeader"
    CRAWLER_LIMITS = "CrawlerLimits"
    EXCLUSION_FILTERS = "ExclusionFilters"
    SCOPE = "Scope"
    USER_AGENT = "UserAgent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inclusion_filters": "InclusionFilters",
        "user_agent_header": "UserAgentHeader",
        "crawler_limits": "CrawlerLimits",
        "exclusion_filters": "ExclusionFilters",
        "scope": "Scope",
        "user_agent": "UserAgent",
    }

    inclusion_filters: Optional[Union[list[str], Ref]] = None
    user_agent_header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    crawler_limits: Optional[WebCrawlerLimits] = None
    exclusion_filters: Optional[Union[list[str], Ref]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_agent: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebCrawlerLimits(PropertyType):
    RATE_LIMIT = "RateLimit"
    MAX_PAGES = "MaxPages"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rate_limit": "RateLimit",
        "max_pages": "MaxPages",
    }

    rate_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_pages: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WebDataSourceConfiguration(PropertyType):
    SOURCE_CONFIGURATION = "SourceConfiguration"
    CRAWLER_CONFIGURATION = "CrawlerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[WebSourceConfiguration] = None
    crawler_configuration: Optional[WebCrawlerConfiguration] = None


@dataclass
class WebSourceConfiguration(PropertyType):
    URL_CONFIGURATION = "UrlConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "url_configuration": "UrlConfiguration",
    }

    url_configuration: Optional[UrlConfiguration] = None

