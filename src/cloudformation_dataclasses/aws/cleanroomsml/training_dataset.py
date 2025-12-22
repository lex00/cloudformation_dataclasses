"""PropertyTypes for AWS::CleanRoomsML::TrainingDataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessBudgetType:
    """AccessBudgetType enum values."""

    CALENDAR_DAY = "CALENDAR_DAY"
    CALENDAR_MONTH = "CALENDAR_MONTH"
    CALENDAR_WEEK = "CALENDAR_WEEK"
    LIFETIME = "LIFETIME"


class AudienceExportJobStatus:
    """AudienceExportJobStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"


class AudienceGenerationJobStatus:
    """AudienceGenerationJobStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class AudienceModelStatus:
    """AudienceModelStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class AudienceSizeType:
    """AudienceSizeType enum values."""

    ABSOLUTE = "ABSOLUTE"
    PERCENTAGE = "PERCENTAGE"


class AutoRefreshMode:
    """AutoRefreshMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ColumnType:
    """ColumnType enum values."""

    USER_ID = "USER_ID"
    ITEM_ID = "ITEM_ID"
    TIMESTAMP = "TIMESTAMP"
    CATEGORICAL_FEATURE = "CATEGORICAL_FEATURE"
    NUMERICAL_FEATURE = "NUMERICAL_FEATURE"


class ConfiguredAudienceModelStatus:
    """ConfiguredAudienceModelStatus enum values."""

    ACTIVE = "ACTIVE"


class DatasetType:
    """DatasetType enum values."""

    INTERACTIONS = "INTERACTIONS"


class EntityType:
    """EntityType enum values."""

    ALL_PERSONALLY_IDENTIFIABLE_INFORMATION = "ALL_PERSONALLY_IDENTIFIABLE_INFORMATION"
    NUMBERS = "NUMBERS"
    CUSTOM = "CUSTOM"


class InferenceInstanceType:
    """InferenceInstanceType enum values."""

    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_R6I_16XLARGE = "ml.r6i.16xlarge"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_R6I_8XLARGE = "ml.r6i.8xlarge"
    ML_R6I_LARGE = "ml.r6i.large"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_LARGE = "ml.c6i.large"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_R6I_32XLARGE = "ml.r6i.32xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_R6I_XLARGE = "ml.r6i.xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R6I_12XLARGE = "ml.r6i.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_R6I_24XLARGE = "ml.r6i.24xlarge"
    ML_R6I_2XLARGE = "ml.r6i.2xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_R6I_4XLARGE = "ml.r6i.4xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"


class InstanceType:
    """InstanceType enum values."""

    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_C5N_XLARGE = "ml.c5n.xlarge"
    ML_C5N_2XLARGE = "ml.c5n.2xlarge"
    ML_C5N_4XLARGE = "ml.c5n.4xlarge"
    ML_C5N_9XLARGE = "ml.c5n.9xlarge"
    ML_C5N_18XLARGE = "ml.c5n.18xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_R5D_LARGE = "ml.r5d.large"
    ML_R5D_XLARGE = "ml.r5d.xlarge"
    ML_R5D_2XLARGE = "ml.r5d.2xlarge"
    ML_R5D_4XLARGE = "ml.r5d.4xlarge"
    ML_R5D_8XLARGE = "ml.r5d.8xlarge"
    ML_R5D_12XLARGE = "ml.r5d.12xlarge"
    ML_R5D_16XLARGE = "ml.r5d.16xlarge"
    ML_R5D_24XLARGE = "ml.r5d.24xlarge"
    ML_T3_MEDIUM = "ml.t3.medium"
    ML_T3_LARGE = "ml.t3.large"
    ML_T3_XLARGE = "ml.t3.xlarge"
    ML_T3_2XLARGE = "ml.t3.2xlarge"
    ML_R5_LARGE = "ml.r5.large"
    ML_R5_XLARGE = "ml.r5.xlarge"
    ML_R5_2XLARGE = "ml.r5.2xlarge"
    ML_R5_4XLARGE = "ml.r5.4xlarge"
    ML_R5_8XLARGE = "ml.r5.8xlarge"
    ML_R5_12XLARGE = "ml.r5.12xlarge"
    ML_R5_16XLARGE = "ml.r5.16xlarge"
    ML_R5_24XLARGE = "ml.r5.24xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_P3DN_24XLARGE = "ml.p3dn.24xlarge"


class LogType:
    """LogType enum values."""

    ALL = "ALL"
    ERROR_SUMMARY = "ERROR_SUMMARY"


class LogsStatus:
    """LogsStatus enum values."""

    PUBLISH_SUCCEEDED = "PUBLISH_SUCCEEDED"
    PUBLISH_FAILED = "PUBLISH_FAILED"


class MLInputChannelStatus:
    """MLInputChannelStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    INACTIVE = "INACTIVE"


