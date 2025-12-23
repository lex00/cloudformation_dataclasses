"""PropertyTypes for AWS::Logs::Transformer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AddKeyEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "overwrite_if_exists": "OverwriteIfExists",
        "value": "Value",
        "key": "Key",
    }

    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AddKeys(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[AddKeyEntry]] = None


@dataclass
class CopyValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[CopyValueEntry]] = None


@dataclass
class CopyValueEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "overwrite_if_exists": "OverwriteIfExists",
        "source": "Source",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Csv(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "quote_character": "QuoteCharacter",
        "delimiter": "Delimiter",
        "columns": "Columns",
        "source": "Source",
    }

    quote_character: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[Union[list[str], Ref]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeConverter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locale": "Locale",
        "target": "Target",
        "match_patterns": "MatchPatterns",
        "source_timezone": "SourceTimezone",
        "target_format": "TargetFormat",
        "target_timezone": "TargetTimezone",
        "source": "Source",
    }

    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_patterns: Optional[Union[list[str], Ref]] = None
    source_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeleteKeys(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class Grok(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
        "match": "Match",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListToMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_key": "ValueKey",
        "target": "Target",
        "flatten": "Flatten",
        "flattened_element": "FlattenedElement",
        "source": "Source",
        "key": "Key",
    }

    value_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    flatten: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    flattened_element: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LowerCaseString(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class MoveKeyEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "overwrite_if_exists": "OverwriteIfExists",
        "source": "Source",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MoveKeys(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[MoveKeyEntry]] = None


@dataclass
class ParseCloudfront(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseJSON(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseKeyValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "key_value_delimiter": "KeyValueDelimiter",
        "overwrite_if_exists": "OverwriteIfExists",
        "field_delimiter": "FieldDelimiter",
        "non_match_value": "NonMatchValue",
        "source": "Source",
        "key_prefix": "KeyPrefix",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_value_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    field_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    non_match_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParsePostgres(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseRoute53(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseToOCSF(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_source": "EventSource",
        "ocsf_version": "OcsfVersion",
        "source": "Source",
    }

    event_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ocsf_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseVPC(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseWAF(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Processor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parse_cloudfront": "ParseCloudfront",
        "lower_case_string": "LowerCaseString",
        "upper_case_string": "UpperCaseString",
        "delete_keys": "DeleteKeys",
        "rename_keys": "RenameKeys",
        "grok": "Grok",
        "split_string": "SplitString",
        "csv": "Csv",
        "add_keys": "AddKeys",
        "parse_to_ocsf": "ParseToOCSF",
        "substitute_string": "SubstituteString",
        "parse_key_value": "ParseKeyValue",
        "parse_waf": "ParseWAF",
        "parse_vpc": "ParseVPC",
        "parse_route53": "ParseRoute53",
        "type_converter": "TypeConverter",
        "parse_json": "ParseJSON",
        "parse_postgres": "ParsePostgres",
        "copy_value": "CopyValue",
        "move_keys": "MoveKeys",
        "date_time_converter": "DateTimeConverter",
        "trim_string": "TrimString",
        "list_to_map": "ListToMap",
    }

    parse_cloudfront: Optional[ParseCloudfront] = None
    lower_case_string: Optional[LowerCaseString] = None
    upper_case_string: Optional[UpperCaseString] = None
    delete_keys: Optional[DeleteKeys] = None
    rename_keys: Optional[RenameKeys] = None
    grok: Optional[Grok] = None
    split_string: Optional[SplitString] = None
    csv: Optional[Csv] = None
    add_keys: Optional[AddKeys] = None
    parse_to_ocsf: Optional[ParseToOCSF] = None
    substitute_string: Optional[SubstituteString] = None
    parse_key_value: Optional[ParseKeyValue] = None
    parse_waf: Optional[ParseWAF] = None
    parse_vpc: Optional[ParseVPC] = None
    parse_route53: Optional[ParseRoute53] = None
    type_converter: Optional[TypeConverter] = None
    parse_json: Optional[ParseJSON] = None
    parse_postgres: Optional[ParsePostgres] = None
    copy_value: Optional[CopyValue] = None
    move_keys: Optional[MoveKeys] = None
    date_time_converter: Optional[DateTimeConverter] = None
    trim_string: Optional[TrimString] = None
    list_to_map: Optional[ListToMap] = None


@dataclass
class RenameKeyEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "overwrite_if_exists": "OverwriteIfExists",
        "rename_to": "RenameTo",
        "key": "Key",
    }

    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rename_to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenameKeys(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[RenameKeyEntry]] = None


@dataclass
class SplitString(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[SplitStringEntry]] = None


@dataclass
class SplitStringEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "source": "Source",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubstituteString(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[SubstituteStringEntry]] = None


@dataclass
class SubstituteStringEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "source": "Source",
    }

    from_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrimString(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class TypeConverter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[TypeConverterEntry]] = None


@dataclass
class TypeConverterEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "key": "Key",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpperCaseString(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None

