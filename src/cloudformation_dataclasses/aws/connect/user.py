"""PropertyTypes for AWS::Connect::User."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessType:
    """AccessType enum values."""

    ALLOW = "ALLOW"


class ActionType:
    """ActionType enum values."""

    CREATE_TASK = "CREATE_TASK"
    ASSIGN_CONTACT_CATEGORY = "ASSIGN_CONTACT_CATEGORY"
    GENERATE_EVENTBRIDGE_EVENT = "GENERATE_EVENTBRIDGE_EVENT"
    SEND_NOTIFICATION = "SEND_NOTIFICATION"
    CREATE_CASE = "CREATE_CASE"
    UPDATE_CASE = "UPDATE_CASE"
    ASSIGN_SLA = "ASSIGN_SLA"
    END_ASSOCIATED_TASKS = "END_ASSOCIATED_TASKS"
    SUBMIT_AUTO_EVALUATION = "SUBMIT_AUTO_EVALUATION"


class AgentAvailabilityTimer:
    """AgentAvailabilityTimer enum values."""

    TIME_SINCE_LAST_ACTIVITY = "TIME_SINCE_LAST_ACTIVITY"
    TIME_SINCE_LAST_INBOUND = "TIME_SINCE_LAST_INBOUND"


class AgentStatusState:
    """AgentStatusState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AgentStatusType:
    """AgentStatusType enum values."""

    ROUTABLE = "ROUTABLE"
    CUSTOM = "CUSTOM"
    OFFLINE = "OFFLINE"


class AiUseCase:
    """AiUseCase enum values."""

    AGENTASSISTANCE = "AgentAssistance"
    SELFSERVICE = "SelfService"


class AllowedUserAction:
    """AllowedUserAction enum values."""

    CALL = "CALL"
    DISCARD = "DISCARD"


class AnsweringMachineDetectionStatus:
    """AnsweringMachineDetectionStatus enum values."""

    ANSWERED = "ANSWERED"
    UNDETECTED = "UNDETECTED"
    ERROR = "ERROR"
    HUMAN_ANSWERED = "HUMAN_ANSWERED"
    SIT_TONE_DETECTED = "SIT_TONE_DETECTED"
    SIT_TONE_BUSY = "SIT_TONE_BUSY"
    SIT_TONE_INVALID_NUMBER = "SIT_TONE_INVALID_NUMBER"
    FAX_MACHINE_DETECTED = "FAX_MACHINE_DETECTED"
    VOICEMAIL_BEEP = "VOICEMAIL_BEEP"
    VOICEMAIL_NO_BEEP = "VOICEMAIL_NO_BEEP"
    AMD_UNRESOLVED = "AMD_UNRESOLVED"
    AMD_UNANSWERED = "AMD_UNANSWERED"
    AMD_ERROR = "AMD_ERROR"
    AMD_NOT_APPLICABLE = "AMD_NOT_APPLICABLE"


class ApplicationType:
    """ApplicationType enum values."""

    MCP = "MCP"
    THIRD_PARTY_APPLICATION = "THIRD_PARTY_APPLICATION"


class ArtifactStatus:
    """ArtifactStatus enum values."""

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    IN_PROGRESS = "IN_PROGRESS"


class AttachedFileInvalidRequestExceptionReason:
    """AttachedFileInvalidRequestExceptionReason enum values."""

    INVALID_FILE_SIZE = "INVALID_FILE_SIZE"
    INVALID_FILE_TYPE = "INVALID_FILE_TYPE"
    INVALID_FILE_NAME = "INVALID_FILE_NAME"


class AttachedFileServiceQuotaExceededExceptionReason:
    """AttachedFileServiceQuotaExceededExceptionReason enum values."""

    TOTAL_FILE_SIZE_EXCEEDED = "TOTAL_FILE_SIZE_EXCEEDED"
    TOTAL_FILE_COUNT_EXCEEDED = "TOTAL_FILE_COUNT_EXCEEDED"


class AutoEvaluationStatus:
    """AutoEvaluationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class BehaviorType:
    """BehaviorType enum values."""

    ROUTE_CURRENT_CHANNEL_ONLY = "ROUTE_CURRENT_CHANNEL_ONLY"
    ROUTE_ANY_CHANNEL = "ROUTE_ANY_CHANNEL"


class BooleanComparisonType:
    """BooleanComparisonType enum values."""

    IS_TRUE = "IS_TRUE"
    IS_FALSE = "IS_FALSE"


class Channel:
    """Channel enum values."""

    VOICE = "VOICE"
    CHAT = "CHAT"
    TASK = "TASK"
    EMAIL = "EMAIL"


class ChatEventType:
    """ChatEventType enum values."""

    DISCONNECT = "DISCONNECT"
    MESSAGE = "MESSAGE"
    EVENT = "EVENT"


class Comparison:
    """Comparison enum values."""

    LT = "LT"


class ContactFlowModuleState:
    """ContactFlowModuleState enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class ContactFlowModuleStatus:
    """ContactFlowModuleStatus enum values."""

    PUBLISHED = "PUBLISHED"
    SAVED = "SAVED"


