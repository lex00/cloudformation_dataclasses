"""PropertyTypes for AWS::RUM::AppMonitor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AppMonitorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_destinations": "MetricDestinations",
        "included_pages": "IncludedPages",
        "excluded_pages": "ExcludedPages",
        "favorite_pages": "FavoritePages",
        "session_sample_rate": "SessionSampleRate",
        "allow_cookies": "AllowCookies",
        "telemetries": "Telemetries",
        "identity_pool_id": "IdentityPoolId",
        "guest_role_arn": "GuestRoleArn",
        "enable_x_ray": "EnableXRay",
    }

    metric_destinations: Optional[list[MetricDestination]] = None
    included_pages: Optional[Union[list[str], Ref]] = None
    excluded_pages: Optional[Union[list[str], Ref]] = None
    favorite_pages: Optional[Union[list[str], Ref]] = None
    session_sample_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    allow_cookies: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    telemetries: Optional[Union[list[str], Ref]] = None
    identity_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    guest_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_x_ray: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CustomEvents(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, CustomEventsStatus, Ref, GetAtt, Sub]] = None


@dataclass
class DeobfuscationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "java_script_source_maps": "JavaScriptSourceMaps",
    }

    java_script_source_maps: Optional[JavaScriptSourceMaps] = None


@dataclass
class JavaScriptSourceMaps(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "s3_uri": "S3Uri",
    }

    status: Optional[Union[str, DeobfuscationStatus, Ref, GetAtt, Sub]] = None
    s3_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_pattern": "EventPattern",
        "value_key": "ValueKey",
        "unit_label": "UnitLabel",
        "dimension_keys": "DimensionKeys",
        "namespace": "Namespace",
        "name": "Name",
    }

    event_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit_label: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimension_keys: Optional[dict[str, str]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "iam_role_arn": "IamRoleArn",
        "metric_definitions": "MetricDefinitions",
        "destination_arn": "DestinationArn",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_definitions: Optional[list[MetricDefinition]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourcePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_revision_id": "PolicyRevisionId",
        "policy_document": "PolicyDocument",
    }

    policy_revision_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_document: Optional[Union[str, Ref, GetAtt, Sub]] = None

