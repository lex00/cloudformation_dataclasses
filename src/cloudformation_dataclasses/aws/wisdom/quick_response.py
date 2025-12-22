"""PropertyTypes for AWS::Wisdom::QuickResponse."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AssistantStatus:
    """AssistantStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"


class AssistantType:
    """AssistantType enum values."""

    AGENT = "AGENT"


class AssociationType:
    """AssociationType enum values."""

    KNOWLEDGE_BASE = "KNOWLEDGE_BASE"


class ContentStatus:
    """ContentStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"
    UPDATE_FAILED = "UPDATE_FAILED"


class ExternalSource:
    """ExternalSource enum values."""

    AMAZON_CONNECT = "AMAZON_CONNECT"


class FilterField:
    """FilterField enum values."""

    NAME = "NAME"


class FilterOperator:
    """FilterOperator enum values."""

    EQUALS = "EQUALS"


class ImportJobStatus:
    """ImportJobStatus enum values."""

    START_IN_PROGRESS = "START_IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"


class ImportJobType:
    """ImportJobType enum values."""

    QUICK_RESPONSES = "QUICK_RESPONSES"


class KnowledgeBaseStatus:
    """KnowledgeBaseStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"


class KnowledgeBaseType:
    """KnowledgeBaseType enum values."""

    EXTERNAL = "EXTERNAL"
    CUSTOM = "CUSTOM"
    QUICK_RESPONSES = "QUICK_RESPONSES"


class Order:
    """Order enum values."""

    ASC = "ASC"
    DESC = "DESC"


class Priority:
    """Priority enum values."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class QuickResponseFilterOperator:
    """QuickResponseFilterOperator enum values."""

    EQUALS = "EQUALS"
    PREFIX = "PREFIX"


class QuickResponseQueryOperator:
    """QuickResponseQueryOperator enum values."""

    CONTAINS = "CONTAINS"
    CONTAINS_AND_PREFIX = "CONTAINS_AND_PREFIX"


class QuickResponseStatus:
    """QuickResponseStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATED = "CREATED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETED = "DELETED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class RecommendationSourceType:
    """RecommendationSourceType enum values."""

    ISSUE_DETECTION = "ISSUE_DETECTION"
    RULE_EVALUATION = "RULE_EVALUATION"
    OTHER = "OTHER"


class RecommendationTriggerType:
    """RecommendationTriggerType enum values."""

    QUERY = "QUERY"


class RecommendationType:
    """RecommendationType enum values."""

    KNOWLEDGE_CONTENT = "KNOWLEDGE_CONTENT"


class RelevanceLevel:
    """RelevanceLevel enum values."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


@dataclass
class GroupingConfiguration(PropertyType):
    VALUES = "Values"
    CRITERIA = "Criteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "criteria": "Criteria",
    }

    values: Optional[Union[list[str], Ref]] = None
    criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuickResponseContentProvider(PropertyType):
    CONTENT = "Content"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
    }

    content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuickResponseContents(PropertyType):
    PLAIN_TEXT = "PlainText"
    MARKDOWN = "Markdown"

    _property_mappings: ClassVar[dict[str, str]] = {
        "plain_text": "PlainText",
        "markdown": "Markdown",
    }

    plain_text: Optional[QuickResponseContentProvider] = None
    markdown: Optional[QuickResponseContentProvider] = None

