"""PropertyTypes for AWS::Lightsail::Container."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessDirection:
    """AccessDirection enum values."""

    INBOUND = "inbound"
    OUTBOUND = "outbound"


class AccessType:
    """AccessType enum values."""

    PUBLIC = "public"
    PRIVATE = "private"


class AccountLevelBpaSyncStatus:
    """AccountLevelBpaSyncStatus enum values."""

    INSYNC = "InSync"
    FAILED = "Failed"
    NEVERSYNCED = "NeverSynced"
    DEFAULTED = "Defaulted"


class AddOnType:
    """AddOnType enum values."""

    AUTOSNAPSHOT = "AutoSnapshot"
    STOPINSTANCEONIDLE = "StopInstanceOnIdle"


class AlarmState:
    """AlarmState enum values."""

    OK = "OK"
    ALARM = "ALARM"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class AppCategory:
    """AppCategory enum values."""

    LFR = "LfR"


class AutoMountStatus:
    """AutoMountStatus enum values."""

    FAILED = "Failed"
    PENDING = "Pending"
    MOUNTED = "Mounted"
    NOTMOUNTED = "NotMounted"


class AutoSnapshotStatus:
    """AutoSnapshotStatus enum values."""

    SUCCESS = "Success"
    FAILED = "Failed"
    INPROGRESS = "InProgress"
    NOTFOUND = "NotFound"


class BPAStatusMessage:
    """BPAStatusMessage enum values."""

    DEFAULTED_FOR_SLR_MISSING = "DEFAULTED_FOR_SLR_MISSING"
    SYNC_ON_HOLD = "SYNC_ON_HOLD"
    DEFAULTED_FOR_SLR_MISSING_ON_HOLD = "DEFAULTED_FOR_SLR_MISSING_ON_HOLD"
    UNKNOWN = "Unknown"


class BehaviorEnum:
    """BehaviorEnum enum values."""

    DONT_CACHE = "dont-cache"
    CACHE = "cache"


class BlueprintType:
    """BlueprintType enum values."""

    OS = "os"
    APP = "app"


class BucketMetricName:
    """BucketMetricName enum values."""

    BUCKETSIZEBYTES = "BucketSizeBytes"
    NUMBEROFOBJECTS = "NumberOfObjects"


class CertificateDomainValidationStatus:
    """CertificateDomainValidationStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class CertificateProvider:
    """CertificateProvider enum values."""

    LETSENCRYPT = "LetsEncrypt"


class CertificateStatus:
    """CertificateStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"


class CloudFormationStackRecordSourceType:
    """CloudFormationStackRecordSourceType enum values."""

    EXPORTSNAPSHOTRECORD = "ExportSnapshotRecord"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"


class ContactMethodStatus:
    """ContactMethodStatus enum values."""

    PENDINGVERIFICATION = "PendingVerification"
    VALID = "Valid"
    INVALID = "Invalid"


class ContactMethodVerificationProtocol:
    """ContactMethodVerificationProtocol enum values."""

    EMAIL = "Email"


class ContactProtocol:
    """ContactProtocol enum values."""

    EMAIL = "Email"
    SMS = "SMS"


class ContainerServiceDeploymentState:
    """ContainerServiceDeploymentState enum values."""

    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    FAILED = "FAILED"


class ContainerServiceMetricName:
    """ContainerServiceMetricName enum values."""

    CPUUTILIZATION = "CPUUtilization"
    MEMORYUTILIZATION = "MemoryUtilization"


class ContainerServicePowerName:
    """ContainerServicePowerName enum values."""

    NANO = "nano"
    MICRO = "micro"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    XLARGE = "xlarge"


class ContainerServiceProtocol:
    """ContainerServiceProtocol enum values."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"
    UDP = "UDP"


class ContainerServiceState:
    """ContainerServiceState enum values."""

    PENDING = "PENDING"
    READY = "READY"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DISABLED = "DISABLED"
    DEPLOYING = "DEPLOYING"


