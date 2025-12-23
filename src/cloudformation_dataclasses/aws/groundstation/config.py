"""PropertyTypes for AWS::GroundStation::Config."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AntennaDownlinkConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "spectrum_config": "SpectrumConfig",
    }

    spectrum_config: Optional[SpectrumConfig] = None


@dataclass
class AntennaDownlinkDemodDecodeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "demodulation_config": "DemodulationConfig",
        "spectrum_config": "SpectrumConfig",
        "decode_config": "DecodeConfig",
    }

    demodulation_config: Optional[DemodulationConfig] = None
    spectrum_config: Optional[SpectrumConfig] = None
    decode_config: Optional[DecodeConfig] = None


@dataclass
class AntennaUplinkConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transmit_disabled": "TransmitDisabled",
        "spectrum_config": "SpectrumConfig",
        "target_eirp": "TargetEirp",
    }

    transmit_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    spectrum_config: Optional[UplinkSpectrumConfig] = None
    target_eirp: Optional[Eirp] = None


@dataclass
class ConfigData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dataflow_endpoint_config": "DataflowEndpointConfig",
        "uplink_echo_config": "UplinkEchoConfig",
        "antenna_downlink_config": "AntennaDownlinkConfig",
        "antenna_downlink_demod_decode_config": "AntennaDownlinkDemodDecodeConfig",
        "tracking_config": "TrackingConfig",
        "antenna_uplink_config": "AntennaUplinkConfig",
        "s3_recording_config": "S3RecordingConfig",
    }

    dataflow_endpoint_config: Optional[DataflowEndpointConfig] = None
    uplink_echo_config: Optional[UplinkEchoConfig] = None
    antenna_downlink_config: Optional[AntennaDownlinkConfig] = None
    antenna_downlink_demod_decode_config: Optional[AntennaDownlinkDemodDecodeConfig] = None
    tracking_config: Optional[TrackingConfig] = None
    antenna_uplink_config: Optional[AntennaUplinkConfig] = None
    s3_recording_config: Optional[S3RecordingConfig] = None


@dataclass
class DataflowEndpointConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dataflow_endpoint_name": "DataflowEndpointName",
        "dataflow_endpoint_region": "DataflowEndpointRegion",
    }

    dataflow_endpoint_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataflow_endpoint_region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecodeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DemodulationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Eirp(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "units": "Units",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Frequency(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "units": "Units",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FrequencyBandwidth(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "units": "Units",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3RecordingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "prefix": "Prefix",
        "role_arn": "RoleArn",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpectrumConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "polarization": "Polarization",
        "bandwidth": "Bandwidth",
        "center_frequency": "CenterFrequency",
    }

    polarization: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bandwidth: Optional[FrequencyBandwidth] = None
    center_frequency: Optional[Frequency] = None


@dataclass
class TrackingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "autotrack": "Autotrack",
    }

    autotrack: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UplinkEchoConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "antenna_uplink_config_arn": "AntennaUplinkConfigArn",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    antenna_uplink_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UplinkSpectrumConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "polarization": "Polarization",
        "center_frequency": "CenterFrequency",
    }

    polarization: Optional[Union[str, Ref, GetAtt, Sub]] = None
    center_frequency: Optional[Frequency] = None

