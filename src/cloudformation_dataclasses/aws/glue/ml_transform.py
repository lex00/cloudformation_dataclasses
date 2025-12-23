"""PropertyTypes for AWS::Glue::MLTransform."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FindMatchesParameters(PropertyType):
    PRECISION_RECALL_TRADEOFF = "PrecisionRecallTradeoff"
    ENFORCE_PROVIDED_LABELS = "EnforceProvidedLabels"
    PRIMARY_KEY_COLUMN_NAME = "PrimaryKeyColumnName"
    ACCURACY_COST_TRADEOFF = "AccuracyCostTradeoff"

    _property_mappings: ClassVar[dict[str, str]] = {
        "precision_recall_tradeoff": "PrecisionRecallTradeoff",
        "enforce_provided_labels": "EnforceProvidedLabels",
        "primary_key_column_name": "PrimaryKeyColumnName",
        "accuracy_cost_tradeoff": "AccuracyCostTradeoff",
    }

    precision_recall_tradeoff: Optional[Union[float, Ref, GetAtt, Sub]] = None
    enforce_provided_labels: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    primary_key_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    accuracy_cost_tradeoff: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class GlueTables(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputRecordTables(PropertyType):
    GLUE_TABLES = "GlueTables"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_tables": "GlueTables",
    }

    glue_tables: Optional[list[GlueTables]] = None


@dataclass
class MLUserDataEncryption(PropertyType):
    ML_USER_DATA_ENCRYPTION_MODE = "MLUserDataEncryptionMode"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_user_data_encryption_mode": "MLUserDataEncryptionMode",
        "kms_key_id": "KmsKeyId",
    }

    ml_user_data_encryption_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TransformEncryption(PropertyType):
    ML_USER_DATA_ENCRYPTION = "MLUserDataEncryption"
    TASK_RUN_SECURITY_CONFIGURATION_NAME = "TaskRunSecurityConfigurationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_user_data_encryption": "MLUserDataEncryption",
        "task_run_security_configuration_name": "TaskRunSecurityConfigurationName",
    }

    ml_user_data_encryption: Optional[MLUserDataEncryption] = None
    task_run_security_configuration_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TransformParameters(PropertyType):
    TRANSFORM_TYPE = "TransformType"
    FIND_MATCHES_PARAMETERS = "FindMatchesParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transform_type": "TransformType",
        "find_matches_parameters": "FindMatchesParameters",
    }

    transform_type: Optional[Union[str, TransformType, Ref, GetAtt, Sub]] = None
    find_matches_parameters: Optional[FindMatchesParameters] = None

