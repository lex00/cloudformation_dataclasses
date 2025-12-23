"""PropertyTypes for AWS::AppSync::Resolver."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppSyncRuntime(PropertyType):
    RUNTIME_VERSION = "RuntimeVersion"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime_version": "RuntimeVersion",
        "name": "Name",
    }

    runtime_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CachingConfig(PropertyType):
    CACHING_KEYS = "CachingKeys"
    TTL = "Ttl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "caching_keys": "CachingKeys",
        "ttl": "Ttl",
    }

    caching_keys: Optional[Union[list[str], Ref]] = None
    ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaConflictHandlerConfig(PropertyType):
    LAMBDA_CONFLICT_HANDLER_ARN = "LambdaConflictHandlerArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_conflict_handler_arn": "LambdaConflictHandlerArn",
    }

    lambda_conflict_handler_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineConfig(PropertyType):
    FUNCTIONS = "Functions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "functions": "Functions",
    }

    functions: Optional[Union[list[str], Ref]] = None


@dataclass
class SyncConfig(PropertyType):
    CONFLICT_HANDLER = "ConflictHandler"
    CONFLICT_DETECTION = "ConflictDetection"
    LAMBDA_CONFLICT_HANDLER_CONFIG = "LambdaConflictHandlerConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "conflict_handler": "ConflictHandler",
        "conflict_detection": "ConflictDetection",
        "lambda_conflict_handler_config": "LambdaConflictHandlerConfig",
    }

    conflict_handler: Optional[Union[str, Ref, GetAtt, Sub]] = None
    conflict_detection: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_conflict_handler_config: Optional[LambdaConflictHandlerConfig] = None

