"""PropertyTypes for AWS::OpsWorks::Stack."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ChefConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "berkshelf_version": "BerkshelfVersion",
        "manage_berkshelf": "ManageBerkshelf",
    }

    berkshelf_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manage_berkshelf: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticIp(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip": "Ip",
        "name": "Name",
    }

    ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsDbInstance(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "db_password": "DbPassword",
        "db_user": "DbUser",
        "rds_db_instance_arn": "RdsDbInstanceArn",
    }

    db_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rds_db_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "password": "Password",
        "revision": "Revision",
        "ssh_key": "SshKey",
        "type_": "Type",
        "url": "Url",
        "username": "Username",
    }

    password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revision: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssh_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    username: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StackConfigurationManager(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "version": "Version",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None

