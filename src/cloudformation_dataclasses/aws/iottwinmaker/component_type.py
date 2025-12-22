"""PropertyTypes for AWS::IoTTwinMaker::ComponentType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ColumnType:
    """ColumnType enum values."""

    NODE = "NODE"
    EDGE = "EDGE"
    VALUE = "VALUE"


class ComponentUpdateType:
    """ComponentUpdateType enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class DestinationType:
    """DestinationType enum values."""

    S3 = "s3"
    IOTSITEWISE = "iotsitewise"
    IOTTWINMAKER = "iottwinmaker"


class ErrorCode:
    """ErrorCode enum values."""

    VALIDATION_ERROR = "VALIDATION_ERROR"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    SYNC_INITIALIZING_ERROR = "SYNC_INITIALIZING_ERROR"
    SYNC_CREATING_ERROR = "SYNC_CREATING_ERROR"
    SYNC_PROCESSING_ERROR = "SYNC_PROCESSING_ERROR"
    SYNC_DELETING_ERROR = "SYNC_DELETING_ERROR"
    PROCESSING_ERROR = "PROCESSING_ERROR"
    COMPOSITE_COMPONENT_FAILURE = "COMPOSITE_COMPONENT_FAILURE"


class GroupType:
    """GroupType enum values."""

    TABULAR = "TABULAR"


class InterpolationType:
    """InterpolationType enum values."""

    LINEAR = "LINEAR"


class MetadataTransferJobState:
    """MetadataTransferJobState enum values."""

    VALIDATING = "VALIDATING"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    CANCELLING = "CANCELLING"
    ERROR = "ERROR"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Order:
    """Order enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class OrderByTime:
    """OrderByTime enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ParentEntityUpdateType:
    """ParentEntityUpdateType enum values."""

    UPDATE = "UPDATE"
    DELETE = "DELETE"


class PricingMode:
    """PricingMode enum values."""

    BASIC = "BASIC"
    STANDARD = "STANDARD"
    TIERED_BUNDLE = "TIERED_BUNDLE"


class PricingTier:
    """PricingTier enum values."""

    TIER_1 = "TIER_1"
    TIER_2 = "TIER_2"
    TIER_3 = "TIER_3"
    TIER_4 = "TIER_4"


class PropertyGroupUpdateType:
    """PropertyGroupUpdateType enum values."""

    UPDATE = "UPDATE"
    DELETE = "DELETE"
    CREATE = "CREATE"


class PropertyUpdateType:
    """PropertyUpdateType enum values."""

    UPDATE = "UPDATE"
    DELETE = "DELETE"
    CREATE = "CREATE"
    RESET_VALUE = "RESET_VALUE"


class SceneErrorCode:
    """SceneErrorCode enum values."""

    MATTERPORT_ERROR = "MATTERPORT_ERROR"


class Scope:
    """Scope enum values."""

    ENTITY = "ENTITY"
    WORKSPACE = "WORKSPACE"


class SourceType:
    """SourceType enum values."""

    S3 = "s3"
    IOTSITEWISE = "iotsitewise"
    IOTTWINMAKER = "iottwinmaker"