class ContactFlowState:
    """ContactFlowState enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class ContactFlowStatus:
    """ContactFlowStatus enum values."""

    PUBLISHED = "PUBLISHED"
    SAVED = "SAVED"


class ContactFlowType:
    """ContactFlowType enum values."""

    CONTACT_FLOW = "CONTACT_FLOW"
    CUSTOMER_QUEUE = "CUSTOMER_QUEUE"
    CUSTOMER_HOLD = "CUSTOMER_HOLD"
    CUSTOMER_WHISPER = "CUSTOMER_WHISPER"
    AGENT_HOLD = "AGENT_HOLD"
    AGENT_WHISPER = "AGENT_WHISPER"
    OUTBOUND_WHISPER = "OUTBOUND_WHISPER"
    AGENT_TRANSFER = "AGENT_TRANSFER"
    QUEUE_TRANSFER = "QUEUE_TRANSFER"
    CAMPAIGN = "CAMPAIGN"


class ContactInitiationMethod:
    """ContactInitiationMethod enum values."""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    TRANSFER = "TRANSFER"
    QUEUE_TRANSFER = "QUEUE_TRANSFER"
    CALLBACK = "CALLBACK"
    API = "API"
    DISCONNECT = "DISCONNECT"
    MONITOR = "MONITOR"
    EXTERNAL_OUTBOUND = "EXTERNAL_OUTBOUND"
    WEBRTC_API = "WEBRTC_API"
    AGENT_REPLY = "AGENT_REPLY"
    FLOW = "FLOW"


class ContactInteractionType:
    """ContactInteractionType enum values."""

    AGENT = "AGENT"
    AUTOMATED = "AUTOMATED"


class ContactMediaProcessingFailureMode:
    """ContactMediaProcessingFailureMode enum values."""

    DELIVER_UNPROCESSED_MESSAGE = "DELIVER_UNPROCESSED_MESSAGE"
    DO_NOT_DELIVER_UNPROCESSED_MESSAGE = "DO_NOT_DELIVER_UNPROCESSED_MESSAGE"


class ContactMetricName:
    """ContactMetricName enum values."""

    POSITION_IN_QUEUE = "POSITION_IN_QUEUE"


class ContactParticipantRole:
    """ContactParticipantRole enum values."""

    AGENT = "AGENT"
    SYSTEM = "SYSTEM"
    CUSTOM_BOT = "CUSTOM_BOT"


class ContactRecordingType:
    """ContactRecordingType enum values."""

    AGENT = "AGENT"
    IVR = "IVR"
    SCREEN = "SCREEN"


class ContactState:
    """ContactState enum values."""

    INCOMING = "INCOMING"
    PENDING = "PENDING"
    CONNECTING = "CONNECTING"
    CONNECTED = "CONNECTED"
    CONNECTED_ONHOLD = "CONNECTED_ONHOLD"
    MISSED = "MISSED"
    ERROR = "ERROR"
    ENDED = "ENDED"
    REJECTED = "REJECTED"


class CurrentMetricName:
    """CurrentMetricName enum values."""

    AGENTS_ONLINE = "AGENTS_ONLINE"
    AGENTS_AVAILABLE = "AGENTS_AVAILABLE"
    AGENTS_ON_CALL = "AGENTS_ON_CALL"
    AGENTS_NON_PRODUCTIVE = "AGENTS_NON_PRODUCTIVE"
    AGENTS_AFTER_CONTACT_WORK = "AGENTS_AFTER_CONTACT_WORK"
    AGENTS_ERROR = "AGENTS_ERROR"
    AGENTS_STAFFED = "AGENTS_STAFFED"
    CONTACTS_IN_QUEUE = "CONTACTS_IN_QUEUE"
    OLDEST_CONTACT_AGE = "OLDEST_CONTACT_AGE"
    CONTACTS_SCHEDULED = "CONTACTS_SCHEDULED"
    AGENTS_ON_CONTACT = "AGENTS_ON_CONTACT"
    SLOTS_ACTIVE = "SLOTS_ACTIVE"
    SLOTS_AVAILABLE = "SLOTS_AVAILABLE"


class DataTableAttributeValueType:
    """DataTableAttributeValueType enum values."""

    TEXT = "TEXT"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    TEXT_LIST = "TEXT_LIST"
    NUMBER_LIST = "NUMBER_LIST"


class DataTableLockLevel:
    """DataTableLockLevel enum values."""

    NONE = "NONE"
    DATA_TABLE = "DATA_TABLE"
    PRIMARY_VALUE = "PRIMARY_VALUE"
    ATTRIBUTE = "ATTRIBUTE"
    VALUE = "VALUE"


class DataTableStatus:
    """DataTableStatus enum values."""

    PUBLISHED = "PUBLISHED"


class DateComparisonType:
    """DateComparisonType enum values."""

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"


class DateTimeComparisonType:
    """DateTimeComparisonType enum values."""

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    RANGE = "RANGE"


class DecimalComparisonType:
    """DecimalComparisonType enum values."""

    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    GREATER = "GREATER"
    LESSER_OR_EQUAL = "LESSER_OR_EQUAL"
    LESSER = "LESSER"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    RANGE = "RANGE"


class DeviceType:
    """DeviceType enum values."""

    GCM = "GCM"
    APNS = "APNS"
    APNS_SANDBOX = "APNS_SANDBOX"


class DirectoryType:
    """DirectoryType enum values."""

    SAML = "SAML"
    CONNECT_MANAGED = "CONNECT_MANAGED"
    EXISTING_DIRECTORY = "EXISTING_DIRECTORY"


class DisconnectOnCustomerExitParticipantType:
    """DisconnectOnCustomerExitParticipantType enum values."""

    AGENT = "AGENT"


class EmailHeaderType:
    """EmailHeaderType enum values."""

    REFERENCES = "REFERENCES"
    MESSAGE_ID = "MESSAGE_ID"
    IN_REPLY_TO = "IN_REPLY_TO"
    X_SES_SPAM_VERDICT = "X_SES_SPAM_VERDICT"
    X_SES_VIRUS_VERDICT = "X_SES_VIRUS_VERDICT"


class EncryptionType:
    """EncryptionType enum values."""

    KMS = "KMS"


class EndpointType:
    """EndpointType enum values."""

    TELEPHONE_NUMBER = "TELEPHONE_NUMBER"
    VOIP = "VOIP"
    CONTACT_FLOW = "CONTACT_FLOW"
    CONNECT_PHONENUMBER_ARN = "CONNECT_PHONENUMBER_ARN"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"


class EntityType:
    """EntityType enum values."""

    USER = "USER"
    AI_AGENT = "AI_AGENT"


class EvaluationFormItemEnablementAction:
    """EvaluationFormItemEnablementAction enum values."""

    DISABLE = "DISABLE"
    ENABLE = "ENABLE"


class EvaluationFormItemEnablementOperator:
    """EvaluationFormItemEnablementOperator enum values."""

    OR = "OR"
    AND = "AND"


class EvaluationFormItemEnablementSourceType:
    """EvaluationFormItemEnablementSourceType enum values."""

    QUESTION_REF_ID = "QUESTION_REF_ID"


class EvaluationFormItemEnablementSourceValueType:
    """EvaluationFormItemEnablementSourceValueType enum values."""

    OPTION_REF_ID = "OPTION_REF_ID"


class EvaluationFormItemSourceValuesComparator:
    """EvaluationFormItemSourceValuesComparator enum values."""

    IN = "IN"
    NOT_IN = "NOT_IN"
    ALL_IN = "ALL_IN"
    EXACT = "EXACT"


class EvaluationFormLanguageCode:
    """EvaluationFormLanguageCode enum values."""

    DE_DE = "de-DE"
    EN_US = "en-US"
    ES_ES = "es-ES"
    FR_FR = "fr-FR"
    IT_IT = "it-IT"
    PT_BR = "pt-BR"


class EvaluationFormMultiSelectQuestionDisplayMode:
    """EvaluationFormMultiSelectQuestionDisplayMode enum values."""

    DROPDOWN = "DROPDOWN"
    CHECKBOX = "CHECKBOX"


class EvaluationFormQuestionAutomationAnswerSourceType:
    """EvaluationFormQuestionAutomationAnswerSourceType enum values."""

    CONTACT_LENS_DATA = "CONTACT_LENS_DATA"
    GEN_AI = "GEN_AI"


class EvaluationFormQuestionType:
    """EvaluationFormQuestionType enum values."""

    TEXT = "TEXT"
    SINGLESELECT = "SINGLESELECT"
    NUMERIC = "NUMERIC"
    MULTISELECT = "MULTISELECT"
    DATETIME = "DATETIME"


class EvaluationFormScoringMode:
    """EvaluationFormScoringMode enum values."""

    QUESTION_ONLY = "QUESTION_ONLY"
    SECTION_ONLY = "SECTION_ONLY"


class EvaluationFormScoringStatus:
    """EvaluationFormScoringStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EvaluationFormSingleSelectQuestionDisplayMode:
    """EvaluationFormSingleSelectQuestionDisplayMode enum values."""

    DROPDOWN = "DROPDOWN"
    RADIO = "RADIO"