class MembershipInferenceAttackVersion:
    """MembershipInferenceAttackVersion enum values."""

    DISTANCE_TO_CLOSEST_RECORD_V1 = "DISTANCE_TO_CLOSEST_RECORD_V1"


class MetricsStatus:
    """MetricsStatus enum values."""

    PUBLISH_SUCCEEDED = "PUBLISH_SUCCEEDED"
    PUBLISH_FAILED = "PUBLISH_FAILED"


class NoiseLevelType:
    """NoiseLevelType enum values."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NONE = "NONE"


class PolicyExistenceCondition:
    """PolicyExistenceCondition enum values."""

    POLICY_MUST_EXIST = "POLICY_MUST_EXIST"
    POLICY_MUST_NOT_EXIST = "POLICY_MUST_NOT_EXIST"


class ResultFormat:
    """ResultFormat enum values."""

    CSV = "CSV"
    PARQUET = "PARQUET"


class S3DataDistributionType:
    """S3DataDistributionType enum values."""

    FULLYREPLICATED = "FullyReplicated"
    SHARDEDBYS3KEY = "ShardedByS3Key"


class SharedAudienceMetrics:
    """SharedAudienceMetrics enum values."""

    ALL = "ALL"
    NONE = "NONE"


class SyntheticDataColumnType:
    """SyntheticDataColumnType enum values."""

    CATEGORICAL = "CATEGORICAL"
    NUMERICAL = "NUMERICAL"


class TagOnCreatePolicy:
    """TagOnCreatePolicy enum values."""

    FROM_PARENT_RESOURCE = "FROM_PARENT_RESOURCE"
    NONE = "NONE"


class TrainedModelArtifactMaxSizeUnitType:
    """TrainedModelArtifactMaxSizeUnitType enum values."""

    GB = "GB"


class TrainedModelExportFileType:
    """TrainedModelExportFileType enum values."""

    MODEL = "MODEL"
    OUTPUT = "OUTPUT"


class TrainedModelExportJobStatus:
    """TrainedModelExportJobStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"


class TrainedModelExportsMaxSizeUnitType:
    """TrainedModelExportsMaxSizeUnitType enum values."""

    GB = "GB"


class TrainedModelInferenceJobStatus:
    """TrainedModelInferenceJobStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_IN_PROGRESS = "CANCEL_IN_PROGRESS"
    CANCEL_FAILED = "CANCEL_FAILED"
    INACTIVE = "INACTIVE"


class TrainedModelInferenceMaxOutputSizeUnitType:
    """TrainedModelInferenceMaxOutputSizeUnitType enum values."""

    GB = "GB"


class TrainedModelStatus:
    """TrainedModelStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    INACTIVE = "INACTIVE"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_IN_PROGRESS = "CANCEL_IN_PROGRESS"
    CANCEL_FAILED = "CANCEL_FAILED"


class TrainingDatasetStatus:
    """TrainingDatasetStatus enum values."""

    ACTIVE = "ACTIVE"


class TrainingInputMode:
    """TrainingInputMode enum values."""

    FILE = "File"
    FASTFILE = "FastFile"
    PIPE = "Pipe"


class WorkerComputeType:
    """WorkerComputeType enum values."""

    CR_1X = "CR.1X"
    CR_4X = "CR.4X"


@dataclass
class ColumnSchema(PropertyType):
    COLUMN_NAME = "ColumnName"
    COLUMN_TYPES = "ColumnTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "column_types": "ColumnTypes",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_types: Optional[Union[list[str], Ref]] = None


@dataclass
class DataSource(PropertyType):
    GLUE_DATA_SOURCE = "GlueDataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_data_source": "GlueDataSource",
    }

    glue_data_source: Optional[GlueDataSource] = None


@dataclass
class Dataset(PropertyType):
    TYPE = "Type"
    INPUT_CONFIG = "InputConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_config": "InputConfig",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_config: Optional[DatasetInputConfig] = None


@dataclass
class DatasetInputConfig(PropertyType):
    SCHEMA = "Schema"
    DATA_SOURCE = "DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema": "Schema",
        "data_source": "DataSource",
    }

    schema: Optional[list[ColumnSchema]] = None
    data_source: Optional[DataSource] = None


@dataclass
class GlueDataSource(PropertyType):
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

