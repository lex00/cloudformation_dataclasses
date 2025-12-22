"""PropertyTypes for AWS::IoTThingsGraph::FlowTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class DefinitionLanguage:
    """DefinitionLanguage enum values."""

    GRAPHQL = "GRAPHQL"


class DeploymentTarget:
    """DeploymentTarget enum values."""

    GREENGRASS = "GREENGRASS"
    CLOUD = "CLOUD"


class EntityFilterName:
    """EntityFilterName enum values."""

    NAME = "NAME"
    NAMESPACE = "NAMESPACE"
    SEMANTIC_TYPE_PATH = "SEMANTIC_TYPE_PATH"
    REFERENCED_ENTITY_ID = "REFERENCED_ENTITY_ID"


class EntityType:
    """EntityType enum values."""

    DEVICE = "DEVICE"
    SERVICE = "SERVICE"
    DEVICE_MODEL = "DEVICE_MODEL"
    CAPABILITY = "CAPABILITY"
    STATE = "STATE"
    ACTION = "ACTION"
    EVENT = "EVENT"
    PROPERTY = "PROPERTY"
    MAPPING = "MAPPING"
    ENUM = "ENUM"


class FlowExecutionEventType:
    """FlowExecutionEventType enum values."""

    EXECUTION_STARTED = "EXECUTION_STARTED"
    EXECUTION_FAILED = "EXECUTION_FAILED"
    EXECUTION_ABORTED = "EXECUTION_ABORTED"
    EXECUTION_SUCCEEDED = "EXECUTION_SUCCEEDED"
    STEP_STARTED = "STEP_STARTED"
    STEP_FAILED = "STEP_FAILED"
    STEP_SUCCEEDED = "STEP_SUCCEEDED"
    ACTIVITY_SCHEDULED = "ACTIVITY_SCHEDULED"
    ACTIVITY_STARTED = "ACTIVITY_STARTED"
    ACTIVITY_FAILED = "ACTIVITY_FAILED"
    ACTIVITY_SUCCEEDED = "ACTIVITY_SUCCEEDED"
    START_FLOW_EXECUTION_TASK = "START_FLOW_EXECUTION_TASK"
    SCHEDULE_NEXT_READY_STEPS_TASK = "SCHEDULE_NEXT_READY_STEPS_TASK"
    THING_ACTION_TASK = "THING_ACTION_TASK"
    THING_ACTION_TASK_FAILED = "THING_ACTION_TASK_FAILED"
    THING_ACTION_TASK_SUCCEEDED = "THING_ACTION_TASK_SUCCEEDED"
    ACKNOWLEDGE_TASK_MESSAGE = "ACKNOWLEDGE_TASK_MESSAGE"


class FlowExecutionStatus:
    """FlowExecutionStatus enum values."""

    RUNNING = "RUNNING"
    ABORTED = "ABORTED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class FlowTemplateFilterName:
    """FlowTemplateFilterName enum values."""

    DEVICE_MODEL_ID = "DEVICE_MODEL_ID"


class NamespaceDeletionStatus:
    """NamespaceDeletionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class NamespaceDeletionStatusErrorCodes:
    """NamespaceDeletionStatusErrorCodes enum values."""

    VALIDATION_FAILED = "VALIDATION_FAILED"


class SystemInstanceDeploymentStatus:
    """SystemInstanceDeploymentStatus enum values."""

    NOT_DEPLOYED = "NOT_DEPLOYED"
    BOOTSTRAP = "BOOTSTRAP"
    DEPLOY_IN_PROGRESS = "DEPLOY_IN_PROGRESS"
    DEPLOYED_IN_TARGET = "DEPLOYED_IN_TARGET"
    UNDEPLOY_IN_PROGRESS = "UNDEPLOY_IN_PROGRESS"
    FAILED = "FAILED"
    PENDING_DELETE = "PENDING_DELETE"
    DELETED_IN_TARGET = "DELETED_IN_TARGET"


class SystemInstanceFilterName:
    """SystemInstanceFilterName enum values."""

    SYSTEM_TEMPLATE_ID = "SYSTEM_TEMPLATE_ID"
    STATUS = "STATUS"
    GREENGRASS_GROUP_NAME = "GREENGRASS_GROUP_NAME"


class SystemTemplateFilterName:
    """SystemTemplateFilterName enum values."""

    FLOW_TEMPLATE_ID = "FLOW_TEMPLATE_ID"


class UploadStatus:
    """UploadStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclass
class DefinitionDocument(PropertyType):
    LANGUAGE = "Language"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language": "Language",
        "text": "Text",
    }

    language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None

