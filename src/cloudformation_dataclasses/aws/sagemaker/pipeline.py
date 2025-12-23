"""PropertyTypes for AWS::SageMaker::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ParallelismConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_parallel_execution_steps": "MaxParallelExecutionSteps",
    }

    max_parallel_execution_steps: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PipelineDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pipeline_definition_body": "PipelineDefinitionBody",
        "pipeline_definition_s3_location": "PipelineDefinitionS3Location",
    }

    pipeline_definition_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pipeline_definition_s3_location: Optional[S3Location] = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "e_tag": "ETag",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    e_tag: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

