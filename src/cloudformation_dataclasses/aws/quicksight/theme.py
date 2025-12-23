"""PropertyTypes for AWS::QuickSight::Theme."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BorderStyle(PropertyType):
    SHOW = "Show"

    _property_mappings: ClassVar[dict[str, str]] = {
        "show": "Show",
    }

    show: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataColorPalette(PropertyType):
    EMPTY_FILL_COLOR = "EmptyFillColor"
    COLORS = "Colors"
    MIN_MAX_GRADIENT = "MinMaxGradient"

    _property_mappings: ClassVar[dict[str, str]] = {
        "empty_fill_color": "EmptyFillColor",
        "colors": "Colors",
        "min_max_gradient": "MinMaxGradient",
    }

    empty_fill_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    colors: Optional[Union[list[str], Ref]] = None
    min_max_gradient: Optional[Union[list[str], Ref]] = None


@dataclass
class Font(PropertyType):
    FONT_FAMILY = "FontFamily"

    _property_mappings: ClassVar[dict[str, str]] = {
        "font_family": "FontFamily",
    }

    font_family: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GutterStyle(PropertyType):
    SHOW = "Show"

    _property_mappings: ClassVar[dict[str, str]] = {
        "show": "Show",
    }

    show: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MarginStyle(PropertyType):
    SHOW = "Show"

    _property_mappings: ClassVar[dict[str, str]] = {
        "show": "Show",
    }

    show: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ResourcePermission(PropertyType):
    ACTIONS = "Actions"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "principal": "Principal",
    }

    actions: Optional[Union[list[str], Ref]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SheetStyle(PropertyType):
    TILE_LAYOUT = "TileLayout"
    TILE = "Tile"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tile_layout": "TileLayout",
        "tile": "Tile",
    }

    tile_layout: Optional[TileLayoutStyle] = None
    tile: Optional[TileStyle] = None


@dataclass
class ThemeConfiguration(PropertyType):
    DATA_COLOR_PALETTE = "DataColorPalette"
    UI_COLOR_PALETTE = "UIColorPalette"
    SHEET = "Sheet"
    TYPOGRAPHY = "Typography"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_color_palette": "DataColorPalette",
        "ui_color_palette": "UIColorPalette",
        "sheet": "Sheet",
        "typography": "Typography",
    }

    data_color_palette: Optional[DataColorPalette] = None
    ui_color_palette: Optional[UIColorPalette] = None
    sheet: Optional[SheetStyle] = None
    typography: Optional[Typography] = None


@dataclass
class ThemeError(PropertyType):
    TYPE = "Type"
    MESSAGE = "Message"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "message": "Message",
    }

    type_: Optional[Union[str, ThemeErrorType, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ThemeVersion(PropertyType):
    STATUS = "Status"
    ERRORS = "Errors"
    DESCRIPTION = "Description"
    CREATED_TIME = "CreatedTime"
    CONFIGURATION = "Configuration"
    BASE_THEME_ID = "BaseThemeId"
    ARN = "Arn"
    VERSION_NUMBER = "VersionNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "errors": "Errors",
        "description": "Description",
        "created_time": "CreatedTime",
        "configuration": "Configuration",
        "base_theme_id": "BaseThemeId",
        "arn": "Arn",
        "version_number": "VersionNumber",
    }

    status: Optional[Union[str, ResourceStatus, Ref, GetAtt, Sub]] = None
    errors: Optional[list[ThemeError]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration: Optional[ThemeConfiguration] = None
    base_theme_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version_number: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TileLayoutStyle(PropertyType):
    GUTTER = "Gutter"
    MARGIN = "Margin"

    _property_mappings: ClassVar[dict[str, str]] = {
        "gutter": "Gutter",
        "margin": "Margin",
    }

    gutter: Optional[GutterStyle] = None
    margin: Optional[MarginStyle] = None


@dataclass
class TileStyle(PropertyType):
    BORDER = "Border"

    _property_mappings: ClassVar[dict[str, str]] = {
        "border": "Border",
    }

    border: Optional[BorderStyle] = None


@dataclass
class Typography(PropertyType):
    FONT_FAMILIES = "FontFamilies"

    _property_mappings: ClassVar[dict[str, str]] = {
        "font_families": "FontFamilies",
    }

    font_families: Optional[list[Font]] = None


@dataclass
class UIColorPalette(PropertyType):
    WARNING = "Warning"
    ACCENT = "Accent"
    ACCENT_FOREGROUND = "AccentForeground"
    SECONDARY_BACKGROUND = "SecondaryBackground"
    DANGER_FOREGROUND = "DangerForeground"
    PRIMARY_BACKGROUND = "PrimaryBackground"
    DIMENSION = "Dimension"
    SECONDARY_FOREGROUND = "SecondaryForeground"
    WARNING_FOREGROUND = "WarningForeground"
    DIMENSION_FOREGROUND = "DimensionForeground"
    PRIMARY_FOREGROUND = "PrimaryForeground"
    SUCCESS = "Success"
    DANGER = "Danger"
    SUCCESS_FOREGROUND = "SuccessForeground"
    MEASURE = "Measure"
    MEASURE_FOREGROUND = "MeasureForeground"

    _property_mappings: ClassVar[dict[str, str]] = {
        "warning": "Warning",
        "accent": "Accent",
        "accent_foreground": "AccentForeground",
        "secondary_background": "SecondaryBackground",
        "danger_foreground": "DangerForeground",
        "primary_background": "PrimaryBackground",
        "dimension": "Dimension",
        "secondary_foreground": "SecondaryForeground",
        "warning_foreground": "WarningForeground",
        "dimension_foreground": "DimensionForeground",
        "primary_foreground": "PrimaryForeground",
        "success": "Success",
        "danger": "Danger",
        "success_foreground": "SuccessForeground",
        "measure": "Measure",
        "measure_foreground": "MeasureForeground",
    }

    warning: Optional[Union[str, Ref, GetAtt, Sub]] = None
    accent: Optional[Union[str, Ref, GetAtt, Sub]] = None
    accent_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_background: Optional[Union[str, Ref, GetAtt, Sub]] = None
    danger_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_background: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    warning_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    success: Optional[Union[str, Ref, GetAtt, Sub]] = None
    danger: Optional[Union[str, Ref, GetAtt, Sub]] = None
    success_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure: Optional[Union[str, Ref, GetAtt, Sub]] = None
    measure_foreground: Optional[Union[str, Ref, GetAtt, Sub]] = None

