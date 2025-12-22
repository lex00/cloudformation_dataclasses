"""PropertyTypes for AWS::Personalize::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BatchInferenceJobMode:
    """BatchInferenceJobMode enum values."""

    BATCH_INFERENCE = "BATCH_INFERENCE"
    THEME_GENERATION = "THEME_GENERATION"


class Domain:
    """Domain enum values."""

    ECOMMERCE = "ECOMMERCE"
    VIDEO_ON_DEMAND = "VIDEO_ON_DEMAND"


class ImportMode:
    """ImportMode enum values."""

    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"


class IngestionMode:
    """IngestionMode enum values."""

    BULK = "BULK"
    PUT = "PUT"
    ALL = "ALL"


class ObjectiveSensitivity:
    """ObjectiveSensitivity enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    OFF = "OFF"


class RankingInfluenceType:
    """RankingInfluenceType enum values."""

    POPULARITY = "POPULARITY"
    FRESHNESS = "FRESHNESS"


class RecipeProvider:
    """RecipeProvider enum values."""

    SERVICE = "SERVICE"


class TrainingMode:
    """TrainingMode enum values."""

    FULL = "FULL"
    UPDATE = "UPDATE"
    AUTOTRAIN = "AUTOTRAIN"


class TrainingType:
    """TrainingType enum values."""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"


@dataclass
class DataSource(PropertyType):
    DATA_LOCATION = "DataLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_location": "DataLocation",
    }

    data_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetImportJob(PropertyType):
    DATASET_ARN = "DatasetArn"
    JOB_NAME = "JobName"
    DATASET_IMPORT_JOB_ARN = "DatasetImportJobArn"
    ROLE_ARN = "RoleArn"
    DATA_SOURCE = "DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_arn": "DatasetArn",
        "job_name": "JobName",
        "dataset_import_job_arn": "DatasetImportJobArn",
        "role_arn": "RoleArn",
        "data_source": "DataSource",
    }

    dataset_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataset_import_job_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source: Optional[DataSource] = None

