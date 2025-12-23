"""PropertyTypes for AWS::ElasticLoadBalancing::LoadBalancer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessLoggingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "emit_interval": "EmitInterval",
        "enabled": "Enabled",
        "s3_bucket_name": "S3BucketName",
        "s3_bucket_prefix": "S3BucketPrefix",
    }

    emit_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AppCookieStickinessPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cookie_name": "CookieName",
        "policy_name": "PolicyName",
    }

    cookie_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionDrainingPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "timeout": "Timeout",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_timeout": "IdleTimeout",
    }

    idle_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheck(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "healthy_threshold": "HealthyThreshold",
        "interval": "Interval",
        "target": "Target",
        "timeout": "Timeout",
        "unhealthy_threshold": "UnhealthyThreshold",
    }

    healthy_threshold: Optional[Union[str, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unhealthy_threshold: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LBCookieStickinessPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cookie_expiration_period": "CookieExpirationPeriod",
        "policy_name": "PolicyName",
    }

    cookie_expiration_period: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Listeners(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_port": "InstancePort",
        "instance_protocol": "InstanceProtocol",
        "load_balancer_port": "LoadBalancerPort",
        "policy_names": "PolicyNames",
        "protocol": "Protocol",
        "ssl_certificate_id": "SSLCertificateId",
    }

    instance_port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_names: Optional[Union[list[str], Ref]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssl_certificate_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Policies(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes": "Attributes",
        "instance_ports": "InstancePorts",
        "load_balancer_ports": "LoadBalancerPorts",
        "policy_name": "PolicyName",
        "policy_type": "PolicyType",
    }

    attributes: Optional[Union[list[dict[str, Any]], Ref]] = None
    instance_ports: Optional[Union[list[str], Ref]] = None
    load_balancer_ports: Optional[Union[list[str], Ref]] = None
    policy_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

