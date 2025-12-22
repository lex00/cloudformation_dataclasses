"""PropertyTypes for AWS::IoTAnalytics::Datastore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChannelStatus:
    """ChannelStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class ComputeType:
    """ComputeType enum values."""

    ACU_1 = "ACU_1"
    ACU_2 = "ACU_2"


class DatasetActionType:
    """DatasetActionType enum values."""

    QUERY = "QUERY"
    CONTAINER = "CONTAINER"


class DatasetContentState:
    """DatasetContentState enum values."""

    CREATING = "CREATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class DatasetStatus:
    """DatasetStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class DatastoreStatus:
    """DatastoreStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class FileFormatType:
    """FileFormatType enum values."""

    JSON = "JSON"
    PARQUET = "PARQUET"


class LoggingLevel:
    """LoggingLevel enum values."""

    ERROR = "ERROR"


class ReprocessingStatus:
    """ReprocessingStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


@dataclass
class Column(PropertyType):
    TYPE = "Type"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomerManagedS3(PropertyType):
    BUCKET = "Bucket"
    ROLE_ARN = "RoleArn"
    KEY_PREFIX = "KeyPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "role_arn": "RoleArn",
        "key_prefix": "KeyPrefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomerManagedS3Storage(PropertyType):
    BUCKET = "Bucket"
    KEY_PREFIX = "KeyPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key_prefix": "KeyPrefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatastorePartition(PropertyType):
    PARTITION = "Partition"
    TIMESTAMP_PARTITION = "TimestampPartition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partition": "Partition",
        "timestamp_partition": "TimestampPartition",
    }

    partition: Optional[Partition] = None
    timestamp_partition: Optional[TimestampPartition] = None


@dataclass
class DatastorePartitions(PropertyType):
    PARTITIONS = "Partitions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "partitions": "Partitions",
    }

    partitions: Optional[list[DatastorePartition]] = None


@dataclass
class DatastoreStorage(PropertyType):
    CUSTOMER_MANAGED_S3 = "CustomerManagedS3"
    SERVICE_MANAGED_S3 = "ServiceManagedS3"
    IOT_SITE_WISE_MULTI_LAYER_STORAGE = "IotSiteWiseMultiLayerStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_s3": "CustomerManagedS3",
        "service_managed_s3": "ServiceManagedS3",
        "iot_site_wise_multi_layer_storage": "IotSiteWiseMultiLayerStorage",
    }

    customer_managed_s3: Optional[CustomerManagedS3] = None
    service_managed_s3: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    iot_site_wise_multi_layer_storage: Optional[IotSiteWiseMultiLayerStorage] = None


@dataclass
class FileFormatConfiguration(PropertyType):
    PARQUET_CONFIGURATION = "ParquetConfiguration"
    JSON_CONFIGURATION = "JsonConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parquet_configuration": "ParquetConfiguration",
        "json_configuration": "JsonConfiguration",
    }

    parquet_configuration: Optional[ParquetConfiguration] = None
    json_configuration: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class IotSiteWiseMultiLayerStorage(PropertyType):
    CUSTOMER_MANAGED_S3_STORAGE = "CustomerManagedS3Storage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_s3_storage": "CustomerManagedS3Storage",
    }

    customer_managed_s3_storage: Optional[CustomerManagedS3Storage] = None


@dataclass
class ParquetConfiguration(PropertyType):
    SCHEMA_DEFINITION = "SchemaDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_definition": "SchemaDefinition",
    }

    schema_definition: Optional[SchemaDefinition] = None


@dataclass
class Partition(PropertyType):
    ATTRIBUTE_NAME = "AttributeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_name": "AttributeName",
    }

    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionPeriod(PropertyType):
    NUMBER_OF_DAYS = "NumberOfDays"
    UNLIMITED = "Unlimited"

    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_days": "NumberOfDays",
        "unlimited": "Unlimited",
    }

    number_of_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlimited: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaDefinition(PropertyType):
    COLUMNS = "Columns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "columns": "Columns",
    }

    columns: Optional[list[Column]] = None


@dataclass
class TimestampPartition(PropertyType):
    ATTRIBUTE_NAME = "AttributeName"
    TIMESTAMP_FORMAT = "TimestampFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_name": "AttributeName",
        "timestamp_format": "TimestampFormat",
    }

    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp_format: Optional[Union[str, Ref, GetAtt, Sub]] = None

