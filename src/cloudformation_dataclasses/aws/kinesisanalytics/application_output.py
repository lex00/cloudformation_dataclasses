"""PropertyTypes for AWS::KinesisAnalytics::ApplicationOutput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationStatus:
    """ApplicationStatus enum values."""

    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    READY = "READY"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"


class InputStartingPosition:
    """InputStartingPosition enum values."""

    NOW = "NOW"
    TRIM_HORIZON = "TRIM_HORIZON"
    LAST_STOPPED_POINT = "LAST_STOPPED_POINT"


class RecordFormatType:
    """RecordFormatType enum values."""

    JSON = "JSON"
    CSV = "CSV"


@dataclass
class DestinationSchema(PropertyType):
    RECORD_FORMAT_TYPE = "RecordFormatType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "record_format_type": "RecordFormatType",
    }

    record_format_type: Optional[Union[str, RecordFormatType, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisFirehoseOutput(PropertyType):
    RESOURCE_ARN = "ResourceARN"
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamsOutput(PropertyType):
    RESOURCE_ARN = "ResourceARN"
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaOutput(PropertyType):
    RESOURCE_ARN = "ResourceARN"
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Output(PropertyType):
    DESTINATION_SCHEMA = "DestinationSchema"
    LAMBDA_OUTPUT = "LambdaOutput"
    KINESIS_FIREHOSE_OUTPUT = "KinesisFirehoseOutput"
    KINESIS_STREAMS_OUTPUT = "KinesisStreamsOutput"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_schema": "DestinationSchema",
        "lambda_output": "LambdaOutput",
        "kinesis_firehose_output": "KinesisFirehoseOutput",
        "kinesis_streams_output": "KinesisStreamsOutput",
        "name": "Name",
    }

    destination_schema: Optional[DestinationSchema] = None
    lambda_output: Optional[LambdaOutput] = None
    kinesis_firehose_output: Optional[KinesisFirehoseOutput] = None
    kinesis_streams_output: Optional[KinesisStreamsOutput] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

