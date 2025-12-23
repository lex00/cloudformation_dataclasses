"""PropertyTypes for AWS::SystemsManagerSAP::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComponentInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ec2_instance_id": "Ec2InstanceId",
        "component_type": "ComponentType",
        "sid": "Sid",
    }

    ec2_instance_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sid: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Credential(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_id": "SecretId",
        "database_name": "DatabaseName",
        "credential_type": "CredentialType",
    }

    secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

