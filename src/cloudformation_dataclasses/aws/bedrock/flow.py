"""PropertyTypes for AWS::Bedrock::Flow."""

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
class AgentFlowNodeConfiguration(PropertyType):
    AGENT_ALIAS_ARN = "AgentAliasArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_alias_arn": "AgentAliasArn",
    }

    agent_alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionFlowNodeConfiguration(PropertyType):
    CONDITIONS = "Conditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "conditions": "Conditions",
    }

    conditions: Optional[list[FlowCondition]] = None


@dataclass
class FieldForReranking(PropertyType):
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_name": "FieldName",
    }

    field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowCondition(PropertyType):
    EXPRESSION = "Expression"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "name": "Name",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowConditionalConnectionConfiguration(PropertyType):
    CONDITION = "Condition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
    }

    condition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowConnection(PropertyType):
    TYPE = "Type"
    TARGET = "Target"
    CONFIGURATION = "Configuration"
    SOURCE = "Source"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "target": "Target",
        "configuration": "Configuration",
        "source": "Source",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration: Optional[FlowConnectionConfiguration] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowConnectionConfiguration(PropertyType):
    DATA = "Data"
    CONDITIONAL = "Conditional"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data": "Data",
        "conditional": "Conditional",
    }

    data: Optional[FlowDataConnectionConfiguration] = None
    conditional: Optional[FlowConditionalConnectionConfiguration] = None


@dataclass
class FlowDataConnectionConfiguration(PropertyType):
    SOURCE_OUTPUT = "SourceOutput"
    TARGET_INPUT = "TargetInput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_output": "SourceOutput",
        "target_input": "TargetInput",
    }

    source_output: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_input: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowDefinition(PropertyType):
    CONNECTIONS = "Connections"
    NODES = "Nodes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connections": "Connections",
        "nodes": "Nodes",
    }

    connections: Optional[list[FlowConnection]] = None
    nodes: Optional[list[FlowNode]] = None


@dataclass
class FlowNode(PropertyType):
    TYPE = "Type"
    CONFIGURATION = "Configuration"
    OUTPUTS = "Outputs"
    INPUTS = "Inputs"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "configuration": "Configuration",
        "outputs": "Outputs",
        "inputs": "Inputs",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration: Optional[FlowNodeConfiguration] = None
    outputs: Optional[list[FlowNodeOutput]] = None
    inputs: Optional[list[FlowNodeInput]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowNodeConfiguration(PropertyType):
    CONDITION = "Condition"
    RETRIEVAL = "Retrieval"
    LOOP = "Loop"
    AGENT = "Agent"
    LAMBDA_FUNCTION = "LambdaFunction"
    INLINE_CODE = "InlineCode"
    LOOP_CONTROLLER = "LoopController"
    INPUT = "Input"
    STORAGE = "Storage"
    KNOWLEDGE_BASE = "KnowledgeBase"
    OUTPUT = "Output"
    ITERATOR = "Iterator"
    COLLECTOR = "Collector"
    LOOP_INPUT = "LoopInput"
    PROMPT = "Prompt"
    LEX = "Lex"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "retrieval": "Retrieval",
        "loop": "Loop",
        "agent": "Agent",
        "lambda_function": "LambdaFunction",
        "inline_code": "InlineCode",
        "loop_controller": "LoopController",
        "input": "Input",
        "storage": "Storage",
        "knowledge_base": "KnowledgeBase",
        "output": "Output",
        "iterator": "Iterator",
        "collector": "Collector",
        "loop_input": "LoopInput",
        "prompt": "Prompt",
        "lex": "Lex",
    }

    condition: Optional[ConditionFlowNodeConfiguration] = None
    retrieval: Optional[RetrievalFlowNodeConfiguration] = None
    loop: Optional[LoopFlowNodeConfiguration] = None
    agent: Optional[AgentFlowNodeConfiguration] = None
    lambda_function: Optional[LambdaFunctionFlowNodeConfiguration] = None
    inline_code: Optional[InlineCodeFlowNodeConfiguration] = None
    loop_controller: Optional[LoopControllerFlowNodeConfiguration] = None
    input: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    storage: Optional[StorageFlowNodeConfiguration] = None
    knowledge_base: Optional[KnowledgeBaseFlowNodeConfiguration] = None
    output: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    iterator: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    collector: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    loop_input: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    prompt: Optional[PromptFlowNodeConfiguration] = None
    lex: Optional[LexFlowNodeConfiguration] = None


