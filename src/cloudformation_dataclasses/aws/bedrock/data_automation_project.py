"""PropertyTypes for AWS::Bedrock::DataAutomationProject."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

