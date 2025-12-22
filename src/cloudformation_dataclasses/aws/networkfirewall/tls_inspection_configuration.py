"""PropertyTypes for AWS::NetworkFirewall::TLSInspectionConfiguration."""

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
class Address(PropertyType):
    ADDRESS_DEFINITION = "AddressDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address_definition": "AddressDefinition",
    }

    address_definition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CheckCertificateRevocationStatus(PropertyType):
    UNKNOWN_STATUS_ACTION = "UnknownStatusAction"
    REVOKED_STATUS_ACTION = "RevokedStatusAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unknown_status_action": "UnknownStatusAction",
        "revoked_status_action": "RevokedStatusAction",
    }

    unknown_status_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revoked_status_action: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortRange(PropertyType):
    FROM_PORT = "FromPort"
    TO_PORT = "ToPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServerCertificate(PropertyType):
    RESOURCE_ARN = "ResourceArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerCertificateConfiguration(PropertyType):
    CERTIFICATE_AUTHORITY_ARN = "CertificateAuthorityArn"
    CHECK_CERTIFICATE_REVOCATION_STATUS = "CheckCertificateRevocationStatus"
    SCOPES = "Scopes"
    SERVER_CERTIFICATES = "ServerCertificates"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_authority_arn": "CertificateAuthorityArn",
        "check_certificate_revocation_status": "CheckCertificateRevocationStatus",
        "scopes": "Scopes",
        "server_certificates": "ServerCertificates",
    }

    certificate_authority_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    check_certificate_revocation_status: Optional[CheckCertificateRevocationStatus] = None
    scopes: Optional[list[ServerCertificateScope]] = None
    server_certificates: Optional[list[ServerCertificate]] = None


@dataclass
class ServerCertificateScope(PropertyType):
    PROTOCOLS = "Protocols"
    DESTINATION_PORTS = "DestinationPorts"
    DESTINATIONS = "Destinations"
    SOURCES = "Sources"
    SOURCE_PORTS = "SourcePorts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "protocols": "Protocols",
        "destination_ports": "DestinationPorts",
        "destinations": "Destinations",
        "sources": "Sources",
        "source_ports": "SourcePorts",
    }

    protocols: Optional[Union[list[int], Ref]] = None
    destination_ports: Optional[list[PortRange]] = None
    destinations: Optional[list[Address]] = None
    sources: Optional[list[Address]] = None
    source_ports: Optional[list[PortRange]] = None


@dataclass
class TLSInspectionConfiguration(PropertyType):
    SERVER_CERTIFICATE_CONFIGURATIONS = "ServerCertificateConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "server_certificate_configurations": "ServerCertificateConfigurations",
    }

    server_certificate_configurations: Optional[list[ServerCertificateConfiguration]] = None