class EvaluationFormVersionStatus:
    """EvaluationFormVersionStatus enum values."""

    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"


class EvaluationQuestionAnswerAnalysisType:
    """EvaluationQuestionAnswerAnalysisType enum values."""

    CONTACT_LENS_DATA = "CONTACT_LENS_DATA"
    GEN_AI = "GEN_AI"


class EvaluationStatus:
    """EvaluationStatus enum values."""

    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"


class EvaluationSuggestedAnswerStatus:
    """EvaluationSuggestedAnswerStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class EvaluationTranscriptType:
    """EvaluationTranscriptType enum values."""

    RAW = "RAW"
    REDACTED = "REDACTED"


class EvaluationType:
    """EvaluationType enum values."""

    STANDARD = "STANDARD"
    CALIBRATION = "CALIBRATION"


class EventSourceName:
    """EventSourceName enum values."""

    ONPOSTCALLANALYSISAVAILABLE = "OnPostCallAnalysisAvailable"
    ONREALTIMECALLANALYSISAVAILABLE = "OnRealTimeCallAnalysisAvailable"
    ONREALTIMECHATANALYSISAVAILABLE = "OnRealTimeChatAnalysisAvailable"
    ONPOSTCHATANALYSISAVAILABLE = "OnPostChatAnalysisAvailable"
    ONZENDESKTICKETCREATE = "OnZendeskTicketCreate"
    ONZENDESKTICKETSTATUSUPDATE = "OnZendeskTicketStatusUpdate"
    ONSALESFORCECASECREATE = "OnSalesforceCaseCreate"
    ONCONTACTEVALUATIONSUBMIT = "OnContactEvaluationSubmit"
    ONMETRICDATAUPDATE = "OnMetricDataUpdate"
    ONCASECREATE = "OnCaseCreate"
    ONCASEUPDATE = "OnCaseUpdate"
    ONSLABREACH = "OnSlaBreach"


class FailureReasonCode:
    """FailureReasonCode enum values."""

    INVALID_ATTRIBUTE_KEY = "INVALID_ATTRIBUTE_KEY"
    INVALID_CUSTOMER_ENDPOINT = "INVALID_CUSTOMER_ENDPOINT"
    INVALID_SYSTEM_ENDPOINT = "INVALID_SYSTEM_ENDPOINT"
    INVALID_QUEUE = "INVALID_QUEUE"
    INVALID_OUTBOUND_STRATEGY = "INVALID_OUTBOUND_STRATEGY"
    MISSING_CAMPAIGN = "MISSING_CAMPAIGN"
    MISSING_CUSTOMER_ENDPOINT = "MISSING_CUSTOMER_ENDPOINT"
    MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT = "MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT"
    REQUEST_THROTTLED = "REQUEST_THROTTLED"
    IDEMPOTENCY_EXCEPTION = "IDEMPOTENCY_EXCEPTION"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class FileStatusType:
    """FileStatusType enum values."""

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class FileUseCaseType:
    """FileUseCaseType enum values."""

    EMAIL_MESSAGE = "EMAIL_MESSAGE"
    ATTACHMENT = "ATTACHMENT"


class FilterV2StringConditionComparisonOperator:
    """FilterV2StringConditionComparisonOperator enum values."""

    NOT_EXISTS = "NOT_EXISTS"


class FlowAssociationResourceType:
    """FlowAssociationResourceType enum values."""

    SMS_PHONE_NUMBER = "SMS_PHONE_NUMBER"
    INBOUND_EMAIL = "INBOUND_EMAIL"
    OUTBOUND_EMAIL = "OUTBOUND_EMAIL"
    ANALYTICS_CONNECTOR = "ANALYTICS_CONNECTOR"
    WHATSAPP_MESSAGING_PHONE_NUMBER = "WHATSAPP_MESSAGING_PHONE_NUMBER"


class FlowModuleType:
    """FlowModuleType enum values."""

    MCP = "MCP"


class Grouping:
    """Grouping enum values."""

    QUEUE = "QUEUE"
    CHANNEL = "CHANNEL"
    ROUTING_PROFILE = "ROUTING_PROFILE"
    ROUTING_STEP_EXPRESSION = "ROUTING_STEP_EXPRESSION"
    AGENT_STATUS = "AGENT_STATUS"


class HierarchyGroupMatchType:
    """HierarchyGroupMatchType enum values."""

    EXACT = "EXACT"
    WITH_CHILD_GROUPS = "WITH_CHILD_GROUPS"


class HistoricalMetricName:
    """HistoricalMetricName enum values."""

    CONTACTS_QUEUED = "CONTACTS_QUEUED"
    CONTACTS_HANDLED = "CONTACTS_HANDLED"
    CONTACTS_ABANDONED = "CONTACTS_ABANDONED"
    CONTACTS_CONSULTED = "CONTACTS_CONSULTED"
    CONTACTS_AGENT_HUNG_UP_FIRST = "CONTACTS_AGENT_HUNG_UP_FIRST"
    CONTACTS_HANDLED_INCOMING = "CONTACTS_HANDLED_INCOMING"
    CONTACTS_HANDLED_OUTBOUND = "CONTACTS_HANDLED_OUTBOUND"
    CONTACTS_HOLD_ABANDONS = "CONTACTS_HOLD_ABANDONS"
    CONTACTS_TRANSFERRED_IN = "CONTACTS_TRANSFERRED_IN"
    CONTACTS_TRANSFERRED_OUT = "CONTACTS_TRANSFERRED_OUT"
    CONTACTS_TRANSFERRED_IN_FROM_QUEUE = "CONTACTS_TRANSFERRED_IN_FROM_QUEUE"
    CONTACTS_TRANSFERRED_OUT_FROM_QUEUE = "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE"
    CONTACTS_MISSED = "CONTACTS_MISSED"
    CALLBACK_CONTACTS_HANDLED = "CALLBACK_CONTACTS_HANDLED"
    API_CONTACTS_HANDLED = "API_CONTACTS_HANDLED"
    OCCUPANCY = "OCCUPANCY"
    HANDLE_TIME = "HANDLE_TIME"
    AFTER_CONTACT_WORK_TIME = "AFTER_CONTACT_WORK_TIME"
    QUEUED_TIME = "QUEUED_TIME"
    ABANDON_TIME = "ABANDON_TIME"
    QUEUE_ANSWER_TIME = "QUEUE_ANSWER_TIME"
    HOLD_TIME = "HOLD_TIME"
    INTERACTION_TIME = "INTERACTION_TIME"
    INTERACTION_AND_HOLD_TIME = "INTERACTION_AND_HOLD_TIME"
    SERVICE_LEVEL = "SERVICE_LEVEL"


class HoursOfOperationDays:
    """HoursOfOperationDays enum values."""

    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class InboundMessageSourceType:
    """InboundMessageSourceType enum values."""

    RAW = "RAW"


class InitiateAs:
    """InitiateAs enum values."""

    CONNECTED_TO_USER = "CONNECTED_TO_USER"
    COMPLETED = "COMPLETED"


class InstanceAttributeType:
    """InstanceAttributeType enum values."""

    INBOUND_CALLS = "INBOUND_CALLS"
    OUTBOUND_CALLS = "OUTBOUND_CALLS"
    CONTACTFLOW_LOGS = "CONTACTFLOW_LOGS"
    CONTACT_LENS = "CONTACT_LENS"
    AUTO_RESOLVE_BEST_VOICES = "AUTO_RESOLVE_BEST_VOICES"
    USE_CUSTOM_TTS_VOICES = "USE_CUSTOM_TTS_VOICES"
    EARLY_MEDIA = "EARLY_MEDIA"
    MULTI_PARTY_CONFERENCE = "MULTI_PARTY_CONFERENCE"
    HIGH_VOLUME_OUTBOUND = "HIGH_VOLUME_OUTBOUND"
    ENHANCED_CONTACT_MONITORING = "ENHANCED_CONTACT_MONITORING"
    ENHANCED_CHAT_MONITORING = "ENHANCED_CHAT_MONITORING"
    MULTI_PARTY_CHAT_CONFERENCE = "MULTI_PARTY_CHAT_CONFERENCE"
    MESSAGE_STREAMING = "MESSAGE_STREAMING"


class InstanceReplicationStatus:
    """InstanceReplicationStatus enum values."""

    INSTANCE_REPLICATION_COMPLETE = "INSTANCE_REPLICATION_COMPLETE"
    INSTANCE_REPLICATION_IN_PROGRESS = "INSTANCE_REPLICATION_IN_PROGRESS"
    INSTANCE_REPLICATION_FAILED = "INSTANCE_REPLICATION_FAILED"
    INSTANCE_REPLICA_DELETING = "INSTANCE_REPLICA_DELETING"
    INSTANCE_REPLICATION_DELETION_FAILED = "INSTANCE_REPLICATION_DELETION_FAILED"
    RESOURCE_REPLICATION_NOT_STARTED = "RESOURCE_REPLICATION_NOT_STARTED"


class InstanceStatus:
    """InstanceStatus enum values."""

    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    CREATION_FAILED = "CREATION_FAILED"


class InstanceStorageResourceType:
    """InstanceStorageResourceType enum values."""

    CHAT_TRANSCRIPTS = "CHAT_TRANSCRIPTS"
    CALL_RECORDINGS = "CALL_RECORDINGS"
    SCHEDULED_REPORTS = "SCHEDULED_REPORTS"
    MEDIA_STREAMS = "MEDIA_STREAMS"
    CONTACT_TRACE_RECORDS = "CONTACT_TRACE_RECORDS"
    AGENT_EVENTS = "AGENT_EVENTS"
    REAL_TIME_CONTACT_ANALYSIS_SEGMENTS = "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS"
    ATTACHMENTS = "ATTACHMENTS"
    CONTACT_EVALUATIONS = "CONTACT_EVALUATIONS"
    SCREEN_RECORDINGS = "SCREEN_RECORDINGS"
    REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS = "REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS"
    REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS = "REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS"
    EMAIL_MESSAGES = "EMAIL_MESSAGES"


class IntegrationType:
    """IntegrationType enum values."""

    EVENT = "EVENT"
    VOICE_ID = "VOICE_ID"
    PINPOINT_APP = "PINPOINT_APP"
    WISDOM_ASSISTANT = "WISDOM_ASSISTANT"
    WISDOM_KNOWLEDGE_BASE = "WISDOM_KNOWLEDGE_BASE"
    WISDOM_QUICK_RESPONSES = "WISDOM_QUICK_RESPONSES"
    Q_MESSAGE_TEMPLATES = "Q_MESSAGE_TEMPLATES"
    CASES_DOMAIN = "CASES_DOMAIN"
    APPLICATION = "APPLICATION"
    FILE_SCANNER = "FILE_SCANNER"
    SES_IDENTITY = "SES_IDENTITY"
    ANALYTICS_CONNECTOR = "ANALYTICS_CONNECTOR"
    CALL_TRANSFER_CONNECTOR = "CALL_TRANSFER_CONNECTOR"
    COGNITO_USER_POOL = "COGNITO_USER_POOL"
    MESSAGE_PROCESSOR = "MESSAGE_PROCESSOR"


class IntervalPeriod:
    """IntervalPeriod enum values."""

    FIFTEEN_MIN = "FIFTEEN_MIN"
    THIRTY_MIN = "THIRTY_MIN"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    TOTAL = "TOTAL"


class IvrRecordingTrack:
    """IvrRecordingTrack enum values."""

    ALL = "ALL"


class LexVersion:
    """LexVersion enum values."""

    V1 = "V1"
    V2 = "V2"


class ListFlowAssociationResourceType:
    """ListFlowAssociationResourceType enum values."""

    WHATSAPP_MESSAGING_PHONE_NUMBER = "WHATSAPP_MESSAGING_PHONE_NUMBER"
    VOICE_PHONE_NUMBER = "VOICE_PHONE_NUMBER"
    INBOUND_EMAIL = "INBOUND_EMAIL"
    OUTBOUND_EMAIL = "OUTBOUND_EMAIL"
    ANALYTICS_CONNECTOR = "ANALYTICS_CONNECTOR"


class MediaStreamType:
    """MediaStreamType enum values."""

    AUDIO = "AUDIO"
    VIDEO = "VIDEO"


class MediaType:
    """MediaType enum values."""

    IMAGE_LOGO_LIGHT_FAVICON = "IMAGE_LOGO_LIGHT_FAVICON"
    IMAGE_LOGO_DARK_FAVICON = "IMAGE_LOGO_DARK_FAVICON"
    IMAGE_LOGO_LIGHT_HORIZONTAL = "IMAGE_LOGO_LIGHT_HORIZONTAL"
    IMAGE_LOGO_DARK_HORIZONTAL = "IMAGE_LOGO_DARK_HORIZONTAL"


class MeetingFeatureStatus:
    """MeetingFeatureStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class MonitorCapability:
    """MonitorCapability enum values."""

    SILENT_MONITOR = "SILENT_MONITOR"
    BARGE = "BARGE"


