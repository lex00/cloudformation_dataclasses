"""PropertyTypes for AWS::Comprehend::Flywheel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataSecurityConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "labels": "Labels",
    }

    mode: Optional[Union[str, DocumentClassifierMode, Ref, GetAtt, Sub]] = None
    labels: Optional[Union[list[str], Ref]] = None


@dataclass
class EntityRecognitionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_types": "EntityTypes",
    }

    entity_types: Optional[list[EntityTypesListItem]] = None


@dataclass
class EntityTypesListItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "subnets": "Subnets",
        "security_group_ids": "SecurityGroupIds",
    }

    subnets: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

