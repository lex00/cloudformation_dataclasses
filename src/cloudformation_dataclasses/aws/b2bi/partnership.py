"""PropertyTypes for AWS::B2BI::Partnership."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CapabilityDirection:
    """CapabilityDirection enum values."""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"


class CapabilityType:
    """CapabilityType enum values."""

    EDI = "edi"


class ConversionSourceFormat:
    """ConversionSourceFormat enum values."""

    JSON = "JSON"
    XML = "XML"


class ConversionTargetFormat:
    """ConversionTargetFormat enum values."""

    X12 = "X12"


class ElementRequirement:
    """ElementRequirement enum values."""

    OPTIONAL = "OPTIONAL"
    MANDATORY = "MANDATORY"


class FileFormat:
    """FileFormat enum values."""

    XML = "XML"
    JSON = "JSON"
    NOT_USED = "NOT_USED"


class FromFormat:
    """FromFormat enum values."""

    X12 = "X12"


class LineTerminator:
    """LineTerminator enum values."""

    CRLF = "CRLF"
    LF = "LF"
    CR = "CR"


class Logging:
    """Logging enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MappingTemplateLanguage:
    """MappingTemplateLanguage enum values."""

    XSLT = "XSLT"
    JSONATA = "JSONATA"


class MappingType:
    """MappingType enum values."""

    JSONATA = "JSONATA"
    XSLT = "XSLT"


class ToFormat:
    """ToFormat enum values."""

    X12 = "X12"