@dataclass
class FlowNodeInput(PropertyType):
    TYPE = "Type"
    CATEGORY = "Category"
    EXPRESSION = "Expression"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "category": "Category",
        "expression": "Expression",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    category: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowNodeOutput(PropertyType):
    TYPE = "Type"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowValidation(PropertyType):
    MESSAGE = "Message"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class InlineCodeFlowNodeConfiguration(PropertyType):
    LANGUAGE = "Language"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language": "Language",
        "code": "Code",
    }

    language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseFlowNodeConfiguration(PropertyType):
    ORCHESTRATION_CONFIGURATION = "OrchestrationConfiguration"
    GUARDRAIL_CONFIGURATION = "GuardrailConfiguration"
    INFERENCE_CONFIGURATION = "InferenceConfiguration"
    KNOWLEDGE_BASE_ID = "KnowledgeBaseId"
    PROMPT_TEMPLATE = "PromptTemplate"
    RERANKING_CONFIGURATION = "RerankingConfiguration"
    NUMBER_OF_RESULTS = "NumberOfResults"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "orchestration_configuration": "OrchestrationConfiguration",
        "guardrail_configuration": "GuardrailConfiguration",
        "inference_configuration": "InferenceConfiguration",
        "knowledge_base_id": "KnowledgeBaseId",
        "prompt_template": "PromptTemplate",
        "reranking_configuration": "RerankingConfiguration",
        "number_of_results": "NumberOfResults",
        "model_id": "ModelId",
    }

    orchestration_configuration: Optional[KnowledgeBaseOrchestrationConfiguration] = None
    guardrail_configuration: Optional[GuardrailConfiguration] = None
    inference_configuration: Optional[PromptInferenceConfiguration] = None
    knowledge_base_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prompt_template: Optional[KnowledgeBasePromptTemplate] = None
    reranking_configuration: Optional[VectorSearchRerankingConfiguration] = None
    number_of_results: Optional[Union[float, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseOrchestrationConfiguration(PropertyType):
    INFERENCE_CONFIG = "InferenceConfig"
    ADDITIONAL_MODEL_REQUEST_FIELDS = "AdditionalModelRequestFields"
    PERFORMANCE_CONFIG = "PerformanceConfig"
    PROMPT_TEMPLATE = "PromptTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_config": "InferenceConfig",
        "additional_model_request_fields": "AdditionalModelRequestFields",
        "performance_config": "PerformanceConfig",
        "prompt_template": "PromptTemplate",
    }

    inference_config: Optional[PromptInferenceConfiguration] = None
    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    performance_config: Optional[PerformanceConfiguration] = None
    prompt_template: Optional[KnowledgeBasePromptTemplate] = None


@dataclass
class KnowledgeBasePromptTemplate(PropertyType):
    TEXT_PROMPT_TEMPLATE = "TextPromptTemplate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_prompt_template": "TextPromptTemplate",
    }

    text_prompt_template: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaFunctionFlowNodeConfiguration(PropertyType):
    LAMBDA_ARN = "LambdaArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LexFlowNodeConfiguration(PropertyType):
    BOT_ALIAS_ARN = "BotAliasArn"
    LOCALE_ID = "LocaleId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bot_alias_arn": "BotAliasArn",
        "locale_id": "LocaleId",
    }

    bot_alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    locale_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoopControllerFlowNodeConfiguration(PropertyType):
    CONTINUE_CONDITION = "ContinueCondition"
    MAX_ITERATIONS = "MaxIterations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "continue_condition": "ContinueCondition",
        "max_iterations": "MaxIterations",
    }

    continue_condition: Optional[FlowCondition] = None
    max_iterations: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LoopFlowNodeConfiguration(PropertyType):
    DEFINITION = "Definition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
    }

    definition: Optional[FlowDefinition] = None


@dataclass
class MetadataConfigurationForReranking(PropertyType):
    SELECTIVE_MODE_CONFIGURATION = "SelectiveModeConfiguration"
    SELECTION_MODE = "SelectionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "selective_mode_configuration": "SelectiveModeConfiguration",
        "selection_mode": "SelectionMode",
    }

    selective_mode_configuration: Optional[RerankingMetadataSelectiveModeConfiguration] = None
    selection_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PerformanceConfiguration(PropertyType):
    LATENCY = "Latency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "latency": "Latency",
    }

    latency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptFlowNodeConfiguration(PropertyType):
    GUARDRAIL_CONFIGURATION = "GuardrailConfiguration"
    SOURCE_CONFIGURATION = "SourceConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_configuration": "GuardrailConfiguration",
        "source_configuration": "SourceConfiguration",
    }

    guardrail_configuration: Optional[GuardrailConfiguration] = None
    source_configuration: Optional[PromptFlowNodeSourceConfiguration] = None


