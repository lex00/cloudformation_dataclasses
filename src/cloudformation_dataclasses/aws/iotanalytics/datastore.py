"""PropertyTypes for AWS::IoTAnalytics::Datastore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Column(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomerManagedS3(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key_prefix": "KeyPrefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatastorePartition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "partition": "Partition",
        "timestamp_partition": "TimestampPartition",
    }

    partition: Optional[Partition] = None
    timestamp_partition: Optional[TimestampPartition] = None


@dataclass
class DatastorePartitions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "partitions": "Partitions",
    }

    partitions: Optional[list[DatastorePartition]] = None


@dataclass
class DatastoreStorage(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "parquet_configuration": "ParquetConfiguration",
        "json_configuration": "JsonConfiguration",
    }

    parquet_configuration: Optional[ParquetConfiguration] = None
    json_configuration: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class IotSiteWiseMultiLayerStorage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_s3_storage": "CustomerManagedS3Storage",
    }

    customer_managed_s3_storage: Optional[CustomerManagedS3Storage] = None


@dataclass
class ParquetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_definition": "SchemaDefinition",
    }

    schema_definition: Optional[SchemaDefinition] = None


@dataclass
class Partition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_name": "AttributeName",
    }

    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionPeriod(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_days": "NumberOfDays",
        "unlimited": "Unlimited",
    }

    number_of_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlimited: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "columns": "Columns",
    }

    columns: Optional[list[Column]] = None


@dataclass
class TimestampPartition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_name": "AttributeName",
        "timestamp_format": "TimestampFormat",
    }

    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp_format: Optional[Union[str, Ref, GetAtt, Sub]] = None