class ContainerServiceStateDetailCode:
    """ContainerServiceStateDetailCode enum values."""

    CREATING_SYSTEM_RESOURCES = "CREATING_SYSTEM_RESOURCES"
    CREATING_NETWORK_INFRASTRUCTURE = "CREATING_NETWORK_INFRASTRUCTURE"
    PROVISIONING_CERTIFICATE = "PROVISIONING_CERTIFICATE"
    PROVISIONING_SERVICE = "PROVISIONING_SERVICE"
    CREATING_DEPLOYMENT = "CREATING_DEPLOYMENT"
    EVALUATING_HEALTH_CHECK = "EVALUATING_HEALTH_CHECK"
    ACTIVATING_DEPLOYMENT = "ACTIVATING_DEPLOYMENT"
    CERTIFICATE_LIMIT_EXCEEDED = "CERTIFICATE_LIMIT_EXCEEDED"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"


class Currency:
    """Currency enum values."""

    USD = "USD"


class DiskSnapshotState:
    """DiskSnapshotState enum values."""

    PENDING = "pending"
    COMPLETED = "completed"
    ERROR = "error"
    UNKNOWN = "unknown"


class DiskState:
    """DiskState enum values."""

    PENDING = "pending"
    ERROR = "error"
    AVAILABLE = "available"
    IN_USE = "in-use"
    UNKNOWN = "unknown"


class DistributionMetricName:
    """DistributionMetricName enum values."""

    REQUESTS = "Requests"
    BYTESDOWNLOADED = "BytesDownloaded"
    BYTESUPLOADED = "BytesUploaded"
    TOTALERRORRATE = "TotalErrorRate"
    HTTP4XXERRORRATE = "Http4xxErrorRate"
    HTTP5XXERRORRATE = "Http5xxErrorRate"


class DnsRecordCreationStateCode:
    """DnsRecordCreationStateCode enum values."""

    SUCCEEDED = "SUCCEEDED"
    STARTED = "STARTED"
    FAILED = "FAILED"


class ExportSnapshotRecordSourceType:
    """ExportSnapshotRecordSourceType enum values."""

    INSTANCESNAPSHOT = "InstanceSnapshot"
    DISKSNAPSHOT = "DiskSnapshot"


class ForwardValues:
    """ForwardValues enum values."""

    NONE = "none"
    ALLOW_LIST = "allow-list"
    ALL = "all"


class HeaderEnum:
    """HeaderEnum enum values."""

    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_DATETIME = "Accept-Datetime"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    AUTHORIZATION = "Authorization"
    CLOUDFRONT_FORWARDED_PROTO = "CloudFront-Forwarded-Proto"
    CLOUDFRONT_IS_DESKTOP_VIEWER = "CloudFront-Is-Desktop-Viewer"
    CLOUDFRONT_IS_MOBILE_VIEWER = "CloudFront-Is-Mobile-Viewer"
    CLOUDFRONT_IS_SMARTTV_VIEWER = "CloudFront-Is-SmartTV-Viewer"
    CLOUDFRONT_IS_TABLET_VIEWER = "CloudFront-Is-Tablet-Viewer"
    CLOUDFRONT_VIEWER_COUNTRY = "CloudFront-Viewer-Country"
    HOST = "Host"
    ORIGIN = "Origin"
    REFERER = "Referer"


class HttpEndpoint:
    """HttpEndpoint enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class HttpProtocolIpv6:
    """HttpProtocolIpv6 enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class HttpTokens:
    """HttpTokens enum values."""

    OPTIONAL = "optional"
    REQUIRED = "required"


class InstanceAccessProtocol:
    """InstanceAccessProtocol enum values."""

    SSH = "ssh"
    RDP = "rdp"


