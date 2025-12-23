"""PropertyTypes for AWS::Personalize::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataSource(PropertyType):
    DATA_LOCATION = "DataLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_location": "DataLocation",
    }

    data_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetImportJob(PropertyType):
    DATASET_ARN = "DatasetArn"
    JOB_NAME = "JobName"
    DATASET_IMPORT_JOB_ARN = "DatasetImportJobArn"
    ROLE_ARN = "RoleArn"
    DATA_SOURCE = "DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_arn": "DatasetArn",
        "job_name": "JobName",
        "dataset_import_job_arn": "DatasetImportJobArn",
        "role_arn": "RoleArn",
        "data_source": "DataSource",
    }

    dataset_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataset_import_job_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source: Optional[DataSource] = None

