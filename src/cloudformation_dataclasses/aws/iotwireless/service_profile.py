"""PropertyTypes for AWS::IoTWireless::ServiceProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoRaWANServiceProfile(PropertyType):
    DL_BUCKET_SIZE = "DlBucketSize"
    MIN_GW_DIVERSITY = "MinGwDiversity"
    DR_MAX = "DrMax"
    REPORT_DEV_STATUS_MARGIN = "ReportDevStatusMargin"
    PR_ALLOWED = "PrAllowed"
    DL_RATE = "DlRate"
    UL_RATE_POLICY = "UlRatePolicy"
    REPORT_DEV_STATUS_BATTERY = "ReportDevStatusBattery"
    CHANNEL_MASK = "ChannelMask"
    UL_RATE = "UlRate"
    ADD_GW_METADATA = "AddGwMetadata"
    DL_RATE_POLICY = "DlRatePolicy"
    HR_ALLOWED = "HrAllowed"
    DR_MIN = "DrMin"
    TARGET_PER = "TargetPer"
    NWK_GEO_LOC = "NwkGeoLoc"
    DEV_STATUS_REQ_FREQ = "DevStatusReqFreq"
    UL_BUCKET_SIZE = "UlBucketSize"
    RA_ALLOWED = "RaAllowed"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dl_bucket_size": "DlBucketSize",
        "min_gw_diversity": "MinGwDiversity",
        "dr_max": "DrMax",
        "report_dev_status_margin": "ReportDevStatusMargin",
        "pr_allowed": "PrAllowed",
        "dl_rate": "DlRate",
        "ul_rate_policy": "UlRatePolicy",
        "report_dev_status_battery": "ReportDevStatusBattery",
        "channel_mask": "ChannelMask",
        "ul_rate": "UlRate",
        "add_gw_metadata": "AddGwMetadata",
        "dl_rate_policy": "DlRatePolicy",
        "hr_allowed": "HrAllowed",
        "dr_min": "DrMin",
        "target_per": "TargetPer",
        "nwk_geo_loc": "NwkGeoLoc",
        "dev_status_req_freq": "DevStatusReqFreq",
        "ul_bucket_size": "UlBucketSize",
        "ra_allowed": "RaAllowed",
    }

    dl_bucket_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_gw_diversity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dr_max: Optional[Union[int, Ref, GetAtt, Sub]] = None
    report_dev_status_margin: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    pr_allowed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dl_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ul_rate_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    report_dev_status_battery: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    channel_mask: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ul_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    add_gw_metadata: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dl_rate_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hr_allowed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dr_min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_per: Optional[Union[int, Ref, GetAtt, Sub]] = None
    nwk_geo_loc: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dev_status_req_freq: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ul_bucket_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ra_allowed: Optional[Union[bool, Ref, GetAtt, Sub]] = None

