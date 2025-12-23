"""PropertyTypes for AWS::SageMaker::InferenceComponent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Alarm(PropertyType):
    ALARM_NAME = "AlarmName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_name": "AlarmName",
    }

    alarm_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AutoRollbackConfiguration(PropertyType):
    ALARMS = "Alarms"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarms": "Alarms",
    }

    alarms: Optional[list[Alarm]] = None


@dataclass
class DeployedImage(PropertyType):
    RESOLUTION_TIME = "ResolutionTime"
    SPECIFIED_IMAGE = "SpecifiedImage"
    RESOLVED_IMAGE = "ResolvedImage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resolution_time": "ResolutionTime",
        "specified_image": "SpecifiedImage",
        "resolved_image": "ResolvedImage",
    }

    resolution_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    specified_image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resolved_image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceComponentCapacitySize(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, InferenceComponentCapacitySizeType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceComponentComputeResourceRequirements(PropertyType):
    NUMBER_OF_ACCELERATOR_DEVICES_REQUIRED = "NumberOfAcceleratorDevicesRequired"
    MAX_MEMORY_REQUIRED_IN_MB = "MaxMemoryRequiredInMb"
    MIN_MEMORY_REQUIRED_IN_MB = "MinMemoryRequiredInMb"
    NUMBER_OF_CPU_CORES_REQUIRED = "NumberOfCpuCoresRequired"

    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_accelerator_devices_required": "NumberOfAcceleratorDevicesRequired",
        "max_memory_required_in_mb": "MaxMemoryRequiredInMb",
        "min_memory_required_in_mb": "MinMemoryRequiredInMb",
        "number_of_cpu_cores_required": "NumberOfCpuCoresRequired",
    }

    number_of_accelerator_devices_required: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_memory_required_in_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_memory_required_in_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    number_of_cpu_cores_required: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceComponentContainerSpecification(PropertyType):
    ARTIFACT_URL = "ArtifactUrl"
    ENVIRONMENT = "Environment"
    DEPLOYED_IMAGE = "DeployedImage"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "artifact_url": "ArtifactUrl",
        "environment": "Environment",
        "deployed_image": "DeployedImage",
        "image": "Image",
    }

    artifact_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment: Optional[dict[str, str]] = None
    deployed_image: Optional[DeployedImage] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceComponentDeploymentConfig(PropertyType):
    AUTO_ROLLBACK_CONFIGURATION = "AutoRollbackConfiguration"
    ROLLING_UPDATE_POLICY = "RollingUpdatePolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_rollback_configuration": "AutoRollbackConfiguration",
        "rolling_update_policy": "RollingUpdatePolicy",
    }

    auto_rollback_configuration: Optional[AutoRollbackConfiguration] = None
    rolling_update_policy: Optional[InferenceComponentRollingUpdatePolicy] = None


@dataclass
class InferenceComponentRollingUpdatePolicy(PropertyType):
    MAXIMUM_EXECUTION_TIMEOUT_IN_SECONDS = "MaximumExecutionTimeoutInSeconds"
    MAXIMUM_BATCH_SIZE = "MaximumBatchSize"
    WAIT_INTERVAL_IN_SECONDS = "WaitIntervalInSeconds"
    ROLLBACK_MAXIMUM_BATCH_SIZE = "RollbackMaximumBatchSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_execution_timeout_in_seconds": "MaximumExecutionTimeoutInSeconds",
        "maximum_batch_size": "MaximumBatchSize",
        "wait_interval_in_seconds": "WaitIntervalInSeconds",
        "rollback_maximum_batch_size": "RollbackMaximumBatchSize",
    }

    maximum_execution_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_batch_size: Optional[InferenceComponentCapacitySize] = None
    wait_interval_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rollback_maximum_batch_size: Optional[InferenceComponentCapacitySize] = None


@dataclass
class InferenceComponentRuntimeConfig(PropertyType):
    CURRENT_COPY_COUNT = "CurrentCopyCount"
    DESIRED_COPY_COUNT = "DesiredCopyCount"
    COPY_COUNT = "CopyCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "current_copy_count": "CurrentCopyCount",
        "desired_copy_count": "DesiredCopyCount",
        "copy_count": "CopyCount",
    }

    current_copy_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    desired_copy_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    copy_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceComponentSpecification(PropertyType):
    CONTAINER = "Container"
    MODEL_NAME = "ModelName"
    COMPUTE_RESOURCE_REQUIREMENTS = "ComputeResourceRequirements"
    BASE_INFERENCE_COMPONENT_NAME = "BaseInferenceComponentName"
    STARTUP_PARAMETERS = "StartupParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container": "Container",
        "model_name": "ModelName",
        "compute_resource_requirements": "ComputeResourceRequirements",
        "base_inference_component_name": "BaseInferenceComponentName",
        "startup_parameters": "StartupParameters",
    }

    container: Optional[InferenceComponentContainerSpecification] = None
    model_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    compute_resource_requirements: Optional[InferenceComponentComputeResourceRequirements] = None
    base_inference_component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    startup_parameters: Optional[InferenceComponentStartupParameters] = None


@dataclass
class InferenceComponentStartupParameters(PropertyType):
    MODEL_DATA_DOWNLOAD_TIMEOUT_IN_SECONDS = "ModelDataDownloadTimeoutInSeconds"
    CONTAINER_STARTUP_HEALTH_CHECK_TIMEOUT_IN_SECONDS = "ContainerStartupHealthCheckTimeoutInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model_data_download_timeout_in_seconds": "ModelDataDownloadTimeoutInSeconds",
        "container_startup_health_check_timeout_in_seconds": "ContainerStartupHealthCheckTimeoutInSeconds",
    }

    model_data_download_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    container_startup_health_check_timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None

