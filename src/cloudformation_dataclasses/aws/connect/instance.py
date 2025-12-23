"""PropertyTypes for AWS::Connect::Instance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Attributes(PropertyType):
    INBOUND_CALLS = "InboundCalls"
    ENHANCED_CONTACT_MONITORING = "EnhancedContactMonitoring"
    ENHANCED_CHAT_MONITORING = "EnhancedChatMonitoring"
    USE_CUSTOM_TTS_VOICES = "UseCustomTTSVoices"
    OUTBOUND_CALLS = "OutboundCalls"
    EARLY_MEDIA = "EarlyMedia"
    MULTI_PARTY_CONFERENCE = "MultiPartyConference"
    CONTACTFLOW_LOGS = "ContactflowLogs"
    CONTACT_LENS = "ContactLens"
    AUTO_RESOLVE_BEST_VOICES = "AutoResolveBestVoices"
    MULTI_PARTY_CHAT_CONFERENCE = "MultiPartyChatConference"
    HIGH_VOLUME_OUT_BOUND = "HighVolumeOutBound"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inbound_calls": "InboundCalls",
        "enhanced_contact_monitoring": "EnhancedContactMonitoring",
        "enhanced_chat_monitoring": "EnhancedChatMonitoring",
        "use_custom_tts_voices": "UseCustomTTSVoices",
        "outbound_calls": "OutboundCalls",
        "early_media": "EarlyMedia",
        "multi_party_conference": "MultiPartyConference",
        "contactflow_logs": "ContactflowLogs",
        "contact_lens": "ContactLens",
        "auto_resolve_best_voices": "AutoResolveBestVoices",
        "multi_party_chat_conference": "MultiPartyChatConference",
        "high_volume_out_bound": "HighVolumeOutBound",
    }

    inbound_calls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enhanced_contact_monitoring: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enhanced_chat_monitoring: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_custom_tts_voices: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    outbound_calls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    early_media: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    multi_party_conference: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    contactflow_logs: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    contact_lens: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    auto_resolve_best_voices: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    multi_party_chat_conference: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    high_volume_out_bound: Optional[Union[bool, Ref, GetAtt, Sub]] = None