@dataclass
class PromptFlowNodeInlineConfiguration(PropertyType):
    INFERENCE_CONFIGURATION = "InferenceConfiguration"
    TEMPLATE_CONFIGURATION = "TemplateConfiguration"
    TEMPLATE_TYPE = "TemplateType"
    MODEL_ID = "ModelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_configuration": "InferenceConfiguration",
        "template_configuration": "TemplateConfiguration",
        "template_type": "TemplateType",
        "model_id": "ModelId",
    }

    inference_configuration: Optional[PromptInferenceConfiguration] = None
    template_configuration: Optional[PromptTemplateConfiguration] = None
    template_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptFlowNodeResourceConfiguration(PropertyType):
    PROMPT_ARN = "PromptArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prompt_arn": "PromptArn",
    }

    prompt_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PromptFlowNodeSourceConfiguration(PropertyType):
    RESOURCE = "Resource"
    INLINE = "Inline"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource": "Resource",
        "inline": "Inline",
    }

    resource: Optional[PromptFlowNodeResourceConfiguration] = None
    inline: Optional[PromptFlowNodeInlineConfiguration] = None


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
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
    }

    text: Optional[TextPromptTemplateConfiguration] = None


@dataclass
class RerankingMetadataSelectiveModeConfiguration(PropertyType):
    FIELDS_TO_INCLUDE = "FieldsToInclude"
    FIELDS_TO_EXCLUDE = "FieldsToExclude"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fields_to_include": "FieldsToInclude",
        "fields_to_exclude": "FieldsToExclude",
    }

    fields_to_include: Optional[list[FieldForReranking]] = None
    fields_to_exclude: Optional[list[FieldForReranking]] = None


@dataclass
class RetrievalFlowNodeConfiguration(PropertyType):
    SERVICE_CONFIGURATION = "ServiceConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_configuration": "ServiceConfiguration",
    }

    service_configuration: Optional[RetrievalFlowNodeServiceConfiguration] = None


@dataclass
class RetrievalFlowNodeS3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetrievalFlowNodeServiceConfiguration(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[RetrievalFlowNodeS3Configuration] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    VERSION = "Version"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageFlowNodeConfiguration(PropertyType):
    SERVICE_CONFIGURATION = "ServiceConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_configuration": "ServiceConfiguration",
    }

    service_configuration: Optional[StorageFlowNodeServiceConfiguration] = None


@dataclass
class StorageFlowNodeS3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageFlowNodeServiceConfiguration(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[StorageFlowNodeS3Configuration] = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    INPUT_VARIABLES = "InputVariables"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_variables": "InputVariables",
        "text": "Text",
    }

    input_variables: Optional[list[PromptInputVariable]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VectorSearchBedrockRerankingConfiguration(PropertyType):
    NUMBER_OF_RERANKED_RESULTS = "NumberOfRerankedResults"
    METADATA_CONFIGURATION = "MetadataConfiguration"
    MODEL_CONFIGURATION = "ModelConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_reranked_results": "NumberOfRerankedResults",
        "metadata_configuration": "MetadataConfiguration",
        "model_configuration": "ModelConfiguration",
    }

    number_of_reranked_results: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metadata_configuration: Optional[MetadataConfigurationForReranking] = None
    model_configuration: Optional[VectorSearchBedrockRerankingModelConfiguration] = None


@dataclass
class VectorSearchBedrockRerankingModelConfiguration(PropertyType):
    MODEL_ARN = "ModelArn"
    ADDITIONAL_MODEL_REQUEST_FIELDS = "AdditionalModelRequestFields"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
        "additional_model_request_fields": "AdditionalModelRequestFields",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_model_request_fields: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class VectorSearchRerankingConfiguration(PropertyType):
    TYPE = "Type"
    BEDROCK_RERANKING_CONFIGURATION = "BedrockRerankingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "bedrock_reranking_configuration": "BedrockRerankingConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_reranking_configuration: Optional[VectorSearchBedrockRerankingConfiguration] = None

