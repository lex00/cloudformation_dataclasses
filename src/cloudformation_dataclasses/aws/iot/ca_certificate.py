"""PropertyTypes for AWS::IoT::CACertificate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RegistrationConfig(PropertyType):
    TEMPLATE_NAME = "TemplateName"
    TEMPLATE_BODY = "TemplateBody"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template_name": "TemplateName",
        "template_body": "TemplateBody",
        "role_arn": "RoleArn",
    }

    template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    template_body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

