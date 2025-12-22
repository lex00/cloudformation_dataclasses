"""PropertyTypes for AWS::Comprehend::Flywheel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AugmentedManifestsDocumentTypeFormat:
    """AugmentedManifestsDocumentTypeFormat enum values."""

    PLAIN_TEXT_DOCUMENT = "PLAIN_TEXT_DOCUMENT"
    SEMI_STRUCTURED_DOCUMENT = "SEMI_STRUCTURED_DOCUMENT"


class BlockType:
    """BlockType enum values."""

    LINE = "LINE"
    WORD = "WORD"


class DatasetDataFormat:
    """DatasetDataFormat enum values."""

    COMPREHEND_CSV = "COMPREHEND_CSV"
    AUGMENTED_MANIFEST = "AUGMENTED_MANIFEST"


class DatasetStatus:
    """DatasetStatus enum values."""

    CREATING = "CREATING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DatasetType:
    """DatasetType enum values."""

    TRAIN = "TRAIN"
    TEST = "TEST"


class DocumentClassifierDataFormat:
    """DocumentClassifierDataFormat enum values."""

    COMPREHEND_CSV = "COMPREHEND_CSV"
    AUGMENTED_MANIFEST = "AUGMENTED_MANIFEST"


class DocumentClassifierDocumentTypeFormat:
    """DocumentClassifierDocumentTypeFormat enum values."""

    PLAIN_TEXT_DOCUMENT = "PLAIN_TEXT_DOCUMENT"
    SEMI_STRUCTURED_DOCUMENT = "SEMI_STRUCTURED_DOCUMENT"


class DocumentClassifierMode:
    """DocumentClassifierMode enum values."""

    MULTI_CLASS = "MULTI_CLASS"
    MULTI_LABEL = "MULTI_LABEL"


class DocumentReadAction:
    """DocumentReadAction enum values."""

    TEXTRACT_DETECT_DOCUMENT_TEXT = "TEXTRACT_DETECT_DOCUMENT_TEXT"
    TEXTRACT_ANALYZE_DOCUMENT = "TEXTRACT_ANALYZE_DOCUMENT"


class DocumentReadFeatureTypes:
    """DocumentReadFeatureTypes enum values."""

    TABLES = "TABLES"
    FORMS = "FORMS"


class DocumentReadMode:
    """DocumentReadMode enum values."""

    SERVICE_DEFAULT = "SERVICE_DEFAULT"
    FORCE_DOCUMENT_READ_ACTION = "FORCE_DOCUMENT_READ_ACTION"


class DocumentType:
    """DocumentType enum values."""

    NATIVE_PDF = "NATIVE_PDF"
    SCANNED_PDF = "SCANNED_PDF"
    MS_WORD = "MS_WORD"
    IMAGE = "IMAGE"
    PLAIN_TEXT = "PLAIN_TEXT"
    TEXTRACT_DETECT_DOCUMENT_TEXT_JSON = "TEXTRACT_DETECT_DOCUMENT_TEXT_JSON"
    TEXTRACT_ANALYZE_DOCUMENT_JSON = "TEXTRACT_ANALYZE_DOCUMENT_JSON"


class EndpointStatus:
    """EndpointStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    IN_SERVICE = "IN_SERVICE"
    UPDATING = "UPDATING"


class EntityRecognizerDataFormat:
    """EntityRecognizerDataFormat enum values."""

    COMPREHEND_CSV = "COMPREHEND_CSV"
    AUGMENTED_MANIFEST = "AUGMENTED_MANIFEST"


class EntityType:
    """EntityType enum values."""

    PERSON = "PERSON"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"
    COMMERCIAL_ITEM = "COMMERCIAL_ITEM"
    EVENT = "EVENT"
    DATE = "DATE"
    QUANTITY = "QUANTITY"
    TITLE = "TITLE"
    OTHER = "OTHER"


class FlywheelIterationStatus:
    """FlywheelIterationStatus enum values."""

    TRAINING = "TRAINING"
    EVALUATING = "EVALUATING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOP_REQUESTED = "STOP_REQUESTED"
    STOPPED = "STOPPED"


class FlywheelStatus:
    """FlywheelStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class InputFormat:
    """InputFormat enum values."""

    ONE_DOC_PER_FILE = "ONE_DOC_PER_FILE"
    ONE_DOC_PER_LINE = "ONE_DOC_PER_LINE"


class InvalidRequestDetailReason:
    """InvalidRequestDetailReason enum values."""

    DOCUMENT_SIZE_EXCEEDED = "DOCUMENT_SIZE_EXCEEDED"
    UNSUPPORTED_DOC_TYPE = "UNSUPPORTED_DOC_TYPE"
    PAGE_LIMIT_EXCEEDED = "PAGE_LIMIT_EXCEEDED"
    TEXTRACT_ACCESS_DENIED = "TEXTRACT_ACCESS_DENIED"


class InvalidRequestReason:
    """InvalidRequestReason enum values."""

    INVALID_DOCUMENT = "INVALID_DOCUMENT"


class JobStatus:
    """JobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOP_REQUESTED = "STOP_REQUESTED"
    STOPPED = "STOPPED"