class MultiSelectQuestionRuleCategoryAutomationCondition:
    """MultiSelectQuestionRuleCategoryAutomationCondition enum values."""

    PRESENT = "PRESENT"
    NOT_PRESENT = "NOT_PRESENT"


class NextContactType:
    """NextContactType enum values."""

    QUICK_CONNECT = "QUICK_CONNECT"


class NotificationContentType:
    """NotificationContentType enum values."""

    PLAIN_TEXT = "PLAIN_TEXT"


class NotificationDeliveryType:
    """NotificationDeliveryType enum values."""

    EMAIL = "EMAIL"


class NumberComparisonType:
    """NumberComparisonType enum values."""

    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    GREATER = "GREATER"
    LESSER_OR_EQUAL = "LESSER_OR_EQUAL"
    LESSER = "LESSER"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    RANGE = "RANGE"


class NumericQuestionPropertyAutomationLabel:
    """NumericQuestionPropertyAutomationLabel enum values."""

    OVERALL_CUSTOMER_SENTIMENT_SCORE = "OVERALL_CUSTOMER_SENTIMENT_SCORE"
    OVERALL_AGENT_SENTIMENT_SCORE = "OVERALL_AGENT_SENTIMENT_SCORE"
    CUSTOMER_SENTIMENT_SCORE_WITHOUT_AGENT = "CUSTOMER_SENTIMENT_SCORE_WITHOUT_AGENT"
    CUSTOMER_SENTIMENT_SCORE_WITH_AGENT = "CUSTOMER_SENTIMENT_SCORE_WITH_AGENT"
    NON_TALK_TIME = "NON_TALK_TIME"
    NON_TALK_TIME_PERCENTAGE = "NON_TALK_TIME_PERCENTAGE"
    NUMBER_OF_INTERRUPTIONS = "NUMBER_OF_INTERRUPTIONS"
    CONTACT_DURATION = "CONTACT_DURATION"
    AGENT_INTERACTION_DURATION = "AGENT_INTERACTION_DURATION"
    CUSTOMER_HOLD_TIME = "CUSTOMER_HOLD_TIME"
    LONGEST_HOLD_DURATION = "LONGEST_HOLD_DURATION"
    NUMBER_OF_HOLDS = "NUMBER_OF_HOLDS"
    AGENT_INTERACTION_AND_HOLD_DURATION = "AGENT_INTERACTION_AND_HOLD_DURATION"


