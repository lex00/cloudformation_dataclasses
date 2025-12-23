"""PropertyTypes for AWS::SES::Template."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Template(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "html_part": "HtmlPart",
        "text_part": "TextPart",
        "template_name": "TemplateName",
        "subject_part": "SubjectPart",
    }

    html_part: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_part: Optional[Union[str, Ref, GetAtt, Sub]] = None
    template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject_part: Optional[Union[str, Ref, GetAtt, Sub]] = None

