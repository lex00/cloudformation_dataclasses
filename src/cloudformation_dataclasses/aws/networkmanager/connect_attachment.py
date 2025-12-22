"""PropertyTypes for AWS::NetworkManager::ConnectAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AttachmentErrorCode:
    """AttachmentErrorCode enum values."""

    VPC_NOT_FOUND = "VPC_NOT_FOUND"
    SUBNET_NOT_FOUND = "SUBNET_NOT_FOUND"
    SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE = "SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE"
    SUBNET_NO_FREE_ADDRESSES = "SUBNET_NO_FREE_ADDRESSES"
    SUBNET_UNSUPPORTED_AVAILABILITY_ZONE = "SUBNET_UNSUPPORTED_AVAILABILITY_ZONE"
    SUBNET_NO_IPV6_CIDRS = "SUBNET_NO_IPV6_CIDRS"
    VPN_CONNECTION_NOT_FOUND = "VPN_CONNECTION_NOT_FOUND"
    MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED = "MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED"
    DIRECT_CONNECT_GATEWAY_NOT_FOUND = "DIRECT_CONNECT_GATEWAY_NOT_FOUND"
    DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS = "DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS"
    DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF = "DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF"
    VPN_EXISTING_ASSOCIATIONS = "VPN_EXISTING_ASSOCIATIONS"
    VPC_UNSUPPORTED_FEATURES = "VPC_UNSUPPORTED_FEATURES"


class AttachmentState:
    """AttachmentState enum values."""

    REJECTED = "REJECTED"
    PENDING_ATTACHMENT_ACCEPTANCE = "PENDING_ATTACHMENT_ACCEPTANCE"
    CREATING = "CREATING"
    FAILED = "FAILED"
    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"
    PENDING_NETWORK_UPDATE = "PENDING_NETWORK_UPDATE"
    PENDING_TAG_ACCEPTANCE = "PENDING_TAG_ACCEPTANCE"
    DELETING = "DELETING"


class AttachmentType:
    """AttachmentType enum values."""

    CONNECT = "CONNECT"
    SITE_TO_SITE_VPN = "SITE_TO_SITE_VPN"
    VPC = "VPC"
    DIRECT_CONNECT_GATEWAY = "DIRECT_CONNECT_GATEWAY"
    TRANSIT_GATEWAY_ROUTE_TABLE = "TRANSIT_GATEWAY_ROUTE_TABLE"


class ChangeAction:
    """ChangeAction enum values."""

    ADD = "ADD"
    MODIFY = "MODIFY"
    REMOVE = "REMOVE"


class ChangeSetState:
    """ChangeSetState enum values."""

    PENDING_GENERATION = "PENDING_GENERATION"
    FAILED_GENERATION = "FAILED_GENERATION"
    READY_TO_EXECUTE = "READY_TO_EXECUTE"
    EXECUTING = "EXECUTING"
    EXECUTION_SUCCEEDED = "EXECUTION_SUCCEEDED"
    OUT_OF_DATE = "OUT_OF_DATE"


class ChangeStatus:
    """ChangeStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class ChangeType:
    """ChangeType enum values."""

    CORE_NETWORK_SEGMENT = "CORE_NETWORK_SEGMENT"
    NETWORK_FUNCTION_GROUP = "NETWORK_FUNCTION_GROUP"
    CORE_NETWORK_EDGE = "CORE_NETWORK_EDGE"
    ATTACHMENT_MAPPING = "ATTACHMENT_MAPPING"
    ATTACHMENT_ROUTE_PROPAGATION = "ATTACHMENT_ROUTE_PROPAGATION"
    ATTACHMENT_ROUTE_STATIC = "ATTACHMENT_ROUTE_STATIC"
    ROUTING_POLICY = "ROUTING_POLICY"
    ROUTING_POLICY_SEGMENT_ASSOCIATION = "ROUTING_POLICY_SEGMENT_ASSOCIATION"
    ROUTING_POLICY_EDGE_ASSOCIATION = "ROUTING_POLICY_EDGE_ASSOCIATION"
    ROUTING_POLICY_ATTACHMENT_ASSOCIATION = "ROUTING_POLICY_ATTACHMENT_ASSOCIATION"
    CORE_NETWORK_CONFIGURATION = "CORE_NETWORK_CONFIGURATION"
    SEGMENTS_CONFIGURATION = "SEGMENTS_CONFIGURATION"
    SEGMENT_ACTIONS_CONFIGURATION = "SEGMENT_ACTIONS_CONFIGURATION"
    ATTACHMENT_POLICIES_CONFIGURATION = "ATTACHMENT_POLICIES_CONFIGURATION"


class ConnectPeerAssociationState:
    """ConnectPeerAssociationState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DELETED = "DELETED"


class ConnectPeerErrorCode:
    """ConnectPeerErrorCode enum values."""

    EDGE_LOCATION_NO_FREE_IPS = "EDGE_LOCATION_NO_FREE_IPS"
    EDGE_LOCATION_PEER_DUPLICATE = "EDGE_LOCATION_PEER_DUPLICATE"
    SUBNET_NOT_FOUND = "SUBNET_NOT_FOUND"
    IP_OUTSIDE_SUBNET_CIDR_RANGE = "IP_OUTSIDE_SUBNET_CIDR_RANGE"
    INVALID_INSIDE_CIDR_BLOCK = "INVALID_INSIDE_CIDR_BLOCK"
    NO_ASSOCIATED_CIDR_BLOCK = "NO_ASSOCIATED_CIDR_BLOCK"


class ConnectPeerState:
    """ConnectPeerState enum values."""

    CREATING = "CREATING"
    FAILED = "FAILED"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"


class ConnectionState:
    """ConnectionState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    UP = "UP"
    DOWN = "DOWN"


