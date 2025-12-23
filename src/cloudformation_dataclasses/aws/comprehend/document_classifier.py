"""PropertyTypes for AWS::Comprehend::DocumentClassifier."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AugmentedManifestsListItem(PropertyType):
    S3_URI = "S3Uri"
    ATTRIBUTE_NAMES = "AttributeNames"
    SPLIT = "Split"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "attribute_names": "AttributeNames",
        "split": "Split",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute_names: Optional[Union[list[str], Ref]] = None
    split: Optional[Union[str, Split, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentClassifierDocuments(PropertyType):
    S3_URI = "S3Uri"
    TEST_S3_URI = "TestS3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_uri": "S3Uri",
        "test_s3_uri": "TestS3Uri",
    }

    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    test_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentClassifierInputDataConfig(PropertyType):
    DOCUMENT_READER_CONFIG = "DocumentReaderConfig"
    S3_URI = "S3Uri"
    DOCUMENTS = "Documents"
    DATA_FORMAT = "DataFormat"
    DOCUMENT_TYPE = "DocumentType"
    AUGMENTED_MANIFESTS = "AugmentedManifests"
    LABEL_DELIMITER = "LabelDelimiter"
    TEST_S3_URI = "TestS3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "document_reader_config": "DocumentReaderConfig",
        "s3_uri": "S3Uri",
        "documents": "Documents",
        "data_format": "DataFormat",
        "document_type": "DocumentType",
        "augmented_manifests": "AugmentedManifests",
        "label_delimiter": "LabelDelimiter",
        "test_s3_uri": "TestS3Uri",
    }

    document_reader_config: Optional[DocumentReaderConfig] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    documents: Optional[DocumentClassifierDocuments] = None
    data_format: Optional[Union[str, DocumentClassifierDataFormat, Ref, GetAtt, Sub]] = None
    document_type: Optional[Union[str, DocumentClassifierDocumentTypeFormat, Ref, GetAtt, Sub]] = None
    augmented_manifests: Optional[list[AugmentedManifestsListItem]] = None
    label_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    test_s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentClassifierOutputDataConfig(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    S3_URI = "S3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "s3_uri": "S3Uri",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentReaderConfig(PropertyType):
    FEATURE_TYPES = "FeatureTypes"
    DOCUMENT_READ_MODE = "DocumentReadMode"
    DOCUMENT_READ_ACTION = "DocumentReadAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "feature_types": "FeatureTypes",
        "document_read_mode": "DocumentReadMode",
        "document_read_action": "DocumentReadAction",
    }

    feature_types: Optional[Union[list[str], Ref]] = None
    document_read_mode: Optional[Union[str, DocumentReadMode, Ref, GetAtt, Sub]] = None
    document_read_action: Optional[Union[str, DocumentReadAction, Ref, GetAtt, Sub]] = None


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

