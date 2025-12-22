"""PropertyTypes for AWS::Bedrock::KnowledgeBase."""

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
class AudioConfiguration(PropertyType):
    SEGMENTATION_CONFIGURATION = "SegmentationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_configuration": "SegmentationConfiguration",
    }

    segmentation_configuration: Optional[AudioSegmentationConfiguration] = None


@dataclass
class AudioSegmentationConfiguration(PropertyType):
    FIXED_LENGTH_DURATION = "FixedLengthDuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fixed_length_duration": "FixedLengthDuration",
    }

    fixed_length_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockEmbeddingModelConfiguration(PropertyType):
    EMBEDDING_DATA_TYPE = "EmbeddingDataType"
    VIDEO = "Video"
    DIMENSIONS = "Dimensions"
    AUDIO = "Audio"

    _property_mappings: ClassVar[dict[str, str]] = {
        "embedding_data_type": "EmbeddingDataType",
        "video": "Video",
        "dimensions": "Dimensions",
        "audio": "Audio",
    }

    embedding_data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    video: Optional[list[VideoConfiguration]] = None
    dimensions: Optional[Union[int, Ref, GetAtt, Sub]] = None
    audio: Optional[list[AudioConfiguration]] = None


@dataclass
class CuratedQuery(PropertyType):
    NATURAL_LANGUAGE = "NaturalLanguage"
    SQL = "Sql"

    _property_mappings: ClassVar[dict[str, str]] = {
        "natural_language": "NaturalLanguage",
        "sql": "Sql",
    }

    natural_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmbeddingModelConfiguration(PropertyType):
    BEDROCK_EMBEDDING_MODEL_CONFIGURATION = "BedrockEmbeddingModelConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_embedding_model_configuration": "BedrockEmbeddingModelConfiguration",
    }

    bedrock_embedding_model_configuration: Optional[BedrockEmbeddingModelConfiguration] = None


@dataclass
class KendraKnowledgeBaseConfiguration(PropertyType):
    KENDRA_INDEX_ARN = "KendraIndexArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kendra_index_arn": "KendraIndexArn",
    }

    kendra_index_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseConfiguration(PropertyType):
    TYPE = "Type"
    SQL_KNOWLEDGE_BASE_CONFIGURATION = "SqlKnowledgeBaseConfiguration"
    KENDRA_KNOWLEDGE_BASE_CONFIGURATION = "KendraKnowledgeBaseConfiguration"
    VECTOR_KNOWLEDGE_BASE_CONFIGURATION = "VectorKnowledgeBaseConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "sql_knowledge_base_configuration": "SqlKnowledgeBaseConfiguration",
        "kendra_knowledge_base_configuration": "KendraKnowledgeBaseConfiguration",
        "vector_knowledge_base_configuration": "VectorKnowledgeBaseConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql_knowledge_base_configuration: Optional[SqlKnowledgeBaseConfiguration] = None
    kendra_knowledge_base_configuration: Optional[KendraKnowledgeBaseConfiguration] = None
    vector_knowledge_base_configuration: Optional[VectorKnowledgeBaseConfiguration] = None


@dataclass
class MongoDbAtlasConfiguration(PropertyType):
    ENDPOINT = "Endpoint"
    COLLECTION_NAME = "CollectionName"
    VECTOR_INDEX_NAME = "VectorIndexName"
    FIELD_MAPPING = "FieldMapping"
    DATABASE_NAME = "DatabaseName"
    ENDPOINT_SERVICE_NAME = "EndpointServiceName"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"
    TEXT_INDEX_NAME = "TextIndexName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "collection_name": "CollectionName",
        "vector_index_name": "VectorIndexName",
        "field_mapping": "FieldMapping",
        "database_name": "DatabaseName",
        "endpoint_service_name": "EndpointServiceName",
        "credentials_secret_arn": "CredentialsSecretArn",
        "text_index_name": "TextIndexName",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    collection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[MongoDbAtlasFieldMapping] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MongoDbAtlasFieldMapping(PropertyType):
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_field": "VectorField",
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NeptuneAnalyticsConfiguration(PropertyType):
    GRAPH_ARN = "GraphArn"
    FIELD_MAPPING = "FieldMapping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "graph_arn": "GraphArn",
        "field_mapping": "FieldMapping",
    }

    graph_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[NeptuneAnalyticsFieldMapping] = None


