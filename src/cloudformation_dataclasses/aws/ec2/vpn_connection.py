"""PropertyTypes for AWS::EC2::VPNConnection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudwatchLogOptionsSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bgp_log_enabled": "BgpLogEnabled",
        "log_enabled": "LogEnabled",
        "log_output_format": "LogOutputFormat",
        "bgp_log_group_arn": "BgpLogGroupArn",
        "log_group_arn": "LogGroupArn",
        "bgp_log_output_format": "BgpLogOutputFormat",
    }

    bgp_log_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_output_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bgp_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bgp_log_output_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IKEVersionsRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Phase1DHGroupNumbersRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Phase1EncryptionAlgorithmsRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Phase1IntegrityAlgorithmsRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Phase2DHGroupNumbersRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Phase2EncryptionAlgorithmsRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Phase2IntegrityAlgorithmsRequestListValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpnTunnelLogOptionsSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloudwatch_log_options": "CloudwatchLogOptions",
    }

    cloudwatch_log_options: Optional[CloudwatchLogOptionsSpecification] = None


@dataclass
class VpnTunnelOptionsSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "phase2_encryption_algorithms": "Phase2EncryptionAlgorithms",
        "phase2_dh_group_numbers": "Phase2DHGroupNumbers",
        "tunnel_inside_ipv6_cidr": "TunnelInsideIpv6Cidr",
        "startup_action": "StartupAction",
        "tunnel_inside_cidr": "TunnelInsideCidr",
        "ike_versions": "IKEVersions",
        "log_options": "LogOptions",
        "phase1_dh_group_numbers": "Phase1DHGroupNumbers",
        "replay_window_size": "ReplayWindowSize",
        "enable_tunnel_lifecycle_control": "EnableTunnelLifecycleControl",
        "rekey_margin_time_seconds": "RekeyMarginTimeSeconds",
        "dpd_timeout_action": "DPDTimeoutAction",
        "phase2_lifetime_seconds": "Phase2LifetimeSeconds",
        "phase2_integrity_algorithms": "Phase2IntegrityAlgorithms",
        "phase1_integrity_algorithms": "Phase1IntegrityAlgorithms",
        "pre_shared_key": "PreSharedKey",
        "phase1_lifetime_seconds": "Phase1LifetimeSeconds",
        "rekey_fuzz_percentage": "RekeyFuzzPercentage",
        "phase1_encryption_algorithms": "Phase1EncryptionAlgorithms",
        "dpd_timeout_seconds": "DPDTimeoutSeconds",
    }

    phase2_encryption_algorithms: Optional[list[Phase2EncryptionAlgorithmsRequestListValue]] = None
    phase2_dh_group_numbers: Optional[list[Phase2DHGroupNumbersRequestListValue]] = None
    tunnel_inside_ipv6_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    startup_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tunnel_inside_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ike_versions: Optional[list[IKEVersionsRequestListValue]] = None
    log_options: Optional[VpnTunnelLogOptionsSpecification] = None
    phase1_dh_group_numbers: Optional[list[Phase1DHGroupNumbersRequestListValue]] = None
    replay_window_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enable_tunnel_lifecycle_control: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rekey_margin_time_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dpd_timeout_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phase2_lifetime_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    phase2_integrity_algorithms: Optional[list[Phase2IntegrityAlgorithmsRequestListValue]] = None
    phase1_integrity_algorithms: Optional[list[Phase1IntegrityAlgorithmsRequestListValue]] = None
    pre_shared_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phase1_lifetime_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rekey_fuzz_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    phase1_encryption_algorithms: Optional[list[Phase1EncryptionAlgorithmsRequestListValue]] = None
    dpd_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None

