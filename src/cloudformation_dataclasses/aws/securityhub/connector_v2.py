"""PropertyTypes for AWS::SecurityHub::ConnectorV2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class JiraCloud(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_key": "ProjectKey",
        "auth_status": "AuthStatus",
        "auth_url": "AuthUrl",
        "domain": "Domain",
        "cloud_id": "CloudId",
    }

    project_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Provider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_now": "ServiceNow",
        "jira_cloud": "JiraCloud",
    }

    service_now: Optional[ServiceNow] = None
    jira_cloud: Optional[JiraCloud] = None


@dataclass
class ServiceNow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_name": "InstanceName",
        "secret_arn": "SecretArn",
        "auth_status": "AuthStatus",
    }

    instance_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_status: Optional[Union[str, Ref, GetAtt, Sub]] = None

