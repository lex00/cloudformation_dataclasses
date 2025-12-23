"""PropertyTypes for AWS::MWAA::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoggingConfiguration(PropertyType):
    SCHEDULER_LOGS = "SchedulerLogs"
    TASK_LOGS = "TaskLogs"
    DAG_PROCESSING_LOGS = "DagProcessingLogs"
    WEBSERVER_LOGS = "WebserverLogs"
    WORKER_LOGS = "WorkerLogs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scheduler_logs": "SchedulerLogs",
        "task_logs": "TaskLogs",
        "dag_processing_logs": "DagProcessingLogs",
        "webserver_logs": "WebserverLogs",
        "worker_logs": "WorkerLogs",
    }

    scheduler_logs: Optional[ModuleLoggingConfiguration] = None
    task_logs: Optional[ModuleLoggingConfiguration] = None
    dag_processing_logs: Optional[ModuleLoggingConfiguration] = None
    webserver_logs: Optional[ModuleLoggingConfiguration] = None
    worker_logs: Optional[ModuleLoggingConfiguration] = None


@dataclass
class ModuleLoggingConfiguration(PropertyType):
    CLOUD_WATCH_LOG_GROUP_ARN = "CloudWatchLogGroupArn"
    ENABLED = "Enabled"
    LOG_LEVEL = "LogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_log_group_arn": "CloudWatchLogGroupArn",
        "enabled": "Enabled",
        "log_level": "LogLevel",
    }

    cloud_watch_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, LoggingLevel, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

