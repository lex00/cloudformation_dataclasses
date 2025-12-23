"""PropertyTypes for AWS::ECS::Service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "test_listener_rule": "TestListenerRule",
        "alternate_target_group_arn": "AlternateTargetGroupArn",
        "production_listener_rule": "ProductionListenerRule",
        "role_arn": "RoleArn",
    }

    test_listener_rule: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alternate_target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    production_listener_rule: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsVpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
        "assign_public_ip": "AssignPublicIp",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None
    assign_public_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CanaryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canary_percent": "CanaryPercent",
        "canary_bake_time_in_minutes": "CanaryBakeTimeInMinutes",
    }

    canary_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None
    canary_bake_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "base": "Base",
        "weight": "Weight",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentAlarms(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alarm_names": "AlarmNames",
        "enable": "Enable",
        "rollback": "Rollback",
    }

    alarm_names: Optional[Union[list[str], Ref]] = None
    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rollback: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentCircuitBreaker(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable": "Enable",
        "rollback": "Rollback",
    }

    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rollback: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "canary_configuration": "CanaryConfiguration",
        "bake_time_in_minutes": "BakeTimeInMinutes",
        "lifecycle_hooks": "LifecycleHooks",
        "alarms": "Alarms",
        "strategy": "Strategy",
        "deployment_circuit_breaker": "DeploymentCircuitBreaker",
        "maximum_percent": "MaximumPercent",
        "minimum_healthy_percent": "MinimumHealthyPercent",
        "linear_configuration": "LinearConfiguration",
    }

    canary_configuration: Optional[CanaryConfiguration] = None
    bake_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    lifecycle_hooks: Optional[list[DeploymentLifecycleHook]] = None
    alarms: Optional[DeploymentAlarms] = None
    strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deployment_circuit_breaker: Optional[DeploymentCircuitBreaker] = None
    maximum_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_healthy_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    linear_configuration: Optional[LinearConfiguration] = None


@dataclass
class DeploymentController(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentLifecycleHook(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lifecycle_stages": "LifecycleStages",
        "hook_target_arn": "HookTargetArn",
        "hook_details": "HookDetails",
        "role_arn": "RoleArn",
    }

    lifecycle_stages: Optional[Union[list[str], Ref]] = None
    hook_target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hook_details: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EBSTagSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "propagate_tags": "PropagateTags",
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    propagate_tags: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None


@dataclass
class ForceNewDeployment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_force_new_deployment": "EnableForceNewDeployment",
        "force_new_deployment_nonce": "ForceNewDeploymentNonce",
    }

    enable_force_new_deployment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    force_new_deployment_nonce: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LinearConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "step_bake_time_in_minutes": "StepBakeTimeInMinutes",
        "step_percent": "StepPercent",
    }

    step_bake_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    step_percent: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LoadBalancer(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_arn": "TargetGroupArn",
        "load_balancer_name": "LoadBalancerName",
        "container_name": "ContainerName",
        "container_port": "ContainerPort",
        "advanced_configuration": "AdvancedConfiguration",
    }

    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    advanced_configuration: Optional[AdvancedConfiguration] = None


@dataclass
class LogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_options": "SecretOptions",
        "options": "Options",
        "log_driver": "LogDriver",
    }

    secret_options: Optional[list[Secret]] = None
    options: Optional[dict[str, str]] = None
    log_driver: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "awsvpc_configuration": "AwsvpcConfiguration",
    }

    awsvpc_configuration: Optional[AwsVpcConfiguration] = None


@dataclass
class PlacementConstraint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "expression": "Expression",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PlacementStrategy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "type_": "Type",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Secret(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_from": "ValueFrom",
        "name": "Name",
    }

    value_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectAccessLogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "include_query_parameters": "IncludeQueryParameters",
    }

    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_query_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectClientAlias(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DnsName",
        "test_traffic_rules": "TestTrafficRules",
        "port": "Port",
    }

    dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    test_traffic_rules: Optional[ServiceConnectTestTrafficRules] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "services": "Services",
        "access_log_configuration": "AccessLogConfiguration",
        "enabled": "Enabled",
        "log_configuration": "LogConfiguration",
        "namespace": "Namespace",
    }

    services: Optional[list[ServiceConnectService]] = None
    access_log_configuration: Optional[ServiceConnectAccessLogConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_configuration: Optional[LogConfiguration] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectService(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout": "Timeout",
        "ingress_port_override": "IngressPortOverride",
        "client_aliases": "ClientAliases",
        "tls": "Tls",
        "discovery_name": "DiscoveryName",
        "port_name": "PortName",
    }

    timeout: Optional[TimeoutConfiguration] = None
    ingress_port_override: Optional[Union[int, Ref, GetAtt, Sub]] = None
    client_aliases: Optional[list[ServiceConnectClientAlias]] = None
    tls: Optional[ServiceConnectTlsConfiguration] = None
    discovery_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTestTrafficRules(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
    }

    header: Optional[ServiceConnectTestTrafficRulesHeader] = None


@dataclass
class ServiceConnectTestTrafficRulesHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[ServiceConnectTestTrafficRulesHeaderValue] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTestTrafficRulesHeaderValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTlsCertificateAuthority(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_pca_authority_arn": "AwsPcaAuthorityArn",
    }

    aws_pca_authority_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConnectTlsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "issuer_certificate_authority": "IssuerCertificateAuthority",
        "kms_key": "KmsKey",
        "role_arn": "RoleArn",
    }

    issuer_certificate_authority: Optional[ServiceConnectTlsCertificateAuthority] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceManagedEBSVolumeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "kms_key_id": "KmsKeyId",
        "tag_specifications": "TagSpecifications",
        "filesystem_type": "FilesystemType",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "volume_initialization_rate": "VolumeInitializationRate",
        "iops": "Iops",
        "size_in_gi_b": "SizeInGiB",
        "role_arn": "RoleArn",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_specifications: Optional[list[EBSTagSpecification]] = None
    filesystem_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_initialization_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceRegistry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "port": "Port",
        "container_port": "ContainerPort",
        "registry_arn": "RegistryArn",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    registry_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceVolumeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_ebs_volume": "ManagedEBSVolume",
        "name": "Name",
    }

    managed_ebs_volume: Optional[ServiceManagedEBSVolumeConfiguration] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeoutConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request_timeout_seconds": "PerRequestTimeoutSeconds",
        "idle_timeout_seconds": "IdleTimeoutSeconds",
    }

    per_request_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    idle_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcLatticeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_arn": "TargetGroupArn",
        "port_name": "PortName",
        "role_arn": "RoleArn",
    }

    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

