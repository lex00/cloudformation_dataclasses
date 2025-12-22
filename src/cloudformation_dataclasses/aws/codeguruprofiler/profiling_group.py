"""PropertyTypes for AWS::CodeGuruProfiler::ProfilingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionGroup:
    """ActionGroup enum values."""

    AGENTPERMISSIONS = "agentPermissions"


class AgentParameterField:
    """AgentParameterField enum values."""

    SAMPLINGINTERVALINMILLISECONDS = "SamplingIntervalInMilliseconds"
    REPORTINGINTERVALINMILLISECONDS = "ReportingIntervalInMilliseconds"
    MINIMUMTIMEFORREPORTINGINMILLISECONDS = "MinimumTimeForReportingInMilliseconds"
    MEMORYUSAGELIMITPERCENT = "MemoryUsageLimitPercent"
    MAXSTACKDEPTH = "MaxStackDepth"


class AggregationPeriod:
    """AggregationPeriod enum values."""

    PT5M = "PT5M"
    PT1H = "PT1H"
    P1D = "P1D"


class ComputePlatform:
    """ComputePlatform enum values."""

    DEFAULT = "Default"
    AWSLAMBDA = "AWSLambda"


class EventPublisher:
    """EventPublisher enum values."""

    ANOMALYDETECTION = "AnomalyDetection"


class FeedbackType:
    """FeedbackType enum values."""

    POSITIVE = "Positive"
    NEGATIVE = "Negative"


class MetadataField:
    """MetadataField enum values."""

    COMPUTEPLATFORM = "ComputePlatform"
    AGENTID = "AgentId"
    AWSREQUESTID = "AwsRequestId"
    EXECUTIONENVIRONMENT = "ExecutionEnvironment"
    LAMBDAFUNCTIONARN = "LambdaFunctionArn"
    LAMBDAMEMORYLIMITINMB = "LambdaMemoryLimitInMB"
    LAMBDAREMAININGTIMEINMILLISECONDS = "LambdaRemainingTimeInMilliseconds"
    LAMBDATIMEGAPBETWEENINVOKESINMILLISECONDS = "LambdaTimeGapBetweenInvokesInMilliseconds"
    LAMBDAPREVIOUSEXECUTIONTIMEINMILLISECONDS = "LambdaPreviousExecutionTimeInMilliseconds"


class MetricType:
    """MetricType enum values."""

    AGGREGATEDRELATIVETOTALTIME = "AggregatedRelativeTotalTime"


class OrderBy:
    """OrderBy enum values."""

    TIMESTAMPDESCENDING = "TimestampDescending"
    TIMESTAMPASCENDING = "TimestampAscending"


@dataclass
class AgentPermissions(PropertyType):
    PRINCIPALS = "Principals"

    _property_mappings: ClassVar[dict[str, str]] = {
        "principals": "Principals",
    }

    principals: Optional[Union[list[str], Ref]] = None


@dataclass
class Channel(PropertyType):
    CHANNEL_URI = "channelUri"
    CHANNEL_ID = "channelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_uri": "channelUri",
        "channel_id": "channelId",
    }

    channel_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    channel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

