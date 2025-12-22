"""PropertyTypes for AWS::Bedrock::DataAutomationProject."""

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
class AudioExtractionCategory(PropertyType):
    TYPES = "Types"
    STATE = "State"
    TYPE_CONFIGURATION = "TypeConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "state": "State",
        "type_configuration": "TypeConfiguration",
    }

    types: Optional[Union[list[str], Ref]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_configuration: Optional[AudioExtractionCategoryTypeConfiguration] = None


@dataclass
class AudioExtractionCategoryTypeConfiguration(PropertyType):
    TRANSCRIPT = "Transcript"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transcript": "Transcript",
    }

    transcript: Optional[TranscriptConfiguration] = None


@dataclass
class AudioLanguageConfiguration(PropertyType):
    IDENTIFY_MULTIPLE_LANGUAGES = "IdentifyMultipleLanguages"
    GENERATIVE_OUTPUT_LANGUAGE = "GenerativeOutputLanguage"
    INPUT_LANGUAGES = "InputLanguages"

    _property_mappings: ClassVar[dict[str, str]] = {
        "identify_multiple_languages": "IdentifyMultipleLanguages",
        "generative_output_language": "GenerativeOutputLanguage",
        "input_languages": "InputLanguages",
    }

    identify_multiple_languages: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    generative_output_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_languages: Optional[Union[list[str], Ref]] = None


@dataclass
class AudioOverrideConfiguration(PropertyType):
    SENSITIVE_DATA_CONFIGURATION = "SensitiveDataConfiguration"
    LANGUAGE_CONFIGURATION = "LanguageConfiguration"
    MODALITY_PROCESSING = "ModalityProcessing"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sensitive_data_configuration": "SensitiveDataConfiguration",
        "language_configuration": "LanguageConfiguration",
        "modality_processing": "ModalityProcessing",
    }

    sensitive_data_configuration: Optional[SensitiveDataConfiguration] = None
    language_configuration: Optional[AudioLanguageConfiguration] = None
    modality_processing: Optional[ModalityProcessingConfiguration] = None


@dataclass
class AudioStandardExtraction(PropertyType):
    CATEGORY = "Category"

    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
    }

    category: Optional[AudioExtractionCategory] = None


@dataclass
class AudioStandardGenerativeField(PropertyType):
    TYPES = "Types"
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "state": "State",
    }

    types: Optional[Union[list[str], Ref]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AudioStandardOutputConfiguration(PropertyType):
    GENERATIVE_FIELD = "GenerativeField"
    EXTRACTION = "Extraction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "generative_field": "GenerativeField",
        "extraction": "Extraction",
    }

    generative_field: Optional[AudioStandardGenerativeField] = None
    extraction: Optional[AudioStandardExtraction] = None


@dataclass
class BlueprintItem(PropertyType):
    BLUEPRINT_VERSION = "BlueprintVersion"
    BLUEPRINT_STAGE = "BlueprintStage"
    BLUEPRINT_ARN = "BlueprintArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "blueprint_version": "BlueprintVersion",
        "blueprint_stage": "BlueprintStage",
        "blueprint_arn": "BlueprintArn",
    }

    blueprint_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    blueprint_stage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    blueprint_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ChannelLabelingConfiguration(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomOutputConfiguration(PropertyType):
    BLUEPRINTS = "Blueprints"

    _property_mappings: ClassVar[dict[str, str]] = {
        "blueprints": "Blueprints",
    }

    blueprints: Optional[list[BlueprintItem]] = None


@dataclass
class DocumentBoundingBox(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentExtractionGranularity(PropertyType):
    TYPES = "Types"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
    }

    types: Optional[Union[list[str], Ref]] = None


@dataclass
class DocumentOutputAdditionalFileFormat(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentOutputFormat(PropertyType):
    TEXT_FORMAT = "TextFormat"
    ADDITIONAL_FILE_FORMAT = "AdditionalFileFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_format": "TextFormat",
        "additional_file_format": "AdditionalFileFormat",
    }

    text_format: Optional[DocumentOutputTextFormat] = None
    additional_file_format: Optional[DocumentOutputAdditionalFileFormat] = None


@dataclass
class DocumentOutputTextFormat(PropertyType):
    TYPES = "Types"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
    }

    types: Optional[Union[list[str], Ref]] = None


