"""PropertyTypes for AWS::ApiGateway::Method."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Integration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_namespace": "CacheNamespace",
        "connection_type": "ConnectionType",
        "integration_responses": "IntegrationResponses",
        "integration_http_method": "IntegrationHttpMethod",
        "response_transfer_mode": "ResponseTransferMode",
        "uri": "Uri",
        "passthrough_behavior": "PassthroughBehavior",
        "request_parameters": "RequestParameters",
        "connection_id": "ConnectionId",
        "type_": "Type",
        "cache_key_parameters": "CacheKeyParameters",
        "integration_target": "IntegrationTarget",
        "content_handling": "ContentHandling",
        "request_templates": "RequestTemplates",
        "timeout_in_millis": "TimeoutInMillis",
        "credentials": "Credentials",
    }

    cache_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    integration_responses: Optional[list[IntegrationResponse]] = None
    integration_http_method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_transfer_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    passthrough_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    request_parameters: Optional[dict[str, str]] = None
    connection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cache_key_parameters: Optional[Union[list[str], Ref]] = None
    integration_target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_handling: Optional[Union[str, Ref, GetAtt, Sub]] = None
    request_templates: Optional[dict[str, str]] = None
    timeout_in_millis: Optional[Union[int, Ref, GetAtt, Sub]] = None
    credentials: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegrationResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "response_templates": "ResponseTemplates",
        "selection_pattern": "SelectionPattern",
        "content_handling": "ContentHandling",
        "response_parameters": "ResponseParameters",
        "status_code": "StatusCode",
    }

    response_templates: Optional[dict[str, str]] = None
    selection_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_handling: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_parameters: Optional[dict[str, str]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MethodResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "response_parameters": "ResponseParameters",
        "status_code": "StatusCode",
        "response_models": "ResponseModels",
    }

    response_parameters: Optional[dict[str, str]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_models: Optional[dict[str, str]] = None

