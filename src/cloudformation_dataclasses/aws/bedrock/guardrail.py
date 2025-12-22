"""PropertyTypes for AWS::Bedrock::Guardrail."""

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
class AutomatedReasoningPolicyConfig(PropertyType):
    POLICIES = "Policies"
    CONFIDENCE_THRESHOLD = "ConfidenceThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policies": "Policies",
        "confidence_threshold": "ConfidenceThreshold",
    }

    policies: Optional[Union[list[str], Ref]] = None
    confidence_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ContentFilterConfig(PropertyType):
    OUTPUT_STRENGTH = "OutputStrength"
    TYPE = "Type"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    INPUT_STRENGTH = "InputStrength"
    INPUT_MODALITIES = "InputModalities"
    OUTPUT_ENABLED = "OutputEnabled"
    OUTPUT_MODALITIES = "OutputModalities"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_strength": "OutputStrength",
        "type_": "Type",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "input_strength": "InputStrength",
        "input_modalities": "InputModalities",
        "output_enabled": "OutputEnabled",
        "output_modalities": "OutputModalities",
    }

    output_strength: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_strength: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_modalities: Optional[Union[list[str], Ref]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    output_modalities: Optional[Union[list[str], Ref]] = None


@dataclass
class ContentFiltersTierConfig(PropertyType):
    TIER_NAME = "TierName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tier_name": "TierName",
    }

    tier_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContentPolicyConfig(PropertyType):
    CONTENT_FILTERS_TIER_CONFIG = "ContentFiltersTierConfig"
    FILTERS_CONFIG = "FiltersConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_filters_tier_config": "ContentFiltersTierConfig",
        "filters_config": "FiltersConfig",
    }

    content_filters_tier_config: Optional[ContentFiltersTierConfig] = None
    filters_config: Optional[list[ContentFilterConfig]] = None


@dataclass
class ContextualGroundingFilterConfig(PropertyType):
    TYPE = "Type"
    ACTION = "Action"
    ENABLED = "Enabled"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "action": "Action",
        "enabled": "Enabled",
        "threshold": "Threshold",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ContextualGroundingPolicyConfig(PropertyType):
    FILTERS_CONFIG = "FiltersConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters_config": "FiltersConfig",
    }

    filters_config: Optional[list[ContextualGroundingFilterConfig]] = None


@dataclass
class GuardrailCrossRegionConfig(PropertyType):
    GUARDRAIL_PROFILE_ARN = "GuardrailProfileArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "guardrail_profile_arn": "GuardrailProfileArn",
    }

    guardrail_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedWordsConfig(PropertyType):
    TYPE = "Type"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PiiEntityConfig(PropertyType):
    TYPE = "Type"
    ACTION = "Action"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "action": "Action",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RegexConfig(PropertyType):
    PATTERN = "Pattern"
    ACTION = "Action"
    INPUT_ENABLED = "InputEnabled"
    DESCRIPTION = "Description"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
        "action": "Action",
        "input_enabled": "InputEnabled",
        "description": "Description",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
        "name": "Name",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SensitiveInformationPolicyConfig(PropertyType):
    REGEXES_CONFIG = "RegexesConfig"
    PII_ENTITIES_CONFIG = "PiiEntitiesConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regexes_config": "RegexesConfig",
        "pii_entities_config": "PiiEntitiesConfig",
    }

    regexes_config: Optional[list[RegexConfig]] = None
    pii_entities_config: Optional[list[PiiEntityConfig]] = None


@dataclass
class TopicConfig(PropertyType):
    TYPE = "Type"
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    DEFINITION = "Definition"
    OUTPUT_ENABLED = "OutputEnabled"
    EXAMPLES = "Examples"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "definition": "Definition",
        "output_enabled": "OutputEnabled",
        "examples": "Examples",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    definition: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    examples: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TopicPolicyConfig(PropertyType):
    TOPICS_TIER_CONFIG = "TopicsTierConfig"
    TOPICS_CONFIG = "TopicsConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topics_tier_config": "TopicsTierConfig",
        "topics_config": "TopicsConfig",
    }

    topics_tier_config: Optional[TopicsTierConfig] = None
    topics_config: Optional[list[TopicConfig]] = None


@dataclass
class TopicsTierConfig(PropertyType):
    TIER_NAME = "TierName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tier_name": "TierName",
    }

    tier_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WordConfig(PropertyType):
    INPUT_ENABLED = "InputEnabled"
    INPUT_ACTION = "InputAction"
    OUTPUT_ACTION = "OutputAction"
    OUTPUT_ENABLED = "OutputEnabled"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_enabled": "InputEnabled",
        "input_action": "InputAction",
        "output_action": "OutputAction",
        "output_enabled": "OutputEnabled",
        "text": "Text",
    }

    input_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WordPolicyConfig(PropertyType):
    MANAGED_WORD_LISTS_CONFIG = "ManagedWordListsConfig"
    WORDS_CONFIG = "WordsConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_word_lists_config": "ManagedWordListsConfig",
        "words_config": "WordsConfig",
    }

    managed_word_lists_config: Optional[list[ManagedWordsConfig]] = None
    words_config: Optional[list[WordConfig]] = None

