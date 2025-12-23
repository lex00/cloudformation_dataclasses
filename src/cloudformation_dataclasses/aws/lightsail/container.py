"""PropertyTypes for AWS::Lightsail::Container."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Container(PropertyType):
    CONTAINER_NAME = "ContainerName"
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    PORTS = "Ports"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "command": "Command",
        "environment": "Environment",
        "ports": "Ports",
        "image": "Image",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[EnvironmentVariable]] = None
    ports: Optional[list[PortInfo]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerServiceDeployment(PropertyType):
    CONTAINERS = "Containers"
    PUBLIC_ENDPOINT = "PublicEndpoint"

    _property_mappings: ClassVar[dict[str, str]] = {
        "containers": "Containers",
        "public_endpoint": "PublicEndpoint",
    }

    containers: Optional[list[Container]] = None
    public_endpoint: Optional[PublicEndpoint] = None


@dataclass
class EcrImagePullerRole(PropertyType):
    PRINCIPAL_ARN = "PrincipalArn"
    IS_ACTIVE = "IsActive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "principal_arn": "PrincipalArn",
        "is_active": "IsActive",
    }

    principal_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentVariable(PropertyType):
    VARIABLE = "Variable"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variable": "Variable",
        "value": "Value",
    }

    variable: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckConfig(PropertyType):
    PATH = "Path"
    TIMEOUT_SECONDS = "TimeoutSeconds"
    SUCCESS_CODES = "SuccessCodes"
    UNHEALTHY_THRESHOLD = "UnhealthyThreshold"
    HEALTHY_THRESHOLD = "HealthyThreshold"
    INTERVAL_SECONDS = "IntervalSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "timeout_seconds": "TimeoutSeconds",
        "success_codes": "SuccessCodes",
        "unhealthy_threshold": "UnhealthyThreshold",
        "healthy_threshold": "HealthyThreshold",
        "interval_seconds": "IntervalSeconds",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    success_codes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unhealthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    healthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PortInfo(PropertyType):
    PORT = "Port"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "protocol": "Protocol",
    }

    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateRegistryAccess(PropertyType):
    ECR_IMAGE_PULLER_ROLE = "EcrImagePullerRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ecr_image_puller_role": "EcrImagePullerRole",
    }

    ecr_image_puller_role: Optional[EcrImagePullerRole] = None


@dataclass
class PublicDomainName(PropertyType):
    CERTIFICATE_NAME = "CertificateName"
    DOMAIN_NAMES = "DomainNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_name": "CertificateName",
        "domain_names": "DomainNames",
    }

    certificate_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_names: Optional[Union[list[str], Ref]] = None


@dataclass
class PublicEndpoint(PropertyType):
    CONTAINER_NAME = "ContainerName"
    CONTAINER_PORT = "ContainerPort"
    HEALTH_CHECK_CONFIG = "HealthCheckConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "container_port": "ContainerPort",
        "health_check_config": "HealthCheckConfig",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    health_check_config: Optional[HealthCheckConfig] = None

