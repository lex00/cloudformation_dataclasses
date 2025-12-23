"""PropertyTypes for AWS::Lambda::Function."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityProviderConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_managed_instances_capacity_provider_config": "LambdaManagedInstancesCapacityProviderConfig",
    }

    lambda_managed_instances_capacity_provider_config: Optional[LambdaManagedInstancesCapacityProviderConfig] = None


@dataclass
class Code(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_kms_key_arn": "SourceKMSKeyArn",
        "s3_object_version": "S3ObjectVersion",
        "s3_bucket": "S3Bucket",
        "zip_file": "ZipFile",
        "s3_key": "S3Key",
        "image_uri": "ImageUri",
    }

    source_kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    zip_file: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeadLetterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_arn": "TargetArn",
    }

    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DurableConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_timeout": "ExecutionTimeout",
        "retention_period_in_days": "RetentionPeriodInDays",
    }

    execution_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    retention_period_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Environment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
    }

    variables: Optional[dict[str, str]] = None


@dataclass
class EphemeralStorage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size": "Size",
    }

    size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FileSystemConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
        "local_mount_path": "LocalMountPath",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_mount_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FunctionScalingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_execution_environments": "MinExecutionEnvironments",
        "max_execution_environments": "MaxExecutionEnvironments",
    }

    min_execution_environments: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_execution_environments: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ImageConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "working_directory": "WorkingDirectory",
        "command": "Command",
        "entry_point": "EntryPoint",
    }

    working_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    command: Optional[Union[list[str], Ref]] = None
    entry_point: Optional[Union[list[str], Ref]] = None


@dataclass
class LambdaManagedInstancesCapacityProviderConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_environment_memory_gi_b_per_v_cpu": "ExecutionEnvironmentMemoryGiBPerVCpu",
        "capacity_provider_arn": "CapacityProviderArn",
        "per_execution_environment_max_concurrency": "PerExecutionEnvironmentMaxConcurrency",
    }

    execution_environment_memory_gi_b_per_v_cpu: Optional[Union[float, Ref, GetAtt, Sub]] = None
    capacity_provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    per_execution_environment_max_concurrency: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_format": "LogFormat",
        "application_log_level": "ApplicationLogLevel",
        "log_group": "LogGroup",
        "system_log_level": "SystemLogLevel",
    }

    log_format: Optional[Union[str, LogFormat, Ref, GetAtt, Sub]] = None
    application_log_level: Optional[Union[str, ApplicationLogLevel, Ref, GetAtt, Sub]] = None
    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    system_log_level: Optional[Union[str, SystemLogLevel, Ref, GetAtt, Sub]] = None


@dataclass
class RuntimeManagementConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "update_runtime_on": "UpdateRuntimeOn",
        "runtime_version_arn": "RuntimeVersionArn",
    }

    update_runtime_on: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnapStart(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "apply_on": "ApplyOn",
    }

    apply_on: Optional[Union[str, SnapStartApplyOn, Ref, GetAtt, Sub]] = None


@dataclass
class SnapStartResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "optimization_status": "OptimizationStatus",
        "apply_on": "ApplyOn",
    }

    optimization_status: Optional[Union[str, SnapStartOptimizationStatus, Ref, GetAtt, Sub]] = None
    apply_on: Optional[Union[str, SnapStartApplyOn, Ref, GetAtt, Sub]] = None


@dataclass
class TenancyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tenant_isolation_mode": "TenantIsolationMode",
    }

    tenant_isolation_mode: Optional[Union[str, TenantIsolationMode, Ref, GetAtt, Sub]] = None


@dataclass
class TracingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, TracingMode, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_allowed_for_dual_stack": "Ipv6AllowedForDualStack",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    ipv6_allowed_for_dual_stack: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

