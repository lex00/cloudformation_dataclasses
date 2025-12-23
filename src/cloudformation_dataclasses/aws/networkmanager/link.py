"""PropertyTypes for AWS::NetworkManager::Link."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Bandwidth(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "download_speed": "DownloadSpeed",
        "upload_speed": "UploadSpeed",
    }

    download_speed: Optional[Union[int, Ref, GetAtt, Sub]] = None
    upload_speed: Optional[Union[int, Ref, GetAtt, Sub]] = None