class InstanceHealthReason:
    """InstanceHealthReason enum values."""

    LB_REGISTRATIONINPROGRESS = "Lb.RegistrationInProgress"
    LB_INITIALHEALTHCHECKING = "Lb.InitialHealthChecking"
    LB_INTERNALERROR = "Lb.InternalError"
    INSTANCE_RESPONSECODEMISMATCH = "Instance.ResponseCodeMismatch"
    INSTANCE_TIMEOUT = "Instance.Timeout"
    INSTANCE_FAILEDHEALTHCHECKS = "Instance.FailedHealthChecks"
    INSTANCE_NOTREGISTERED = "Instance.NotRegistered"
    INSTANCE_NOTINUSE = "Instance.NotInUse"
    INSTANCE_DEREGISTRATIONINPROGRESS = "Instance.DeregistrationInProgress"
    INSTANCE_INVALIDSTATE = "Instance.InvalidState"
    INSTANCE_IPUNUSABLE = "Instance.IpUnusable"


class InstanceHealthState:
    """InstanceHealthState enum values."""

    INITIAL = "initial"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNUSED = "unused"
    DRAINING = "draining"
    UNAVAILABLE = "unavailable"


class InstanceMetadataState:
    """InstanceMetadataState enum values."""

    PENDING = "pending"
    APPLIED = "applied"


class InstanceMetricName:
    """InstanceMetricName enum values."""

    CPUUTILIZATION = "CPUUtilization"
    NETWORKIN = "NetworkIn"
    NETWORKOUT = "NetworkOut"
    STATUSCHECKFAILED = "StatusCheckFailed"
    STATUSCHECKFAILED_INSTANCE = "StatusCheckFailed_Instance"
    STATUSCHECKFAILED_SYSTEM = "StatusCheckFailed_System"
    BURSTCAPACITYTIME = "BurstCapacityTime"
    BURSTCAPACITYPERCENTAGE = "BurstCapacityPercentage"
    METADATANOTOKEN = "MetadataNoToken"


class InstancePlatform:
    """InstancePlatform enum values."""

    LINUX_UNIX = "LINUX_UNIX"
    WINDOWS = "WINDOWS"


class InstanceSnapshotState:
    """InstanceSnapshotState enum values."""

    PENDING = "pending"
    ERROR = "error"
    AVAILABLE = "available"


class IpAddressType:
    """IpAddressType enum values."""

    DUALSTACK = "dualstack"
    IPV4 = "ipv4"
    IPV6 = "ipv6"


class LoadBalancerAttributeName:
    """LoadBalancerAttributeName enum values."""

    HEALTHCHECKPATH = "HealthCheckPath"
    SESSIONSTICKINESSENABLED = "SessionStickinessEnabled"
    SESSIONSTICKINESS_LB_COOKIEDURATIONSECONDS = "SessionStickiness_LB_CookieDurationSeconds"
    HTTPSREDIRECTIONENABLED = "HttpsRedirectionEnabled"
    TLSPOLICYNAME = "TlsPolicyName"


class LoadBalancerMetricName:
    """LoadBalancerMetricName enum values."""

    CLIENTTLSNEGOTIATIONERRORCOUNT = "ClientTLSNegotiationErrorCount"
    HEALTHYHOSTCOUNT = "HealthyHostCount"
    UNHEALTHYHOSTCOUNT = "UnhealthyHostCount"
    HTTPCODE_LB_4XX_COUNT = "HTTPCode_LB_4XX_Count"
    HTTPCODE_LB_5XX_COUNT = "HTTPCode_LB_5XX_Count"
    HTTPCODE_INSTANCE_2XX_COUNT = "HTTPCode_Instance_2XX_Count"
    HTTPCODE_INSTANCE_3XX_COUNT = "HTTPCode_Instance_3XX_Count"
    HTTPCODE_INSTANCE_4XX_COUNT = "HTTPCode_Instance_4XX_Count"
    HTTPCODE_INSTANCE_5XX_COUNT = "HTTPCode_Instance_5XX_Count"
    INSTANCERESPONSETIME = "InstanceResponseTime"
    REJECTEDCONNECTIONCOUNT = "RejectedConnectionCount"
    REQUESTCOUNT = "RequestCount"