class OutboundMessageSourceType:
    """OutboundMessageSourceType enum values."""

    TEMPLATE = "TEMPLATE"
    RAW = "RAW"


class OutboundStrategyType:
    """OutboundStrategyType enum values."""

    AGENT_FIRST = "AGENT_FIRST"


class OverrideDays:
    """OverrideDays enum values."""

    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class ParticipantRole:
    """ParticipantRole enum values."""

    AGENT = "AGENT"
    CUSTOMER = "CUSTOMER"
    SYSTEM = "SYSTEM"
    CUSTOM_BOT = "CUSTOM_BOT"
    SUPERVISOR = "SUPERVISOR"


class ParticipantState:
    """ParticipantState enum values."""

    INITIAL = "INITIAL"
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    MISSED = "MISSED"


class ParticipantTimerAction:
    """ParticipantTimerAction enum values."""

    UNSET = "Unset"


class ParticipantTimerType:
    """ParticipantTimerType enum values."""

    IDLE = "IDLE"
    DISCONNECT_NONCUSTOMER = "DISCONNECT_NONCUSTOMER"


class ParticipantType:
    """ParticipantType enum values."""

    ALL = "ALL"
    MANAGER = "MANAGER"
    AGENT = "AGENT"
    CUSTOMER = "CUSTOMER"
    THIRDPARTY = "THIRDPARTY"


