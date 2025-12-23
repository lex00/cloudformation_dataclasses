"""PropertyTypes for AWS::CleanRooms::Membership."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MembershipJobComputePaymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MembershipMLPaymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_inference": "ModelInference",
        "synthetic_data_generation": "SyntheticDataGeneration",
        "model_training": "ModelTraining",
    }

    model_inference: Optional[MembershipModelInferencePaymentConfig] = None
    synthetic_data_generation: Optional[MembershipSyntheticDataGenerationPaymentConfig] = None
    model_training: Optional[MembershipModelTrainingPaymentConfig] = None


@dataclass
class MembershipModelInferencePaymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MembershipModelTrainingPaymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MembershipPaymentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "job_compute": "JobCompute",
        "query_compute": "QueryCompute",
        "machine_learning": "MachineLearning",
    }

    job_compute: Optional[MembershipJobComputePaymentConfig] = None
    query_compute: Optional[MembershipQueryComputePaymentConfig] = None
    machine_learning: Optional[MembershipMLPaymentConfig] = None


@dataclass
class MembershipProtectedJobOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[ProtectedJobS3OutputConfigurationInput] = None


@dataclass
class MembershipProtectedJobResultConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_configuration": "OutputConfiguration",
        "role_arn": "RoleArn",
    }

    output_configuration: Optional[MembershipProtectedJobOutputConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MembershipProtectedQueryOutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[ProtectedQueryS3OutputConfiguration] = None


@dataclass
class MembershipProtectedQueryResultConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_configuration": "OutputConfiguration",
        "role_arn": "RoleArn",
    }

    output_configuration: Optional[MembershipProtectedQueryOutputConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MembershipQueryComputePaymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MembershipSyntheticDataGenerationPaymentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_responsible": "IsResponsible",
    }

    is_responsible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ProtectedJobS3OutputConfigurationInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key_prefix": "KeyPrefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProtectedQueryS3OutputConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "result_format": "ResultFormat",
        "key_prefix": "KeyPrefix",
        "single_file_output": "SingleFileOutput",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    result_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    single_file_output: Optional[Union[bool, Ref, GetAtt, Sub]] = None