class LoadBalancerProtocol:
    """LoadBalancerProtocol enum values."""

    HTTP_HTTPS = "HTTP_HTTPS"
    HTTP = "HTTP"


class LoadBalancerState:
    """LoadBalancerState enum values."""

    ACTIVE = "active"
    PROVISIONING = "provisioning"
    ACTIVE_IMPAIRED = "active_impaired"
    FAILED = "failed"
    UNKNOWN = "unknown"


class LoadBalancerTlsCertificateDnsRecordCreationStateCode:
    """LoadBalancerTlsCertificateDnsRecordCreationStateCode enum values."""

    SUCCEEDED = "SUCCEEDED"
    STARTED = "STARTED"
    FAILED = "FAILED"


class LoadBalancerTlsCertificateDomainStatus:
    """LoadBalancerTlsCertificateDomainStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class LoadBalancerTlsCertificateFailureReason:
    """LoadBalancerTlsCertificateFailureReason enum values."""

    NO_AVAILABLE_CONTACTS = "NO_AVAILABLE_CONTACTS"
    ADDITIONAL_VERIFICATION_REQUIRED = "ADDITIONAL_VERIFICATION_REQUIRED"
    DOMAIN_NOT_ALLOWED = "DOMAIN_NOT_ALLOWED"
    INVALID_PUBLIC_DOMAIN = "INVALID_PUBLIC_DOMAIN"
    OTHER = "OTHER"


class LoadBalancerTlsCertificateRenewalStatus:
    """LoadBalancerTlsCertificateRenewalStatus enum values."""

    PENDING_AUTO_RENEWAL = "PENDING_AUTO_RENEWAL"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class LoadBalancerTlsCertificateRevocationReason:
    """LoadBalancerTlsCertificateRevocationReason enum values."""

    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CA_COMPROMISE = "CA_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERCEDED = "SUPERCEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    CERTIFICATE_HOLD = "CERTIFICATE_HOLD"
    REMOVE_FROM_CRL = "REMOVE_FROM_CRL"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


class LoadBalancerTlsCertificateStatus:
    """LoadBalancerTlsCertificateStatus enum values."""

    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


class MetricName:
    """MetricName enum values."""

    CPUUTILIZATION = "CPUUtilization"
    NETWORKIN = "NetworkIn"
    NETWORKOUT = "NetworkOut"
    STATUSCHECKFAILED = "StatusCheckFailed"
    STATUSCHECKFAILED_INSTANCE = "StatusCheckFailed_Instance"
    STATUSCHECKFAILED_SYSTEM = "StatusCheckFailed_System"
    CLIENTTLSNEGOTIATIONERRORCOUNT = "ClientTLSNegotiationErrorCount"
    HEALTHYHOSTCOUNT = "HealthyHostCount"
    UNHEALTHYHOSTCOUNT = "UnhealthyHostCount"
    HTTPCODE_LB_4XX_COUNT = "HTTPCode_LB_4XX_Count"
    HTTPCODE_LB_5XX_COUNT = "HTTPCode_LB_5XX_Count"
    HTTPCODE_INSTANCE_2XX_COUNT = "HTTPCode_Instance_2XX_Count"
    HTTPCODE_INSTANCE_3XX_COUNT = "HTTPCode_Instance_3XX_Count"
    HTTPCODE_INSTANCE_4XX_COUNT = "HTTPCode_Instance_4XX_Count"
    HTTPCODE_INSTANCE_5XX_COUNT = "HTTPCode_Instance_5XX_Count"
    INSTANCERESPONSETIME = "InstanceResponseTime"
    REJECTEDCONNECTIONCOUNT = "RejectedConnectionCount"
    REQUESTCOUNT = "RequestCount"
    DATABASECONNECTIONS = "DatabaseConnections"
    DISKQUEUEDEPTH = "DiskQueueDepth"
    FREESTORAGESPACE = "FreeStorageSpace"
    NETWORKRECEIVETHROUGHPUT = "NetworkReceiveThroughput"
    NETWORKTRANSMITTHROUGHPUT = "NetworkTransmitThroughput"
    BURSTCAPACITYTIME = "BurstCapacityTime"
    BURSTCAPACITYPERCENTAGE = "BurstCapacityPercentage"


class MetricStatistic:
    """MetricStatistic enum values."""

    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    SUM = "Sum"
    AVERAGE = "Average"
    SAMPLECOUNT = "SampleCount"


class MetricUnit:
    """MetricUnit enum values."""

    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


class NameServersUpdateStateCode:
    """NameServersUpdateStateCode enum values."""

    SUCCEEDED = "SUCCEEDED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    STARTED = "STARTED"


class NetworkProtocol:
    """NetworkProtocol enum values."""

    TCP = "tcp"
    ALL = "all"
    UDP = "udp"
    ICMP = "icmp"
    ICMPV6 = "icmpv6"


class OperationStatus:
    """OperationStatus enum values."""

    NOTSTARTED = "NotStarted"
    STARTED = "Started"
    FAILED = "Failed"
    COMPLETED = "Completed"
    SUCCEEDED = "Succeeded"


class OperationType:
    """OperationType enum values."""

    DELETEKNOWNHOSTKEYS = "DeleteKnownHostKeys"
    DELETEINSTANCE = "DeleteInstance"
    CREATEINSTANCE = "CreateInstance"
    STOPINSTANCE = "StopInstance"
    STARTINSTANCE = "StartInstance"
    REBOOTINSTANCE = "RebootInstance"
    OPENINSTANCEPUBLICPORTS = "OpenInstancePublicPorts"
    PUTINSTANCEPUBLICPORTS = "PutInstancePublicPorts"
    CLOSEINSTANCEPUBLICPORTS = "CloseInstancePublicPorts"
    ALLOCATESTATICIP = "AllocateStaticIp"
    RELEASESTATICIP = "ReleaseStaticIp"
    ATTACHSTATICIP = "AttachStaticIp"
    DETACHSTATICIP = "DetachStaticIp"
    UPDATEDOMAINENTRY = "UpdateDomainEntry"
    DELETEDOMAINENTRY = "DeleteDomainEntry"
    CREATEDOMAIN = "CreateDomain"
    DELETEDOMAIN = "DeleteDomain"
    CREATEINSTANCESNAPSHOT = "CreateInstanceSnapshot"
    DELETEINSTANCESNAPSHOT = "DeleteInstanceSnapshot"
    CREATEINSTANCESFROMSNAPSHOT = "CreateInstancesFromSnapshot"
    CREATELOADBALANCER = "CreateLoadBalancer"
    DELETELOADBALANCER = "DeleteLoadBalancer"
    ATTACHINSTANCESTOLOADBALANCER = "AttachInstancesToLoadBalancer"
    DETACHINSTANCESFROMLOADBALANCER = "DetachInstancesFromLoadBalancer"
    UPDATELOADBALANCERATTRIBUTE = "UpdateLoadBalancerAttribute"
    CREATELOADBALANCERTLSCERTIFICATE = "CreateLoadBalancerTlsCertificate"
    DELETELOADBALANCERTLSCERTIFICATE = "DeleteLoadBalancerTlsCertificate"
    ATTACHLOADBALANCERTLSCERTIFICATE = "AttachLoadBalancerTlsCertificate"
    CREATEDISK = "CreateDisk"
    DELETEDISK = "DeleteDisk"
    ATTACHDISK = "AttachDisk"
    DETACHDISK = "DetachDisk"
    CREATEDISKSNAPSHOT = "CreateDiskSnapshot"
    DELETEDISKSNAPSHOT = "DeleteDiskSnapshot"
    CREATEDISKFROMSNAPSHOT = "CreateDiskFromSnapshot"
    CREATERELATIONALDATABASE = "CreateRelationalDatabase"
    UPDATERELATIONALDATABASE = "UpdateRelationalDatabase"
    DELETERELATIONALDATABASE = "DeleteRelationalDatabase"
    CREATERELATIONALDATABASEFROMSNAPSHOT = "CreateRelationalDatabaseFromSnapshot"
    CREATERELATIONALDATABASESNAPSHOT = "CreateRelationalDatabaseSnapshot"
    DELETERELATIONALDATABASESNAPSHOT = "DeleteRelationalDatabaseSnapshot"
    UPDATERELATIONALDATABASEPARAMETERS = "UpdateRelationalDatabaseParameters"
    STARTRELATIONALDATABASE = "StartRelationalDatabase"
    REBOOTRELATIONALDATABASE = "RebootRelationalDatabase"
    STOPRELATIONALDATABASE = "StopRelationalDatabase"
    ENABLEADDON = "EnableAddOn"
    DISABLEADDON = "DisableAddOn"
    PUTALARM = "PutAlarm"
    GETALARMS = "GetAlarms"
    DELETEALARM = "DeleteAlarm"
    TESTALARM = "TestAlarm"
    CREATECONTACTMETHOD = "CreateContactMethod"
    GETCONTACTMETHODS = "GetContactMethods"
    SENDCONTACTMETHODVERIFICATION = "SendContactMethodVerification"
    DELETECONTACTMETHOD = "DeleteContactMethod"
    CREATEDISTRIBUTION = "CreateDistribution"
    UPDATEDISTRIBUTION = "UpdateDistribution"
    DELETEDISTRIBUTION = "DeleteDistribution"
    RESETDISTRIBUTIONCACHE = "ResetDistributionCache"
    ATTACHCERTIFICATETODISTRIBUTION = "AttachCertificateToDistribution"
    DETACHCERTIFICATEFROMDISTRIBUTION = "DetachCertificateFromDistribution"
    UPDATEDISTRIBUTIONBUNDLE = "UpdateDistributionBundle"
    SETIPADDRESSTYPE = "SetIpAddressType"
    CREATECERTIFICATE = "CreateCertificate"
    DELETECERTIFICATE = "DeleteCertificate"
    CREATECONTAINERSERVICE = "CreateContainerService"
    UPDATECONTAINERSERVICE = "UpdateContainerService"
    DELETECONTAINERSERVICE = "DeleteContainerService"
    CREATECONTAINERSERVICEDEPLOYMENT = "CreateContainerServiceDeployment"
    CREATECONTAINERSERVICEREGISTRYLOGIN = "CreateContainerServiceRegistryLogin"
    REGISTERCONTAINERIMAGE = "RegisterContainerImage"
    DELETECONTAINERIMAGE = "DeleteContainerImage"
    CREATEBUCKET = "CreateBucket"
    DELETEBUCKET = "DeleteBucket"
    CREATEBUCKETACCESSKEY = "CreateBucketAccessKey"
    DELETEBUCKETACCESSKEY = "DeleteBucketAccessKey"
    UPDATEBUCKETBUNDLE = "UpdateBucketBundle"
    UPDATEBUCKET = "UpdateBucket"
    SETRESOURCEACCESSFORBUCKET = "SetResourceAccessForBucket"
    UPDATEINSTANCEMETADATAOPTIONS = "UpdateInstanceMetadataOptions"
    STARTGUISESSION = "StartGUISession"
    STOPGUISESSION = "StopGUISession"
    SETUPINSTANCEHTTPS = "SetupInstanceHttps"


class OriginProtocolPolicyEnum:
    """OriginProtocolPolicyEnum enum values."""

    HTTP_ONLY = "http-only"
    HTTPS_ONLY = "https-only"


class PortAccessType:
    """PortAccessType enum values."""

    PUBLIC = "Public"
    PRIVATE = "Private"


class PortInfoSourceType:
    """PortInfoSourceType enum values."""

    DEFAULT = "DEFAULT"
    INSTANCE = "INSTANCE"
    NONE = "NONE"
    CLOSED = "CLOSED"


class PortState:
    """PortState enum values."""

    OPEN = "open"
    CLOSED = "closed"


class PricingUnit:
    """PricingUnit enum values."""

    GB = "GB"
    HRS = "Hrs"
    GB_MO = "GB-Mo"
    BUNDLES = "Bundles"
    QUERIES = "Queries"


class R53HostedZoneDeletionStateCode:
    """R53HostedZoneDeletionStateCode enum values."""

    SUCCEEDED = "SUCCEEDED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    STARTED = "STARTED"


class RecordState:
    """RecordState enum values."""

    STARTED = "Started"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class RegionName:
    """RegionName enum values."""

    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    EU_WEST_3 = "eu-west-3"
    EU_CENTRAL_1 = "eu-central-1"
    CA_CENTRAL_1 = "ca-central-1"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    EU_NORTH_1 = "eu-north-1"
    AP_SOUTHEAST_3 = "ap-southeast-3"


class RelationalDatabaseEngine:
    """RelationalDatabaseEngine enum values."""

    MYSQL = "mysql"


class RelationalDatabaseMetricName:
    """RelationalDatabaseMetricName enum values."""

    CPUUTILIZATION = "CPUUtilization"
    DATABASECONNECTIONS = "DatabaseConnections"
    DISKQUEUEDEPTH = "DiskQueueDepth"
    FREESTORAGESPACE = "FreeStorageSpace"
    NETWORKRECEIVETHROUGHPUT = "NetworkReceiveThroughput"
    NETWORKTRANSMITTHROUGHPUT = "NetworkTransmitThroughput"


class RelationalDatabasePasswordVersion:
    """RelationalDatabasePasswordVersion enum values."""

    CURRENT = "CURRENT"
    PREVIOUS = "PREVIOUS"
    PENDING = "PENDING"


class RenewalStatus:
    """RenewalStatus enum values."""

    PENDINGAUTORENEWAL = "PendingAutoRenewal"
    PENDINGVALIDATION = "PendingValidation"
    SUCCESS = "Success"
    FAILED = "Failed"


class ResourceBucketAccess:
    """ResourceBucketAccess enum values."""

    ALLOW = "allow"
    DENY = "deny"


class ResourceType:
    """ResourceType enum values."""

    CONTAINERSERVICE = "ContainerService"
    INSTANCE = "Instance"
    STATICIP = "StaticIp"
    KEYPAIR = "KeyPair"
    INSTANCESNAPSHOT = "InstanceSnapshot"
    DOMAIN = "Domain"
    PEEREDVPC = "PeeredVpc"
    LOADBALANCER = "LoadBalancer"
    LOADBALANCERTLSCERTIFICATE = "LoadBalancerTlsCertificate"
    DISK = "Disk"
    DISKSNAPSHOT = "DiskSnapshot"
    RELATIONALDATABASE = "RelationalDatabase"
    RELATIONALDATABASESNAPSHOT = "RelationalDatabaseSnapshot"
    EXPORTSNAPSHOTRECORD = "ExportSnapshotRecord"
    CLOUDFORMATIONSTACKRECORD = "CloudFormationStackRecord"
    ALARM = "Alarm"
    CONTACTMETHOD = "ContactMethod"
    DISTRIBUTION = "Distribution"
    CERTIFICATE = "Certificate"
    BUCKET = "Bucket"


class SetupStatus:
    """SetupStatus enum values."""

    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INPROGRESS = "inProgress"


class Status:
    """Status enum values."""

    STARTEXPIRED = "startExpired"
    NOTSTARTED = "notStarted"
    STARTED = "started"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"
    SETTINGUPINSTANCE = "settingUpInstance"
    FAILEDINSTANCECREATION = "failedInstanceCreation"
    FAILEDSTARTINGGUISESSION = "failedStartingGUISession"
    FAILEDSTOPPINGGUISESSION = "failedStoppingGUISession"


class StatusType:
    """StatusType enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class TreatMissingData:
    """TreatMissingData enum values."""

    BREACHING = "breaching"
    NOTBREACHING = "notBreaching"
    IGNORE = "ignore"
    MISSING = "missing"


