"""PropertyTypes for AWS::IoT::EncryptionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigurationDetails(PropertyType):
    CONFIGURATION_STATUS = "ConfigurationStatus"
    ERROR_CODE = "ErrorCode"
    ERROR_MESSAGE = "ErrorMessage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_status": "ConfigurationStatus",
        "error_code": "ErrorCode",
        "error_message": "ErrorMessage",
    }

    configuration_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_message: Optional[Union[str, Ref, GetAtt, Sub]] = None

