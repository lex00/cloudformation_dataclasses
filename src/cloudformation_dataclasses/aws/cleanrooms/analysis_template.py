"""PropertyTypes for AWS::CleanRooms::AnalysisTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnalysisParameter(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    TYPE = "Type"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "type_": "Type",
        "name": "Name",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisSchema(PropertyType):
    REFERENCED_TABLES = "ReferencedTables"

    _property_mappings: ClassVar[dict[str, str]] = {
        "referenced_tables": "ReferencedTables",
    }

    referenced_tables: Optional[Union[list[str], Ref]] = None


@dataclass
class AnalysisSource(PropertyType):
    ARTIFACTS = "Artifacts"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "artifacts": "Artifacts",
        "text": "Text",
    }

    artifacts: Optional[AnalysisTemplateArtifacts] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisSourceMetadata(PropertyType):
    ARTIFACTS = "Artifacts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "artifacts": "Artifacts",
    }

    artifacts: Optional[AnalysisTemplateArtifactMetadata] = None


@dataclass
class AnalysisTemplateArtifact(PropertyType):
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "location": "Location",
    }

    location: Optional[S3Location] = None


@dataclass
class AnalysisTemplateArtifactMetadata(PropertyType):
    ENTRY_POINT_HASH = "EntryPointHash"
    ADDITIONAL_ARTIFACT_HASHES = "AdditionalArtifactHashes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entry_point_hash": "EntryPointHash",
        "additional_artifact_hashes": "AdditionalArtifactHashes",
    }

    entry_point_hash: Optional[Hash] = None
    additional_artifact_hashes: Optional[list[Hash]] = None


@dataclass
class AnalysisTemplateArtifacts(PropertyType):
    ADDITIONAL_ARTIFACTS = "AdditionalArtifacts"
    ENTRY_POINT = "EntryPoint"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_artifacts": "AdditionalArtifacts",
        "entry_point": "EntryPoint",
        "role_arn": "RoleArn",
    }

    additional_artifacts: Optional[list[AnalysisTemplateArtifact]] = None
    entry_point: Optional[AnalysisTemplateArtifact] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ColumnClassificationDetails(PropertyType):
    COLUMN_MAPPING = "ColumnMapping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_mapping": "ColumnMapping",
    }

    column_mapping: Optional[list[SyntheticDataColumnProperties]] = None


@dataclass
class ErrorMessageConfiguration(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Hash(PropertyType):
    SHA256 = "Sha256"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sha256": "Sha256",
    }

    sha256: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MLSyntheticDataParameters(PropertyType):
    COLUMN_CLASSIFICATION = "ColumnClassification"
    EPSILON = "Epsilon"
    MAX_MEMBERSHIP_INFERENCE_ATTACK_SCORE = "MaxMembershipInferenceAttackScore"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_classification": "ColumnClassification",
        "epsilon": "Epsilon",
        "max_membership_inference_attack_score": "MaxMembershipInferenceAttackScore",
    }

    column_classification: Optional[ColumnClassificationDetails] = None
    epsilon: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_membership_inference_attack_score: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SyntheticDataColumnProperties(PropertyType):
    COLUMN_NAME = "ColumnName"
    COLUMN_TYPE = "ColumnType"
    IS_PREDICTIVE_VALUE = "IsPredictiveValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "column_type": "ColumnType",
        "is_predictive_value": "IsPredictiveValue",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_predictive_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SyntheticDataParameters(PropertyType):
    ML_SYNTHETIC_DATA_PARAMETERS = "MlSyntheticDataParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_synthetic_data_parameters": "MlSyntheticDataParameters",
    }

    ml_synthetic_data_parameters: Optional[MLSyntheticDataParameters] = None

