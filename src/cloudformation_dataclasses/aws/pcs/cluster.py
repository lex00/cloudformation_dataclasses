"""PropertyTypes for AWS::PCS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Accounting(PropertyType):
    DEFAULT_PURGE_TIME_IN_DAYS = "DefaultPurgeTimeInDays"
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_purge_time_in_days": "DefaultPurgeTimeInDays",
        "mode": "Mode",
    }

    default_purge_time_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthKey(PropertyType):
    SECRET_ARN = "SecretArn"
    SECRET_VERSION = "SecretVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "secret_version": "SecretVersion",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoint(PropertyType):
    PUBLIC_IP_ADDRESS = "PublicIpAddress"
    TYPE = "Type"
    PRIVATE_IP_ADDRESS = "PrivateIpAddress"
    PORT = "Port"
    IPV6_ADDRESS = "Ipv6Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "public_ip_address": "PublicIpAddress",
        "type_": "Type",
        "private_ip_address": "PrivateIpAddress",
        "port": "Port",
        "ipv6_address": "Ipv6Address",
    }

    public_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorInfo(PropertyType):
    MESSAGE = "Message"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JwtAuth(PropertyType):
    JWT_KEY = "JwtKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jwt_key": "JwtKey",
    }

    jwt_key: Optional[JwtKey] = None


@dataclass
class JwtKey(PropertyType):
    SECRET_ARN = "SecretArn"
    SECRET_VERSION = "SecretVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "secret_version": "SecretVersion",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Networking(PropertyType):
    NETWORK_TYPE = "NetworkType"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_type": "NetworkType",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    network_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class Scheduler(PropertyType):
    TYPE = "Type"
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "version": "Version",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlurmConfiguration(PropertyType):
    JWT_AUTH = "JwtAuth"
    ACCOUNTING = "Accounting"
    AUTH_KEY = "AuthKey"
    SCALE_DOWN_IDLE_TIME_IN_SECONDS = "ScaleDownIdleTimeInSeconds"
    SLURM_CUSTOM_SETTINGS = "SlurmCustomSettings"
    SLURM_REST = "SlurmRest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jwt_auth": "JwtAuth",
        "accounting": "Accounting",
        "auth_key": "AuthKey",
        "scale_down_idle_time_in_seconds": "ScaleDownIdleTimeInSeconds",
        "slurm_custom_settings": "SlurmCustomSettings",
        "slurm_rest": "SlurmRest",
    }

    jwt_auth: Optional[JwtAuth] = None
    accounting: Optional[Accounting] = None
    auth_key: Optional[AuthKey] = None
    scale_down_idle_time_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    slurm_custom_settings: Optional[list[SlurmCustomSetting]] = None
    slurm_rest: Optional[SlurmRest] = None


@dataclass
class SlurmCustomSetting(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_NAME = "ParameterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlurmRest(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None

