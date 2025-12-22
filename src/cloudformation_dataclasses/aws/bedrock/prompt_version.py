"""PropertyTypes for AWS::Bedrock::PromptVersion."""

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
class CachePointBlock(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ChatPromptTemplateConfiguration(PropertyType):
    MESSAGES = "Messages"
    INPUT_VARIABLES = "InputVariables"
    TOOL_CONFIGURATION = "ToolConfiguration"
    SYSTEM = "System"

    _property_mappings: ClassVar[dict[str, str]] = {
        "messages": "Messages",
        "input_variables": "InputVariables",
        "tool_configuration": "ToolConfiguration",
        "system": "System",
    }

    messages: Optional[list[Message]] = None
    input_variables: Optional[list[PromptInputVariable]] = None
    tool_configuration: Optional[ToolConfiguration] = None
    system: Optional[list[SystemContentBlock]] = None


@dataclass
class ContentBlock(PropertyType):
    CACHE_POINT = "CachePoint"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_point": "CachePoint",
        "text": "Text",
    }

    cache_point: Optional[CachePointBlock] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Message(PropertyType):
    ROLE = "Role"
    CONTENT = "Content"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "content": "Content",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content: Optional[list[ContentBlock]] = None


@dataclass
class PromptAgentResource(PropertyType):
    AGENT_IDENTIFIER = "AgentIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_identifier": "AgentIdentifier",
    }

    agent_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptGenAiResource(PropertyType):
    AGENT = "Agent"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent": "Agent",
    }

    agent: Optional[PromptAgentResource] = None


@dataclass
class PromptInferenceConfiguration(PropertyType):
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
    }

    text: Optional[PromptModelInferenceConfiguration] = None


@dataclass
class PromptInputVariable(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptMetadataEntry(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptModelInferenceConfiguration(PropertyType):
    TEMPERATURE = "Temperature"
    STOP_SEQUENCES = "StopSequences"
    MAX_TOKENS = "MaxTokens"
    TOP_P = "TopP"

    _property_mappings: ClassVar[dict[str, str]] = {
        "temperature": "Temperature",
        "stop_sequences": "StopSequences",
        "max_tokens": "MaxTokens",
        "top_p": "TopP",
    }

    temperature: Optional[Union[float, Ref, GetAtt, Sub]] = None
    stop_sequences: Optional[Union[list[str], Ref]] = None
    max_tokens: Optional[Union[float, Ref, GetAtt, Sub]] = None
    top_p: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PromptTemplateConfiguration(PropertyType):
    CHAT = "Chat"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "chat": "Chat",
        "text": "Text",
    }

    chat: Optional[ChatPromptTemplateConfiguration] = None
    text: Optional[TextPromptTemplateConfiguration] = None


@dataclass
class PromptVariant(PropertyType):
    ADDITIONAL_MODEL_REQUEST_FIELDS = "AdditionalModelRequestFields"
    INFERENCE_CONFIGURATION = "InferenceConfiguration"
    METADATA = "Metadata"
    GEN_AI_RESOURCE = "GenAiResource"
    TEMPLATE_CONFIGURATION = "TemplateConfiguration"
    TEMPLATE_TYPE = "TemplateType"
    MODEL_ID = "ModelId"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_model_request_fields": "AdditionalModelRequestFields",
        "inference_configuration": "InferenceConfiguration",
        "metadata": "Metadata",
        "gen_ai_resource": "GenAiResource",
        "template_configuration": "TemplateConfiguration",
        "template_type": "TemplateType",
        "model_id": "ModelId",
        "name": "Name",
    }

    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    inference_configuration: Optional[PromptInferenceConfiguration] = None
    metadata: Optional[list[PromptMetadataEntry]] = None
    gen_ai_resource: Optional[PromptGenAiResource] = None
    template_configuration: Optional[PromptTemplateConfiguration] = None
    template_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpecificToolChoice(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SystemContentBlock(PropertyType):
    CACHE_POINT = "CachePoint"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_point": "CachePoint",
        "text": "Text",
    }

    cache_point: Optional[CachePointBlock] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    INPUT_VARIABLES = "InputVariables"
    CACHE_POINT = "CachePoint"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_variables": "InputVariables",
        "cache_point": "CachePoint",
        "text": "Text",
    }

    input_variables: Optional[list[PromptInputVariable]] = None
    cache_point: Optional[CachePointBlock] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tool(PropertyType):
    CACHE_POINT = "CachePoint"
    TOOL_SPEC = "ToolSpec"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_point": "CachePoint",
        "tool_spec": "ToolSpec",
    }

    cache_point: Optional[CachePointBlock] = None
    tool_spec: Optional[ToolSpecification] = None


@dataclass
class ToolChoice(PropertyType):
    AUTO = "Auto"
    ANY = "Any"
    TOOL = "Tool"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto": "Auto",
        "any": "Any",
        "tool": "Tool",
    }

    auto: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    any: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    tool: Optional[SpecificToolChoice] = None


@dataclass
class ToolConfiguration(PropertyType):
    TOOL_CHOICE = "ToolChoice"
    TOOLS = "Tools"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tool_choice": "ToolChoice",
        "tools": "Tools",
    }

    tool_choice: Optional[ToolChoice] = None
    tools: Optional[list[Tool]] = None


@dataclass
class ToolInputSchema(PropertyType):
    JSON = "Json"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json": "Json",
    }

    json: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class ToolSpecification(PropertyType):
    DESCRIPTION = "Description"
    INPUT_SCHEMA = "InputSchema"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "input_schema": "InputSchema",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_schema: Optional[ToolInputSchema] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

