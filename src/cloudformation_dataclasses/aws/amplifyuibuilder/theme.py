"""PropertyTypes for AWS::AmplifyUIBuilder::Theme."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CodegenGenericDataFieldDataType:
    """CodegenGenericDataFieldDataType enum values."""

    ID = "ID"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    AWSDATE = "AWSDate"
    AWSTIME = "AWSTime"
    AWSDATETIME = "AWSDateTime"
    AWSTIMESTAMP = "AWSTimestamp"
    AWSEMAIL = "AWSEmail"
    AWSURL = "AWSURL"
    AWSIPADDRESS = "AWSIPAddress"
    BOOLEAN = "Boolean"
    AWSJSON = "AWSJSON"
    AWSPHONE = "AWSPhone"
    ENUM = "Enum"
    MODEL = "Model"
    NONMODEL = "NonModel"


class CodegenJobGenericDataSourceType:
    """CodegenJobGenericDataSourceType enum values."""

    DATASTORE = "DataStore"


class CodegenJobStatus:
    """CodegenJobStatus enum values."""

    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    SUCCEEDED = "succeeded"


class FixedPosition:
    """FixedPosition enum values."""

    FIRST = "first"


class FormActionType:
    """FormActionType enum values."""

    CREATE = "create"
    UPDATE = "update"


class FormButtonsPosition:
    """FormButtonsPosition enum values."""

    TOP = "top"
    BOTTOM = "bottom"
    TOP_AND_BOTTOM = "top_and_bottom"


class FormDataSourceType:
    """FormDataSourceType enum values."""

    DATASTORE = "DataStore"
    CUSTOM = "Custom"


class GenericDataRelationshipType:
    """GenericDataRelationshipType enum values."""

    HAS_MANY = "HAS_MANY"
    HAS_ONE = "HAS_ONE"
    BELONGS_TO = "BELONGS_TO"


class JSModule:
    """JSModule enum values."""

    ES2020 = "es2020"
    ESNEXT = "esnext"


class JSScript:
    """JSScript enum values."""

    JSX = "jsx"
    TSX = "tsx"
    JS = "js"


class JSTarget:
    """JSTarget enum values."""

    ES2015 = "es2015"
    ES2020 = "es2020"


class LabelDecorator:
    """LabelDecorator enum values."""

    REQUIRED = "required"
    OPTIONAL = "optional"
    NONE = "none"


class SortDirection:
    """SortDirection enum values."""

    ASC = "ASC"
    DESC = "DESC"


class StorageAccessLevel:
    """StorageAccessLevel enum values."""

    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"


class TokenProviders:
    """TokenProviders enum values."""

    FIGMA = "figma"


@dataclass
class ThemeValue(PropertyType):
    VALUE = "Value"
    CHILDREN = "Children"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "children": "Children",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    children: Optional[list[ThemeValues]] = None


@dataclass
class ThemeValues(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[ThemeValue] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

