"""PropertyTypes for AWS::LookoutEquipment::InferenceScheduler."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataInputConfiguration(PropertyType):
    INFERENCE_INPUT_NAME_CONFIGURATION = "InferenceInputNameConfiguration"
    S3_INPUT_CONFIGURATION = "S3InputConfiguration"
    INPUT_TIME_ZONE_OFFSET = "InputTimeZoneOffset"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inference_input_name_configuration": "InferenceInputNameConfiguration",
        "s3_input_configuration": "S3InputConfiguration",
        "input_time_zone_offset": "InputTimeZoneOffset",
    }

    inference_input_name_configuration: Optional[InputNameConfiguration] = None
    s3_input_configuration: Optional[S3InputConfiguration] = None
    input_time_zone_offset: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataOutputConfiguration(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    S3_OUTPUT_CONFIGURATION = "S3OutputConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "s3_output_configuration": "S3OutputConfiguration",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_configuration: Optional[S3OutputConfiguration] = None


@dataclass
class InputNameConfiguration(PropertyType):
    COMPONENT_TIMESTAMP_DELIMITER = "ComponentTimestampDelimiter"
    TIMESTAMP_FORMAT = "TimestampFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "component_timestamp_delimiter": "ComponentTimestampDelimiter",
        "timestamp_format": "TimestampFormat",
    }

    component_timestamp_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestamp_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3InputConfiguration(PropertyType):
    BUCKET = "Bucket"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3OutputConfiguration(PropertyType):
    BUCKET = "Bucket"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

