"""PropertyTypes for AWS::BCMDataExports::Export."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataQuery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_configurations": "TableConfigurations",
        "query_statement": "QueryStatement",
    }

    table_configurations: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    query_statement: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DestinationConfigurations(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_destination": "S3Destination",
    }

    s3_destination: Optional[S3Destination] = None


@dataclass
class Export(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "refresh_cadence": "RefreshCadence",
        "export_arn": "ExportArn",
        "data_query": "DataQuery",
        "destination_configurations": "DestinationConfigurations",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_cadence: Optional[RefreshCadence] = None
    export_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_query: Optional[DataQuery] = None
    destination_configurations: Optional[DestinationConfigurations] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RefreshCadence(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "frequency": "Frequency",
    }

    frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Destination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "s3_output_configurations": "S3OutputConfigurations",
        "s3_region": "S3Region",
        "s3_prefix": "S3Prefix",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_configurations: Optional[S3OutputConfigurations] = None
    s3_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3OutputConfigurations(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compression": "Compression",
        "overwrite": "Overwrite",
        "format": "Format",
        "output_type": "OutputType",
    }

    compression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

