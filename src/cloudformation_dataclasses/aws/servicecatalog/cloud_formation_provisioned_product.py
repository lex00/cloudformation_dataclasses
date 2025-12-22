"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProvisionedProduct."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessLevelFilterKey:
    """AccessLevelFilterKey enum values."""

    ACCOUNT = "Account"
    ROLE = "Role"
    USER = "User"


class AccessStatus:
    """AccessStatus enum values."""

    ENABLED = "ENABLED"
    UNDER_CHANGE = "UNDER_CHANGE"
    DISABLED = "DISABLED"


class ChangeAction:
    """ChangeAction enum values."""

    ADD = "ADD"
    MODIFY = "MODIFY"
    REMOVE = "REMOVE"


class CopyOption:
    """CopyOption enum values."""

    COPYTAGS = "CopyTags"


class CopyProductStatus:
    """CopyProductStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class DescribePortfolioShareType:
    """DescribePortfolioShareType enum values."""

    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"
    ORGANIZATIONAL_UNIT = "ORGANIZATIONAL_UNIT"
    ORGANIZATION_MEMBER_ACCOUNT = "ORGANIZATION_MEMBER_ACCOUNT"


class EngineWorkflowStatus:
    """EngineWorkflowStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class EvaluationType:
    """EvaluationType enum values."""

    STATIC = "STATIC"
    DYNAMIC = "DYNAMIC"


class LastSyncStatus:
    """LastSyncStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class OrganizationNodeType:
    """OrganizationNodeType enum values."""

    ORGANIZATION = "ORGANIZATION"
    ORGANIZATIONAL_UNIT = "ORGANIZATIONAL_UNIT"
    ACCOUNT = "ACCOUNT"


class PortfolioShareType:
    """PortfolioShareType enum values."""

    IMPORTED = "IMPORTED"
    AWS_SERVICECATALOG = "AWS_SERVICECATALOG"
    AWS_ORGANIZATIONS = "AWS_ORGANIZATIONS"


class PrincipalType:
    """PrincipalType enum values."""

    IAM = "IAM"
    IAM_PATTERN = "IAM_PATTERN"


class ProductSource:
    """ProductSource enum values."""

    ACCOUNT = "ACCOUNT"


class ProductType:
    """ProductType enum values."""

    CLOUD_FORMATION_TEMPLATE = "CLOUD_FORMATION_TEMPLATE"
    MARKETPLACE = "MARKETPLACE"
    TERRAFORM_OPEN_SOURCE = "TERRAFORM_OPEN_SOURCE"
    TERRAFORM_CLOUD = "TERRAFORM_CLOUD"
    EXTERNAL = "EXTERNAL"


class ProductViewFilterBy:
    """ProductViewFilterBy enum values."""

    FULLTEXTSEARCH = "FullTextSearch"
    OWNER = "Owner"
    PRODUCTTYPE = "ProductType"
    SOURCEPRODUCTID = "SourceProductId"


class ProductViewSortBy:
    """ProductViewSortBy enum values."""

    TITLE = "Title"
    VERSIONCOUNT = "VersionCount"
    CREATIONDATE = "CreationDate"


class PropertyKey:
    """PropertyKey enum values."""

    OWNER = "OWNER"
    LAUNCH_ROLE = "LAUNCH_ROLE"


class ProvisionedProductPlanStatus:
    """ProvisionedProductPlanStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_SUCCESS = "CREATE_SUCCESS"
    CREATE_FAILED = "CREATE_FAILED"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_SUCCESS = "EXECUTE_SUCCESS"
    EXECUTE_FAILED = "EXECUTE_FAILED"


class ProvisionedProductPlanType:
    """ProvisionedProductPlanType enum values."""

    CLOUDFORMATION = "CLOUDFORMATION"


