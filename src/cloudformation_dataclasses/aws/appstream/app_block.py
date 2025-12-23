"""PropertyTypes for AWS::AppStream::AppBlock."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class S3Location(PropertyType):
    S3_BUCKET = "S3Bucket"
    S3_KEY = "S3Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "s3_key": "S3Key",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScriptDetails(PropertyType):
    TIMEOUT_IN_SECONDS = "TimeoutInSeconds"
    SCRIPT_S3_LOCATION = "ScriptS3Location"
    EXECUTABLE_PATH = "ExecutablePath"
    EXECUTABLE_PARAMETERS = "ExecutableParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_in_seconds": "TimeoutInSeconds",
        "script_s3_location": "ScriptS3Location",
        "executable_path": "ExecutablePath",
        "executable_parameters": "ExecutableParameters",
    }

    timeout_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    script_s3_location: Optional[S3Location] = None
    executable_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    executable_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None