@dataclass
class DocumentOverrideConfiguration(PropertyType):
    SENSITIVE_DATA_CONFIGURATION = "SensitiveDataConfiguration"
    SPLITTER = "Splitter"
    MODALITY_PROCESSING = "ModalityProcessing"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sensitive_data_configuration": "SensitiveDataConfiguration",
        "splitter": "Splitter",
        "modality_processing": "ModalityProcessing",
    }

    sensitive_data_configuration: Optional[SensitiveDataConfiguration] = None
    splitter: Optional[SplitterConfiguration] = None
    modality_processing: Optional[ModalityProcessingConfiguration] = None


@dataclass
class DocumentStandardExtraction(PropertyType):
    BOUNDING_BOX = "BoundingBox"
    GRANULARITY = "Granularity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bounding_box": "BoundingBox",
        "granularity": "Granularity",
    }

    bounding_box: Optional[DocumentBoundingBox] = None
    granularity: Optional[DocumentExtractionGranularity] = None


@dataclass
class DocumentStandardGenerativeField(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentStandardOutputConfiguration(PropertyType):
    OUTPUT_FORMAT = "OutputFormat"
    GENERATIVE_FIELD = "GenerativeField"
    EXTRACTION = "Extraction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_format": "OutputFormat",
        "generative_field": "GenerativeField",
        "extraction": "Extraction",
    }

    output_format: Optional[DocumentOutputFormat] = None
    generative_field: Optional[DocumentStandardGenerativeField] = None
    extraction: Optional[DocumentStandardExtraction] = None


@dataclass
class ImageBoundingBox(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageExtractionCategory(PropertyType):
    TYPES = "Types"
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "state": "State",
    }

    types: Optional[Union[list[str], Ref]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageOverrideConfiguration(PropertyType):
    SENSITIVE_DATA_CONFIGURATION = "SensitiveDataConfiguration"
    MODALITY_PROCESSING = "ModalityProcessing"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sensitive_data_configuration": "SensitiveDataConfiguration",
        "modality_processing": "ModalityProcessing",
    }

    sensitive_data_configuration: Optional[SensitiveDataConfiguration] = None
    modality_processing: Optional[ModalityProcessingConfiguration] = None


@dataclass
class ImageStandardExtraction(PropertyType):
    CATEGORY = "Category"
    BOUNDING_BOX = "BoundingBox"

    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "bounding_box": "BoundingBox",
    }

    category: Optional[ImageExtractionCategory] = None
    bounding_box: Optional[ImageBoundingBox] = None


@dataclass
class ImageStandardGenerativeField(PropertyType):
    TYPES = "Types"
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "state": "State",
    }

    types: Optional[Union[list[str], Ref]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageStandardOutputConfiguration(PropertyType):
    GENERATIVE_FIELD = "GenerativeField"
    EXTRACTION = "Extraction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "generative_field": "GenerativeField",
        "extraction": "Extraction",
    }

    generative_field: Optional[ImageStandardGenerativeField] = None
    extraction: Optional[ImageStandardExtraction] = None


@dataclass
class ModalityProcessingConfiguration(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModalityRoutingConfiguration(PropertyType):
    MP4 = "mp4"
    MOV = "mov"
    PNG = "png"
    JPEG = "jpeg"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mp4": "mp4",
        "mov": "mov",
        "png": "png",
        "jpeg": "jpeg",
    }

    mp4: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mov: Optional[Union[str, Ref, GetAtt, Sub]] = None
    png: Optional[Union[str, Ref, GetAtt, Sub]] = None
    jpeg: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OverrideConfiguration(PropertyType):
    VIDEO = "Video"
    MODALITY_ROUTING = "ModalityRouting"
    DOCUMENT = "Document"
    AUDIO = "Audio"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "video": "Video",
        "modality_routing": "ModalityRouting",
        "document": "Document",
        "audio": "Audio",
        "image": "Image",
    }

    video: Optional[VideoOverrideConfiguration] = None
    modality_routing: Optional[ModalityRoutingConfiguration] = None
    document: Optional[DocumentOverrideConfiguration] = None
    audio: Optional[AudioOverrideConfiguration] = None
    image: Optional[ImageOverrideConfiguration] = None


