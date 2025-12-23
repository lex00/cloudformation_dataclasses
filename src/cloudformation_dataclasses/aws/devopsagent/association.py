"""PropertyTypes for AWS::DevOpsAgent::Association."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AWSConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "assumable_role_arn": "AssumableRoleArn",
        "account_id": "AccountId",
        "resources": "Resources",
        "account_type": "AccountType",
        "tags": "Tags",
    }

    assumable_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resources: Optional[list[AWSResource]] = None
    account_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[KeyValuePair]] = None


@dataclass
class AWSResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "resource_type": "ResourceType",
        "resource_metadata": "ResourceMetadata",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_metadata: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class DynatraceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "env_id": "EnvId",
        "resources": "Resources",
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    env_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resources: Optional[Union[list[str], Ref]] = None
    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EventChannelConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class GitHubConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
        "owner_type": "OwnerType",
        "repo_name": "RepoName",
        "repo_id": "RepoId",
    }

    owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    owner_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repo_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repo_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GitLabConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_id": "ProjectId",
        "instance_identifier": "InstanceIdentifier",
        "project_path": "ProjectPath",
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    project_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    project_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValuePair(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MCPServerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "endpoint": "Endpoint",
        "tools": "Tools",
        "name": "Name",
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tools: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MCPServerDatadogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "endpoint": "Endpoint",
        "name": "Name",
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MCPServerNewRelicConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "account_id": "AccountId",
        "endpoint": "Endpoint",
    }

    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MCPServerSplunkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "endpoint": "Endpoint",
        "name": "Name",
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp_server": "MCPServer",
        "event_channel": "EventChannel",
        "service_now": "ServiceNow",
        "source_aws": "SourceAws",
        "slack": "Slack",
        "git_hub": "GitHub",
        "mcp_server_datadog": "MCPServerDatadog",
        "dynatrace": "Dynatrace",
        "mcp_server_splunk": "MCPServerSplunk",
        "aws": "Aws",
        "mcp_server_new_relic": "MCPServerNewRelic",
        "git_lab": "GitLab",
    }

    mcp_server: Optional[MCPServerConfiguration] = None
    event_channel: Optional[EventChannelConfiguration] = None
    service_now: Optional[ServiceNowConfiguration] = None
    source_aws: Optional[SourceAwsConfiguration] = None
    slack: Optional[SlackConfiguration] = None
    git_hub: Optional[GitHubConfiguration] = None
    mcp_server_datadog: Optional[MCPServerDatadogConfiguration] = None
    dynatrace: Optional[DynatraceConfiguration] = None
    mcp_server_splunk: Optional[MCPServerSplunkConfiguration] = None
    aws: Optional[AWSConfiguration] = None
    mcp_server_new_relic: Optional[MCPServerNewRelicConfiguration] = None
    git_lab: Optional[GitLabConfiguration] = None


@dataclass
class ServiceNowConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_id": "InstanceId",
        "enable_webhook_updates": "EnableWebhookUpdates",
    }

    instance_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_webhook_updates: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class SlackChannel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_name": "ChannelName",
        "channel_id": "ChannelId",
    }

    channel_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlackConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transmission_target": "TransmissionTarget",
        "workspace_id": "WorkspaceId",
        "workspace_name": "WorkspaceName",
    }

    transmission_target: Optional[SlackTransmissionTarget] = None
    workspace_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workspace_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlackTransmissionTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "incident_response_target": "IncidentResponseTarget",
    }

    incident_response_target: Optional[SlackChannel] = None


@dataclass
class SourceAwsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "assumable_role_arn": "AssumableRoleArn",
        "account_id": "AccountId",
        "resources": "Resources",
        "account_type": "AccountType",
        "tags": "Tags",
    }

    assumable_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resources: Optional[list[AWSResource]] = None
    account_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[KeyValuePair]] = None

