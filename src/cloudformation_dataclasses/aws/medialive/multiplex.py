"""PropertyTypes for AWS::MediaLive::Multiplex."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MultiplexMediaConnectOutputDestinationSettings(PropertyType):
    ENTITLEMENT_ARN = "EntitlementArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entitlement_arn": "EntitlementArn",
    }

    entitlement_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiplexOutputDestination(PropertyType):
    MULTIPLEX_MEDIA_CONNECT_OUTPUT_DESTINATION_SETTINGS = "MultiplexMediaConnectOutputDestinationSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multiplex_media_connect_output_destination_settings": "MultiplexMediaConnectOutputDestinationSettings",
    }

    multiplex_media_connect_output_destination_settings: Optional[MultiplexMediaConnectOutputDestinationSettings] = None


@dataclass
class MultiplexSettings(PropertyType):
    TRANSPORT_STREAM_BITRATE = "TransportStreamBitrate"
    MAXIMUM_VIDEO_BUFFER_DELAY_MILLISECONDS = "MaximumVideoBufferDelayMilliseconds"
    TRANSPORT_STREAM_ID = "TransportStreamId"
    TRANSPORT_STREAM_RESERVED_BITRATE = "TransportStreamReservedBitrate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transport_stream_bitrate": "TransportStreamBitrate",
        "maximum_video_buffer_delay_milliseconds": "MaximumVideoBufferDelayMilliseconds",
        "transport_stream_id": "TransportStreamId",
        "transport_stream_reserved_bitrate": "TransportStreamReservedBitrate",
    }

    transport_stream_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_video_buffer_delay_milliseconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transport_stream_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transport_stream_reserved_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

