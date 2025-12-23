"""PropertyTypes for AWS::APS::Scraper."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmpConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "workspace_arn": "WorkspaceArn",
    }

    workspace_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ComponentConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
    }

    options: Optional[dict[str, str]] = None


@dataclass
class Destination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "amp_configuration": "AmpConfiguration",
    }

    amp_configuration: Optional[AmpConfiguration] = None


@dataclass
class EksConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_arn": "ClusterArn",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class RoleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_role_arn": "TargetRoleArn",
        "source_role_arn": "SourceRoleArn",
    }

    target_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScrapeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configuration_blob": "ConfigurationBlob",
    }

    configuration_blob: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScraperComponent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "config": "Config",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    config: Optional[ComponentConfig] = None


@dataclass
class ScraperLoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logging_destination": "LoggingDestination",
        "scraper_components": "ScraperComponents",
    }

    logging_destination: Optional[ScraperLoggingDestination] = None
    scraper_components: Optional[list[ScraperComponent]] = None


@dataclass
class ScraperLoggingDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs": "CloudWatchLogs",
    }

    cloud_watch_logs: Optional[CloudWatchLogDestination] = None


@dataclass
class Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "eks_configuration": "EksConfiguration",
        "vpc_configuration": "VpcConfiguration",
    }

    eks_configuration: Optional[EksConfiguration] = None
    vpc_configuration: Optional[VpcConfiguration] = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

