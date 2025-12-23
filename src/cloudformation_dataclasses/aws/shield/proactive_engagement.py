"""PropertyTypes for AWS::Shield::ProactiveEngagement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EmergencyContact(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_notes": "ContactNotes",
        "phone_number": "PhoneNumber",
        "email_address": "EmailAddress",
    }

    contact_notes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

