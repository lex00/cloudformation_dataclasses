"""PropertyTypes for AWS::IoTWireless::PartnerAccount."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SidewalkAccountInfo(PropertyType):
    APP_SERVER_PRIVATE_KEY = "AppServerPrivateKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_server_private_key": "AppServerPrivateKey",
    }

    app_server_private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SidewalkAccountInfoWithFingerprint(PropertyType):
    FINGERPRINT = "Fingerprint"
    AMAZON_ID = "AmazonId"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fingerprint": "Fingerprint",
        "amazon_id": "AmazonId",
        "arn": "Arn",
    }

    fingerprint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    amazon_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SidewalkUpdateAccount(PropertyType):
    APP_SERVER_PRIVATE_KEY = "AppServerPrivateKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_server_private_key": "AppServerPrivateKey",
    }

    app_server_private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