class PhoneNumberCountryCode:
    """PhoneNumberCountryCode enum values."""

    AF = "AF"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BA = "BA"
    BW = "BW"
    BR = "BR"
    IO = "IO"
    VG = "VG"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CK = "CK"
    CR = "CR"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    CD = "CD"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    TL = "TL"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    PF = "PF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    CI = "CI"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    AN = "AN"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    KP = "KP"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    CG = "CG"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    KR = "KR"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    VI = "VI"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VA = "VA"
    VE = "VE"
    VN = "VN"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"


class PhoneNumberType:
    """PhoneNumberType enum values."""

    TOLL_FREE = "TOLL_FREE"
    DID = "DID"
    UIFN = "UIFN"
    SHARED = "SHARED"
    THIRD_PARTY_TF = "THIRD_PARTY_TF"
    THIRD_PARTY_DID = "THIRD_PARTY_DID"
    SHORT_CODE = "SHORT_CODE"


class PhoneNumberWorkflowStatus:
    """PhoneNumberWorkflowStatus enum values."""

    CLAIMED = "CLAIMED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class PhoneType:
    """PhoneType enum values."""

    SOFT_PHONE = "SOFT_PHONE"
    DESK_PHONE = "DESK_PHONE"


class PropertyValidationExceptionReason:
    """PropertyValidationExceptionReason enum values."""

    INVALID_FORMAT = "INVALID_FORMAT"
    UNIQUE_CONSTRAINT_VIOLATED = "UNIQUE_CONSTRAINT_VIOLATED"
    REFERENCED_RESOURCE_NOT_FOUND = "REFERENCED_RESOURCE_NOT_FOUND"
    RESOURCE_NAME_ALREADY_EXISTS = "RESOURCE_NAME_ALREADY_EXISTS"
    REQUIRED_PROPERTY_MISSING = "REQUIRED_PROPERTY_MISSING"
    NOT_SUPPORTED = "NOT_SUPPORTED"


class QuestionRuleCategoryAutomationCondition:
    """QuestionRuleCategoryAutomationCondition enum values."""

    PRESENT = "PRESENT"
    NOT_PRESENT = "NOT_PRESENT"


class QueueStatus:
    """QueueStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class QueueType:
    """QueueType enum values."""

    STANDARD = "STANDARD"
    AGENT = "AGENT"


class QuickConnectType:
    """QuickConnectType enum values."""

    USER = "USER"
    QUEUE = "QUEUE"
    PHONE_NUMBER = "PHONE_NUMBER"
    FLOW = "FLOW"


class RealTimeContactAnalysisOutputType:
    """RealTimeContactAnalysisOutputType enum values."""

    RAW = "Raw"
    REDACTED = "Redacted"


class RealTimeContactAnalysisPostContactSummaryFailureCode:
    """RealTimeContactAnalysisPostContactSummaryFailureCode enum values."""

    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    INSUFFICIENT_CONVERSATION_CONTENT = "INSUFFICIENT_CONVERSATION_CONTENT"
    FAILED_SAFETY_GUIDELINES = "FAILED_SAFETY_GUIDELINES"
    INVALID_ANALYSIS_CONFIGURATION = "INVALID_ANALYSIS_CONFIGURATION"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class RealTimeContactAnalysisPostContactSummaryStatus:
    """RealTimeContactAnalysisPostContactSummaryStatus enum values."""

    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class RealTimeContactAnalysisSegmentType:
    """RealTimeContactAnalysisSegmentType enum values."""

    TRANSCRIPT = "Transcript"
    CATEGORIES = "Categories"
    ISSUES = "Issues"
    EVENT = "Event"
    ATTACHMENTS = "Attachments"
    POSTCONTACTSUMMARY = "PostContactSummary"


class RealTimeContactAnalysisSentimentLabel:
    """RealTimeContactAnalysisSentimentLabel enum values."""

    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"


class RealTimeContactAnalysisStatus:
    """RealTimeContactAnalysisStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class RealTimeContactAnalysisSupportedChannel:
    """RealTimeContactAnalysisSupportedChannel enum values."""

    VOICE = "VOICE"
    CHAT = "CHAT"