@dataclass
class PIIEntitiesConfiguration(PropertyType):
    PII_ENTITY_TYPES = "PiiEntityTypes"
    REDACTION_MASK_MODE = "RedactionMaskMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pii_entity_types": "PiiEntityTypes",
        "redaction_mask_mode": "RedactionMaskMode",
    }

    pii_entity_types: Optional[Union[list[str], Ref]] = None
    redaction_mask_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SensitiveDataConfiguration(PropertyType):
    DETECTION_MODE = "DetectionMode"
    PII_ENTITIES_CONFIGURATION = "PiiEntitiesConfiguration"
    DETECTION_SCOPE = "DetectionScope"

    _property_mappings: ClassVar[dict[str, str]] = {
        "detection_mode": "DetectionMode",
        "pii_entities_configuration": "PiiEntitiesConfiguration",
        "detection_scope": "DetectionScope",
    }

    detection_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pii_entities_configuration: Optional[PIIEntitiesConfiguration] = None
    detection_scope: Optional[Union[list[str], Ref]] = None


@dataclass
class SpeakerLabelingConfiguration(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SplitterConfiguration(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StandardOutputConfiguration(PropertyType):
    VIDEO = "Video"
    DOCUMENT = "Document"
    IMAGE = "Image"
    AUDIO = "Audio"

    _property_mappings: ClassVar[dict[str, str]] = {
        "video": "Video",
        "document": "Document",
        "image": "Image",
        "audio": "Audio",
    }

    video: Optional[VideoStandardOutputConfiguration] = None
    document: Optional[DocumentStandardOutputConfiguration] = None
    image: Optional[ImageStandardOutputConfiguration] = None
    audio: Optional[AudioStandardOutputConfiguration] = None


@dataclass
class TranscriptConfiguration(PropertyType):
    CHANNEL_LABELING = "ChannelLabeling"
    SPEAKER_LABELING = "SpeakerLabeling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_labeling": "ChannelLabeling",
        "speaker_labeling": "SpeakerLabeling",
    }

    channel_labeling: Optional[ChannelLabelingConfiguration] = None
    speaker_labeling: Optional[SpeakerLabelingConfiguration] = None


@dataclass
class VideoBoundingBox(PropertyType):
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VideoExtractionCategory(PropertyType):
    TYPES = "Types"
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "state": "State",
    }

    types: Optional[Union[list[str], Ref]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VideoOverrideConfiguration(PropertyType):
    SENSITIVE_DATA_CONFIGURATION = "SensitiveDataConfiguration"
    MODALITY_PROCESSING = "ModalityProcessing"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sensitive_data_configuration": "SensitiveDataConfiguration",
        "modality_processing": "ModalityProcessing",
    }

    sensitive_data_configuration: Optional[SensitiveDataConfiguration] = None
    modality_processing: Optional[ModalityProcessingConfiguration] = None


@dataclass
class VideoStandardExtraction(PropertyType):
    CATEGORY = "Category"
    BOUNDING_BOX = "BoundingBox"

    _property_mappings: ClassVar[dict[str, str]] = {
        "category": "Category",
        "bounding_box": "BoundingBox",
    }

    category: Optional[VideoExtractionCategory] = None
    bounding_box: Optional[VideoBoundingBox] = None


@dataclass
class VideoStandardGenerativeField(PropertyType):
    TYPES = "Types"
    STATE = "State"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "state": "State",
    }

    types: Optional[Union[list[str], Ref]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VideoStandardOutputConfiguration(PropertyType):
    GENERATIVE_FIELD = "GenerativeField"
    EXTRACTION = "Extraction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "generative_field": "GenerativeField",
        "extraction": "Extraction",
    }

    generative_field: Optional[VideoStandardGenerativeField] = None
    extraction: Optional[VideoStandardExtraction] = None