@dataclass
class NeptuneAnalyticsFieldMapping(PropertyType):
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchManagedClusterConfiguration(PropertyType):
    DOMAIN_ENDPOINT = "DomainEndpoint"
    VECTOR_INDEX_NAME = "VectorIndexName"
    FIELD_MAPPING = "FieldMapping"
    DOMAIN_ARN = "DomainArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_endpoint": "DomainEndpoint",
        "vector_index_name": "VectorIndexName",
        "field_mapping": "FieldMapping",
        "domain_arn": "DomainArn",
    }

    domain_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[OpenSearchManagedClusterFieldMapping] = None
    domain_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchManagedClusterFieldMapping(PropertyType):
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_field": "VectorField",
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchServerlessConfiguration(PropertyType):
    COLLECTION_ARN = "CollectionArn"
    VECTOR_INDEX_NAME = "VectorIndexName"
    FIELD_MAPPING = "FieldMapping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "collection_arn": "CollectionArn",
        "vector_index_name": "VectorIndexName",
        "field_mapping": "FieldMapping",
    }

    collection_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[OpenSearchServerlessFieldMapping] = None


@dataclass
class OpenSearchServerlessFieldMapping(PropertyType):
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_field": "VectorField",
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PineconeConfiguration(PropertyType):
    FIELD_MAPPING = "FieldMapping"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"
    CONNECTION_STRING = "ConnectionString"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_mapping": "FieldMapping",
        "credentials_secret_arn": "CredentialsSecretArn",
        "connection_string": "ConnectionString",
        "namespace": "Namespace",
    }

    field_mapping: Optional[PineconeFieldMapping] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PineconeFieldMapping(PropertyType):
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationColumn(PropertyType):
    DESCRIPTION = "Description"
    INCLUSION = "Inclusion"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "inclusion": "Inclusion",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationConfiguration(PropertyType):
    GENERATION_CONTEXT = "GenerationContext"
    EXECUTION_TIMEOUT_SECONDS = "ExecutionTimeoutSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "generation_context": "GenerationContext",
        "execution_timeout_seconds": "ExecutionTimeoutSeconds",
    }

    generation_context: Optional[QueryGenerationContext] = None
    execution_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationContext(PropertyType):
    CURATED_QUERIES = "CuratedQueries"
    TABLES = "Tables"

    _property_mappings: ClassVar[dict[str, str]] = {
        "curated_queries": "CuratedQueries",
        "tables": "Tables",
    }

    curated_queries: Optional[list[CuratedQuery]] = None
    tables: Optional[list[QueryGenerationTable]] = None


@dataclass
class QueryGenerationTable(PropertyType):
    DESCRIPTION = "Description"
    INCLUSION = "Inclusion"
    COLUMNS = "Columns"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "inclusion": "Inclusion",
        "columns": "Columns",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[QueryGenerationColumn]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsConfiguration(PropertyType):
    RESOURCE_ARN = "ResourceArn"
    TABLE_NAME = "TableName"
    FIELD_MAPPING = "FieldMapping"
    DATABASE_NAME = "DatabaseName"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "table_name": "TableName",
        "field_mapping": "FieldMapping",
        "database_name": "DatabaseName",
        "credentials_secret_arn": "CredentialsSecretArn",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[RdsFieldMapping] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsFieldMapping(PropertyType):
    PRIMARY_KEY_FIELD = "PrimaryKeyField"
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    CUSTOM_METADATA_FIELD = "CustomMetadataField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_key_field": "PrimaryKeyField",
        "vector_field": "VectorField",
        "text_field": "TextField",
        "custom_metadata_field": "CustomMetadataField",
        "metadata_field": "MetadataField",
    }

    primary_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftConfiguration(PropertyType):
    QUERY_ENGINE_CONFIGURATION = "QueryEngineConfiguration"
    STORAGE_CONFIGURATIONS = "StorageConfigurations"
    QUERY_GENERATION_CONFIGURATION = "QueryGenerationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_engine_configuration": "QueryEngineConfiguration",
        "storage_configurations": "StorageConfigurations",
        "query_generation_configuration": "QueryGenerationConfiguration",
    }

    query_engine_configuration: Optional[RedshiftQueryEngineConfiguration] = None
    storage_configurations: Optional[list[RedshiftQueryEngineStorageConfiguration]] = None
    query_generation_configuration: Optional[QueryGenerationConfiguration] = None


