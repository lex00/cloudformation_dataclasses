"""PropertyTypes for AWS::AppRunner::Service."""

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
class AuthenticationConfiguration(PropertyType):
    ACCESS_ROLE_ARN = "AccessRoleArn"
    CONNECTION_ARN = "ConnectionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_role_arn": "AccessRoleArn",
        "connection_arn": "ConnectionArn",
    }

    access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CodeConfiguration(PropertyType):
    CONFIGURATION_SOURCE = "ConfigurationSource"
    CODE_CONFIGURATION_VALUES = "CodeConfigurationValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_source": "ConfigurationSource",
        "code_configuration_values": "CodeConfigurationValues",
    }

    configuration_source: Optional[Union[str, ConfigurationSource, Ref, GetAtt, Sub]] = None
    code_configuration_values: Optional[CodeConfigurationValues] = None


@dataclass
class CodeConfigurationValues(PropertyType):
    RUNTIME_ENVIRONMENT_SECRETS = "RuntimeEnvironmentSecrets"
    RUNTIME = "Runtime"
    START_COMMAND = "StartCommand"
    RUNTIME_ENVIRONMENT_VARIABLES = "RuntimeEnvironmentVariables"
    PORT = "Port"
    BUILD_COMMAND = "BuildCommand"

    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime_environment_secrets": "RuntimeEnvironmentSecrets",
        "runtime": "Runtime",
        "start_command": "StartCommand",
        "runtime_environment_variables": "RuntimeEnvironmentVariables",
        "port": "Port",
        "build_command": "BuildCommand",
    }

    runtime_environment_secrets: Optional[list[KeyValuePair]] = None
    runtime: Optional[Union[str, Runtime, Ref, GetAtt, Sub]] = None
    start_command: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_environment_variables: Optional[list[KeyValuePair]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    build_command: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CodeRepository(PropertyType):
    SOURCE_CODE_VERSION = "SourceCodeVersion"
    CODE_CONFIGURATION = "CodeConfiguration"
    SOURCE_DIRECTORY = "SourceDirectory"
    REPOSITORY_URL = "RepositoryUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_code_version": "SourceCodeVersion",
        "code_configuration": "CodeConfiguration",
        "source_directory": "SourceDirectory",
        "repository_url": "RepositoryUrl",
    }

    source_code_version: Optional[SourceCodeVersion] = None
    code_configuration: Optional[CodeConfiguration] = None
    source_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EgressConfiguration(PropertyType):
    VPC_CONNECTOR_ARN = "VpcConnectorArn"
    EGRESS_TYPE = "EgressType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_connector_arn": "VpcConnectorArn",
        "egress_type": "EgressType",
    }

    vpc_connector_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    egress_type: Optional[Union[str, EgressType, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key": "KmsKey",
    }

    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckConfiguration(PropertyType):
    PATH = "Path"
    UNHEALTHY_THRESHOLD = "UnhealthyThreshold"
    TIMEOUT = "Timeout"
    HEALTHY_THRESHOLD = "HealthyThreshold"
    PROTOCOL = "Protocol"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "unhealthy_threshold": "UnhealthyThreshold",
        "timeout": "Timeout",
        "healthy_threshold": "HealthyThreshold",
        "protocol": "Protocol",
        "interval": "Interval",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unhealthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    healthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, HealthCheckProtocol, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ImageConfiguration(PropertyType):
    RUNTIME_ENVIRONMENT_SECRETS = "RuntimeEnvironmentSecrets"
    START_COMMAND = "StartCommand"
    RUNTIME_ENVIRONMENT_VARIABLES = "RuntimeEnvironmentVariables"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime_environment_secrets": "RuntimeEnvironmentSecrets",
        "start_command": "StartCommand",
        "runtime_environment_variables": "RuntimeEnvironmentVariables",
        "port": "Port",
    }

    runtime_environment_secrets: Optional[list[KeyValuePair]] = None
    start_command: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_environment_variables: Optional[list[KeyValuePair]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageRepository(PropertyType):
    IMAGE_IDENTIFIER = "ImageIdentifier"
    IMAGE_CONFIGURATION = "ImageConfiguration"
    IMAGE_REPOSITORY_TYPE = "ImageRepositoryType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_identifier": "ImageIdentifier",
        "image_configuration": "ImageConfiguration",
        "image_repository_type": "ImageRepositoryType",
    }

    image_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_configuration: Optional[ImageConfiguration] = None
    image_repository_type: Optional[Union[str, ImageRepositoryType, Ref, GetAtt, Sub]] = None


@dataclass
class IngressConfiguration(PropertyType):
    IS_PUBLICLY_ACCESSIBLE = "IsPubliclyAccessible"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_publicly_accessible": "IsPubliclyAccessible",
    }

    is_publicly_accessible: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceConfiguration(PropertyType):
    INSTANCE_ROLE_ARN = "InstanceRoleArn"
    MEMORY = "Memory"
    CPU = "Cpu"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_role_arn": "InstanceRoleArn",
        "memory": "Memory",
        "cpu": "Cpu",
    }

    instance_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValuePair(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    IP_ADDRESS_TYPE = "IpAddressType"
    EGRESS_CONFIGURATION = "EgressConfiguration"
    INGRESS_CONFIGURATION = "IngressConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "egress_configuration": "EgressConfiguration",
        "ingress_configuration": "IngressConfiguration",
    }

    ip_address_type: Optional[Union[str, IpAddressType, Ref, GetAtt, Sub]] = None
    egress_configuration: Optional[EgressConfiguration] = None
    ingress_configuration: Optional[IngressConfiguration] = None


@dataclass
class ServiceObservabilityConfiguration(PropertyType):
    OBSERVABILITY_ENABLED = "ObservabilityEnabled"
    OBSERVABILITY_CONFIGURATION_ARN = "ObservabilityConfigurationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "observability_enabled": "ObservabilityEnabled",
        "observability_configuration_arn": "ObservabilityConfigurationArn",
    }

    observability_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    observability_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceCodeVersion(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, SourceCodeVersionType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConfiguration(PropertyType):
    AUTHENTICATION_CONFIGURATION = "AuthenticationConfiguration"
    CODE_REPOSITORY = "CodeRepository"
    IMAGE_REPOSITORY = "ImageRepository"
    AUTO_DEPLOYMENTS_ENABLED = "AutoDeploymentsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_configuration": "AuthenticationConfiguration",
        "code_repository": "CodeRepository",
        "image_repository": "ImageRepository",
        "auto_deployments_enabled": "AutoDeploymentsEnabled",
    }

    authentication_configuration: Optional[AuthenticationConfiguration] = None
    code_repository: Optional[CodeRepository] = None
    image_repository: Optional[ImageRepository] = None
    auto_deployments_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

