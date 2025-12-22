"""PropertyTypes for AWS::AppRunner::VpcIngressConnection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AutoScalingConfigurationStatus:
    """AutoScalingConfigurationStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class CertificateValidationRecordStatus:
    """CertificateValidationRecordStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class ConfigurationSource:
    """ConfigurationSource enum values."""

    REPOSITORY = "REPOSITORY"
    API = "API"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    PENDING_HANDSHAKE = "PENDING_HANDSHAKE"
    AVAILABLE = "AVAILABLE"
    ERROR = "ERROR"
    DELETED = "DELETED"


class CustomDomainAssociationStatus:
    """CustomDomainAssociationStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    PENDING_CERTIFICATE_DNS_VALIDATION = "PENDING_CERTIFICATE_DNS_VALIDATION"
    BINDING_CERTIFICATE = "BINDING_CERTIFICATE"


class EgressType:
    """EgressType enum values."""

    DEFAULT = "DEFAULT"
    VPC = "VPC"


class HealthCheckProtocol:
    """HealthCheckProtocol enum values."""

    TCP = "TCP"
    HTTP = "HTTP"


class ImageRepositoryType:
    """ImageRepositoryType enum values."""

    ECR = "ECR"
    ECR_PUBLIC = "ECR_PUBLIC"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "IPV4"
    DUAL_STACK = "DUAL_STACK"


class ObservabilityConfigurationStatus:
    """ObservabilityConfigurationStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class OperationStatus:
    """OperationStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_SUCCEEDED = "ROLLBACK_SUCCEEDED"


class OperationType:
    """OperationType enum values."""

    START_DEPLOYMENT = "START_DEPLOYMENT"
    CREATE_SERVICE = "CREATE_SERVICE"
    PAUSE_SERVICE = "PAUSE_SERVICE"
    RESUME_SERVICE = "RESUME_SERVICE"
    DELETE_SERVICE = "DELETE_SERVICE"
    UPDATE_SERVICE = "UPDATE_SERVICE"


class ProviderType:
    """ProviderType enum values."""

    GITHUB = "GITHUB"
    BITBUCKET = "BITBUCKET"


class Runtime:
    """Runtime enum values."""

    PYTHON_3 = "PYTHON_3"
    NODEJS_12 = "NODEJS_12"
    NODEJS_14 = "NODEJS_14"
    CORRETTO_8 = "CORRETTO_8"
    CORRETTO_11 = "CORRETTO_11"
    NODEJS_16 = "NODEJS_16"
    GO_1 = "GO_1"
    DOTNET_6 = "DOTNET_6"
    PHP_81 = "PHP_81"
    RUBY_31 = "RUBY_31"
    PYTHON_311 = "PYTHON_311"
    NODEJS_18 = "NODEJS_18"
    NODEJS_22 = "NODEJS_22"


class ServiceStatus:
    """ServiceStatus enum values."""

    CREATE_FAILED = "CREATE_FAILED"
    RUNNING = "RUNNING"
    DELETED = "DELETED"
    DELETE_FAILED = "DELETE_FAILED"
    PAUSED = "PAUSED"
    OPERATION_IN_PROGRESS = "OPERATION_IN_PROGRESS"


class SourceCodeVersionType:
    """SourceCodeVersionType enum values."""

    BRANCH = "BRANCH"


class TracingVendor:
    """TracingVendor enum values."""

    AWSXRAY = "AWSXRAY"


class VpcConnectorStatus:
    """VpcConnectorStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class VpcIngressConnectionStatus:
    """VpcIngressConnectionStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING_CREATION = "PENDING_CREATION"
    PENDING_UPDATE = "PENDING_UPDATE"
    PENDING_DELETION = "PENDING_DELETION"
    FAILED_CREATION = "FAILED_CREATION"
    FAILED_UPDATE = "FAILED_UPDATE"
    FAILED_DELETION = "FAILED_DELETION"
    DELETED = "DELETED"


@dataclass
class IngressVpcConfiguration(PropertyType):
    VPC_ID = "VpcId"
    VPC_ENDPOINT_ID = "VpcEndpointId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