@dataclass
class RedshiftProvisionedAuthConfiguration(PropertyType):
    TYPE = "Type"
    DATABASE_USER = "DatabaseUser"
    USERNAME_PASSWORD_SECRET_ARN = "UsernamePasswordSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "database_user": "DatabaseUser",
        "username_password_secret_arn": "UsernamePasswordSecretArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftProvisionedConfiguration(PropertyType):
    AUTH_CONFIGURATION = "AuthConfiguration"
    CLUSTER_IDENTIFIER = "ClusterIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_configuration": "AuthConfiguration",
        "cluster_identifier": "ClusterIdentifier",
    }

    auth_configuration: Optional[RedshiftProvisionedAuthConfiguration] = None
    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(PropertyType):
    TABLE_NAMES = "TableNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_names": "TableNames",
    }

    table_names: Optional[Union[list[str], Ref]] = None


@dataclass
class RedshiftQueryEngineConfiguration(PropertyType):
    TYPE = "Type"
    PROVISIONED_CONFIGURATION = "ProvisionedConfiguration"
    SERVERLESS_CONFIGURATION = "ServerlessConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "provisioned_configuration": "ProvisionedConfiguration",
        "serverless_configuration": "ServerlessConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provisioned_configuration: Optional[RedshiftProvisionedConfiguration] = None
    serverless_configuration: Optional[RedshiftServerlessConfiguration] = None


@dataclass
class RedshiftQueryEngineRedshiftStorageConfiguration(PropertyType):
    DATABASE_NAME = "DatabaseName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftQueryEngineStorageConfiguration(PropertyType):
    TYPE = "Type"
    REDSHIFT_CONFIGURATION = "RedshiftConfiguration"
    AWS_DATA_CATALOG_CONFIGURATION = "AwsDataCatalogConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "redshift_configuration": "RedshiftConfiguration",
        "aws_data_catalog_configuration": "AwsDataCatalogConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redshift_configuration: Optional[RedshiftQueryEngineRedshiftStorageConfiguration] = None
    aws_data_catalog_configuration: Optional[RedshiftQueryEngineAwsDataCatalogStorageConfiguration] = None


@dataclass
class RedshiftServerlessAuthConfiguration(PropertyType):
    TYPE = "Type"
    USERNAME_PASSWORD_SECRET_ARN = "UsernamePasswordSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "username_password_secret_arn": "UsernamePasswordSecretArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftServerlessConfiguration(PropertyType):
    WORKGROUP_ARN = "WorkgroupArn"
    AUTH_CONFIGURATION = "AuthConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_arn": "WorkgroupArn",
        "auth_configuration": "AuthConfiguration",
    }

    workgroup_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_configuration: Optional[RedshiftServerlessAuthConfiguration] = None


@dataclass
class S3Location(PropertyType):
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3VectorsConfiguration(PropertyType):
    INDEX_NAME = "IndexName"
    VECTOR_BUCKET_ARN = "VectorBucketArn"
    INDEX_ARN = "IndexArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "vector_bucket_arn": "VectorBucketArn",
        "index_arn": "IndexArn",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SqlKnowledgeBaseConfiguration(PropertyType):
    TYPE = "Type"
    REDSHIFT_CONFIGURATION = "RedshiftConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "redshift_configuration": "RedshiftConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redshift_configuration: Optional[RedshiftConfiguration] = None


