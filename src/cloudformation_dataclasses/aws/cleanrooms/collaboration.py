"""PropertyTypes for AWS::CleanRooms::Collaboration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataEncryptionMetadata(PropertyType):
    ALLOW_CLEARTEXT = "AllowCleartext"
    PRESERVE_NULLS = "PreserveNulls"
    ALLOW_JOINS_ON_COLUMNS_WITH_DIFFERENT_NAMES = "AllowJoinsOnColumnsWithDifferentNames"
    ALLOW_DUPLICATES = "AllowDuplicates"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_cleartext": "AllowCleartext",
        "preserve_nulls": "PreserveNulls",
        "allow_joins_on_columns_with_different_names": "AllowJoinsOnColumnsWithDifferentNames",
        "allow_duplicates": "AllowDuplicates",
    }

    allow_cleartext: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    preserve_nulls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    allow_joins_on_columns_with_different_names: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    allow_duplicates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class JobComputePaymentConfig(PropertyType):
    IS_RESPONSIBLE = "IsResponsible"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MLMemberAbilities(PropertyType):
    CUSTOM_ML_MEMBER_ABILITIES = "CustomMLMemberAbilities"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_ml_member_abilities": "CustomMLMemberAbilities",
    }

    custom_ml_member_abilities: Optional[Union[list[str], Ref]] = None


@dataclass
class MLPaymentConfig(PropertyType):
    MODEL_INFERENCE = "ModelInference"
    SYNTHETIC_DATA_GENERATION = "SyntheticDataGeneration"
    MODEL_TRAINING = "ModelTraining"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_inference": "ModelInference",
        "synthetic_data_generation": "SyntheticDataGeneration",
        "model_training": "ModelTraining",
    }

    model_inference: Optional[ModelInferencePaymentConfig] = None
    synthetic_data_generation: Optional[SyntheticDataGenerationPaymentConfig] = None
    model_training: Optional[ModelTrainingPaymentConfig] = None


@dataclass
class MemberSpecification(PropertyType):
    ACCOUNT_ID = "AccountId"
    ML_MEMBER_ABILITIES = "MLMemberAbilities"
    DISPLAY_NAME = "DisplayName"
    MEMBER_ABILITIES = "MemberAbilities"
    PAYMENT_CONFIGURATION = "PaymentConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_id": "AccountId",
        "ml_member_abilities": "MLMemberAbilities",
        "display_name": "DisplayName",
        "member_abilities": "MemberAbilities",
        "payment_configuration": "PaymentConfiguration",
    }

    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ml_member_abilities: Optional[MLMemberAbilities] = None
    display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    member_abilities: Optional[Union[list[str], Ref]] = None
    payment_configuration: Optional[PaymentConfiguration] = None


@dataclass
class ModelInferencePaymentConfig(PropertyType):
    IS_RESPONSIBLE = "IsResponsible"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ModelTrainingPaymentConfig(PropertyType):
    IS_RESPONSIBLE = "IsResponsible"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PaymentConfiguration(PropertyType):
    JOB_COMPUTE = "JobCompute"
    QUERY_COMPUTE = "QueryCompute"
    MACHINE_LEARNING = "MachineLearning"

    _property_mappings: ClassVar[dict[str, str]] = {
        "job_compute": "JobCompute",
        "query_compute": "QueryCompute",
        "machine_learning": "MachineLearning",
    }

    job_compute: Optional[JobComputePaymentConfig] = None
    query_compute: Optional[QueryComputePaymentConfig] = None
    machine_learning: Optional[MLPaymentConfig] = None


@dataclass
class QueryComputePaymentConfig(PropertyType):
    IS_RESPONSIBLE = "IsResponsible"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SyntheticDataGenerationPaymentConfig(PropertyType):
    IS_RESPONSIBLE = "IsResponsible"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None

