"""PropertyTypes for AWS::Bedrock::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BedrockDataAutomationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_modality": "ParsingModality",
    }

    parsing_modality: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
        "parsing_modality": "ParsingModality",
        "parsing_prompt": "ParsingPrompt",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parsing_modality: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parsing_prompt: Optional[ParsingPrompt] = None


@dataclass
class BedrockFoundationModelContextEnrichmentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enrichment_strategy_configuration": "EnrichmentStrategyConfiguration",
        "model_arn": "ModelArn",
    }

    enrichment_strategy_configuration: Optional[EnrichmentStrategyConfiguration] = None
    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ChunkingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "chunking_strategy": "ChunkingStrategy",
        "fixed_size_chunking_configuration": "FixedSizeChunkingConfiguration",
        "semantic_chunking_configuration": "SemanticChunkingConfiguration",
        "hierarchical_chunking_configuration": "HierarchicalChunkingConfiguration",
    }

    chunking_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fixed_size_chunking_configuration: Optional[FixedSizeChunkingConfiguration] = None
    semantic_chunking_configuration: Optional[SemanticChunkingConfiguration] = None
    hierarchical_chunking_configuration: Optional[HierarchicalChunkingConfiguration] = None


@dataclass
class ConfluenceCrawlerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_configuration": "FilterConfiguration",
    }

    filter_configuration: Optional[CrawlFilterConfiguration] = None


@dataclass
class ConfluenceDataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[ConfluenceSourceConfiguration] = None
    crawler_configuration: Optional[ConfluenceCrawlerConfiguration] = None


@dataclass
class ConfluenceSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "host_url": "HostUrl",
        "host_type": "HostType",
        "auth_type": "AuthType",
        "credentials_secret_arn": "CredentialsSecretArn",
    }

    host_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContextEnrichmentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "bedrock_foundation_model_configuration": "BedrockFoundationModelConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bedrock_foundation_model_configuration: Optional[BedrockFoundationModelContextEnrichmentConfiguration] = None


@dataclass
class CrawlFilterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "pattern_object_filter": "PatternObjectFilter",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_object_filter: Optional[PatternObjectFilterConfiguration] = None


@dataclass
class CustomTransformationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "intermediate_storage": "IntermediateStorage",
        "transformations": "Transformations",
    }

    intermediate_storage: Optional[IntermediateStorage] = None
    transformations: Optional[list[Transformation]] = None


@dataclass
class DataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "s3_configuration": "S3Configuration",
        "salesforce_configuration": "SalesforceConfiguration",
        "confluence_configuration": "ConfluenceConfiguration",
        "share_point_configuration": "SharePointConfiguration",
        "web_configuration": "WebConfiguration",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_configuration: Optional[S3DataSourceConfiguration] = None
    salesforce_configuration: Optional[SalesforceDataSourceConfiguration] = None
    confluence_configuration: Optional[ConfluenceDataSourceConfiguration] = None
    share_point_configuration: Optional[SharePointDataSourceConfiguration] = None
    web_configuration: Optional[WebDataSourceConfiguration] = None


@dataclass
class EnrichmentStrategyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "method": "Method",
    }

    method: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "overlap_percentage": "OverlapPercentage",
        "max_tokens": "MaxTokens",
    }

    overlap_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "overlap_tokens": "OverlapTokens",
        "level_configurations": "LevelConfigurations",
    }

    overlap_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None
    level_configurations: Optional[list[HierarchicalChunkingLevelConfiguration]] = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_tokens": "MaxTokens",
    }

    max_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IntermediateStorage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_location": "S3Location",
    }

    s3_location: Optional[S3Location] = None


@dataclass
class ParsingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_data_automation_configuration": "BedrockDataAutomationConfiguration",
        "bedrock_foundation_model_configuration": "BedrockFoundationModelConfiguration",
        "parsing_strategy": "ParsingStrategy",
    }

    bedrock_data_automation_configuration: Optional[BedrockDataAutomationConfiguration] = None
    bedrock_foundation_model_configuration: Optional[BedrockFoundationModelConfiguration] = None
    parsing_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParsingPrompt(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_prompt_text": "ParsingPromptText",
    }

    parsing_prompt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PatternObjectFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object_type": "ObjectType",
        "inclusion_filters": "InclusionFilters",
        "exclusion_filters": "ExclusionFilters",
    }

    object_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion_filters: Optional[Union[list[str], Ref]] = None
    exclusion_filters: Optional[Union[list[str], Ref]] = None


@dataclass
class PatternObjectFilterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
    }

    filters: Optional[list[PatternObjectFilter]] = None


@dataclass
class S3DataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "bucket_owner_account_id": "BucketOwnerAccountId",
        "inclusion_prefixes": "InclusionPrefixes",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inclusion_prefixes: Optional[Union[list[str], Ref]] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceCrawlerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_configuration": "FilterConfiguration",
    }

    filter_configuration: Optional[CrawlFilterConfiguration] = None


@dataclass
class SalesforceDataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[SalesforceSourceConfiguration] = None
    crawler_configuration: Optional[SalesforceCrawlerConfiguration] = None


@dataclass
class SalesforceSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "host_url": "HostUrl",
        "auth_type": "AuthType",
        "credentials_secret_arn": "CredentialsSecretArn",
    }

    host_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SeedUrl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url": "Url",
    }

    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "buffer_size": "BufferSize",
        "max_tokens": "MaxTokens",
        "breakpoint_percentile_threshold": "BreakpointPercentileThreshold",
    }

    buffer_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_tokens: Optional[Union[int, Ref, GetAtt, Sub]] = None
    breakpoint_percentile_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SharePointCrawlerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_configuration": "FilterConfiguration",
    }

    filter_configuration: Optional[CrawlFilterConfiguration] = None


@dataclass
class SharePointDataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[SharePointSourceConfiguration] = None
    crawler_configuration: Optional[SharePointCrawlerConfiguration] = None


@dataclass
class SharePointSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "site_urls": "SiteUrls",
        "host_type": "HostType",
        "tenant_id": "TenantId",
        "auth_type": "AuthType",
        "credentials_secret_arn": "CredentialsSecretArn",
        "domain": "Domain",
    }

    site_urls: Optional[Union[list[str], Ref]] = None
    host_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tenant_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credentials_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "step_to_apply": "StepToApply",
        "transformation_function": "TransformationFunction",
    }

    step_to_apply: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transformation_function: Optional[TransformationFunction] = None


@dataclass
class TransformationFunction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transformation_lambda_configuration": "TransformationLambdaConfiguration",
    }

    transformation_lambda_configuration: Optional[TransformationLambdaConfiguration] = None


@dataclass
class TransformationLambdaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UrlConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "seed_urls": "SeedUrls",
    }

    seed_urls: Optional[list[SeedUrl]] = None


@dataclass
class VectorIngestionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_configuration": "ParsingConfiguration",
        "context_enrichment_configuration": "ContextEnrichmentConfiguration",
        "custom_transformation_configuration": "CustomTransformationConfiguration",
        "chunking_configuration": "ChunkingConfiguration",
    }

    parsing_configuration: Optional[ParsingConfiguration] = None
    context_enrichment_configuration: Optional[ContextEnrichmentConfiguration] = None
    custom_transformation_configuration: Optional[CustomTransformationConfiguration] = None
    chunking_configuration: Optional[ChunkingConfiguration] = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "inclusion_filters": "InclusionFilters",
        "user_agent_header": "UserAgentHeader",
        "crawler_limits": "CrawlerLimits",
        "exclusion_filters": "ExclusionFilters",
        "scope": "Scope",
        "user_agent": "UserAgent",
    }

    inclusion_filters: Optional[Union[list[str], Ref]] = None
    user_agent_header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    crawler_limits: Optional[WebCrawlerLimits] = None
    exclusion_filters: Optional[Union[list[str], Ref]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_agent: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebCrawlerLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rate_limit": "RateLimit",
        "max_pages": "MaxPages",
    }

    rate_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_pages: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WebDataSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_configuration": "SourceConfiguration",
        "crawler_configuration": "CrawlerConfiguration",
    }

    source_configuration: Optional[WebSourceConfiguration] = None
    crawler_configuration: Optional[WebCrawlerConfiguration] = None


@dataclass
class WebSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url_configuration": "UrlConfiguration",
    }

    url_configuration: Optional[UrlConfiguration] = None

