"""PropertyTypes for AWS::LakeFormation::DataLakeSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Admins(PropertyType):
    pass


@dataclass
class CreateDatabaseDefaultPermissions(PropertyType):
    pass


@dataclass
class CreateTableDefaultPermissions(PropertyType):
    pass


@dataclass
class DataLakePrincipal(PropertyType):
    DATA_LAKE_PRINCIPAL_IDENTIFIER = "DataLakePrincipalIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_lake_principal_identifier": "DataLakePrincipalIdentifier",
    }

    data_lake_principal_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExternalDataFilteringAllowList(PropertyType):
    pass


@dataclass
class PrincipalPermissions(PropertyType):
    PERMISSIONS = "Permissions"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "permissions": "Permissions",
        "principal": "Principal",
    }

    permissions: Optional[Union[list[str], Ref]] = None
    principal: Optional[DataLakePrincipal] = None


@dataclass
class ReadOnlyAdmins(PropertyType):
    pass

