"""PropertyTypes for AWS::Route53RecoveryReadiness::ResourceSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Readiness:
    """Readiness enum values."""

    READY = "READY"
    NOT_READY = "NOT_READY"
    UNKNOWN = "UNKNOWN"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"


@dataclass
class DNSTargetResource(PropertyType):
    TARGET_RESOURCE = "TargetResource"
    RECORD_TYPE = "RecordType"
    DOMAIN_NAME = "DomainName"
    HOSTED_ZONE_ARN = "HostedZoneArn"
    RECORD_SET_ID = "RecordSetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_resource": "TargetResource",
        "record_type": "RecordType",
        "domain_name": "DomainName",
        "hosted_zone_arn": "HostedZoneArn",
        "record_set_id": "RecordSetId",
    }

    target_resource: Optional[TargetResource] = None
    record_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_set_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NLBResource(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class R53ResourceRecord(PropertyType):
    DOMAIN_NAME = "DomainName"
    RECORD_SET_ID = "RecordSetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_name": "DomainName",
        "record_set_id": "RecordSetId",
    }

    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    record_set_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Resource(PropertyType):
    RESOURCE_ARN = "ResourceArn"
    DNS_TARGET_RESOURCE = "DnsTargetResource"
    READINESS_SCOPES = "ReadinessScopes"
    COMPONENT_ID = "ComponentId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "dns_target_resource": "DnsTargetResource",
        "readiness_scopes": "ReadinessScopes",
        "component_id": "ComponentId",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_target_resource: Optional[DNSTargetResource] = None
    readiness_scopes: Optional[Union[list[str], Ref]] = None
    component_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetResource(PropertyType):
    R53_RESOURCE = "R53Resource"
    NLB_RESOURCE = "NLBResource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "r53_resource": "R53Resource",
        "nlb_resource": "NLBResource",
    }

    r53_resource: Optional[R53ResourceRecord] = None
    nlb_resource: Optional[NLBResource] = None

