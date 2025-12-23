"""PropertyTypes for AWS::SageMaker::CodeRepository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GitConfig(PropertyType):
    SECRET_ARN = "SecretArn"
    BRANCH = "Branch"
    REPOSITORY_URL = "RepositoryUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "branch": "Branch",
        "repository_url": "RepositoryUrl",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    branch: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

