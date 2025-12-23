"""PropertyTypes for AWS::Lambda::EventSourceMapping."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmazonManagedKafkaEventSourceConfig(PropertyType):
    CONSUMER_GROUP_ID = "ConsumerGroupId"
    SCHEMA_REGISTRY_CONFIG = "SchemaRegistryConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupId",
        "schema_registry_config": "SchemaRegistryConfig",
    }

    consumer_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_registry_config: Optional[SchemaRegistryConfig] = None


@dataclass
class DestinationConfig(PropertyType):
    ON_FAILURE = "OnFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_failure": "OnFailure",
    }

    on_failure: Optional[OnFailure] = None


@dataclass
class DocumentDBEventSourceConfig(PropertyType):
    FULL_DOCUMENT = "FullDocument"
    COLLECTION_NAME = "CollectionName"
    DATABASE_NAME = "DatabaseName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "full_document": "FullDocument",
        "collection_name": "CollectionName",
        "database_name": "DatabaseName",
    }

    full_document: Optional[Union[str, FullDocument, Ref, GetAtt, Sub]] = None
    collection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoints(PropertyType):
    KAFKA_BOOTSTRAP_SERVERS = "KafkaBootstrapServers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kafka_bootstrap_servers": "KafkaBootstrapServers",
    }

    kafka_bootstrap_servers: Optional[Union[list[str], Ref]] = None


@dataclass
class Filter(PropertyType):
    PATTERN = "Pattern"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pattern": "Pattern",
    }

    pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FilterCriteria(PropertyType):
    FILTERS = "Filters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
    }

    filters: Optional[list[Filter]] = None


@dataclass
class LoggingConfig(PropertyType):
    SYSTEM_LOG_LEVEL = "SystemLogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "system_log_level": "SystemLogLevel",
    }

    system_log_level: Optional[Union[str, SystemLogLevel, Ref, GetAtt, Sub]] = None


@dataclass
class MetricsConfig(PropertyType):
    METRICS = "Metrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metrics": "Metrics",
    }

    metrics: Optional[Union[list[str], Ref]] = None


@dataclass
class OnFailure(PropertyType):
    DESTINATION = "Destination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisionedPollerConfig(PropertyType):
    POLLER_GROUP_NAME = "PollerGroupName"
    MINIMUM_POLLERS = "MinimumPollers"
    MAXIMUM_POLLERS = "MaximumPollers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "poller_group_name": "PollerGroupName",
        "minimum_pollers": "MinimumPollers",
        "maximum_pollers": "MaximumPollers",
    }

    poller_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_pollers: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_pollers: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingConfig(PropertyType):
    MAXIMUM_CONCURRENCY = "MaximumConcurrency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_concurrency": "MaximumConcurrency",
    }

    maximum_concurrency: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaRegistryAccessConfig(PropertyType):
    TYPE = "Type"
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "uri": "URI",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaRegistryConfig(PropertyType):
    SCHEMA_VALIDATION_CONFIGS = "SchemaValidationConfigs"
    SCHEMA_REGISTRY_URI = "SchemaRegistryURI"
    EVENT_RECORD_FORMAT = "EventRecordFormat"
    ACCESS_CONFIGS = "AccessConfigs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_validation_configs": "SchemaValidationConfigs",
        "schema_registry_uri": "SchemaRegistryURI",
        "event_record_format": "EventRecordFormat",
        "access_configs": "AccessConfigs",
    }

    schema_validation_configs: Optional[list[SchemaValidationConfig]] = None
    schema_registry_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_record_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_configs: Optional[list[SchemaRegistryAccessConfig]] = None


@dataclass
class SchemaValidationConfig(PropertyType):
    ATTRIBUTE = "Attribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelfManagedEventSource(PropertyType):
    ENDPOINTS = "Endpoints"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoints": "Endpoints",
    }

    endpoints: Optional[Endpoints] = None


@dataclass
class SelfManagedKafkaEventSourceConfig(PropertyType):
    CONSUMER_GROUP_ID = "ConsumerGroupId"
    SCHEMA_REGISTRY_CONFIG = "SchemaRegistryConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_group_id": "ConsumerGroupId",
        "schema_registry_config": "SchemaRegistryConfig",
    }

    consumer_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_registry_config: Optional[SchemaRegistryConfig] = None


@dataclass
class SourceAccessConfiguration(PropertyType):
    TYPE = "Type"
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "uri": "URI",
    }

    type_: Optional[Union[str, SourceAccessType, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None

