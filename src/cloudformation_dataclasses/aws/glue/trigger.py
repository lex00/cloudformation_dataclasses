"""PropertyTypes for AWS::Glue::Trigger."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_property": "NotificationProperty",
        "crawler_name": "CrawlerName",
        "timeout": "Timeout",
        "job_name": "JobName",
        "arguments": "Arguments",
        "security_configuration": "SecurityConfiguration",
    }

    notification_property: Optional[NotificationProperty] = None
    crawler_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arguments: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    security_configuration: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Condition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "crawler_name": "CrawlerName",
        "state": "State",
        "crawl_state": "CrawlState",
        "logical_operator": "LogicalOperator",
        "job_name": "JobName",
    }

    crawler_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, JobRunState, Ref, GetAtt, Sub]] = None
    crawl_state: Optional[Union[str, CrawlState, Ref, GetAtt, Sub]] = None
    logical_operator: Optional[Union[str, LogicalOperator, Ref, GetAtt, Sub]] = None
    job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventBatchingCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_size": "BatchSize",
        "batch_window": "BatchWindow",
    }

    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    batch_window: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notify_delay_after": "NotifyDelayAfter",
    }

    notify_delay_after: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Predicate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logical": "Logical",
        "conditions": "Conditions",
    }

    logical: Optional[Union[str, Logical, Ref, GetAtt, Sub]] = None
    conditions: Optional[list[Condition]] = None