class LanguageCode:
    """LanguageCode enum values."""

    EN = "en"
    ES = "es"
    FR = "fr"
    DE = "de"
    IT = "it"
    PT = "pt"
    AR = "ar"
    HI = "hi"
    JA = "ja"
    KO = "ko"
    ZH = "zh"
    ZH_TW = "zh-TW"


class ModelStatus:
    """ModelStatus enum values."""

    SUBMITTED = "SUBMITTED"
    TRAINING = "TRAINING"
    DELETING = "DELETING"
    STOP_REQUESTED = "STOP_REQUESTED"
    STOPPED = "STOPPED"
    IN_ERROR = "IN_ERROR"
    TRAINED = "TRAINED"
    TRAINED_WITH_WARNING = "TRAINED_WITH_WARNING"


class ModelType:
    """ModelType enum values."""

    DOCUMENT_CLASSIFIER = "DOCUMENT_CLASSIFIER"
    ENTITY_RECOGNIZER = "ENTITY_RECOGNIZER"


class PageBasedErrorCode:
    """PageBasedErrorCode enum values."""

    TEXTRACT_BAD_PAGE = "TEXTRACT_BAD_PAGE"
    TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED = "TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED"
    PAGE_CHARACTERS_EXCEEDED = "PAGE_CHARACTERS_EXCEEDED"
    PAGE_SIZE_EXCEEDED = "PAGE_SIZE_EXCEEDED"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"


class PageBasedWarningCode:
    """PageBasedWarningCode enum values."""

    INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL = "INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL"
    INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL = "INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL"


class PartOfSpeechTagType:
    """PartOfSpeechTagType enum values."""

    ADJ = "ADJ"
    ADP = "ADP"
    ADV = "ADV"
    AUX = "AUX"
    CONJ = "CONJ"
    CCONJ = "CCONJ"
    DET = "DET"
    INTJ = "INTJ"
    NOUN = "NOUN"
    NUM = "NUM"
    O = "O"
    PART = "PART"
    PRON = "PRON"
    PROPN = "PROPN"
    PUNCT = "PUNCT"
    SCONJ = "SCONJ"
    SYM = "SYM"
    VERB = "VERB"


class PiiEntitiesDetectionMaskMode:
    """PiiEntitiesDetectionMaskMode enum values."""

    MASK = "MASK"
    REPLACE_WITH_PII_ENTITY_TYPE = "REPLACE_WITH_PII_ENTITY_TYPE"


class PiiEntitiesDetectionMode:
    """PiiEntitiesDetectionMode enum values."""

    ONLY_REDACTION = "ONLY_REDACTION"
    ONLY_OFFSETS = "ONLY_OFFSETS"


class PiiEntityType:
    """PiiEntityType enum values."""

    BANK_ACCOUNT_NUMBER = "BANK_ACCOUNT_NUMBER"
    BANK_ROUTING = "BANK_ROUTING"
    CREDIT_DEBIT_NUMBER = "CREDIT_DEBIT_NUMBER"
    CREDIT_DEBIT_CVV = "CREDIT_DEBIT_CVV"
    CREDIT_DEBIT_EXPIRY = "CREDIT_DEBIT_EXPIRY"
    PIN = "PIN"
    EMAIL = "EMAIL"
    ADDRESS = "ADDRESS"
    NAME = "NAME"
    PHONE = "PHONE"
    SSN = "SSN"
    DATE_TIME = "DATE_TIME"
    PASSPORT_NUMBER = "PASSPORT_NUMBER"
    DRIVER_ID = "DRIVER_ID"
    URL = "URL"
    AGE = "AGE"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    AWS_ACCESS_KEY = "AWS_ACCESS_KEY"
    AWS_SECRET_KEY = "AWS_SECRET_KEY"
    IP_ADDRESS = "IP_ADDRESS"
    MAC_ADDRESS = "MAC_ADDRESS"
    ALL = "ALL"
    LICENSE_PLATE = "LICENSE_PLATE"
    VEHICLE_IDENTIFICATION_NUMBER = "VEHICLE_IDENTIFICATION_NUMBER"
    UK_NATIONAL_INSURANCE_NUMBER = "UK_NATIONAL_INSURANCE_NUMBER"
    CA_SOCIAL_INSURANCE_NUMBER = "CA_SOCIAL_INSURANCE_NUMBER"
    US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER = "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER"
    UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER = "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER"
    IN_PERMANENT_ACCOUNT_NUMBER = "IN_PERMANENT_ACCOUNT_NUMBER"
    IN_NREGA = "IN_NREGA"
    INTERNATIONAL_BANK_ACCOUNT_NUMBER = "INTERNATIONAL_BANK_ACCOUNT_NUMBER"
    SWIFT_CODE = "SWIFT_CODE"
    UK_NATIONAL_HEALTH_SERVICE_NUMBER = "UK_NATIONAL_HEALTH_SERVICE_NUMBER"
    CA_HEALTH_NUMBER = "CA_HEALTH_NUMBER"
    IN_AADHAAR = "IN_AADHAAR"
    IN_VOTER_NUMBER = "IN_VOTER_NUMBER"


