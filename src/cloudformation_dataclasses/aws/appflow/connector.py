"""PropertyTypes for AWS::AppFlow::Connector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectorProvisioningConfig(PropertyType):
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_": "Lambda",
    }

    lambda_: Optional[LambdaConnectorProvisioningConfig] = None


@dataclass
class LambdaConnectorProvisioningConfig(PropertyType):
    LAMBDA_ARN = "LambdaArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

