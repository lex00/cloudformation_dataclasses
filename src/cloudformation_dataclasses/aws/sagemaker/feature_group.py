"""PropertyTypes for AWS::SageMaker::FeatureGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataCatalogConfig(PropertyType):
    TABLE_NAME = "TableName"
    DATABASE = "Database"
    CATALOG = "Catalog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database": "Database",
        "catalog": "Catalog",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FeatureDefinition(PropertyType):
    FEATURE_TYPE = "FeatureType"
    FEATURE_NAME = "FeatureName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "feature_type": "FeatureType",
        "feature_name": "FeatureName",
    }

    feature_type: Optional[Union[str, FeatureType, Ref, GetAtt, Sub]] = None
    feature_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OfflineStoreConfig(PropertyType):
    DATA_CATALOG_CONFIG = "DataCatalogConfig"
    S3_STORAGE_CONFIG = "S3StorageConfig"
    DISABLE_GLUE_TABLE_CREATION = "DisableGlueTableCreation"
    TABLE_FORMAT = "TableFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_catalog_config": "DataCatalogConfig",
        "s3_storage_config": "S3StorageConfig",
        "disable_glue_table_creation": "DisableGlueTableCreation",
        "table_format": "TableFormat",
    }

    data_catalog_config: Optional[DataCatalogConfig] = None
    s3_storage_config: Optional[S3StorageConfig] = None
    disable_glue_table_creation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    table_format: Optional[Union[str, TableFormat, Ref, GetAtt, Sub]] = None


@dataclass
class OnlineStoreConfig(PropertyType):
    ENABLE_ONLINE_STORE = "EnableOnlineStore"
    STORAGE_TYPE = "StorageType"
    SECURITY_CONFIG = "SecurityConfig"
    TTL_DURATION = "TtlDuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_online_store": "EnableOnlineStore",
        "storage_type": "StorageType",
        "security_config": "SecurityConfig",
        "ttl_duration": "TtlDuration",
    }

    enable_online_store: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    storage_type: Optional[Union[str, StorageType, Ref, GetAtt, Sub]] = None
    security_config: Optional[OnlineStoreSecurityConfig] = None
    ttl_duration: Optional[TtlDuration] = None


@dataclass
class OnlineStoreSecurityConfig(PropertyType):
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3StorageConfig(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    S3_URI = "S3Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "s3_uri": "S3Uri",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ThroughputConfig(PropertyType):
    PROVISIONED_READ_CAPACITY_UNITS = "ProvisionedReadCapacityUnits"
    PROVISIONED_WRITE_CAPACITY_UNITS = "ProvisionedWriteCapacityUnits"
    THROUGHPUT_MODE = "ThroughputMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_read_capacity_units": "ProvisionedReadCapacityUnits",
        "provisioned_write_capacity_units": "ProvisionedWriteCapacityUnits",
        "throughput_mode": "ThroughputMode",
    }

    provisioned_read_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    provisioned_write_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    throughput_mode: Optional[Union[str, ThroughputMode, Ref, GetAtt, Sub]] = None


@dataclass
class TtlDuration(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, TtlDurationUnit, Ref, GetAtt, Sub]] = None

