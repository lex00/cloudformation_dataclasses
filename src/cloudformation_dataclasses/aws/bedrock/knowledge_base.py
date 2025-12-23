"""PropertyTypes for AWS::Bedrock::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AudioConfiguration(PropertyType):
    SEGMENTATION_CONFIGURATION = "SegmentationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_configuration": "SegmentationConfiguration",
    }

    segmentation_configuration: Optional[AudioSegmentationConfiguration] = None


@dataclass
class AudioSegmentationConfiguration(PropertyType):
    FIXED_LENGTH_DURATION = "FixedLengthDuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fixed_length_duration": "FixedLengthDuration",
    }

    fixed_length_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockEmbeddingModelConfiguration(PropertyType):
    EMBEDDING_DATA_TYPE = "EmbeddingDataType"
    VIDEO = "Video"
    DIMENSIONS = "Dimensions"
    AUDIO = "Audio"

    _property_mappings: ClassVar[dict[str, str]] = {
        "embedding_data_type": "EmbeddingDataType",
        "video": "Video",
        "dimensions": "Dimensions",
        "audio": "Audio",
    }

    embedding_data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    video: Optional[list[VideoConfiguration]] = None
    dimensions: Optional[Union[int, Ref, GetAtt, Sub]] = None
    audio: Optional[list[AudioConfiguration]] = None


@dataclass
class CuratedQuery(PropertyType):
    NATURAL_LANGUAGE = "NaturalLanguage"
    SQL = "Sql"

    _property_mappings: ClassVar[dict[str, str]] = {
        "natural_language": "NaturalLanguage",
        "sql": "Sql",
    }

    natural_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmbeddingModelConfiguration(PropertyType):
    BEDROCK_EMBEDDING_MODEL_CONFIGURATION = "BedrockEmbeddingModelConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_embedding_model_configuration": "BedrockEmbeddingModelConfiguration",
    }

    bedrock_embedding_model_configuration: Optional[BedrockEmbeddingModelConfiguration] = None


@dataclass
class KendraKnowledgeBaseConfiguration(PropertyType):
    KENDRA_INDEX_ARN = "KendraIndexArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kendra_index_arn": "KendraIndexArn",
    }

    kendra_index_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseConfiguration(PropertyType):
    TYPE = "Type"
    SQL_KNOWLEDGE_BASE_CONFIGURATION = "SqlKnowledgeBaseConfiguration"
    KENDRA_KNOWLEDGE_BASE_CONFIGURATION = "KendraKnowledgeBaseConfiguration"
    VECTOR_KNOWLEDGE_BASE_CONFIGURATION = "VectorKnowledgeBaseConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "sql_knowledge_base_configuration": "SqlKnowledgeBaseConfiguration",
        "kendra_knowledge_base_configuration": "KendraKnowledgeBaseConfiguration",
        "vector_knowledge_base_configuration": "VectorKnowledgeBaseConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql_knowledge_base_configuration: Optional[SqlKnowledgeBaseConfiguration] = None
    kendra_knowledge_base_configuration: Optional[KendraKnowledgeBaseConfiguration] = None
    vector_knowledge_base_configuration: Optional[VectorKnowledgeBaseConfiguration] = None


@dataclass
class MongoDbAtlasConfiguration(PropertyType):
    ENDPOINT = "Endpoint"
    COLLECTION_NAME = "CollectionName"
    VECTOR_INDEX_NAME = "VectorIndexName"
    FIELD_MAPPING = "FieldMapping"
    DATABASE_NAME = "DatabaseName"
    ENDPOINT_SERVICE_NAME = "EndpointServiceName"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"
    TEXT_INDEX_NAME = "TextIndexName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "collection_name": "CollectionName",
        "vector_index_name": "VectorIndexName",
        "field_mapping": "FieldMapping",
        "database_name": "DatabaseName",
        "endpoint_service_name": "EndpointServiceName",
        "credentials_secret_arn": "CredentialsSecretArn",
        "text_index_name": "TextIndexName",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    collection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[MongoDbAtlasFieldMapping] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MongoDbAtlasFieldMapping(PropertyType):
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_field": "VectorField",
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NeptuneAnalyticsConfiguration(PropertyType):
    GRAPH_ARN = "GraphArn"
    FIELD_MAPPING = "FieldMapping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "graph_arn": "GraphArn",
        "field_mapping": "FieldMapping",
    }

    graph_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[NeptuneAnalyticsFieldMapping] = None


@dataclass
class NeptuneAnalyticsFieldMapping(PropertyType):
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchManagedClusterConfiguration(PropertyType):
    DOMAIN_ENDPOINT = "DomainEndpoint"
    VECTOR_INDEX_NAME = "VectorIndexName"
    FIELD_MAPPING = "FieldMapping"
    DOMAIN_ARN = "DomainArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_endpoint": "DomainEndpoint",
        "vector_index_name": "VectorIndexName",
        "field_mapping": "FieldMapping",
        "domain_arn": "DomainArn",
    }

    domain_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[OpenSearchManagedClusterFieldMapping] = None
    domain_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchManagedClusterFieldMapping(PropertyType):
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_field": "VectorField",
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchServerlessConfiguration(PropertyType):
    COLLECTION_ARN = "CollectionArn"
    VECTOR_INDEX_NAME = "VectorIndexName"
    FIELD_MAPPING = "FieldMapping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "collection_arn": "CollectionArn",
        "vector_index_name": "VectorIndexName",
        "field_mapping": "FieldMapping",
    }

    collection_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[OpenSearchServerlessFieldMapping] = None


@dataclass
class OpenSearchServerlessFieldMapping(PropertyType):
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_field": "VectorField",
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PineconeConfiguration(PropertyType):
    FIELD_MAPPING = "FieldMapping"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"
    CONNECTION_STRING = "ConnectionString"
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_mapping": "FieldMapping",
        "credentials_secret_arn": "CredentialsSecretArn",
        "connection_string": "ConnectionString",
        "namespace": "Namespace",
    }

    field_mapping: Optional[PineconeFieldMapping] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PineconeFieldMapping(PropertyType):
    TEXT_FIELD = "TextField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationColumn(PropertyType):
    DESCRIPTION = "Description"
    INCLUSION = "Inclusion"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "inclusion": "Inclusion",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationConfiguration(PropertyType):
    GENERATION_CONTEXT = "GenerationContext"
    EXECUTION_TIMEOUT_SECONDS = "ExecutionTimeoutSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "generation_context": "GenerationContext",
        "execution_timeout_seconds": "ExecutionTimeoutSeconds",
    }

    generation_context: Optional[QueryGenerationContext] = None
    execution_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationContext(PropertyType):
    CURATED_QUERIES = "CuratedQueries"
    TABLES = "Tables"

    _property_mappings: ClassVar[dict[str, str]] = {
        "curated_queries": "CuratedQueries",
        "tables": "Tables",
    }

    curated_queries: Optional[list[CuratedQuery]] = None
    tables: Optional[list[QueryGenerationTable]] = None


@dataclass
class QueryGenerationTable(PropertyType):
    DESCRIPTION = "Description"
    INCLUSION = "Inclusion"
    COLUMNS = "Columns"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "inclusion": "Inclusion",
        "columns": "Columns",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[QueryGenerationColumn]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsConfiguration(PropertyType):
    RESOURCE_ARN = "ResourceArn"
    TABLE_NAME = "TableName"
    FIELD_MAPPING = "FieldMapping"
    DATABASE_NAME = "DatabaseName"
    CREDENTIALS_SECRET_ARN = "CredentialsSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "table_name": "TableName",
        "field_mapping": "FieldMapping",
        "database_name": "DatabaseName",
        "credentials_secret_arn": "CredentialsSecretArn",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[RdsFieldMapping] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsFieldMapping(PropertyType):
    PRIMARY_KEY_FIELD = "PrimaryKeyField"
    VECTOR_FIELD = "VectorField"
    TEXT_FIELD = "TextField"
    CUSTOM_METADATA_FIELD = "CustomMetadataField"
    METADATA_FIELD = "MetadataField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_key_field": "PrimaryKeyField",
        "vector_field": "VectorField",
        "text_field": "TextField",
        "custom_metadata_field": "CustomMetadataField",
        "metadata_field": "MetadataField",
    }

    primary_key_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftConfiguration(PropertyType):
    QUERY_ENGINE_CONFIGURATION = "QueryEngineConfiguration"
    STORAGE_CONFIGURATIONS = "StorageConfigurations"
    QUERY_GENERATION_CONFIGURATION = "QueryGenerationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_engine_configuration": "QueryEngineConfiguration",
        "storage_configurations": "StorageConfigurations",
        "query_generation_configuration": "QueryGenerationConfiguration",
    }

    query_engine_configuration: Optional[RedshiftQueryEngineConfiguration] = None
    storage_configurations: Optional[list[RedshiftQueryEngineStorageConfiguration]] = None
    query_generation_configuration: Optional[QueryGenerationConfiguration] = None


@dataclass
class RedshiftProvisionedAuthConfiguration(PropertyType):
    TYPE = "Type"
    DATABASE_USER = "DatabaseUser"
    USERNAME_PASSWORD_SECRET_ARN = "UsernamePasswordSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "database_user": "DatabaseUser",
        "username_password_secret_arn": "UsernamePasswordSecretArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftProvisionedConfiguration(PropertyType):
    AUTH_CONFIGURATION = "AuthConfiguration"
    CLUSTER_IDENTIFIER = "ClusterIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_configuration": "AuthConfiguration",
        "cluster_identifier": "ClusterIdentifier",
    }

    auth_configuration: Optional[RedshiftProvisionedAuthConfiguration] = None
    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(PropertyType):
    TABLE_NAMES = "TableNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_names": "TableNames",
    }

    table_names: Optional[Union[list[str], Ref]] = None


@dataclass
class RedshiftQueryEngineConfiguration(PropertyType):
    TYPE = "Type"
    PROVISIONED_CONFIGURATION = "ProvisionedConfiguration"
    SERVERLESS_CONFIGURATION = "ServerlessConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "provisioned_configuration": "ProvisionedConfiguration",
        "serverless_configuration": "ServerlessConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provisioned_configuration: Optional[RedshiftProvisionedConfiguration] = None
    serverless_configuration: Optional[RedshiftServerlessConfiguration] = None


@dataclass
class RedshiftQueryEngineRedshiftStorageConfiguration(PropertyType):
    DATABASE_NAME = "DatabaseName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftQueryEngineStorageConfiguration(PropertyType):
    TYPE = "Type"
    REDSHIFT_CONFIGURATION = "RedshiftConfiguration"
    AWS_DATA_CATALOG_CONFIGURATION = "AwsDataCatalogConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "redshift_configuration": "RedshiftConfiguration",
        "aws_data_catalog_configuration": "AwsDataCatalogConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redshift_configuration: Optional[RedshiftQueryEngineRedshiftStorageConfiguration] = None
    aws_data_catalog_configuration: Optional[RedshiftQueryEngineAwsDataCatalogStorageConfiguration] = None


@dataclass
class RedshiftServerlessAuthConfiguration(PropertyType):
    TYPE = "Type"
    USERNAME_PASSWORD_SECRET_ARN = "UsernamePasswordSecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "username_password_secret_arn": "UsernamePasswordSecretArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftServerlessConfiguration(PropertyType):
    WORKGROUP_ARN = "WorkgroupArn"
    AUTH_CONFIGURATION = "AuthConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_arn": "WorkgroupArn",
        "auth_configuration": "AuthConfiguration",
    }

    workgroup_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_configuration: Optional[RedshiftServerlessAuthConfiguration] = None


@dataclass
class S3Location(PropertyType):
    URI = "URI"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3VectorsConfiguration(PropertyType):
    INDEX_NAME = "IndexName"
    VECTOR_BUCKET_ARN = "VectorBucketArn"
    INDEX_ARN = "IndexArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_name": "IndexName",
        "vector_bucket_arn": "VectorBucketArn",
        "index_arn": "IndexArn",
    }

    index_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vector_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SqlKnowledgeBaseConfiguration(PropertyType):
    TYPE = "Type"
    REDSHIFT_CONFIGURATION = "RedshiftConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "redshift_configuration": "RedshiftConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redshift_configuration: Optional[RedshiftConfiguration] = None


@dataclass
class StorageConfiguration(PropertyType):
    S3_VECTORS_CONFIGURATION = "S3VectorsConfiguration"
    OPENSEARCH_MANAGED_CLUSTER_CONFIGURATION = "OpensearchManagedClusterConfiguration"
    OPENSEARCH_SERVERLESS_CONFIGURATION = "OpensearchServerlessConfiguration"
    NEPTUNE_ANALYTICS_CONFIGURATION = "NeptuneAnalyticsConfiguration"
    TYPE = "Type"
    MONGO_DB_ATLAS_CONFIGURATION = "MongoDbAtlasConfiguration"
    RDS_CONFIGURATION = "RdsConfiguration"
    PINECONE_CONFIGURATION = "PineconeConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_vectors_configuration": "S3VectorsConfiguration",
        "opensearch_managed_cluster_configuration": "OpensearchManagedClusterConfiguration",
        "opensearch_serverless_configuration": "OpensearchServerlessConfiguration",
        "neptune_analytics_configuration": "NeptuneAnalyticsConfiguration",
        "type_": "Type",
        "mongo_db_atlas_configuration": "MongoDbAtlasConfiguration",
        "rds_configuration": "RdsConfiguration",
        "pinecone_configuration": "PineconeConfiguration",
    }

    s3_vectors_configuration: Optional[S3VectorsConfiguration] = None
    opensearch_managed_cluster_configuration: Optional[OpenSearchManagedClusterConfiguration] = None
    opensearch_serverless_configuration: Optional[OpenSearchServerlessConfiguration] = None
    neptune_analytics_configuration: Optional[NeptuneAnalyticsConfiguration] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mongo_db_atlas_configuration: Optional[MongoDbAtlasConfiguration] = None
    rds_configuration: Optional[RdsConfiguration] = None
    pinecone_configuration: Optional[PineconeConfiguration] = None


@dataclass
class SupplementalDataStorageConfiguration(PropertyType):
    SUPPLEMENTAL_DATA_STORAGE_LOCATIONS = "SupplementalDataStorageLocations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "supplemental_data_storage_locations": "SupplementalDataStorageLocations",
    }

    supplemental_data_storage_locations: Optional[list[SupplementalDataStorageLocation]] = None


@dataclass
class SupplementalDataStorageLocation(PropertyType):
    SUPPLEMENTAL_DATA_STORAGE_LOCATION_TYPE = "SupplementalDataStorageLocationType"
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "supplemental_data_storage_location_type": "SupplementalDataStorageLocationType",
        "s3_location": "S3Location",
    }

    supplemental_data_storage_location_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_location: Optional[S3Location] = None


@dataclass
class VectorKnowledgeBaseConfiguration(PropertyType):
    EMBEDDING_MODEL_CONFIGURATION = "EmbeddingModelConfiguration"
    EMBEDDING_MODEL_ARN = "EmbeddingModelArn"
    SUPPLEMENTAL_DATA_STORAGE_CONFIGURATION = "SupplementalDataStorageConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "embedding_model_configuration": "EmbeddingModelConfiguration",
        "embedding_model_arn": "EmbeddingModelArn",
        "supplemental_data_storage_configuration": "SupplementalDataStorageConfiguration",
    }

    embedding_model_configuration: Optional[EmbeddingModelConfiguration] = None
    embedding_model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    supplemental_data_storage_configuration: Optional[SupplementalDataStorageConfiguration] = None


@dataclass
class VideoConfiguration(PropertyType):
    SEGMENTATION_CONFIGURATION = "SegmentationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_configuration": "SegmentationConfiguration",
    }

    segmentation_configuration: Optional[VideoSegmentationConfiguration] = None


@dataclass
class VideoSegmentationConfiguration(PropertyType):
    FIXED_LENGTH_DURATION = "FixedLengthDuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fixed_length_duration": "FixedLengthDuration",
    }

    fixed_length_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None

