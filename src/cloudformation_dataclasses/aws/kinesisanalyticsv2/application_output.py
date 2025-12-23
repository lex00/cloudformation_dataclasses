"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationOutput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisStreamsOutput(PropertyType):
    RESOURCE_ARN = "ResourceARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaOutput(PropertyType):
    RESOURCE_ARN = "ResourceARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

