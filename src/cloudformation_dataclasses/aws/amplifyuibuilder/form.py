"""PropertyTypes for AWS::AmplifyUIBuilder::Form."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FieldConfig(PropertyType):
    VALIDATIONS = "Validations"
    INPUT_TYPE = "InputType"
    POSITION = "Position"
    LABEL = "Label"
    EXCLUDED = "Excluded"

    _property_mappings: ClassVar[dict[str, str]] = {
        "validations": "Validations",
        "input_type": "InputType",
        "position": "Position",
        "label": "Label",
        "excluded": "Excluded",
    }

    validations: Optional[list[FieldValidationConfiguration]] = None
    input_type: Optional[FieldInputConfig] = None
    position: Optional[FieldPosition] = None
    label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    excluded: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FieldInputConfig(PropertyType):
    READ_ONLY = "ReadOnly"
    PLACEHOLDER = "Placeholder"
    FILE_UPLOADER_CONFIG = "FileUploaderConfig"
    IS_ARRAY = "IsArray"
    VALUE_MAPPINGS = "ValueMappings"
    DEFAULT_COUNTRY_CODE = "DefaultCountryCode"
    MAX_VALUE = "MaxValue"
    STEP = "Step"
    NAME = "Name"
    DEFAULT_VALUE = "DefaultValue"
    DESCRIPTIVE_TEXT = "DescriptiveText"
    TYPE = "Type"
    REQUIRED = "Required"
    MIN_VALUE = "MinValue"
    VALUE = "Value"
    DEFAULT_CHECKED = "DefaultChecked"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only": "ReadOnly",
        "placeholder": "Placeholder",
        "file_uploader_config": "FileUploaderConfig",
        "is_array": "IsArray",
        "value_mappings": "ValueMappings",
        "default_country_code": "DefaultCountryCode",
        "max_value": "MaxValue",
        "step": "Step",
        "name": "Name",
        "default_value": "DefaultValue",
        "descriptive_text": "DescriptiveText",
        "type_": "Type",
        "required": "Required",
        "min_value": "MinValue",
        "value": "Value",
        "default_checked": "DefaultChecked",
    }

    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    placeholder: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_uploader_config: Optional[FileUploaderFieldConfig] = None
    is_array: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    value_mappings: Optional[ValueMappings] = None
    default_country_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    step: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    descriptive_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    min_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_checked: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FieldPosition(PropertyType):
    BELOW = "Below"
    RIGHT_OF = "RightOf"
    FIXED = "Fixed"

    _property_mappings: ClassVar[dict[str, str]] = {
        "below": "Below",
        "right_of": "RightOf",
        "fixed": "Fixed",
    }

    below: Optional[Union[str, Ref, GetAtt, Sub]] = None
    right_of: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fixed: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FieldValidationConfiguration(PropertyType):
    TYPE = "Type"
    VALIDATION_MESSAGE = "ValidationMessage"
    STR_VALUES = "StrValues"
    NUM_VALUES = "NumValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "validation_message": "ValidationMessage",
        "str_values": "StrValues",
        "num_values": "NumValues",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    validation_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    str_values: Optional[Union[list[str], Ref]] = None
    num_values: Optional[Union[list[float], Ref]] = None


@dataclass
class FileUploaderFieldConfig(PropertyType):
    IS_RESUMABLE = "IsResumable"
    SHOW_THUMBNAILS = "ShowThumbnails"
    ACCEPTED_FILE_TYPES = "AcceptedFileTypes"
    MAX_FILE_COUNT = "MaxFileCount"
    MAX_SIZE = "MaxSize"
    ACCESS_LEVEL = "AccessLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_resumable": "IsResumable",
        "show_thumbnails": "ShowThumbnails",
        "accepted_file_types": "AcceptedFileTypes",
        "max_file_count": "MaxFileCount",
        "max_size": "MaxSize",
        "access_level": "AccessLevel",
    }

    is_resumable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    show_thumbnails: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    accepted_file_types: Optional[Union[list[str], Ref]] = None
    max_file_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    access_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormButton(PropertyType):
    POSITION = "Position"
    CHILDREN = "Children"
    EXCLUDED = "Excluded"

    _property_mappings: ClassVar[dict[str, str]] = {
        "position": "Position",
        "children": "Children",
        "excluded": "Excluded",
    }

    position: Optional[FieldPosition] = None
    children: Optional[Union[str, Ref, GetAtt, Sub]] = None
    excluded: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FormCTA(PropertyType):
    POSITION = "Position"
    CANCEL = "Cancel"
    SUBMIT = "Submit"
    CLEAR = "Clear"

    _property_mappings: ClassVar[dict[str, str]] = {
        "position": "Position",
        "cancel": "Cancel",
        "submit": "Submit",
        "clear": "Clear",
    }

    position: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cancel: Optional[FormButton] = None
    submit: Optional[FormButton] = None
    clear: Optional[FormButton] = None


@dataclass
class FormDataTypeConfig(PropertyType):
    DATA_SOURCE_TYPE = "DataSourceType"
    DATA_TYPE_NAME = "DataTypeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_type": "DataSourceType",
        "data_type_name": "DataTypeName",
    }

    data_source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormInputBindingPropertiesValue(PropertyType):
    TYPE = "Type"
    BINDING_PROPERTIES = "BindingProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "binding_properties": "BindingProperties",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    binding_properties: Optional[FormInputBindingPropertiesValueProperties] = None


@dataclass
class FormInputBindingPropertiesValueProperties(PropertyType):
    MODEL = "Model"

    _property_mappings: ClassVar[dict[str, str]] = {
        "model": "Model",
    }

    model: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormInputValueProperty(PropertyType):
    CONCAT = "Concat"
    BINDING_PROPERTIES = "BindingProperties"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "concat": "Concat",
        "binding_properties": "BindingProperties",
        "value": "Value",
    }

    concat: Optional[list[FormInputValueProperty]] = None
    binding_properties: Optional[FormInputValuePropertyBindingProperties] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormInputValuePropertyBindingProperties(PropertyType):
    FIELD = "Field"
    PROPERTY = "Property"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "property": "Property",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormStyle(PropertyType):
    VERTICAL_GAP = "VerticalGap"
    OUTER_PADDING = "OuterPadding"
    HORIZONTAL_GAP = "HorizontalGap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vertical_gap": "VerticalGap",
        "outer_padding": "OuterPadding",
        "horizontal_gap": "HorizontalGap",
    }

    vertical_gap: Optional[FormStyleConfig] = None
    outer_padding: Optional[FormStyleConfig] = None
    horizontal_gap: Optional[FormStyleConfig] = None


@dataclass
class FormStyleConfig(PropertyType):
    VALUE = "Value"
    TOKEN_REFERENCE = "TokenReference"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "token_reference": "TokenReference",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SectionalElement(PropertyType):
    TYPE = "Type"
    POSITION = "Position"
    TEXT = "Text"
    LEVEL = "Level"
    ORIENTATION = "Orientation"
    EXCLUDED = "Excluded"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "position": "Position",
        "text": "Text",
        "level": "Level",
        "orientation": "Orientation",
        "excluded": "Excluded",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    position: Optional[FieldPosition] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    orientation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    excluded: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ValueMapping(PropertyType):
    DISPLAY_VALUE = "DisplayValue"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "display_value": "DisplayValue",
        "value": "Value",
    }

    display_value: Optional[FormInputValueProperty] = None
    value: Optional[FormInputValueProperty] = None


@dataclass
class ValueMappings(PropertyType):
    BINDING_PROPERTIES = "BindingProperties"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "binding_properties": "BindingProperties",
        "values": "Values",
    }

    binding_properties: Optional[dict[str, Any]] = None
    values: Optional[list[ValueMapping]] = None

