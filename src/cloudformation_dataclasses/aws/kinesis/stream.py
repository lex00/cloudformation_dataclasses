"""PropertyTypes for AWS::Kinesis::Stream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class StreamEncryption(PropertyType):
    ENCRYPTION_TYPE = "EncryptionType"
    KEY_ID = "KeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "key_id": "KeyId",
    }

    encryption_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamModeDetails(PropertyType):
    STREAM_MODE = "StreamMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_mode": "StreamMode",
    }

    stream_mode: Optional[Union[str, StreamMode, Ref, GetAtt, Sub]] = None


@dataclass
class WarmThroughputObject(PropertyType):
    CURRENT_MI_BPS = "CurrentMiBps"
    TARGET_MI_BPS = "TargetMiBps"

    _property_mappings: ClassVar[dict[str, str]] = {
        "current_mi_bps": "CurrentMiBps",
        "target_mi_bps": "TargetMiBps",
    }

    current_mi_bps: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_mi_bps: Optional[Union[int, Ref, GetAtt, Sub]] = None

