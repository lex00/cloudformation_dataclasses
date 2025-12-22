"""PropertyTypes for AWS::NetworkFirewall::VpcEndpointAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AttachmentStatus:
    """AttachmentStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    ERROR = "ERROR"
    SCALING = "SCALING"
    READY = "READY"


class ConfigurationSyncState:
    """ConfigurationSyncState enum values."""

    PENDING = "PENDING"
    IN_SYNC = "IN_SYNC"
    CAPACITY_CONSTRAINED = "CAPACITY_CONSTRAINED"


class EnabledAnalysisType:
    """EnabledAnalysisType enum values."""

    TLS_SNI = "TLS_SNI"
    HTTP_HOST = "HTTP_HOST"


class EncryptionType:
    """EncryptionType enum values."""

    CUSTOMER_KMS = "CUSTOMER_KMS"
    AWS_OWNED_KMS_KEY = "AWS_OWNED_KMS_KEY"


class FirewallStatusValue:
    """FirewallStatusValue enum values."""

    PROVISIONING = "PROVISIONING"
    DELETING = "DELETING"
    READY = "READY"


class FlowOperationStatus:
    """FlowOperationStatus enum values."""

    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"


class FlowOperationType:
    """FlowOperationType enum values."""

    FLOW_FLUSH = "FLOW_FLUSH"
    FLOW_CAPTURE = "FLOW_CAPTURE"


class GeneratedRulesType:
    """GeneratedRulesType enum values."""

    ALLOWLIST = "ALLOWLIST"
    DENYLIST = "DENYLIST"
    REJECTLIST = "REJECTLIST"
    ALERTLIST = "ALERTLIST"


class IPAddressType:
    """IPAddressType enum values."""

    DUALSTACK = "DUALSTACK"
    IPV4 = "IPV4"
    IPV6 = "IPV6"


class IdentifiedType:
    """IdentifiedType enum values."""

    STATELESS_RULE_FORWARDING_ASYMMETRICALLY = "STATELESS_RULE_FORWARDING_ASYMMETRICALLY"
    STATELESS_RULE_CONTAINS_TCP_FLAGS = "STATELESS_RULE_CONTAINS_TCP_FLAGS"


class ListenerPropertyType:
    """ListenerPropertyType enum values."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"


class LogDestinationType:
    """LogDestinationType enum values."""

    S3 = "S3"
    CLOUDWATCHLOGS = "CloudWatchLogs"
    KINESISDATAFIREHOSE = "KinesisDataFirehose"


class LogType:
    """LogType enum values."""

    ALERT = "ALERT"
    FLOW = "FLOW"
    TLS = "TLS"


class OverrideAction:
    """OverrideAction enum values."""

    DROP_TO_ALERT = "DROP_TO_ALERT"


class PerObjectSyncStatus:
    """PerObjectSyncStatus enum values."""

    PENDING = "PENDING"
    IN_SYNC = "IN_SYNC"
    CAPACITY_CONSTRAINED = "CAPACITY_CONSTRAINED"
    NOT_SUBSCRIBED = "NOT_SUBSCRIBED"
    DEPRECATED = "DEPRECATED"


class ProxyModifyState:
    """ProxyModifyState enum values."""

    MODIFYING = "MODIFYING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ProxyRulePhaseAction:
    """ProxyRulePhaseAction enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"
    ALERT = "ALERT"


class ProxyState:
    """ProxyState enum values."""

    ATTACHING = "ATTACHING"
    ATTACHED = "ATTACHED"
    DETACHING = "DETACHING"
    DETACHED = "DETACHED"
    ATTACH_FAILED = "ATTACH_FAILED"
    DETACH_FAILED = "DETACH_FAILED"


class ResourceManagedStatus:
    """ResourceManagedStatus enum values."""

    MANAGED = "MANAGED"
    ACCOUNT = "ACCOUNT"


class ResourceManagedType:
    """ResourceManagedType enum values."""

    AWS_MANAGED_THREAT_SIGNATURES = "AWS_MANAGED_THREAT_SIGNATURES"
    AWS_MANAGED_DOMAIN_LISTS = "AWS_MANAGED_DOMAIN_LISTS"
    ACTIVE_THREAT_DEFENSE = "ACTIVE_THREAT_DEFENSE"
    PARTNER_MANAGED = "PARTNER_MANAGED"


class ResourceStatus:
    """ResourceStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    ERROR = "ERROR"


class RevocationCheckAction:
    """RevocationCheckAction enum values."""

    PASS = "PASS"
    DROP = "DROP"
    REJECT = "REJECT"


class RuleGroupRequestPhase:
    """RuleGroupRequestPhase enum values."""

    PRE_DNS = "PRE_DNS"
    PRE_REQ = "PRE_REQ"
    POST_RES = "POST_RES"


class RuleGroupType:
    """RuleGroupType enum values."""

    STATELESS = "STATELESS"
    STATEFUL = "STATEFUL"


class RuleOrder:
    """RuleOrder enum values."""

    DEFAULT_ACTION_ORDER = "DEFAULT_ACTION_ORDER"
    STRICT_ORDER = "STRICT_ORDER"


class StatefulAction:
    """StatefulAction enum values."""

    PASS = "PASS"
    DROP = "DROP"
    ALERT = "ALERT"
    REJECT = "REJECT"


class StatefulRuleDirection:
    """StatefulRuleDirection enum values."""

    FORWARD = "FORWARD"
    ANY = "ANY"


class StatefulRuleProtocol:
    """StatefulRuleProtocol enum values."""

    IP = "IP"
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"
    HTTP = "HTTP"
    FTP = "FTP"
    TLS = "TLS"
    SMB = "SMB"
    DNS = "DNS"
    DCERPC = "DCERPC"
    SSH = "SSH"
    SMTP = "SMTP"
    IMAP = "IMAP"
    MSN = "MSN"
    KRB5 = "KRB5"
    IKEV2 = "IKEV2"
    TFTP = "TFTP"
    NTP = "NTP"
    DHCP = "DHCP"
    HTTP2 = "HTTP2"
    QUIC = "QUIC"


class StreamExceptionPolicy:
    """StreamExceptionPolicy enum values."""

    DROP = "DROP"
    CONTINUE = "CONTINUE"
    REJECT = "REJECT"


class SubscriptionStatus:
    """SubscriptionStatus enum values."""

    NOT_SUBSCRIBED = "NOT_SUBSCRIBED"
    SUBSCRIBED = "SUBSCRIBED"


class SummaryRuleOption:
    """SummaryRuleOption enum values."""

    SID = "SID"
    MSG = "MSG"
    METADATA = "METADATA"


class TCPFlag:
    """TCPFlag enum values."""

    FIN = "FIN"
    SYN = "SYN"
    RST = "RST"
    PSH = "PSH"
    ACK = "ACK"
    URG = "URG"
    ECE = "ECE"
    CWR = "CWR"


class TargetType:
    """TargetType enum values."""

    TLS_SNI = "TLS_SNI"
    HTTP_HOST = "HTTP_HOST"


class TlsInterceptMode:
    """TlsInterceptMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TransitGatewayAttachmentStatus:
    """TransitGatewayAttachmentStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED = "FAILED"
    ERROR = "ERROR"
    READY = "READY"
    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    REJECTING = "REJECTING"
    REJECTED = "REJECTED"


@dataclass
class SubnetMapping(PropertyType):
    IP_ADDRESS_TYPE = "IPAddressType"
    SUBNET_ID = "SubnetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IPAddressType",
        "subnet_id": "SubnetId",
    }

    ip_address_type: Optional[Union[str, IPAddressType, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

