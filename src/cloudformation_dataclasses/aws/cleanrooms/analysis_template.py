"""PropertyTypes for AWS::CleanRooms::AnalysisTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnalysisParameter(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "referenced_tables": "ReferencedTables",
    }

    referenced_tables: Optional[Union[list[str], Ref]] = None


@dataclass
class AnalysisSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "artifacts": "Artifacts",
        "text": "Text",
    }

    artifacts: Optional[AnalysisTemplateArtifacts] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisSourceMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "artifacts": "Artifacts",
    }

    artifacts: Optional[AnalysisTemplateArtifactMetadata] = None


@dataclass
class AnalysisTemplateArtifact(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "location": "Location",
    }

    location: Optional[S3Location] = None


@dataclass
class AnalysisTemplateArtifactMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entry_point_hash": "EntryPointHash",
        "additional_artifact_hashes": "AdditionalArtifactHashes",
    }

    entry_point_hash: Optional[Hash] = None
    additional_artifact_hashes: Optional[list[Hash]] = None


@dataclass
class AnalysisTemplateArtifacts(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "column_mapping": "ColumnMapping",
    }

    column_mapping: Optional[list[SyntheticDataColumnProperties]] = None


@dataclass
class ErrorMessageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Hash(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sha256": "Sha256",
    }

    sha256: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MLSyntheticDataParameters(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SyntheticDataColumnProperties(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_synthetic_data_parameters": "MlSyntheticDataParameters",
    }

    ml_synthetic_data_parameters: Optional[MLSyntheticDataParameters] = None

