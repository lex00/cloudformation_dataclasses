"""PropertyTypes for AWS::Wisdom::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppIntegrationsConfiguration(PropertyType):
    OBJECT_FIELDS = "ObjectFields"
    APP_INTEGRATION_ARN = "AppIntegrationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_fields": "ObjectFields",
        "app_integration_arn": "AppIntegrationArn",
    }

    object_fields: Optional[Union[list[str], Ref]] = None
    app_integration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    MODEL_ARN = "ModelArn"
    PARSING_PROMPT = "ParsingPrompt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
        "parsing_prompt": "ParsingPrompt",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parsing_prompt: Optional[ParsingPrompt] = None


@dataclass
class ChunkingConfiguration(PropertyType):
    CHUNKING_STRATEGY = "ChunkingStrategy"
    FIXED_SIZE_CHUNKING_CONFIGURATION = "FixedSizeChunkingConfiguration"
    SEMANTIC_CHUNKING_CONFIGURATION = "SemanticChunkingConfiguration"
    HIERARCHICAL_CHUNKING_CONFIGURATION = "HierarchicalChunkingConfiguration"

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
class CrawlerLimits(PropertyType):
    RATE_LIMIT = "RateLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rate_limit": "RateLimit",
    }

    rate_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    OVERLAP_PERCENTAGE = "OverlapPercentage"
    MAX_TOKENS = "MaxTokens"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overlap_percentage": "OverlapPercentage",
        "max_tokens": "MaxTokens",
    }

    overlap_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_tokens: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    OVERLAP_TOKENS = "OverlapTokens"
    LEVEL_CONFIGURATIONS = "LevelConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overlap_tokens": "OverlapTokens",
        "level_configurations": "LevelConfigurations",
    }

    overlap_tokens: Optional[Union[float, Ref, GetAtt, Sub]] = None
    level_configurations: Optional[list[HierarchicalChunkingLevelConfiguration]] = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    MAX_TOKENS = "MaxTokens"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_tokens": "MaxTokens",
    }

    max_tokens: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedSourceConfiguration(PropertyType):
    WEB_CRAWLER_CONFIGURATION = "WebCrawlerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "web_crawler_configuration": "WebCrawlerConfiguration",
    }

    web_crawler_configuration: Optional[WebCrawlerConfiguration] = None


@dataclass
class ParsingConfiguration(PropertyType):
    BEDROCK_FOUNDATION_MODEL_CONFIGURATION = "BedrockFoundationModelConfiguration"
    PARSING_STRATEGY = "ParsingStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bedrock_foundation_model_configuration": "BedrockFoundationModelConfiguration",
        "parsing_strategy": "ParsingStrategy",
    }

    bedrock_foundation_model_configuration: Optional[BedrockFoundationModelConfiguration] = None
    parsing_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParsingPrompt(PropertyType):
    PARSING_PROMPT_TEXT = "ParsingPromptText"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_prompt_text": "ParsingPromptText",
    }

    parsing_prompt_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenderingConfiguration(PropertyType):
    TEMPLATE_URI = "TemplateUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template_uri": "TemplateUri",
    }

    template_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SeedUrl(PropertyType):
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "url": "Url",
    }

    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    BUFFER_SIZE = "BufferSize"
    MAX_TOKENS = "MaxTokens"
    BREAKPOINT_PERCENTILE_THRESHOLD = "BreakpointPercentileThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "buffer_size": "BufferSize",
        "max_tokens": "MaxTokens",
        "breakpoint_percentile_threshold": "BreakpointPercentileThreshold",
    }

    buffer_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_tokens: Optional[Union[float, Ref, GetAtt, Sub]] = None
    breakpoint_percentile_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConfiguration(PropertyType):
    APP_INTEGRATIONS = "AppIntegrations"
    MANAGED_SOURCE_CONFIGURATION = "ManagedSourceConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_integrations": "AppIntegrations",
        "managed_source_configuration": "ManagedSourceConfiguration",
    }

    app_integrations: Optional[AppIntegrationsConfiguration] = None
    managed_source_configuration: Optional[ManagedSourceConfiguration] = None


@dataclass
class UrlConfiguration(PropertyType):
    SEED_URLS = "SeedUrls"

    _property_mappings: ClassVar[dict[str, str]] = {
        "seed_urls": "SeedUrls",
    }

    seed_urls: Optional[list[SeedUrl]] = None


@dataclass
class VectorIngestionConfiguration(PropertyType):
    PARSING_CONFIGURATION = "ParsingConfiguration"
    CHUNKING_CONFIGURATION = "ChunkingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parsing_configuration": "ParsingConfiguration",
        "chunking_configuration": "ChunkingConfiguration",
    }

    parsing_configuration: Optional[ParsingConfiguration] = None
    chunking_configuration: Optional[ChunkingConfiguration] = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    URL_CONFIGURATION = "UrlConfiguration"
    INCLUSION_FILTERS = "InclusionFilters"
    CRAWLER_LIMITS = "CrawlerLimits"
    EXCLUSION_FILTERS = "ExclusionFilters"
    SCOPE = "Scope"

    _property_mappings: ClassVar[dict[str, str]] = {
        "url_configuration": "UrlConfiguration",
        "inclusion_filters": "InclusionFilters",
        "crawler_limits": "CrawlerLimits",
        "exclusion_filters": "ExclusionFilters",
        "scope": "Scope",
    }

    url_configuration: Optional[UrlConfiguration] = None
    inclusion_filters: Optional[Union[list[str], Ref]] = None
    crawler_limits: Optional[CrawlerLimits] = None
    exclusion_filters: Optional[Union[list[str], Ref]] = None
    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None

