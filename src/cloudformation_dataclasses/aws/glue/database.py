"""PropertyTypes for AWS::Glue::Database."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataLakePrincipal(PropertyType):
    DATA_LAKE_PRINCIPAL_IDENTIFIER = "DataLakePrincipalIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_lake_principal_identifier": "DataLakePrincipalIdentifier",
    }

    data_lake_principal_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseIdentifier(PropertyType):
    DATABASE_NAME = "DatabaseName"
    REGION = "Region"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
        "region": "Region",
        "catalog_id": "CatalogId",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseInput(PropertyType):
    LOCATION_URI = "LocationUri"
    CREATE_TABLE_DEFAULT_PERMISSIONS = "CreateTableDefaultPermissions"
    DESCRIPTION = "Description"
    PARAMETERS = "Parameters"
    TARGET_DATABASE = "TargetDatabase"
    FEDERATED_DATABASE = "FederatedDatabase"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "location_uri": "LocationUri",
        "create_table_default_permissions": "CreateTableDefaultPermissions",
        "description": "Description",
        "parameters": "Parameters",
        "target_database": "TargetDatabase",
        "federated_database": "FederatedDatabase",
        "name": "Name",
    }

    location_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    create_table_default_permissions: Optional[list[PrincipalPrivileges]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    target_database: Optional[DatabaseIdentifier] = None
    federated_database: Optional[FederatedDatabase] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FederatedDatabase(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    IDENTIFIER = "Identifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "identifier": "Identifier",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrincipalPrivileges(PropertyType):
    PERMISSIONS = "Permissions"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "permissions": "Permissions",
        "principal": "Principal",
    }

    permissions: Optional[Union[list[str], Ref]] = None
    principal: Optional[DataLakePrincipal] = None

