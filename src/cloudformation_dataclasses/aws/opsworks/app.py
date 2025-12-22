"""PropertyTypes for AWS::OpsWorks::App."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataSource(PropertyType):
    ARN = "Arn"
    DATABASE_NAME = "DatabaseName"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
        "database_name": "DatabaseName",
        "type_": "Type",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentVariable(PropertyType):
    KEY = "Key"
    SECURE = "Secure"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key": "Key",
        "secure": "Secure",
        "value": "Value",
    }

    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secure: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    PASSWORD = "Password"
    REVISION = "Revision"
    SSH_KEY = "SshKey"
    TYPE = "Type"
    URL = "Url"
    USERNAME = "Username"

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
class SslConfiguration(PropertyType):
    CERTIFICATE = "Certificate"
    CHAIN = "Chain"
    PRIVATE_KEY = "PrivateKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate": "Certificate",
        "chain": "Chain",
        "private_key": "PrivateKey",
    }

    certificate: Optional[Union[str, Ref, GetAtt, Sub]] = None
    chain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

