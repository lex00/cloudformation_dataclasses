"""PropertyTypes for AWS::Bedrock::Agent."""

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
class APISchema(PropertyType):
    S3 = "S3"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "payload": "Payload",
    }

    s3: Optional[S3Identifier] = None
    payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ActionGroupExecutor(PropertyType):
    CUSTOM_CONTROL = "CustomControl"
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_control": "CustomControl",
        "lambda_": "Lambda",
    }

    custom_control: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentActionGroup(PropertyType):
    DESCRIPTION = "Description"
    API_SCHEMA = "ApiSchema"
    FUNCTION_SCHEMA = "FunctionSchema"
    SKIP_RESOURCE_IN_USE_CHECK_ON_DELETE = "SkipResourceInUseCheckOnDelete"
    PARENT_ACTION_GROUP_SIGNATURE = "ParentActionGroupSignature"
    ACTION_GROUP_EXECUTOR = "ActionGroupExecutor"
    ACTION_GROUP_NAME = "ActionGroupName"
    ACTION_GROUP_STATE = "ActionGroupState"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "api_schema": "ApiSchema",
        "function_schema": "FunctionSchema",
        "skip_resource_in_use_check_on_delete": "SkipResourceInUseCheckOnDelete",
        "parent_action_group_signature": "ParentActionGroupSignature",
        "action_group_executor": "ActionGroupExecutor",
        "action_group_name": "ActionGroupName",
        "action_group_state": "ActionGroupState",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_schema: Optional[APISchema] = None
    function_schema: Optional[FunctionSchema] = None
    skip_resource_in_use_check_on_delete: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    parent_action_group_signature: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_group_executor: Optional[ActionGroupExecutor] = None
    action_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_group_state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentCollaborator(PropertyType):
    AGENT_DESCRIPTOR = "AgentDescriptor"
    COLLABORATION_INSTRUCTION = "CollaborationInstruction"
    RELAY_CONVERSATION_HISTORY = "RelayConversationHistory"
    COLLABORATOR_NAME = "CollaboratorName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_descriptor": "AgentDescriptor",
        "collaboration_instruction": "CollaborationInstruction",
        "relay_conversation_history": "RelayConversationHistory",
        "collaborator_name": "CollaboratorName",
    }

    agent_descriptor: Optional[AgentDescriptor] = None
    collaboration_instruction: Optional[Union[str, Ref, GetAtt, Sub]] = None
    relay_conversation_history: Optional[Union[str, Ref, GetAtt, Sub]] = None
    collaborator_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentDescriptor(PropertyType):
    ALIAS_ARN = "AliasArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias_arn": "AliasArn",
    }

    alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AgentKnowledgeBase(PropertyType):
    DESCRIPTION = "Description"
    KNOWLEDGE_BASE_STATE = "KnowledgeBaseState"
    KNOWLEDGE_BASE_ID = "KnowledgeBaseId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "knowledge_base_state": "KnowledgeBaseState",
        "knowledge_base_id": "KnowledgeBaseId",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    knowledge_base_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    knowledge_base_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomOrchestration(PropertyType):
    EXECUTOR = "Executor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "executor": "Executor",
    }

    executor: Optional[OrchestrationExecutor] = None


@dataclass
class Function(PropertyType):
    DESCRIPTION = "Description"
    PARAMETERS = "Parameters"
    REQUIRE_CONFIRMATION = "RequireConfirmation"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "parameters": "Parameters",
        "require_confirmation": "RequireConfirmation",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[dict[str, Any]] = None
    require_confirmation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FunctionSchema(PropertyType):
    FUNCTIONS = "Functions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "functions": "Functions",
    }

    functions: Optional[list[Function]] = None


@dataclass
class GuardrailConfiguration(PropertyType):
    GUARDRAIL_IDENTIFIER = "GuardrailIdentifier"
    GUARDRAIL_VERSION = "GuardrailVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_identifier": "GuardrailIdentifier",
        "guardrail_version": "GuardrailVersion",
    }

    guardrail_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    guardrail_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceConfiguration(PropertyType):
    TOP_K = "TopK"
    TEMPERATURE = "Temperature"
    MAXIMUM_LENGTH = "MaximumLength"
    STOP_SEQUENCES = "StopSequences"
    TOP_P = "TopP"

    _property_mappings: ClassVar[dict[str, str]] = {
        "top_k": "TopK",
        "temperature": "Temperature",
        "maximum_length": "MaximumLength",
        "stop_sequences": "StopSequences",
        "top_p": "TopP",
    }

    top_k: Optional[Union[float, Ref, GetAtt, Sub]] = None
    temperature: Optional[Union[float, Ref, GetAtt, Sub]] = None
    maximum_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    stop_sequences: Optional[Union[list[str], Ref]] = None
    top_p: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class MemoryConfiguration(PropertyType):
    SESSION_SUMMARY_CONFIGURATION = "SessionSummaryConfiguration"
    ENABLED_MEMORY_TYPES = "EnabledMemoryTypes"
    STORAGE_DAYS = "StorageDays"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_summary_configuration": "SessionSummaryConfiguration",
        "enabled_memory_types": "EnabledMemoryTypes",
        "storage_days": "StorageDays",
    }

    session_summary_configuration: Optional[SessionSummaryConfiguration] = None
    enabled_memory_types: Optional[Union[list[str], Ref]] = None
    storage_days: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OrchestrationExecutor(PropertyType):
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_": "Lambda",
    }

    lambda_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterDetail(PropertyType):
    TYPE = "Type"
    DESCRIPTION = "Description"
    REQUIRED = "Required"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "required": "Required",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PromptConfiguration(PropertyType):
    PROMPT_TYPE = "PromptType"
    PROMPT_STATE = "PromptState"
    ADDITIONAL_MODEL_REQUEST_FIELDS = "AdditionalModelRequestFields"
    BASE_PROMPT_TEMPLATE = "BasePromptTemplate"
    FOUNDATION_MODEL = "FoundationModel"
    INFERENCE_CONFIGURATION = "InferenceConfiguration"
    PROMPT_CREATION_MODE = "PromptCreationMode"
    PARSER_MODE = "ParserMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_type": "PromptType",
        "prompt_state": "PromptState",
        "additional_model_request_fields": "AdditionalModelRequestFields",
        "base_prompt_template": "BasePromptTemplate",
        "foundation_model": "FoundationModel",
        "inference_configuration": "InferenceConfiguration",
        "prompt_creation_mode": "PromptCreationMode",
        "parser_mode": "ParserMode",
    }

    prompt_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prompt_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    base_prompt_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    foundation_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inference_configuration: Optional[InferenceConfiguration] = None
    prompt_creation_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parser_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptOverrideConfiguration(PropertyType):
    PROMPT_CONFIGURATIONS = "PromptConfigurations"
    OVERRIDE_LAMBDA = "OverrideLambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_configurations": "PromptConfigurations",
        "override_lambda": "OverrideLambda",
    }

    prompt_configurations: Optional[list[PromptConfiguration]] = None
    override_lambda: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Identifier(PropertyType):
    S3_BUCKET_NAME = "S3BucketName"
    S3_OBJECT_KEY = "S3ObjectKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_name": "S3BucketName",
        "s3_object_key": "S3ObjectKey",
    }

    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionSummaryConfiguration(PropertyType):
    MAX_RECENT_SESSIONS = "MaxRecentSessions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_recent_sessions": "MaxRecentSessions",
    }

    max_recent_sessions: Optional[Union[float, Ref, GetAtt, Sub]] = None

