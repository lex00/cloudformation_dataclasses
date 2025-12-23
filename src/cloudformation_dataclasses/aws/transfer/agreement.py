"""PropertyTypes for AWS::Transfer::Agreement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomDirectories(PropertyType):
    FAILED_FILES_DIRECTORY = "FailedFilesDirectory"
    TEMPORARY_FILES_DIRECTORY = "TemporaryFilesDirectory"
    MDN_FILES_DIRECTORY = "MdnFilesDirectory"
    PAYLOAD_FILES_DIRECTORY = "PayloadFilesDirectory"
    STATUS_FILES_DIRECTORY = "StatusFilesDirectory"

    _property_mappings: ClassVar[dict[str, str]] = {
        "failed_files_directory": "FailedFilesDirectory",
        "temporary_files_directory": "TemporaryFilesDirectory",
        "mdn_files_directory": "MdnFilesDirectory",
        "payload_files_directory": "PayloadFilesDirectory",
        "status_files_directory": "StatusFilesDirectory",
    }

    failed_files_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    temporary_files_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mdn_files_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_files_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_files_directory: Optional[Union[str, Ref, GetAtt, Sub]] = None

