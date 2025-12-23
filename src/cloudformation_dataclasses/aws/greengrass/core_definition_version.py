"""PropertyTypes for AWS::Greengrass::CoreDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Core(PropertyType):
    SYNC_SHADOW = "SyncShadow"
    THING_ARN = "ThingArn"
    ID = "Id"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sync_shadow": "SyncShadow",
        "thing_arn": "ThingArn",
        "id": "Id",
        "certificate_arn": "CertificateArn",
    }

    sync_shadow: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    thing_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

