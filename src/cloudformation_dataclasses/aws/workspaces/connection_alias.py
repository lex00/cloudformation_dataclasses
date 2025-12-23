"""PropertyTypes for AWS::WorkSpaces::ConnectionAlias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionAliasAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "associated_account_id": "AssociatedAccountId",
        "resource_id": "ResourceId",
        "connection_identifier": "ConnectionIdentifier",
        "association_status": "AssociationStatus",
    }

    associated_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    association_status: Optional[Union[str, AssociationStatus, Ref, GetAtt, Sub]] = None

