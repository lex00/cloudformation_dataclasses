"""PropertyTypes for AWS::FraudDetector::EventType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AsyncJobStatus:
    """AsyncJobStatus enum values."""

    IN_PROGRESS_INITIALIZING = "IN_PROGRESS_INITIALIZING"
    IN_PROGRESS = "IN_PROGRESS"
    CANCEL_IN_PROGRESS = "CANCEL_IN_PROGRESS"
    CANCELED = "CANCELED"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class DataSource:
    """DataSource enum values."""

    EVENT = "EVENT"
    MODEL_SCORE = "MODEL_SCORE"
    EXTERNAL_MODEL_SCORE = "EXTERNAL_MODEL_SCORE"


class DataType:
    """DataType enum values."""

    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    BOOLEAN = "BOOLEAN"
    DATETIME = "DATETIME"


class DetectorVersionStatus:
    """DetectorVersionStatus enum values."""

    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class EventIngestion:
    """EventIngestion enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Language:
    """Language enum values."""

    DETECTORPL = "DETECTORPL"


class ListUpdateMode:
    """ListUpdateMode enum values."""

    REPLACE = "REPLACE"
    APPEND = "APPEND"
    REMOVE = "REMOVE"


class ModelEndpointStatus:
    """ModelEndpointStatus enum values."""

    ASSOCIATED = "ASSOCIATED"
    DISSOCIATED = "DISSOCIATED"


class ModelInputDataFormat:
    """ModelInputDataFormat enum values."""

    TEXT_CSV = "TEXT_CSV"
    APPLICATION_JSON = "APPLICATION_JSON"


class ModelOutputDataFormat:
    """ModelOutputDataFormat enum values."""

    TEXT_CSV = "TEXT_CSV"
    APPLICATION_JSONLINES = "APPLICATION_JSONLINES"


class ModelSource:
    """ModelSource enum values."""

    SAGEMAKER = "SAGEMAKER"


class ModelTypeEnum:
    """ModelTypeEnum enum values."""

    ONLINE_FRAUD_INSIGHTS = "ONLINE_FRAUD_INSIGHTS"
    TRANSACTION_FRAUD_INSIGHTS = "TRANSACTION_FRAUD_INSIGHTS"
    ACCOUNT_TAKEOVER_INSIGHTS = "ACCOUNT_TAKEOVER_INSIGHTS"


class ModelVersionStatus:
    """ModelVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    TRAINING_CANCELLED = "TRAINING_CANCELLED"


class RuleExecutionMode:
    """RuleExecutionMode enum values."""

    ALL_MATCHED = "ALL_MATCHED"
    FIRST_MATCHED = "FIRST_MATCHED"


class TrainingDataSourceEnum:
    """TrainingDataSourceEnum enum values."""

    EXTERNAL_EVENTS = "EXTERNAL_EVENTS"
    INGESTED_EVENTS = "INGESTED_EVENTS"


class UnlabeledEventsTreatment:
    """UnlabeledEventsTreatment enum values."""

    IGNORE = "IGNORE"
    FRAUD = "FRAUD"
    LEGIT = "LEGIT"
    AUTO = "AUTO"


@dataclass
class EntityType(PropertyType):
    DESCRIPTION = "Description"
    CREATED_TIME = "CreatedTime"
    LAST_UPDATED_TIME = "LastUpdatedTime"
    INLINE = "Inline"
    ARN = "Arn"
    TAGS = "Tags"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "created_time": "CreatedTime",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventVariable(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    DESCRIPTION = "Description"
    CREATED_TIME = "CreatedTime"
    VARIABLE_TYPE = "VariableType"
    DATA_TYPE = "DataType"
    LAST_UPDATED_TIME = "LastUpdatedTime"
    INLINE = "Inline"
    ARN = "Arn"
    TAGS = "Tags"
    NAME = "Name"
    DATA_SOURCE = "DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "description": "Description",
        "created_time": "CreatedTime",
        "variable_type": "VariableType",
        "data_type": "DataType",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
        "data_source": "DataSource",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variable_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Label(PropertyType):
    DESCRIPTION = "Description"
    CREATED_TIME = "CreatedTime"
    LAST_UPDATED_TIME = "LastUpdatedTime"
    INLINE = "Inline"
    ARN = "Arn"
    TAGS = "Tags"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "created_time": "CreatedTime",
        "last_updated_time": "LastUpdatedTime",
        "inline": "Inline",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_updated_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inline: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

