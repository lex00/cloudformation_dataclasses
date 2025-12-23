"""PropertyTypes for AWS::GuardDuty::Detector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CFNDataSourceConfigurations(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "malware_protection": "MalwareProtection",
        "s3_logs": "S3Logs",
        "kubernetes": "Kubernetes",
    }

    malware_protection: Optional[CFNMalwareProtectionConfiguration] = None
    s3_logs: Optional[CFNS3LogsConfiguration] = None
    kubernetes: Optional[CFNKubernetesConfiguration] = None


@dataclass
class CFNFeatureAdditionalConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CFNFeatureConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "additional_configuration": "AdditionalConfiguration",
        "name": "Name",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_configuration: Optional[list[CFNFeatureAdditionalConfiguration]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CFNKubernetesAuditLogsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable": "Enable",
    }

    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CFNKubernetesConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "audit_logs": "AuditLogs",
    }

    audit_logs: Optional[CFNKubernetesAuditLogsConfiguration] = None


@dataclass
class CFNMalwareProtectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scan_ec2_instance_with_findings": "ScanEc2InstanceWithFindings",
    }

    scan_ec2_instance_with_findings: Optional[CFNScanEc2InstanceWithFindingsConfiguration] = None


@dataclass
class CFNS3LogsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable": "Enable",
    }

    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CFNScanEc2InstanceWithFindingsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_volumes": "EbsVolumes",
    }

    ebs_volumes: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TagItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