class ConnectionType:
    """ConnectionType enum values."""

    BGP = "BGP"
    IPSEC = "IPSEC"


class CoreNetworkPolicyAlias:
    """CoreNetworkPolicyAlias enum values."""

    LIVE = "LIVE"
    LATEST = "LATEST"


class CoreNetworkState:
    """CoreNetworkState enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"


class CustomerGatewayAssociationState:
    """CustomerGatewayAssociationState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DELETED = "DELETED"


class DeviceState:
    """DeviceState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class GlobalNetworkState:
    """GlobalNetworkState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class LinkAssociationState:
    """LinkAssociationState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DELETED = "DELETED"


class LinkState:
    """LinkState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class PeeringErrorCode:
    """PeeringErrorCode enum values."""

    TRANSIT_GATEWAY_NOT_FOUND = "TRANSIT_GATEWAY_NOT_FOUND"
    TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED = "TRANSIT_GATEWAY_PEERS_LIMIT_EXCEEDED"
    MISSING_PERMISSIONS = "MISSING_PERMISSIONS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    EDGE_LOCATION_PEER_DUPLICATE = "EDGE_LOCATION_PEER_DUPLICATE"
    INVALID_TRANSIT_GATEWAY_STATE = "INVALID_TRANSIT_GATEWAY_STATE"


class PeeringState:
    """PeeringState enum values."""

    CREATING = "CREATING"
    FAILED = "FAILED"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"


class PeeringType:
    """PeeringType enum values."""

    TRANSIT_GATEWAY = "TRANSIT_GATEWAY"


class RouteAnalysisCompletionReasonCode:
    """RouteAnalysisCompletionReasonCode enum values."""

    TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND = "TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND"
    TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY = "TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY"
    CYCLIC_PATH_DETECTED = "CYCLIC_PATH_DETECTED"
    TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND = "TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND"
    ROUTE_NOT_FOUND = "ROUTE_NOT_FOUND"
    BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND = "BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND"
    INACTIVE_ROUTE_FOR_DESTINATION_FOUND = "INACTIVE_ROUTE_FOR_DESTINATION_FOUND"
    TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH = "TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH"
    MAX_HOPS_EXCEEDED = "MAX_HOPS_EXCEEDED"
    POSSIBLE_MIDDLEBOX = "POSSIBLE_MIDDLEBOX"
    NO_DESTINATION_ARN_PROVIDED = "NO_DESTINATION_ARN_PROVIDED"


class RouteAnalysisCompletionResultCode:
    """RouteAnalysisCompletionResultCode enum values."""

    CONNECTED = "CONNECTED"
    NOT_CONNECTED = "NOT_CONNECTED"


class RouteAnalysisStatus:
    """RouteAnalysisStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class RouteState:
    """RouteState enum values."""

    ACTIVE = "ACTIVE"
    BLACKHOLE = "BLACKHOLE"


class RouteTableType:
    """RouteTableType enum values."""

    TRANSIT_GATEWAY_ROUTE_TABLE = "TRANSIT_GATEWAY_ROUTE_TABLE"
    CORE_NETWORK_SEGMENT = "CORE_NETWORK_SEGMENT"
    NETWORK_FUNCTION_GROUP = "NETWORK_FUNCTION_GROUP"


class RouteType:
    """RouteType enum values."""

    PROPAGATED = "PROPAGATED"
    STATIC = "STATIC"


class RoutingPolicyDirection:
    """RoutingPolicyDirection enum values."""

    INBOUND = "inbound"
    OUTBOUND = "outbound"


class SegmentActionServiceInsertion:
    """SegmentActionServiceInsertion enum values."""

    SEND_VIA = "send-via"
    SEND_TO = "send-to"


class SendViaMode:
    """SendViaMode enum values."""

    DUAL_HOP = "dual-hop"
    SINGLE_HOP = "single-hop"


class SiteState:
    """SiteState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class TransitGatewayConnectPeerAssociationState:
    """TransitGatewayConnectPeerAssociationState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DELETED = "DELETED"


class TransitGatewayRegistrationState:
    """TransitGatewayRegistrationState enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED = "FAILED"


class TunnelProtocol:
    """TunnelProtocol enum values."""

    GRE = "GRE"
    NO_ENCAP = "NO_ENCAP"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "UnknownOperation"
    CANNOTPARSE = "CannotParse"
    FIELDVALIDATIONFAILED = "FieldValidationFailed"
    OTHER = "Other"


@dataclass
class ConnectAttachmentOptions(PropertyType):
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol": "Protocol",
    }

    protocol: Optional[Union[str, TunnelProtocol, Ref, GetAtt, Sub]] = None


@dataclass
class ProposedNetworkFunctionGroupChange(PropertyType):
    TAGS = "Tags"
    NETWORK_FUNCTION_GROUP_NAME = "NetworkFunctionGroupName"
    ATTACHMENT_POLICY_RULE_NUMBER = "AttachmentPolicyRuleNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tags": "Tags",
        "network_function_group_name": "NetworkFunctionGroupName",
        "attachment_policy_rule_number": "AttachmentPolicyRuleNumber",
    }

    tags: Optional[list[Tag]] = None
    network_function_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attachment_policy_rule_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ProposedSegmentChange(PropertyType):
    SEGMENT_NAME = "SegmentName"
    TAGS = "Tags"
    ATTACHMENT_POLICY_RULE_NUMBER = "AttachmentPolicyRuleNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_name": "SegmentName",
        "tags": "Tags",
        "attachment_policy_rule_number": "AttachmentPolicyRuleNumber",
    }

    segment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    attachment_policy_rule_number: Optional[Union[int, Ref, GetAtt, Sub]] = None

