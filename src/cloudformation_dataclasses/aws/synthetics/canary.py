"""PropertyTypes for AWS::Synthetics::Canary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ArtifactConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_encryption": "S3Encryption",
    }

    s3_encryption: Optional[S3Encryption] = None


@dataclass
class BaseScreenshot(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ignore_coordinates": "IgnoreCoordinates",
        "screenshot_name": "ScreenshotName",
    }

    ignore_coordinates: Optional[Union[list[str], Ref]] = None
    screenshot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BrowserConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "browser_type": "BrowserType",
    }

    browser_type: Optional[Union[str, BrowserType, Ref, GetAtt, Sub]] = None


@dataclass
class Code(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "script": "Script",
        "s3_object_version": "S3ObjectVersion",
        "s3_bucket": "S3Bucket",
        "s3_key": "S3Key",
        "blueprint_types": "BlueprintTypes",
        "handler": "Handler",
        "source_location_arn": "SourceLocationArn",
        "dependencies": "Dependencies",
    }

    script: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    blueprint_types: Optional[Union[list[str], Ref]] = None
    handler: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_location_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dependencies: Optional[list[Dependency]] = None


@dataclass
class Dependency(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "reference": "Reference",
    }

    type_: Optional[Union[str, DependencyType, Ref, GetAtt, Sub]] = None
    reference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetryConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_retries": "MaxRetries",
    }

    max_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RunConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_in_seconds": "TimeoutInSeconds",
        "environment_variables": "EnvironmentVariables",
        "memory_in_mb": "MemoryInMB",
        "ephemeral_storage": "EphemeralStorage",
        "active_tracing": "ActiveTracing",
    }

    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    environment_variables: Optional[dict[str, str]] = None
    memory_in_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ephemeral_storage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    active_tracing: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3Encryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "encryption_mode": "EncryptionMode",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_seconds": "DurationInSeconds",
        "retry_config": "RetryConfig",
        "expression": "Expression",
    }

    duration_in_seconds: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retry_config: Optional[RetryConfig] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VPCConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_allowed_for_dual_stack": "Ipv6AllowedForDualStack",
        "vpc_id": "VpcId",
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    ipv6_allowed_for_dual_stack: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class VisualReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "base_screenshots": "BaseScreenshots",
        "browser_type": "BrowserType",
        "base_canary_run_id": "BaseCanaryRunId",
    }

    base_screenshots: Optional[list[BaseScreenshot]] = None
    browser_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base_canary_run_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

