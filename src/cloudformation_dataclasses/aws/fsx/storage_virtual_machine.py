"""PropertyTypes for AWS::FSx::StorageVirtualMachine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActiveDirectoryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "self_managed_active_directory_configuration": "SelfManagedActiveDirectoryConfiguration",
        "net_bios_name": "NetBiosName",
    }

    self_managed_active_directory_configuration: Optional[SelfManagedActiveDirectoryConfiguration] = None
    net_bios_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelfManagedActiveDirectoryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_administrators_group": "FileSystemAdministratorsGroup",
        "user_name": "UserName",
        "domain_name": "DomainName",
        "organizational_unit_distinguished_name": "OrganizationalUnitDistinguishedName",
        "domain_join_service_account_secret": "DomainJoinServiceAccountSecret",
        "dns_ips": "DnsIps",
        "password": "Password",
    }

    file_system_administrators_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organizational_unit_distinguished_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_join_service_account_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_ips: Optional[Union[list[str], Ref]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None

