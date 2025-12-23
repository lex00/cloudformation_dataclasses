"""PropertyTypes for AWS::ConnectCampaigns::Campaign."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AgentlessDialerConfig(PropertyType):
    DIALING_CAPACITY = "DialingCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dialing_capacity": "DialingCapacity",
    }

    dialing_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class AnswerMachineDetectionConfig(PropertyType):
    ENABLE_ANSWER_MACHINE_DETECTION = "EnableAnswerMachineDetection"
    AWAIT_ANSWER_MACHINE_PROMPT = "AwaitAnswerMachinePrompt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_answer_machine_detection": "EnableAnswerMachineDetection",
        "await_answer_machine_prompt": "AwaitAnswerMachinePrompt",
    }

    enable_answer_machine_detection: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    await_answer_machine_prompt: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DialerConfig(PropertyType):
    AGENTLESS_DIALER_CONFIG = "AgentlessDialerConfig"
    PREDICTIVE_DIALER_CONFIG = "PredictiveDialerConfig"
    PROGRESSIVE_DIALER_CONFIG = "ProgressiveDialerConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agentless_dialer_config": "AgentlessDialerConfig",
        "predictive_dialer_config": "PredictiveDialerConfig",
        "progressive_dialer_config": "ProgressiveDialerConfig",
    }

    agentless_dialer_config: Optional[AgentlessDialerConfig] = None
    predictive_dialer_config: Optional[PredictiveDialerConfig] = None
    progressive_dialer_config: Optional[ProgressiveDialerConfig] = None


@dataclass
class OutboundCallConfig(PropertyType):
    CONNECT_CONTACT_FLOW_ARN = "ConnectContactFlowArn"
    CONNECT_QUEUE_ARN = "ConnectQueueArn"
    ANSWER_MACHINE_DETECTION_CONFIG = "AnswerMachineDetectionConfig"
    CONNECT_SOURCE_PHONE_NUMBER = "ConnectSourcePhoneNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connect_contact_flow_arn": "ConnectContactFlowArn",
        "connect_queue_arn": "ConnectQueueArn",
        "answer_machine_detection_config": "AnswerMachineDetectionConfig",
        "connect_source_phone_number": "ConnectSourcePhoneNumber",
    }

    connect_contact_flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connect_queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    answer_machine_detection_config: Optional[AnswerMachineDetectionConfig] = None
    connect_source_phone_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PredictiveDialerConfig(PropertyType):
    DIALING_CAPACITY = "DialingCapacity"
    BANDWIDTH_ALLOCATION = "BandwidthAllocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dialing_capacity": "DialingCapacity",
        "bandwidth_allocation": "BandwidthAllocation",
    }

    dialing_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    bandwidth_allocation: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ProgressiveDialerConfig(PropertyType):
    DIALING_CAPACITY = "DialingCapacity"
    BANDWIDTH_ALLOCATION = "BandwidthAllocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dialing_capacity": "DialingCapacity",
        "bandwidth_allocation": "BandwidthAllocation",
    }

    dialing_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    bandwidth_allocation: Optional[Union[float, Ref, GetAtt, Sub]] = None

