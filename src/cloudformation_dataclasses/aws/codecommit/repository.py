"""PropertyTypes for AWS::CodeCommit::Repository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApprovalState:
    """ApprovalState enum values."""

    APPROVE = "APPROVE"
    REVOKE = "REVOKE"


class BatchGetRepositoriesErrorCodeEnum:
    """BatchGetRepositoriesErrorCodeEnum enum values."""

    ENCRYPTIONINTEGRITYCHECKSFAILEDEXCEPTION = "EncryptionIntegrityChecksFailedException"
    ENCRYPTIONKEYACCESSDENIEDEXCEPTION = "EncryptionKeyAccessDeniedException"
    ENCRYPTIONKEYDISABLEDEXCEPTION = "EncryptionKeyDisabledException"
    ENCRYPTIONKEYNOTFOUNDEXCEPTION = "EncryptionKeyNotFoundException"
    ENCRYPTIONKEYUNAVAILABLEEXCEPTION = "EncryptionKeyUnavailableException"
    REPOSITORYDOESNOTEXISTEXCEPTION = "RepositoryDoesNotExistException"


class ChangeTypeEnum:
    """ChangeTypeEnum enum values."""

    A = "A"
    M = "M"
    D = "D"


class ConflictDetailLevelTypeEnum:
    """ConflictDetailLevelTypeEnum enum values."""

    FILE_LEVEL = "FILE_LEVEL"
    LINE_LEVEL = "LINE_LEVEL"


class ConflictResolutionStrategyTypeEnum:
    """ConflictResolutionStrategyTypeEnum enum values."""

    NONE = "NONE"
    ACCEPT_SOURCE = "ACCEPT_SOURCE"
    ACCEPT_DESTINATION = "ACCEPT_DESTINATION"
    AUTOMERGE = "AUTOMERGE"


class FileModeTypeEnum:
    """FileModeTypeEnum enum values."""

    EXECUTABLE = "EXECUTABLE"
    NORMAL = "NORMAL"
    SYMLINK = "SYMLINK"


class MergeOptionTypeEnum:
    """MergeOptionTypeEnum enum values."""

    FAST_FORWARD_MERGE = "FAST_FORWARD_MERGE"
    SQUASH_MERGE = "SQUASH_MERGE"
    THREE_WAY_MERGE = "THREE_WAY_MERGE"


class ObjectTypeEnum:
    """ObjectTypeEnum enum values."""

    FILE = "FILE"
    DIRECTORY = "DIRECTORY"
    GIT_LINK = "GIT_LINK"
    SYMBOLIC_LINK = "SYMBOLIC_LINK"


class OrderEnum:
    """OrderEnum enum values."""

    ASCENDING = "ascending"
    DESCENDING = "descending"


class OverrideStatus:
    """OverrideStatus enum values."""

    OVERRIDE = "OVERRIDE"
    REVOKE = "REVOKE"


class PullRequestEventType:
    """PullRequestEventType enum values."""

    PULL_REQUEST_CREATED = "PULL_REQUEST_CREATED"
    PULL_REQUEST_STATUS_CHANGED = "PULL_REQUEST_STATUS_CHANGED"
    PULL_REQUEST_SOURCE_REFERENCE_UPDATED = "PULL_REQUEST_SOURCE_REFERENCE_UPDATED"
    PULL_REQUEST_MERGE_STATE_CHANGED = "PULL_REQUEST_MERGE_STATE_CHANGED"
    PULL_REQUEST_APPROVAL_RULE_CREATED = "PULL_REQUEST_APPROVAL_RULE_CREATED"
    PULL_REQUEST_APPROVAL_RULE_UPDATED = "PULL_REQUEST_APPROVAL_RULE_UPDATED"
    PULL_REQUEST_APPROVAL_RULE_DELETED = "PULL_REQUEST_APPROVAL_RULE_DELETED"
    PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN = "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN"
    PULL_REQUEST_APPROVAL_STATE_CHANGED = "PULL_REQUEST_APPROVAL_STATE_CHANGED"


class PullRequestStatusEnum:
    """PullRequestStatusEnum enum values."""

    OPEN = "OPEN"
    CLOSED = "CLOSED"


class RelativeFileVersionEnum:
    """RelativeFileVersionEnum enum values."""

    BEFORE = "BEFORE"
    AFTER = "AFTER"


class ReplacementTypeEnum:
    """ReplacementTypeEnum enum values."""

    KEEP_BASE = "KEEP_BASE"
    KEEP_SOURCE = "KEEP_SOURCE"
    KEEP_DESTINATION = "KEEP_DESTINATION"
    USE_NEW_CONTENT = "USE_NEW_CONTENT"


class RepositoryTriggerEventEnum:
    """RepositoryTriggerEventEnum enum values."""

    ALL = "all"
    UPDATEREFERENCE = "updateReference"
    CREATEREFERENCE = "createReference"
    DELETEREFERENCE = "deleteReference"


class SortByEnum:
    """SortByEnum enum values."""

    REPOSITORYNAME = "repositoryName"
    LASTMODIFIEDDATE = "lastModifiedDate"


@dataclass
class Code(PropertyType):
    S3 = "S3"
    BRANCH_NAME = "BranchName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "branch_name": "BranchName",
    }

    s3: Optional[S3] = None
    branch_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RepositoryTrigger(PropertyType):
    EVENTS = "Events"
    BRANCHES = "Branches"
    CUSTOM_DATA = "CustomData"
    DESTINATION_ARN = "DestinationArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
        "branches": "Branches",
        "custom_data": "CustomData",
        "destination_arn": "DestinationArn",
        "name": "Name",
    }

    events: Optional[Union[list[str], Ref]] = None
    branches: Optional[Union[list[str], Ref]] = None
    custom_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3(PropertyType):
    OBJECT_VERSION = "ObjectVersion"
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_version": "ObjectVersion",
        "bucket": "Bucket",
        "key": "Key",
    }

    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

