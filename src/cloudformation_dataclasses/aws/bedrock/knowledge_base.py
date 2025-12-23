"""PropertyTypes for AWS::Bedrock::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AudioConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_configuration": "SegmentationConfiguration",
    }

    segmentation_configuration: Optional[AudioSegmentationConfiguration] = None


@dataclass
class AudioSegmentationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fixed_length_duration": "FixedLengthDuration",
    }

    fixed_length_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockEmbeddingModelConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "natural_language": "NaturalLanguage",
        "sql": "Sql",
    }

    natural_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EmbeddingModelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_embedding_model_configuration": "BedrockEmbeddingModelConfiguration",
    }

    bedrock_embedding_model_configuration: Optional[BedrockEmbeddingModelConfiguration] = None


@dataclass
class KendraKnowledgeBaseConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kendra_index_arn": "KendraIndexArn",
    }

    kendra_index_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KnowledgeBaseConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "graph_arn": "GraphArn",
        "field_mapping": "FieldMapping",
    }

    graph_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_mapping: Optional[NeptuneAnalyticsFieldMapping] = None


@dataclass
class NeptuneAnalyticsFieldMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchManagedClusterConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_field": "TextField",
        "metadata_field": "MetadataField",
    }

    text_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationColumn(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "generation_context": "GenerationContext",
        "execution_timeout_seconds": "ExecutionTimeoutSeconds",
    }

    generation_context: Optional[QueryGenerationContext] = None
    execution_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QueryGenerationContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "curated_queries": "CuratedQueries",
        "tables": "Tables",
    }

    curated_queries: Optional[list[CuratedQuery]] = None
    tables: Optional[list[QueryGenerationTable]] = None


@dataclass
class QueryGenerationTable(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_configuration": "AuthConfiguration",
        "cluster_identifier": "ClusterIdentifier",
    }

    auth_configuration: Optional[RedshiftProvisionedAuthConfiguration] = None
    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_names": "TableNames",
    }

    table_names: Optional[Union[list[str], Ref]] = None


@dataclass
class RedshiftQueryEngineConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftQueryEngineStorageConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "username_password_secret_arn": "UsernamePasswordSecretArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username_password_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftServerlessConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_arn": "WorkgroupArn",
        "auth_configuration": "AuthConfiguration",
    }

    workgroup_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_configuration: Optional[RedshiftServerlessAuthConfiguration] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3VectorsConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "redshift_configuration": "RedshiftConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redshift_configuration: Optional[RedshiftConfiguration] = None


@dataclass
class StorageConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "supplemental_data_storage_locations": "SupplementalDataStorageLocations",
    }

    supplemental_data_storage_locations: Optional[list[SupplementalDataStorageLocation]] = None


@dataclass
class SupplementalDataStorageLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supplemental_data_storage_location_type": "SupplementalDataStorageLocationType",
        "s3_location": "S3Location",
    }

    supplemental_data_storage_location_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_location: Optional[S3Location] = None


@dataclass
class VectorKnowledgeBaseConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "segmentation_configuration": "SegmentationConfiguration",
    }

    segmentation_configuration: Optional[VideoSegmentationConfiguration] = None


@dataclass
class VideoSegmentationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "fixed_length_duration": "FixedLengthDuration",
    }

    fixed_length_duration: Optional[Union[int, Ref, GetAtt, Sub]] = None