class RelationshipType:
    """RelationshipType enum values."""

    CHILD = "CHILD"


class SentimentType:
    """SentimentType enum values."""

    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    MIXED = "MIXED"


class Split:
    """Split enum values."""

    TRAIN = "TRAIN"
    TEST = "TEST"


class SyntaxLanguageCode:
    """SyntaxLanguageCode enum values."""

    EN = "en"
    ES = "es"
    FR = "fr"
    DE = "de"
    IT = "it"
    PT = "pt"


class TargetedSentimentEntityType:
    """TargetedSentimentEntityType enum values."""

    PERSON = "PERSON"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"
    FACILITY = "FACILITY"
    BRAND = "BRAND"
    COMMERCIAL_ITEM = "COMMERCIAL_ITEM"
    MOVIE = "MOVIE"
    MUSIC = "MUSIC"
    BOOK = "BOOK"
    SOFTWARE = "SOFTWARE"
    GAME = "GAME"
    PERSONAL_TITLE = "PERSONAL_TITLE"
    EVENT = "EVENT"
    DATE = "DATE"
    QUANTITY = "QUANTITY"
    ATTRIBUTE = "ATTRIBUTE"
    OTHER = "OTHER"


class ToxicContentType:
    """ToxicContentType enum values."""

    GRAPHIC = "GRAPHIC"
    HARASSMENT_OR_ABUSE = "HARASSMENT_OR_ABUSE"
    HATE_SPEECH = "HATE_SPEECH"
    INSULT = "INSULT"
    PROFANITY = "PROFANITY"
    SEXUAL = "SEXUAL"
    VIOLENCE_OR_THREAT = "VIOLENCE_OR_THREAT"


@dataclass
class DataSecurityConfig(PropertyType):
    VPC_CONFIG = "VpcConfig"
    VOLUME_KMS_KEY_ID = "VolumeKmsKeyId"
    MODEL_KMS_KEY_ID = "ModelKmsKeyId"
    DATA_LAKE_KMS_KEY_ID = "DataLakeKmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_config": "VpcConfig",
        "volume_kms_key_id": "VolumeKmsKeyId",
        "model_kms_key_id": "ModelKmsKeyId",
        "data_lake_kms_key_id": "DataLakeKmsKeyId",
    }

    vpc_config: Optional[VpcConfig] = None
    volume_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    model_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_lake_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentClassificationConfig(PropertyType):
    MODE = "Mode"
    LABELS = "Labels"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "labels": "Labels",
    }

    mode: Optional[Union[str, DocumentClassifierMode, Ref, GetAtt, Sub]] = None
    labels: Optional[Union[list[str], Ref]] = None


@dataclass
class EntityRecognitionConfig(PropertyType):
    ENTITY_TYPES = "EntityTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_types": "EntityTypes",
    }

    entity_types: Optional[list[EntityTypesListItem]] = None


@dataclass
class EntityTypesListItem(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskConfig(PropertyType):
    LANGUAGE_CODE = "LanguageCode"
    DOCUMENT_CLASSIFICATION_CONFIG = "DocumentClassificationConfig"
    ENTITY_RECOGNITION_CONFIG = "EntityRecognitionConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language_code": "LanguageCode",
        "document_classification_config": "DocumentClassificationConfig",
        "entity_recognition_config": "EntityRecognitionConfig",
    }

    language_code: Optional[Union[str, LanguageCode, Ref, GetAtt, Sub]] = None
    document_classification_config: Optional[DocumentClassificationConfig] = None
    entity_recognition_config: Optional[EntityRecognitionConfig] = None


@dataclass
class VpcConfig(PropertyType):
    SUBNETS = "Subnets"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