@dataclass
class StorageConfiguration(PropertyType):
    S3_VECTORS_CONFIGURATION = "S3VectorsConfiguration"
    OPENSEARCH_MANAGED_CLUSTER_CONFIGURATION = "OpensearchManagedClusterConfiguration"
    OPENSEARCH_SERVERLESS_CONFIGURATION = "OpensearchServerlessConfiguration"
    NEPTUNE_ANALYTICS_CONFIGURATION = "NeptuneAnalyticsConfiguration"
    TYPE = "Type"
    MONGO_DB_ATLAS_CONFIGURATION = "MongoDbAtlasConfiguration"
    RDS_CONFIGURATION = "RdsConfiguration"
    PINECONE_CONFIGURATION = "PineconeConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_vectors_configuration": "S3VectorsConfiguration",
        "opensearch_managed_cluster_configuration": "OpensearchManagedClusterConfiguration",
        "opensearch_serverless_configuration": "OpensearchServerlessConfiguration",
        "neptune_analytics_configuration": "NeptuneAnalyticsConfiguration",
        "type_": "Type",
        "mongo_db_atlas_configuration": "MongoDbAtlasConfiguration",
        "rds_configuration": "RdsConfiguration",
        "pinecone_configuration": "PineconeConfiguration",
    }

    s3_vectors_configuration: Optional[S3VectorsConfiguration] = None
    opensearch_managed_cluster_configuration: Optional[OpenSearchManagedClusterConfiguration] = None
    opensearch_serverless_configuration: Optional[OpenSearchServerlessConfiguration] = None
    neptune_analytics_configuration: Optional[NeptuneAnalyticsConfiguration] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mongo_db_atlas_configuration: Optional[MongoDbAtlasConfiguration] = None
    rds_configuration: Optional[RdsConfiguration] = None
    pinecone_configuration: Optional[PineconeConfiguration] = None


@dataclass
class SupplementalDataStorageConfiguration(PropertyType):
    SUPPLEMENTAL_DATA_STORAGE_LOCATIONS = "SupplementalDataStorageLocations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "supplemental_data_storage_locations": "SupplementalDataStorageLocations",
    }

    supplemental_data_storage_locations: Optional[list[SupplementalDataStorageLocation]] = None


@dataclass
class SupplementalDataStorageLocation(PropertyType):
    SUPPLEMENTAL_DATA_STORAGE_LOCATION_TYPE = "SupplementalDataStorageLocationType"
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "supplemental_data_storage_location_type": "SupplementalDataStorageLocationType",
        "s3_location": "S3Location",
    }

    supplemental_data_storage_location_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_location: Optional[S3Location] = None


@dataclass
class VectorKnowledgeBaseConfiguration(PropertyType):
    EMBEDDING_MODEL_CONFIGURATION = "EmbeddingModelConfiguration"
    EMBEDDING_MODEL_ARN = "EmbeddingModelArn"
    SUPPLEMENTAL_DATA_STORAGE_CONFIGURATION = "SupplementalDataStorageConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "embedding_model_configuration": "EmbeddingModelConfiguration",
        "embedding_model_arn": "EmbeddingModelArn",
        "supplemental_data_storage_configuration": "SupplementalDataStorageConfiguration",
    }

    embedding_model_configuration: Optional[EmbeddingModelConfiguration] = None
    embedding_model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    supplemental_data_storage_configuration: Optional[SupplementalDataStorageConfiguration] = None


@dataclass
class VideoConfiguration(PropertyType):
    SEGMENTATION_CONFIGURATION = "SegmentationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_configuration": "SegmentationConfiguration",
    }

    segmentation_configuration: Optional[VideoSegmentationConfiguration] = None


@dataclass
class VideoSegmentationConfiguration(PropertyType):
    FIXED_LENGTH_DURATION = "FixedLengthDuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fixed_length_duration": "FixedLengthDuration",
    }

    fixed_length_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None

