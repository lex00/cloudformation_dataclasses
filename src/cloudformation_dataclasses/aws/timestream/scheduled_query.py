"""PropertyTypes for AWS::Timestream::ScheduledQuery."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DimensionMapping(PropertyType):
    DIMENSION_VALUE_TYPE = "DimensionValueType"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_value_type": "DimensionValueType",
        "name": "Name",
    }

    dimension_value_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorReportConfiguration(PropertyType):
    S3_CONFIGURATION = "S3Configuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_configuration": "S3Configuration",
    }

    s3_configuration: Optional[S3Configuration] = None


@dataclass
class MixedMeasureMapping(PropertyType):
    MEASURE_NAME = "MeasureName"
    SOURCE_COLUMN = "SourceColumn"
    TARGET_MEASURE_NAME = "TargetMeasureName"
    MEASURE_VALUE_TYPE = "MeasureValueType"
    MULTI_MEASURE_ATTRIBUTE_MAPPINGS = "MultiMeasureAttributeMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "measure_name": "MeasureName",
        "source_column": "SourceColumn",
        "target_measure_name": "TargetMeasureName",
        "measure_value_type": "MeasureValueType",
        "multi_measure_attribute_mappings": "MultiMeasureAttributeMappings",
    }

    measure_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_measure_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure_value_type: Optional[Union[str, MeasureValueType, Ref, GetAtt, Sub]] = None
    multi_measure_attribute_mappings: Optional[list[MultiMeasureAttributeMapping]] = None


@dataclass
class MultiMeasureAttributeMapping(PropertyType):
    SOURCE_COLUMN = "SourceColumn"
    TARGET_MULTI_MEASURE_ATTRIBUTE_NAME = "TargetMultiMeasureAttributeName"
    MEASURE_VALUE_TYPE = "MeasureValueType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_column": "SourceColumn",
        "target_multi_measure_attribute_name": "TargetMultiMeasureAttributeName",
        "measure_value_type": "MeasureValueType",
    }

    source_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_multi_measure_attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure_value_type: Optional[Union[str, ScalarMeasureValueType, Ref, GetAtt, Sub]] = None


@dataclass
class MultiMeasureMappings(PropertyType):
    TARGET_MULTI_MEASURE_NAME = "TargetMultiMeasureName"
    MULTI_MEASURE_ATTRIBUTE_MAPPINGS = "MultiMeasureAttributeMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_multi_measure_name": "TargetMultiMeasureName",
        "multi_measure_attribute_mappings": "MultiMeasureAttributeMappings",
    }

    target_multi_measure_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multi_measure_attribute_mappings: Optional[list[MultiMeasureAttributeMapping]] = None


@dataclass
class NotificationConfiguration(PropertyType):
    SNS_CONFIGURATION = "SnsConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_configuration": "SnsConfiguration",
    }

    sns_configuration: Optional[SnsConfiguration] = None


@dataclass
class S3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"
    OBJECT_KEY_PREFIX = "ObjectKeyPrefix"
    ENCRYPTION_OPTION = "EncryptionOption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "object_key_prefix": "ObjectKeyPrefix",
        "encryption_option": "EncryptionOption",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_option: Optional[Union[str, S3EncryptionOption, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduleConfiguration(PropertyType):
    SCHEDULE_EXPRESSION = "ScheduleExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnsConfiguration(PropertyType):
    TOPIC_ARN = "TopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetConfiguration(PropertyType):
    TIMESTREAM_CONFIGURATION = "TimestreamConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timestream_configuration": "TimestreamConfiguration",
    }

    timestream_configuration: Optional[TimestreamConfiguration] = None


@dataclass
class TimestreamConfiguration(PropertyType):
    TIME_COLUMN = "TimeColumn"
    TABLE_NAME = "TableName"
    DIMENSION_MAPPINGS = "DimensionMappings"
    MIXED_MEASURE_MAPPINGS = "MixedMeasureMappings"
    MEASURE_NAME_COLUMN = "MeasureNameColumn"
    DATABASE_NAME = "DatabaseName"
    MULTI_MEASURE_MAPPINGS = "MultiMeasureMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "time_column": "TimeColumn",
        "table_name": "TableName",
        "dimension_mappings": "DimensionMappings",
        "mixed_measure_mappings": "MixedMeasureMappings",
        "measure_name_column": "MeasureNameColumn",
        "database_name": "DatabaseName",
        "multi_measure_mappings": "MultiMeasureMappings",
    }

    time_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_mappings: Optional[list[DimensionMapping]] = None
    mixed_measure_mappings: Optional[list[MixedMeasureMapping]] = None
    measure_name_column: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multi_measure_mappings: Optional[MultiMeasureMappings] = None

