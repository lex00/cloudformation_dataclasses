"""PropertyTypes for AWS::DataZone::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataSourceConfigurationInput(PropertyType):
    REDSHIFT_RUN_CONFIGURATION = "RedshiftRunConfiguration"
    GLUE_RUN_CONFIGURATION = "GlueRunConfiguration"
    SAGE_MAKER_RUN_CONFIGURATION = "SageMakerRunConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "redshift_run_configuration": "RedshiftRunConfiguration",
        "glue_run_configuration": "GlueRunConfiguration",
        "sage_maker_run_configuration": "SageMakerRunConfiguration",
    }

    redshift_run_configuration: Optional[RedshiftRunConfigurationInput] = None
    glue_run_configuration: Optional[GlueRunConfigurationInput] = None
    sage_maker_run_configuration: Optional[SageMakerRunConfigurationInput] = None


@dataclass
class FilterExpression(PropertyType):
    TYPE = "Type"
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "expression": "Expression",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FormInput(PropertyType):
    TYPE_IDENTIFIER = "TypeIdentifier"
    TYPE_REVISION = "TypeRevision"
    CONTENT = "Content"
    FORM_NAME = "FormName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_identifier": "TypeIdentifier",
        "type_revision": "TypeRevision",
        "content": "Content",
        "form_name": "FormName",
    }

    type_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_revision: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content: Optional[Union[str, Ref, GetAtt, Sub]] = None
    form_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GlueRunConfigurationInput(PropertyType):
    DATA_ACCESS_ROLE = "DataAccessRole"
    AUTO_IMPORT_DATA_QUALITY_RESULT = "AutoImportDataQualityResult"
    RELATIONAL_FILTER_CONFIGURATIONS = "RelationalFilterConfigurations"
    CATALOG_NAME = "CatalogName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_access_role": "DataAccessRole",
        "auto_import_data_quality_result": "AutoImportDataQualityResult",
        "relational_filter_configurations": "RelationalFilterConfigurations",
        "catalog_name": "CatalogName",
    }

    data_access_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_import_data_quality_result: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    relational_filter_configurations: Optional[list[RelationalFilterConfiguration]] = None
    catalog_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecommendationConfiguration(PropertyType):
    ENABLE_BUSINESS_NAME_GENERATION = "EnableBusinessNameGeneration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_business_name_generation": "EnableBusinessNameGeneration",
    }

    enable_business_name_generation: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftClusterStorage(PropertyType):
    CLUSTER_NAME = "ClusterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_name": "ClusterName",
    }

    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftCredentialConfiguration(PropertyType):
    SECRET_MANAGER_ARN = "SecretManagerArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_manager_arn": "SecretManagerArn",
    }

    secret_manager_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftRunConfigurationInput(PropertyType):
    DATA_ACCESS_ROLE = "DataAccessRole"
    RELATIONAL_FILTER_CONFIGURATIONS = "RelationalFilterConfigurations"
    REDSHIFT_CREDENTIAL_CONFIGURATION = "RedshiftCredentialConfiguration"
    REDSHIFT_STORAGE = "RedshiftStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_access_role": "DataAccessRole",
        "relational_filter_configurations": "RelationalFilterConfigurations",
        "redshift_credential_configuration": "RedshiftCredentialConfiguration",
        "redshift_storage": "RedshiftStorage",
    }

    data_access_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    relational_filter_configurations: Optional[list[RelationalFilterConfiguration]] = None
    redshift_credential_configuration: Optional[RedshiftCredentialConfiguration] = None
    redshift_storage: Optional[RedshiftStorage] = None


@dataclass
class RedshiftServerlessStorage(PropertyType):
    WORKGROUP_NAME = "WorkgroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_name": "WorkgroupName",
    }

    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftStorage(PropertyType):
    REDSHIFT_CLUSTER_SOURCE = "RedshiftClusterSource"
    REDSHIFT_SERVERLESS_SOURCE = "RedshiftServerlessSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "redshift_cluster_source": "RedshiftClusterSource",
        "redshift_serverless_source": "RedshiftServerlessSource",
    }

    redshift_cluster_source: Optional[RedshiftClusterStorage] = None
    redshift_serverless_source: Optional[RedshiftServerlessStorage] = None


@dataclass
class RelationalFilterConfiguration(PropertyType):
    FILTER_EXPRESSIONS = "FilterExpressions"
    DATABASE_NAME = "DatabaseName"
    SCHEMA_NAME = "SchemaName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_expressions": "FilterExpressions",
        "database_name": "DatabaseName",
        "schema_name": "SchemaName",
    }

    filter_expressions: Optional[list[FilterExpression]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SageMakerRunConfigurationInput(PropertyType):
    TRACKING_ASSETS = "TrackingAssets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tracking_assets": "TrackingAssets",
    }

    tracking_assets: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class ScheduleConfiguration(PropertyType):
    TIMEZONE = "Timezone"
    SCHEDULE = "Schedule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timezone": "Timezone",
        "schedule": "Schedule",
    }

    timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule: Optional[Union[str, Ref, GetAtt, Sub]] = None

