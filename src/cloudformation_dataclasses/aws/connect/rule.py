"""PropertyTypes for AWS::Connect::Rule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Actions(PropertyType):
    EVENT_BRIDGE_ACTIONS = "EventBridgeActions"
    UPDATE_CASE_ACTIONS = "UpdateCaseActions"
    CREATE_CASE_ACTIONS = "CreateCaseActions"
    ASSIGN_CONTACT_CATEGORY_ACTIONS = "AssignContactCategoryActions"
    TASK_ACTIONS = "TaskActions"
    SUBMIT_AUTO_EVALUATION_ACTIONS = "SubmitAutoEvaluationActions"
    SEND_NOTIFICATION_ACTIONS = "SendNotificationActions"
    END_ASSOCIATED_TASKS_ACTIONS = "EndAssociatedTasksActions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bridge_actions": "EventBridgeActions",
        "update_case_actions": "UpdateCaseActions",
        "create_case_actions": "CreateCaseActions",
        "assign_contact_category_actions": "AssignContactCategoryActions",
        "task_actions": "TaskActions",
        "submit_auto_evaluation_actions": "SubmitAutoEvaluationActions",
        "send_notification_actions": "SendNotificationActions",
        "end_associated_tasks_actions": "EndAssociatedTasksActions",
    }

    event_bridge_actions: Optional[list[EventBridgeAction]] = None
    update_case_actions: Optional[list[UpdateCaseAction]] = None
    create_case_actions: Optional[list[CreateCaseAction]] = None
    assign_contact_category_actions: Optional[Union[list[dict[str, Any]], Ref]] = None
    task_actions: Optional[list[TaskAction]] = None
    submit_auto_evaluation_actions: Optional[list[SubmitAutoEvaluationAction]] = None
    send_notification_actions: Optional[list[SendNotificationAction]] = None
    end_associated_tasks_actions: Optional[Union[list[dict[str, Any]], Ref]] = None


@dataclass
class CreateCaseAction(PropertyType):
    FIELDS = "Fields"
    TEMPLATE_ID = "TemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fields": "Fields",
        "template_id": "TemplateId",
    }

    fields: Optional[list[Field]] = None
    template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeAction(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Field(PropertyType):
    VALUE = "Value"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "id": "Id",
    }

    value: Optional[FieldValue] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FieldValue(PropertyType):
    DOUBLE_VALUE = "DoubleValue"
    BOOLEAN_VALUE = "BooleanValue"
    STRING_VALUE = "StringValue"
    EMPTY_VALUE = "EmptyValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "double_value": "DoubleValue",
        "boolean_value": "BooleanValue",
        "string_value": "StringValue",
        "empty_value": "EmptyValue",
    }

    double_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    boolean_value: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    empty_value: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class NotificationRecipientType(PropertyType):
    USER_TAGS = "UserTags"
    USER_ARNS = "UserArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_tags": "UserTags",
        "user_arns": "UserArns",
    }

    user_tags: Optional[dict[str, str]] = None
    user_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class Reference(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, ReferenceType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleTriggerEventSource(PropertyType):
    INTEGRATION_ASSOCIATION_ARN = "IntegrationAssociationArn"
    EVENT_SOURCE_NAME = "EventSourceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "integration_association_arn": "IntegrationAssociationArn",
        "event_source_name": "EventSourceName",
    }

    integration_association_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_source_name: Optional[Union[str, EventSourceName, Ref, GetAtt, Sub]] = None


@dataclass
class SendNotificationAction(PropertyType):
    DELIVERY_METHOD = "DeliveryMethod"
    CONTENT_TYPE = "ContentType"
    CONTENT = "Content"
    RECIPIENT = "Recipient"
    SUBJECT = "Subject"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_method": "DeliveryMethod",
        "content_type": "ContentType",
        "content": "Content",
        "recipient": "Recipient",
        "subject": "Subject",
    }

    delivery_method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recipient: Optional[NotificationRecipientType] = None
    subject: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubmitAutoEvaluationAction(PropertyType):
    EVALUATION_FORM_ARN = "EvaluationFormArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "evaluation_form_arn": "EvaluationFormArn",
    }

    evaluation_form_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskAction(PropertyType):
    DESCRIPTION = "Description"
    REFERENCES = "References"
    CONTACT_FLOW_ARN = "ContactFlowArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "references": "References",
        "contact_flow_arn": "ContactFlowArn",
        "name": "Name",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    references: Optional[dict[str, Any]] = None
    contact_flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateCaseAction(PropertyType):
    FIELDS = "Fields"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fields": "Fields",
    }

    fields: Optional[list[Field]] = None

