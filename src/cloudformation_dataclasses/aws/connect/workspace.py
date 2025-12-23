"""PropertyTypes for AWS::Connect::Workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FontFamily(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default": "Default",
    }

    default: Optional[Union[str, WorkspaceFontFamily, Ref, GetAtt, Sub]] = None


@dataclass
class MediaItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "source": "Source",
    }

    type_: Optional[Union[str, MediaType, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PaletteCanvas(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_background": "ContainerBackground",
        "active_background": "ActiveBackground",
        "page_background": "PageBackground",
    }

    container_background: Optional[Union[str, Ref, GetAtt, Sub]] = None
    active_background: Optional[Union[str, Ref, GetAtt, Sub]] = None
    page_background: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PaletteHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "background": "Background",
        "text": "Text",
        "text_hover": "TextHover",
        "invert_actions_colors": "InvertActionsColors",
    }

    background: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_hover: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invert_actions_colors: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PaletteNavigation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text_background_hover": "TextBackgroundHover",
        "background": "Background",
        "text_background_active": "TextBackgroundActive",
        "text": "Text",
        "text_hover": "TextHover",
        "text_active": "TextActive",
        "invert_actions_colors": "InvertActionsColors",
    }

    text_background_hover: Optional[Union[str, Ref, GetAtt, Sub]] = None
    background: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_background_active: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_hover: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_active: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invert_actions_colors: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PalettePrimary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "active": "Active",
        "default": "Default",
        "contrast_text": "ContrastText",
    }

    active: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default: Optional[Union[str, Ref, GetAtt, Sub]] = None
    contrast_text: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkspacePage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "page": "Page",
        "slug": "Slug",
        "input_data": "InputData",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    page: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slug: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_data: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkspaceTheme(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "light": "Light",
        "dark": "Dark",
    }

    light: Optional[WorkspaceThemeConfig] = None
    dark: Optional[WorkspaceThemeConfig] = None


@dataclass
class WorkspaceThemeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "palette": "Palette",
        "typography": "Typography",
    }

    palette: Optional[WorkspaceThemePalette] = None
    typography: Optional[WorkspaceThemeTypography] = None


@dataclass
class WorkspaceThemePalette(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "navigation": "Navigation",
        "header": "Header",
        "canvas": "Canvas",
        "primary": "Primary",
    }

    navigation: Optional[PaletteNavigation] = None
    header: Optional[PaletteHeader] = None
    canvas: Optional[PaletteCanvas] = None
    primary: Optional[PalettePrimary] = None


@dataclass
class WorkspaceThemeTypography(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "font_family": "FontFamily",
    }

    font_family: Optional[FontFamily] = None