class RecordingStatus:
    """RecordingStatus enum values."""

    AVAILABLE = "AVAILABLE"
    DELETED = "DELETED"


class ReferenceStatus:
    """ReferenceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    DELETED = "DELETED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class ReferenceType:
    """ReferenceType enum values."""

    URL = "URL"
    ATTACHMENT = "ATTACHMENT"
    CONTACT_ANALYSIS = "CONTACT_ANALYSIS"
    NUMBER = "NUMBER"
    STRING = "STRING"
    DATE = "DATE"
    EMAIL = "EMAIL"
    EMAIL_MESSAGE = "EMAIL_MESSAGE"
    EMAIL_MESSAGE_PLAIN_TEXT = "EMAIL_MESSAGE_PLAIN_TEXT"


class RehydrationType:
    """RehydrationType enum values."""

    ENTIRE_PAST_SESSION = "ENTIRE_PAST_SESSION"
    FROM_SEGMENT = "FROM_SEGMENT"


class ResourceType:
    """ResourceType enum values."""

    CONTACT = "CONTACT"
    CONTACT_FLOW = "CONTACT_FLOW"
    INSTANCE = "INSTANCE"
    PARTICIPANT = "PARTICIPANT"
    HIERARCHY_LEVEL = "HIERARCHY_LEVEL"
    HIERARCHY_GROUP = "HIERARCHY_GROUP"
    USER = "USER"
    PHONE_NUMBER = "PHONE_NUMBER"


class ResponseMode:
    """ResponseMode enum values."""

    INCREMENTAL = "INCREMENTAL"
    COMPLETE = "COMPLETE"


class RoutingCriteriaStepStatus:
    """RoutingCriteriaStepStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    JOINED = "JOINED"
    EXPIRED = "EXPIRED"


class RulePublishStatus:
    """RulePublishStatus enum values."""

    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"


class ScreenShareCapability:
    """ScreenShareCapability enum values."""

    SEND = "SEND"


class SearchContactsMatchType:
    """SearchContactsMatchType enum values."""

    MATCH_ALL = "MATCH_ALL"
    MATCH_ANY = "MATCH_ANY"
    MATCH_EXACT = "MATCH_EXACT"
    MATCH_NONE = "MATCH_NONE"


class SearchContactsTimeRangeConditionType:
    """SearchContactsTimeRangeConditionType enum values."""

    NOT_EXISTS = "NOT_EXISTS"


class SearchContactsTimeRangeType:
    """SearchContactsTimeRangeType enum values."""

    INITIATION_TIMESTAMP = "INITIATION_TIMESTAMP"
    SCHEDULED_TIMESTAMP = "SCHEDULED_TIMESTAMP"
    CONNECTED_TO_AGENT_TIMESTAMP = "CONNECTED_TO_AGENT_TIMESTAMP"
    DISCONNECT_TIMESTAMP = "DISCONNECT_TIMESTAMP"
    ENQUEUE_TIMESTAMP = "ENQUEUE_TIMESTAMP"


class SearchableQueueType:
    """SearchableQueueType enum values."""

    STANDARD = "STANDARD"


class SingleSelectQuestionRuleCategoryAutomationCondition:
    """SingleSelectQuestionRuleCategoryAutomationCondition enum values."""

    PRESENT = "PRESENT"
    NOT_PRESENT = "NOT_PRESENT"


class SlaAssignmentType:
    """SlaAssignmentType enum values."""

    CASES = "CASES"


class SlaType:
    """SlaType enum values."""

    CASEFIELD = "CaseField"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SortableFieldName:
    """SortableFieldName enum values."""

    INITIATION_TIMESTAMP = "INITIATION_TIMESTAMP"
    SCHEDULED_TIMESTAMP = "SCHEDULED_TIMESTAMP"
    CONNECTED_TO_AGENT_TIMESTAMP = "CONNECTED_TO_AGENT_TIMESTAMP"
    DISCONNECT_TIMESTAMP = "DISCONNECT_TIMESTAMP"
    INITIATION_METHOD = "INITIATION_METHOD"
    CHANNEL = "CHANNEL"
    EXPIRY_TIMESTAMP = "EXPIRY_TIMESTAMP"


class SourceType:
    """SourceType enum values."""

    SALESFORCE = "SALESFORCE"
    ZENDESK = "ZENDESK"
    CASES = "CASES"


class Statistic:
    """Statistic enum values."""

    SUM = "SUM"
    MAX = "MAX"
    AVG = "AVG"


class Status:
    """Status enum values."""

    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    DELETED = "DELETED"


class StorageType:
    """StorageType enum values."""

    S3 = "S3"
    KINESIS_VIDEO_STREAM = "KINESIS_VIDEO_STREAM"
    KINESIS_STREAM = "KINESIS_STREAM"
    KINESIS_FIREHOSE = "KINESIS_FIREHOSE"


class StringComparisonType:
    """StringComparisonType enum values."""

    STARTS_WITH = "STARTS_WITH"
    CONTAINS = "CONTAINS"
    EXACT = "EXACT"


class TargetListType:
    """TargetListType enum values."""

    PROFICIENCIES = "PROFICIENCIES"