class ProvisionedProductStatus:
    """ProvisionedProductStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UNDER_CHANGE = "UNDER_CHANGE"
    TAINTED = "TAINTED"
    ERROR = "ERROR"
    PLAN_IN_PROGRESS = "PLAN_IN_PROGRESS"


class ProvisionedProductViewFilterBy:
    """ProvisionedProductViewFilterBy enum values."""

    SEARCHQUERY = "SearchQuery"


class ProvisioningArtifactGuidance:
    """ProvisioningArtifactGuidance enum values."""

    DEFAULT = "DEFAULT"
    DEPRECATED = "DEPRECATED"


class ProvisioningArtifactPropertyName:
    """ProvisioningArtifactPropertyName enum values."""

    ID = "Id"


class ProvisioningArtifactType:
    """ProvisioningArtifactType enum values."""

    CLOUD_FORMATION_TEMPLATE = "CLOUD_FORMATION_TEMPLATE"
    MARKETPLACE_AMI = "MARKETPLACE_AMI"
    MARKETPLACE_CAR = "MARKETPLACE_CAR"
    TERRAFORM_OPEN_SOURCE = "TERRAFORM_OPEN_SOURCE"
    TERRAFORM_CLOUD = "TERRAFORM_CLOUD"
    EXTERNAL = "EXTERNAL"


class RecordStatus:
    """RecordStatus enum values."""

    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    IN_PROGRESS_IN_ERROR = "IN_PROGRESS_IN_ERROR"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class Replacement:
    """Replacement enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"
    CONDITIONAL = "CONDITIONAL"


class RequiresRecreation:
    """RequiresRecreation enum values."""

    NEVER = "NEVER"
    CONDITIONALLY = "CONDITIONALLY"
    ALWAYS = "ALWAYS"


class ResourceAttribute:
    """ResourceAttribute enum values."""

    PROPERTIES = "PROPERTIES"
    METADATA = "METADATA"
    CREATIONPOLICY = "CREATIONPOLICY"
    UPDATEPOLICY = "UPDATEPOLICY"
    DELETIONPOLICY = "DELETIONPOLICY"
    TAGS = "TAGS"


class ServiceActionAssociationErrorCode:
    """ServiceActionAssociationErrorCode enum values."""

    DUPLICATE_RESOURCE = "DUPLICATE_RESOURCE"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    THROTTLING = "THROTTLING"
    INVALID_PARAMETER = "INVALID_PARAMETER"


class ServiceActionDefinitionKey:
    """ServiceActionDefinitionKey enum values."""

    NAME = "Name"
    VERSION = "Version"
    ASSUMEROLE = "AssumeRole"
    PARAMETERS = "Parameters"


class ServiceActionDefinitionType:
    """ServiceActionDefinitionType enum values."""

    SSM_AUTOMATION = "SSM_AUTOMATION"


class ShareStatus:
    """ShareStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"
    ERROR = "ERROR"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SourceType:
    """SourceType enum values."""

    CODESTAR = "CODESTAR"


class StackInstanceStatus:
    """StackInstanceStatus enum values."""

    CURRENT = "CURRENT"
    OUTDATED = "OUTDATED"
    INOPERABLE = "INOPERABLE"


class StackSetOperationType:
    """StackSetOperationType enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class Status:
    """Status enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    FAILED = "FAILED"


@dataclass
class ProvisioningParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisioningPreferences(PropertyType):
    STACK_SET_ACCOUNTS = "StackSetAccounts"
    STACK_SET_FAILURE_TOLERANCE_COUNT = "StackSetFailureToleranceCount"
    STACK_SET_MAX_CONCURRENCY_PERCENTAGE = "StackSetMaxConcurrencyPercentage"
    STACK_SET_MAX_CONCURRENCY_COUNT = "StackSetMaxConcurrencyCount"
    STACK_SET_REGIONS = "StackSetRegions"
    STACK_SET_OPERATION_TYPE = "StackSetOperationType"
    STACK_SET_FAILURE_TOLERANCE_PERCENTAGE = "StackSetFailureTolerancePercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stack_set_accounts": "StackSetAccounts",
        "stack_set_failure_tolerance_count": "StackSetFailureToleranceCount",
        "stack_set_max_concurrency_percentage": "StackSetMaxConcurrencyPercentage",
        "stack_set_max_concurrency_count": "StackSetMaxConcurrencyCount",
        "stack_set_regions": "StackSetRegions",
        "stack_set_operation_type": "StackSetOperationType",
        "stack_set_failure_tolerance_percentage": "StackSetFailureTolerancePercentage",
    }

    stack_set_accounts: Optional[Union[list[str], Ref]] = None
    stack_set_failure_tolerance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stack_set_max_concurrency_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stack_set_max_concurrency_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stack_set_regions: Optional[Union[list[str], Ref]] = None
    stack_set_operation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stack_set_failure_tolerance_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None

