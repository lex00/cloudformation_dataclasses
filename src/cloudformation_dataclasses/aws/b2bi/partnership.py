"""PropertyTypes for AWS::B2BI::Partnership."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapabilityOptions(PropertyType):
    INBOUND_EDI = "InboundEdi"
    OUTBOUND_EDI = "OutboundEdi"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inbound_edi": "InboundEdi",
        "outbound_edi": "OutboundEdi",
    }

    inbound_edi: Optional[InboundEdiOptions] = None
    outbound_edi: Optional[OutboundEdiOptions] = None


@dataclass
class InboundEdiOptions(PropertyType):
    X12 = "X12"

    _property_mappings: ClassVar[dict[str, str]] = {
        "x12": "X12",
    }

    x12: Optional[X12InboundEdiOptions] = None


@dataclass
class OutboundEdiOptions(PropertyType):
    X12 = "X12"

    _property_mappings: ClassVar[dict[str, str]] = {
        "x12": "X12",
    }

    x12: Optional[X12Envelope] = None


@dataclass
class WrapOptions(PropertyType):
    LINE_LENGTH = "LineLength"
    WRAP_BY = "WrapBy"
    LINE_TERMINATOR = "LineTerminator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "line_length": "LineLength",
        "wrap_by": "WrapBy",
        "line_terminator": "LineTerminator",
    }

    line_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    wrap_by: Optional[Union[str, Ref, GetAtt, Sub]] = None
    line_terminator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12AcknowledgmentOptions(PropertyType):
    TECHNICAL_ACKNOWLEDGMENT = "TechnicalAcknowledgment"
    FUNCTIONAL_ACKNOWLEDGMENT = "FunctionalAcknowledgment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "technical_acknowledgment": "TechnicalAcknowledgment",
        "functional_acknowledgment": "FunctionalAcknowledgment",
    }

    technical_acknowledgment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    functional_acknowledgment: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12ControlNumbers(PropertyType):
    STARTING_FUNCTIONAL_GROUP_CONTROL_NUMBER = "StartingFunctionalGroupControlNumber"
    STARTING_INTERCHANGE_CONTROL_NUMBER = "StartingInterchangeControlNumber"
    STARTING_TRANSACTION_SET_CONTROL_NUMBER = "StartingTransactionSetControlNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "starting_functional_group_control_number": "StartingFunctionalGroupControlNumber",
        "starting_interchange_control_number": "StartingInterchangeControlNumber",
        "starting_transaction_set_control_number": "StartingTransactionSetControlNumber",
    }

    starting_functional_group_control_number: Optional[Union[float, Ref, GetAtt, Sub]] = None
    starting_interchange_control_number: Optional[Union[float, Ref, GetAtt, Sub]] = None
    starting_transaction_set_control_number: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class X12Delimiters(PropertyType):
    SEGMENT_TERMINATOR = "SegmentTerminator"
    COMPONENT_SEPARATOR = "ComponentSeparator"
    DATA_ELEMENT_SEPARATOR = "DataElementSeparator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_terminator": "SegmentTerminator",
        "component_separator": "ComponentSeparator",
        "data_element_separator": "DataElementSeparator",
    }

    segment_terminator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_separator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_element_separator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12Envelope(PropertyType):
    WRAP_OPTIONS = "WrapOptions"
    COMMON = "Common"

    _property_mappings: ClassVar[dict[str, str]] = {
        "wrap_options": "WrapOptions",
        "common": "Common",
    }

    wrap_options: Optional[WrapOptions] = None
    common: Optional[X12OutboundEdiHeaders] = None


@dataclass
class X12FunctionalGroupHeaders(PropertyType):
    APPLICATION_SENDER_CODE = "ApplicationSenderCode"
    APPLICATION_RECEIVER_CODE = "ApplicationReceiverCode"
    RESPONSIBLE_AGENCY_CODE = "ResponsibleAgencyCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_sender_code": "ApplicationSenderCode",
        "application_receiver_code": "ApplicationReceiverCode",
        "responsible_agency_code": "ResponsibleAgencyCode",
    }

    application_sender_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_receiver_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    responsible_agency_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12InboundEdiOptions(PropertyType):
    ACKNOWLEDGMENT_OPTIONS = "AcknowledgmentOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "acknowledgment_options": "AcknowledgmentOptions",
    }

    acknowledgment_options: Optional[X12AcknowledgmentOptions] = None


@dataclass
class X12InterchangeControlHeaders(PropertyType):
    RECEIVER_ID = "ReceiverId"
    ACKNOWLEDGMENT_REQUESTED_CODE = "AcknowledgmentRequestedCode"
    SENDER_ID_QUALIFIER = "SenderIdQualifier"
    USAGE_INDICATOR_CODE = "UsageIndicatorCode"
    REPETITION_SEPARATOR = "RepetitionSeparator"
    SENDER_ID = "SenderId"
    RECEIVER_ID_QUALIFIER = "ReceiverIdQualifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "receiver_id": "ReceiverId",
        "acknowledgment_requested_code": "AcknowledgmentRequestedCode",
        "sender_id_qualifier": "SenderIdQualifier",
        "usage_indicator_code": "UsageIndicatorCode",
        "repetition_separator": "RepetitionSeparator",
        "sender_id": "SenderId",
        "receiver_id_qualifier": "ReceiverIdQualifier",
    }

    receiver_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    acknowledgment_requested_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sender_id_qualifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    usage_indicator_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repetition_separator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sender_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    receiver_id_qualifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12OutboundEdiHeaders(PropertyType):
    DELIMITERS = "Delimiters"
    CONTROL_NUMBERS = "ControlNumbers"
    FUNCTIONAL_GROUP_HEADERS = "FunctionalGroupHeaders"
    INTERCHANGE_CONTROL_HEADERS = "InterchangeControlHeaders"
    VALIDATE_EDI = "ValidateEdi"
    GS05_TIME_FORMAT = "Gs05TimeFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiters": "Delimiters",
        "control_numbers": "ControlNumbers",
        "functional_group_headers": "FunctionalGroupHeaders",
        "interchange_control_headers": "InterchangeControlHeaders",
        "validate_edi": "ValidateEdi",
        "gs05_time_format": "Gs05TimeFormat",
    }

    delimiters: Optional[X12Delimiters] = None
    control_numbers: Optional[X12ControlNumbers] = None
    functional_group_headers: Optional[X12FunctionalGroupHeaders] = None
    interchange_control_headers: Optional[X12InterchangeControlHeaders] = None
    validate_edi: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    gs05_time_format: Optional[Union[str, Ref, GetAtt, Sub]] = None