class TaskTemplateFieldType:
    """TaskTemplateFieldType enum values."""

    NAME = "NAME"
    DESCRIPTION = "DESCRIPTION"
    SCHEDULED_TIME = "SCHEDULED_TIME"
    QUICK_CONNECT = "QUICK_CONNECT"
    URL = "URL"
    NUMBER = "NUMBER"
    TEXT = "TEXT"
    TEXT_AREA = "TEXT_AREA"
    DATE_TIME = "DATE_TIME"
    BOOLEAN = "BOOLEAN"
    SINGLE_SELECT = "SINGLE_SELECT"
    EMAIL = "EMAIL"
    SELF_ASSIGN = "SELF_ASSIGN"
    EXPIRY_DURATION = "EXPIRY_DURATION"


class TaskTemplateStatus:
    """TaskTemplateStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TimerEligibleParticipantRoles:
    """TimerEligibleParticipantRoles enum values."""

    CUSTOMER = "CUSTOMER"
    AGENT = "AGENT"


class TrafficDistributionGroupStatus:
    """TrafficDistributionGroupStatus enum values."""

    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    CREATION_FAILED = "CREATION_FAILED"
    PENDING_DELETION = "PENDING_DELETION"
    DELETION_FAILED = "DELETION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"


class TrafficType:
    """TrafficType enum values."""

    GENERAL = "GENERAL"
    CAMPAIGN = "CAMPAIGN"


class Unit:
    """Unit enum values."""

    SECONDS = "SECONDS"
    COUNT = "COUNT"
    PERCENT = "PERCENT"


class UseCaseType:
    """UseCaseType enum values."""

    RULES_EVALUATION = "RULES_EVALUATION"
    CONNECT_CAMPAIGNS = "CONNECT_CAMPAIGNS"


class VideoCapability:
    """VideoCapability enum values."""

    SEND = "SEND"


class ViewStatus:
    """ViewStatus enum values."""

    PUBLISHED = "PUBLISHED"
    SAVED = "SAVED"


class ViewType:
    """ViewType enum values."""

    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    AWS_MANAGED = "AWS_MANAGED"


class Visibility:
    """Visibility enum values."""

    ALL = "ALL"
    ASSIGNED = "ASSIGNED"
    NONE = "NONE"


class VocabularyLanguageCode:
    """VocabularyLanguageCode enum values."""

    AR_AE = "ar-AE"
    DE_CH = "de-CH"
    DE_DE = "de-DE"
    EN_AB = "en-AB"
    EN_AU = "en-AU"
    EN_GB = "en-GB"
    EN_IE = "en-IE"
    EN_IN = "en-IN"
    EN_US = "en-US"
    EN_WL = "en-WL"
    ES_ES = "es-ES"
    ES_US = "es-US"
    FR_CA = "fr-CA"
    FR_FR = "fr-FR"
    HI_IN = "hi-IN"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    PT_BR = "pt-BR"
    PT_PT = "pt-PT"
    ZH_CN = "zh-CN"
    EN_NZ = "en-NZ"
    EN_ZA = "en-ZA"
    CA_ES = "ca-ES"
    DA_DK = "da-DK"
    FI_FI = "fi-FI"
    ID_ID = "id-ID"
    MS_MY = "ms-MY"
    NL_NL = "nl-NL"
    NO_NO = "no-NO"
    PL_PL = "pl-PL"
    SV_SE = "sv-SE"
    TL_PH = "tl-PH"


class VocabularyState:
    """VocabularyState enum values."""

    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    ACTIVE = "ACTIVE"
    CREATION_FAILED = "CREATION_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"


class VoiceRecordingTrack:
    """VoiceRecordingTrack enum values."""

    FROM_AGENT = "FROM_AGENT"
    TO_AGENT = "TO_AGENT"
    ALL = "ALL"


class WorkspaceFontFamily:
    """WorkspaceFontFamily enum values."""

    ARIAL = "Arial"
    COURIER_NEW = "Courier New"
    GEORGIA = "Georgia"
    TIMES_NEW_ROMAN = "Times New Roman"
    TREBUCHET = "Trebuchet"
    VERDANA = "Verdana"


@dataclass
class UserIdentityInfo(PropertyType):
    EMAIL = "Email"
    FIRST_NAME = "FirstName"
    SECONDARY_EMAIL = "SecondaryEmail"
    LAST_NAME = "LastName"
    MOBILE = "Mobile"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email": "Email",
        "first_name": "FirstName",
        "secondary_email": "SecondaryEmail",
        "last_name": "LastName",
        "mobile": "Mobile",
    }

    email: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_email: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mobile: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserPhoneConfig(PropertyType):
    AUTO_ACCEPT = "AutoAccept"
    PHONE_TYPE = "PhoneType"
    PERSISTENT_CONNECTION = "PersistentConnection"
    DESK_PHONE_NUMBER = "DeskPhoneNumber"
    AFTER_CONTACT_WORK_TIME_LIMIT = "AfterContactWorkTimeLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_accept": "AutoAccept",
        "phone_type": "PhoneType",
        "persistent_connection": "PersistentConnection",
        "desk_phone_number": "DeskPhoneNumber",
        "after_contact_work_time_limit": "AfterContactWorkTimeLimit",
    }

    auto_accept: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    phone_type: Optional[Union[str, PhoneType, Ref, GetAtt, Sub]] = None
    persistent_connection: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    desk_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None
    after_contact_work_time_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class UserProficiency(PropertyType):
    ATTRIBUTE_VALUE = "AttributeValue"
    ATTRIBUTE_NAME = "AttributeName"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_value": "AttributeValue",
        "attribute_name": "AttributeName",
        "level": "Level",
    }

    attribute_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attribute_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    level: Optional[Union[float, Ref, GetAtt, Sub]] = None