class State:
    """State enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"


class SyncJobState:
    """SyncJobState enum values."""

    CREATING = "CREATING"
    INITIALIZING = "INITIALIZING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    ERROR = "ERROR"


class SyncResourceState:
    """SyncResourceState enum values."""

    INITIALIZING = "INITIALIZING"
    PROCESSING = "PROCESSING"
    DELETED = "DELETED"
    IN_SYNC = "IN_SYNC"
    ERROR = "ERROR"


class SyncResourceType:
    """SyncResourceType enum values."""

    ENTITY = "ENTITY"
    COMPONENT_TYPE = "COMPONENT_TYPE"


class Type:
    """Type enum values."""

    RELATIONSHIP = "RELATIONSHIP"
    STRING = "STRING"
    LONG = "LONG"
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    LIST = "LIST"
    MAP = "MAP"


class UpdateReason:
    """UpdateReason enum values."""

    DEFAULT = "DEFAULT"
    PRICING_TIER_UPDATE = "PRICING_TIER_UPDATE"
    ENTITY_COUNT_UPDATE = "ENTITY_COUNT_UPDATE"
    PRICING_MODE_UPDATE = "PRICING_MODE_UPDATE"
    OVERWRITTEN = "OVERWRITTEN"


@dataclass
class CompositeComponentType(PropertyType):
    COMPONENT_TYPE_ID = "ComponentTypeId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "component_type_id": "ComponentTypeId",
    }

    component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataConnector(PropertyType):
    IS_NATIVE = "IsNative"
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_native": "IsNative",
        "lambda_": "Lambda",
    }

    is_native: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    lambda_: Optional[LambdaFunction] = None


@dataclass
class DataType(PropertyType):
    TYPE = "Type"
    ALLOWED_VALUES = "AllowedValues"
    UNIT_OF_MEASURE = "UnitOfMeasure"
    RELATIONSHIP = "Relationship"
    NESTED_TYPE = "NestedType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "allowed_values": "AllowedValues",
        "unit_of_measure": "UnitOfMeasure",
        "relationship": "Relationship",
        "nested_type": "NestedType",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[list[DataValue]] = None
    unit_of_measure: Optional[Union[str, Ref, GetAtt, Sub]] = None
    relationship: Optional[Relationship] = None
    nested_type: Optional[DataType] = None


@dataclass
class DataValue(PropertyType):
    DOUBLE_VALUE = "DoubleValue"
    EXPRESSION = "Expression"
    BOOLEAN_VALUE = "BooleanValue"
    INTEGER_VALUE = "IntegerValue"
    LIST_VALUE = "ListValue"
    LONG_VALUE = "LongValue"
    MAP_VALUE = "MapValue"
    RELATIONSHIP_VALUE = "RelationshipValue"
    STRING_VALUE = "StringValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "double_value": "DoubleValue",
        "expression": "Expression",
        "boolean_value": "BooleanValue",
        "integer_value": "IntegerValue",
        "list_value": "ListValue",
        "long_value": "LongValue",
        "map_value": "MapValue",
        "relationship_value": "RelationshipValue",
        "string_value": "StringValue",
    }

    double_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    boolean_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    integer_value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    list_value: Optional[list[DataValue]] = None
    long_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    map_value: Optional[dict[str, Any]] = None
    relationship_value: Optional[RelationshipValue] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Error(PropertyType):
    MESSAGE = "Message"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Function(PropertyType):
    SCOPE = "Scope"
    REQUIRED_PROPERTIES = "RequiredProperties"
    IMPLEMENTED_BY = "ImplementedBy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "required_properties": "RequiredProperties",
        "implemented_by": "ImplementedBy",
    }

    scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required_properties: Optional[Union[list[str], Ref]] = None
    implemented_by: Optional[DataConnector] = None


@dataclass
class LambdaFunction(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PropertyDefinition(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    IS_EXTERNAL_ID = "IsExternalId"
    IS_STORED_EXTERNALLY = "IsStoredExternally"
    IS_TIME_SERIES = "IsTimeSeries"
    IS_REQUIRED_IN_ENTITY = "IsRequiredInEntity"
    DATA_TYPE = "DataType"
    CONFIGURATIONS = "Configurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "is_external_id": "IsExternalId",
        "is_stored_externally": "IsStoredExternally",
        "is_time_series": "IsTimeSeries",
        "is_required_in_entity": "IsRequiredInEntity",
        "data_type": "DataType",
        "configurations": "Configurations",
    }

    default_value: Optional[DataValue] = None
    is_external_id: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_stored_externally: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_time_series: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_required_in_entity: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_type: Optional[DataType] = None
    configurations: Optional[dict[str, str]] = None


@dataclass
class PropertyGroup(PropertyType):
    GROUP_TYPE = "GroupType"
    PROPERTY_NAMES = "PropertyNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_type": "GroupType",
        "property_names": "PropertyNames",
    }

    group_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property_names: Optional[Union[list[str], Ref]] = None


@dataclass
class Relationship(PropertyType):
    RELATIONSHIP_TYPE = "RelationshipType"
    TARGET_COMPONENT_TYPE_ID = "TargetComponentTypeId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "relationship_type": "RelationshipType",
        "target_component_type_id": "TargetComponentTypeId",
    }

    relationship_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_component_type_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RelationshipValue(PropertyType):
    TARGET_COMPONENT_NAME = "TargetComponentName"
    TARGET_ENTITY_ID = "TargetEntityId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_component_name": "TargetComponentName",
        "target_entity_id": "TargetEntityId",
    }

    target_component_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Status(PropertyType):
    STATE = "State"
    ERROR = "Error"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "error": "Error",
    }

    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error: Optional[Error] = None