class ViewerMinimumTlsProtocolVersionEnum:
    """ViewerMinimumTlsProtocolVersionEnum enum values."""

    TLSV1_1_2016 = "TLSv1.1_2016"
    TLSV1_2_2018 = "TLSv1.2_2018"
    TLSV1_2_2019 = "TLSv1.2_2019"
    TLSV1_2_2021 = "TLSv1.2_2021"


@dataclass
class Container(PropertyType):
    CONTAINER_NAME = "ContainerName"
    COMMAND = "Command"
    ENVIRONMENT = "Environment"
    PORTS = "Ports"
    IMAGE = "Image"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "command": "Command",
        "environment": "Environment",
        "ports": "Ports",
        "image": "Image",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    command: Optional[Union[list[str], Ref]] = None
    environment: Optional[list[EnvironmentVariable]] = None
    ports: Optional[list[PortInfo]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContainerServiceDeployment(PropertyType):
    CONTAINERS = "Containers"
    PUBLIC_ENDPOINT = "PublicEndpoint"

    _property_mappings: ClassVar[dict[str, str]] = {
        "containers": "Containers",
        "public_endpoint": "PublicEndpoint",
    }

    containers: Optional[list[Container]] = None
    public_endpoint: Optional[PublicEndpoint] = None


@dataclass
class EcrImagePullerRole(PropertyType):
    PRINCIPAL_ARN = "PrincipalArn"
    IS_ACTIVE = "IsActive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "principal_arn": "PrincipalArn",
        "is_active": "IsActive",
    }

    principal_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_active: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentVariable(PropertyType):
    VARIABLE = "Variable"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "variable": "Variable",
        "value": "Value",
    }

    variable: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckConfig(PropertyType):
    PATH = "Path"
    TIMEOUT_SECONDS = "TimeoutSeconds"
    SUCCESS_CODES = "SuccessCodes"
    UNHEALTHY_THRESHOLD = "UnhealthyThreshold"
    HEALTHY_THRESHOLD = "HealthyThreshold"
    INTERVAL_SECONDS = "IntervalSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "timeout_seconds": "TimeoutSeconds",
        "success_codes": "SuccessCodes",
        "unhealthy_threshold": "UnhealthyThreshold",
        "healthy_threshold": "HealthyThreshold",
        "interval_seconds": "IntervalSeconds",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    success_codes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unhealthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    healthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PortInfo(PropertyType):
    PORT = "Port"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "protocol": "Protocol",
    }

    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateRegistryAccess(PropertyType):
    ECR_IMAGE_PULLER_ROLE = "EcrImagePullerRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ecr_image_puller_role": "EcrImagePullerRole",
    }

    ecr_image_puller_role: Optional[EcrImagePullerRole] = None


@dataclass
class PublicDomainName(PropertyType):
    CERTIFICATE_NAME = "CertificateName"
    DOMAIN_NAMES = "DomainNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_name": "CertificateName",
        "domain_names": "DomainNames",
    }

    certificate_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_names: Optional[Union[list[str], Ref]] = None


@dataclass
class PublicEndpoint(PropertyType):
    CONTAINER_NAME = "ContainerName"
    CONTAINER_PORT = "ContainerPort"
    HEALTH_CHECK_CONFIG = "HealthCheckConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "container_port": "ContainerPort",
        "health_check_config": "HealthCheckConfig",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    health_check_config: Optional[HealthCheckConfig] = None