class TransformerJobStatus:
    """TransformerJobStatus enum values."""

    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class TransformerStatus:
    """TransformerStatus enum values."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class WrapFormat:
    """WrapFormat enum values."""

    SEGMENT = "SEGMENT"
    ONE_LINE = "ONE_LINE"
    LINE_LENGTH = "LINE_LENGTH"


class X12FunctionalAcknowledgment:
    """X12FunctionalAcknowledgment enum values."""

    DO_NOT_GENERATE = "DO_NOT_GENERATE"
    GENERATE_ALL_SEGMENTS = "GENERATE_ALL_SEGMENTS"
    GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP = "GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP"


class X12GS05TimeFormat:
    """X12GS05TimeFormat enum values."""

    HHMM = "HHMM"
    HHMMSS = "HHMMSS"
    HHMMSSDD = "HHMMSSDD"


class X12SplitBy:
    """X12SplitBy enum values."""

    NONE = "NONE"
    TRANSACTION = "TRANSACTION"


class X12TechnicalAcknowledgment:
    """X12TechnicalAcknowledgment enum values."""

    DO_NOT_GENERATE = "DO_NOT_GENERATE"
    GENERATE_ALL_SEGMENTS = "GENERATE_ALL_SEGMENTS"


class X12TransactionSet:
    """X12TransactionSet enum values."""

    X12_100 = "X12_100"
    X12_101 = "X12_101"
    X12_102 = "X12_102"
    X12_103 = "X12_103"
    X12_104 = "X12_104"
    X12_105 = "X12_105"
    X12_106 = "X12_106"
    X12_107 = "X12_107"
    X12_108 = "X12_108"
    X12_109 = "X12_109"
    X12_110 = "X12_110"
    X12_111 = "X12_111"
    X12_112 = "X12_112"
    X12_113 = "X12_113"
    X12_120 = "X12_120"
    X12_121 = "X12_121"
    X12_124 = "X12_124"
    X12_125 = "X12_125"
    X12_126 = "X12_126"
    X12_127 = "X12_127"
    X12_128 = "X12_128"
    X12_129 = "X12_129"
    X12_130 = "X12_130"
    X12_131 = "X12_131"
    X12_132 = "X12_132"
    X12_133 = "X12_133"
    X12_135 = "X12_135"
    X12_138 = "X12_138"
    X12_139 = "X12_139"
    X12_140 = "X12_140"
    X12_141 = "X12_141"
    X12_142 = "X12_142"
    X12_143 = "X12_143"
    X12_144 = "X12_144"
    X12_146 = "X12_146"
    X12_147 = "X12_147"
    X12_148 = "X12_148"
    X12_149 = "X12_149"
    X12_150 = "X12_150"
    X12_151 = "X12_151"
    X12_152 = "X12_152"
    X12_153 = "X12_153"
    X12_154 = "X12_154"
    X12_155 = "X12_155"
    X12_157 = "X12_157"
    X12_158 = "X12_158"
    X12_159 = "X12_159"
    X12_160 = "X12_160"
    X12_161 = "X12_161"
    X12_163 = "X12_163"
    X12_170 = "X12_170"
    X12_175 = "X12_175"
    X12_176 = "X12_176"
    X12_179 = "X12_179"
    X12_180 = "X12_180"
    X12_185 = "X12_185"
    X12_186 = "X12_186"
    X12_187 = "X12_187"
    X12_188 = "X12_188"
    X12_189 = "X12_189"
    X12_190 = "X12_190"
    X12_191 = "X12_191"
    X12_194 = "X12_194"
    X12_195 = "X12_195"
    X12_196 = "X12_196"
    X12_197 = "X12_197"
    X12_198 = "X12_198"
    X12_199 = "X12_199"
    X12_200 = "X12_200"
    X12_201 = "X12_201"
    X12_202 = "X12_202"
    X12_203 = "X12_203"
    X12_204 = "X12_204"
    X12_205 = "X12_205"
    X12_206 = "X12_206"
    X12_210 = "X12_210"
    X12_211 = "X12_211"
    X12_212 = "X12_212"
    X12_213 = "X12_213"
    X12_214 = "X12_214"
    X12_215 = "X12_215"
    X12_216 = "X12_216"
    X12_217 = "X12_217"
    X12_218 = "X12_218"
    X12_219 = "X12_219"
    X12_220 = "X12_220"
    X12_222 = "X12_222"
    X12_223 = "X12_223"
    X12_224 = "X12_224"
    X12_225 = "X12_225"
    X12_227 = "X12_227"
    X12_228 = "X12_228"
    X12_240 = "X12_240"
    X12_242 = "X12_242"
    X12_244 = "X12_244"
    X12_245 = "X12_245"
    X12_248 = "X12_248"
    X12_249 = "X12_249"
    X12_250 = "X12_250"
    X12_251 = "X12_251"
    X12_252 = "X12_252"
    X12_255 = "X12_255"
    X12_256 = "X12_256"
    X12_259 = "X12_259"
    X12_260 = "X12_260"
    X12_261 = "X12_261"
    X12_262 = "X12_262"
    X12_263 = "X12_263"
    X12_264 = "X12_264"
    X12_265 = "X12_265"
    X12_266 = "X12_266"
    X12_267 = "X12_267"
    X12_268 = "X12_268"
    X12_269 = "X12_269"
    X12_270 = "X12_270"
    X12_271 = "X12_271"
    X12_272 = "X12_272"
    X12_273 = "X12_273"
    X12_274 = "X12_274"
    X12_275 = "X12_275"
    X12_276 = "X12_276"
    X12_277 = "X12_277"
    X12_278 = "X12_278"
    X12_280 = "X12_280"
    X12_283 = "X12_283"
    X12_284 = "X12_284"
    X12_285 = "X12_285"
    X12_286 = "X12_286"
    X12_288 = "X12_288"
    X12_290 = "X12_290"
    X12_300 = "X12_300"
    X12_301 = "X12_301"
    X12_303 = "X12_303"
    X12_304 = "X12_304"
    X12_309 = "X12_309"
    X12_310 = "X12_310"
    X12_311 = "X12_311"
    X12_312 = "X12_312"
    X12_313 = "X12_313"
    X12_315 = "X12_315"
    X12_317 = "X12_317"
    X12_319 = "X12_319"
    X12_322 = "X12_322"
    X12_323 = "X12_323"
    X12_324 = "X12_324"
    X12_325 = "X12_325"
    X12_326 = "X12_326"
    X12_350 = "X12_350"
    X12_352 = "X12_352"
    X12_353 = "X12_353"
    X12_354 = "X12_354"
    X12_355 = "X12_355"
    X12_356 = "X12_356"
    X12_357 = "X12_357"
    X12_358 = "X12_358"
    X12_361 = "X12_361"
    X12_362 = "X12_362"
    X12_404 = "X12_404"
    X12_410 = "X12_410"
    X12_412 = "X12_412"
    X12_414 = "X12_414"
    X12_417 = "X12_417"
    X12_418 = "X12_418"
    X12_419 = "X12_419"
    X12_420 = "X12_420"
    X12_421 = "X12_421"
    X12_422 = "X12_422"
    X12_423 = "X12_423"
    X12_424 = "X12_424"
    X12_425 = "X12_425"
    X12_426 = "X12_426"
    X12_429 = "X12_429"
    X12_431 = "X12_431"
    X12_432 = "X12_432"
    X12_433 = "X12_433"
    X12_434 = "X12_434"
    X12_435 = "X12_435"
    X12_436 = "X12_436"
    X12_437 = "X12_437"
    X12_440 = "X12_440"
    X12_451 = "X12_451"
    X12_452 = "X12_452"
    X12_453 = "X12_453"
    X12_455 = "X12_455"
    X12_456 = "X12_456"
    X12_460 = "X12_460"
    X12_463 = "X12_463"
    X12_466 = "X12_466"
    X12_468 = "X12_468"
    X12_470 = "X12_470"
    X12_475 = "X12_475"
    X12_485 = "X12_485"
    X12_486 = "X12_486"
    X12_490 = "X12_490"
    X12_492 = "X12_492"
    X12_494 = "X12_494"
    X12_500 = "X12_500"
    X12_501 = "X12_501"
    X12_503 = "X12_503"
    X12_504 = "X12_504"
    X12_511 = "X12_511"
    X12_517 = "X12_517"
    X12_521 = "X12_521"
    X12_527 = "X12_527"
    X12_536 = "X12_536"
    X12_540 = "X12_540"
    X12_561 = "X12_561"
    X12_567 = "X12_567"
    X12_568 = "X12_568"
    X12_601 = "X12_601"
    X12_602 = "X12_602"
    X12_620 = "X12_620"
    X12_625 = "X12_625"
    X12_650 = "X12_650"
    X12_715 = "X12_715"
    X12_753 = "X12_753"
    X12_754 = "X12_754"
    X12_805 = "X12_805"
    X12_806 = "X12_806"
    X12_810 = "X12_810"
    X12_811 = "X12_811"
    X12_812 = "X12_812"
    X12_813 = "X12_813"
    X12_814 = "X12_814"
    X12_815 = "X12_815"
    X12_816 = "X12_816"
    X12_818 = "X12_818"
    X12_819 = "X12_819"
    X12_820 = "X12_820"
    X12_821 = "X12_821"
    X12_822 = "X12_822"
    X12_823 = "X12_823"
    X12_824 = "X12_824"
    X12_826 = "X12_826"
    X12_827 = "X12_827"
    X12_828 = "X12_828"
    X12_829 = "X12_829"
    X12_830 = "X12_830"
    X12_831 = "X12_831"
    X12_832 = "X12_832"
    X12_833 = "X12_833"
    X12_834 = "X12_834"
    X12_835 = "X12_835"
    X12_836 = "X12_836"
    X12_837 = "X12_837"
    X12_838 = "X12_838"
    X12_839 = "X12_839"
    X12_840 = "X12_840"
    X12_841 = "X12_841"
    X12_842 = "X12_842"
    X12_843 = "X12_843"
    X12_844 = "X12_844"
    X12_845 = "X12_845"
    X12_846 = "X12_846"
    X12_847 = "X12_847"
    X12_848 = "X12_848"
    X12_849 = "X12_849"
    X12_850 = "X12_850"
    X12_851 = "X12_851"
    X12_852 = "X12_852"
    X12_853 = "X12_853"
    X12_854 = "X12_854"
    X12_855 = "X12_855"
    X12_856 = "X12_856"
    X12_857 = "X12_857"
    X12_858 = "X12_858"
    X12_859 = "X12_859"
    X12_860 = "X12_860"
    X12_861 = "X12_861"
    X12_862 = "X12_862"
    X12_863 = "X12_863"
    X12_864 = "X12_864"
    X12_865 = "X12_865"
    X12_866 = "X12_866"
    X12_867 = "X12_867"
    X12_868 = "X12_868"
    X12_869 = "X12_869"
    X12_870 = "X12_870"
    X12_871 = "X12_871"
    X12_872 = "X12_872"
    X12_873 = "X12_873"
    X12_874 = "X12_874"
    X12_875 = "X12_875"
    X12_876 = "X12_876"
    X12_877 = "X12_877"
    X12_878 = "X12_878"
    X12_879 = "X12_879"
    X12_880 = "X12_880"
    X12_881 = "X12_881"
    X12_882 = "X12_882"
    X12_883 = "X12_883"
    X12_884 = "X12_884"
    X12_885 = "X12_885"
    X12_886 = "X12_886"
    X12_887 = "X12_887"
    X12_888 = "X12_888"
    X12_889 = "X12_889"
    X12_891 = "X12_891"
    X12_893 = "X12_893"
    X12_894 = "X12_894"
    X12_895 = "X12_895"
    X12_896 = "X12_896"
    X12_920 = "X12_920"
    X12_924 = "X12_924"
    X12_925 = "X12_925"
    X12_926 = "X12_926"
    X12_928 = "X12_928"
    X12_940 = "X12_940"
    X12_943 = "X12_943"
    X12_944 = "X12_944"
    X12_945 = "X12_945"
    X12_947 = "X12_947"
    X12_980 = "X12_980"
    X12_990 = "X12_990"
    X12_993 = "X12_993"
    X12_996 = "X12_996"
    X12_997 = "X12_997"
    X12_998 = "X12_998"
    X12_999 = "X12_999"
    X12_270_X279 = "X12_270_X279"
    X12_271_X279 = "X12_271_X279"
    X12_275_X210 = "X12_275_X210"
    X12_275_X211 = "X12_275_X211"
    X12_276_X212 = "X12_276_X212"
    X12_277_X212 = "X12_277_X212"
    X12_277_X214 = "X12_277_X214"
    X12_277_X364 = "X12_277_X364"
    X12_278_X217 = "X12_278_X217"
    X12_820_X218 = "X12_820_X218"
    X12_820_X306 = "X12_820_X306"
    X12_824_X186 = "X12_824_X186"
    X12_834_X220 = "X12_834_X220"
    X12_834_X307 = "X12_834_X307"
    X12_834_X318 = "X12_834_X318"
    X12_835_X221 = "X12_835_X221"
    X12_837_X222 = "X12_837_X222"
    X12_837_X223 = "X12_837_X223"
    X12_837_X224 = "X12_837_X224"
    X12_837_X291 = "X12_837_X291"
    X12_837_X292 = "X12_837_X292"
    X12_837_X298 = "X12_837_X298"
    X12_999_X231 = "X12_999_X231"


class X12Version:
    """X12Version enum values."""

    VERSION_4010 = "VERSION_4010"
    VERSION_4030 = "VERSION_4030"
    VERSION_4050 = "VERSION_4050"
    VERSION_4060 = "VERSION_4060"
    VERSION_5010 = "VERSION_5010"
    VERSION_5010_HIPAA = "VERSION_5010_HIPAA"


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

