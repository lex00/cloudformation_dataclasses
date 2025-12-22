"""PropertyTypes for AWS::QuickSight::DataSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionConnectorErrorType:
    """ActionConnectorErrorType enum values."""

    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class ActionConnectorSearchFilterNameEnum:
    """ActionConnectorSearchFilterNameEnum enum values."""

    ACTION_CONNECTOR_NAME = "ACTION_CONNECTOR_NAME"
    ACTION_CONNECTOR_TYPE = "ACTION_CONNECTOR_TYPE"
    QUICKSIGHT_OWNER = "QUICKSIGHT_OWNER"
    QUICKSIGHT_VIEWER_OR_OWNER = "QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"


class ActionConnectorType:
    """ActionConnectorType enum values."""

    GENERIC_HTTP = "GENERIC_HTTP"
    SERVICENOW_NOW_PLATFORM = "SERVICENOW_NOW_PLATFORM"
    SALESFORCE_CRM = "SALESFORCE_CRM"
    MICROSOFT_OUTLOOK = "MICROSOFT_OUTLOOK"
    PAGERDUTY_ADVANCE = "PAGERDUTY_ADVANCE"
    JIRA_CLOUD = "JIRA_CLOUD"
    ATLASSIAN_CONFLUENCE = "ATLASSIAN_CONFLUENCE"
    AMAZON_S3 = "AMAZON_S3"
    AMAZON_BEDROCK_AGENT_RUNTIME = "AMAZON_BEDROCK_AGENT_RUNTIME"
    AMAZON_BEDROCK_RUNTIME = "AMAZON_BEDROCK_RUNTIME"
    AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME = "AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME"
    AMAZON_TEXTRACT = "AMAZON_TEXTRACT"
    AMAZON_COMPREHEND = "AMAZON_COMPREHEND"
    AMAZON_COMPREHEND_MEDICAL = "AMAZON_COMPREHEND_MEDICAL"
    MICROSOFT_ONEDRIVE = "MICROSOFT_ONEDRIVE"
    MICROSOFT_SHAREPOINT = "MICROSOFT_SHAREPOINT"
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    SAP_BUSINESSPARTNER = "SAP_BUSINESSPARTNER"
    SAP_PRODUCTMASTERDATA = "SAP_PRODUCTMASTERDATA"
    SAP_PHYSICALINVENTORY = "SAP_PHYSICALINVENTORY"
    SAP_BILLOFMATERIALS = "SAP_BILLOFMATERIALS"
    SAP_MATERIALSTOCK = "SAP_MATERIALSTOCK"
    ZENDESK_SUITE = "ZENDESK_SUITE"
    SMARTSHEET = "SMARTSHEET"
    SLACK = "SLACK"
    ASANA = "ASANA"
    BAMBOO_HR = "BAMBOO_HR"


class AggType:
    """AggType enum values."""

    SUM = "SUM"
    MIN = "MIN"
    MAX = "MAX"
    COUNT = "COUNT"
    AVERAGE = "AVERAGE"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    VAR = "VAR"
    VARP = "VARP"
    PERCENTILE = "PERCENTILE"
    MEDIAN = "MEDIAN"
    PTD_SUM = "PTD_SUM"
    PTD_MIN = "PTD_MIN"
    PTD_MAX = "PTD_MAX"
    PTD_COUNT = "PTD_COUNT"
    PTD_DISTINCT_COUNT = "PTD_DISTINCT_COUNT"
    PTD_AVERAGE = "PTD_AVERAGE"
    COLUMN = "COLUMN"
    CUSTOM = "CUSTOM"


class AnalysisErrorType:
    """AnalysisErrorType enum values."""

    ACCESS_DENIED = "ACCESS_DENIED"
    SOURCE_NOT_FOUND = "SOURCE_NOT_FOUND"
    DATA_SET_NOT_FOUND = "DATA_SET_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    PARAMETER_VALUE_INCOMPATIBLE = "PARAMETER_VALUE_INCOMPATIBLE"
    PARAMETER_TYPE_INVALID = "PARAMETER_TYPE_INVALID"
    PARAMETER_NOT_FOUND = "PARAMETER_NOT_FOUND"
    COLUMN_TYPE_MISMATCH = "COLUMN_TYPE_MISMATCH"
    COLUMN_GEOGRAPHIC_ROLE_MISMATCH = "COLUMN_GEOGRAPHIC_ROLE_MISMATCH"
    COLUMN_REPLACEMENT_MISSING = "COLUMN_REPLACEMENT_MISSING"


class AnalysisFilterAttribute:
    """AnalysisFilterAttribute enum values."""

    QUICKSIGHT_USER = "QUICKSIGHT_USER"
    QUICKSIGHT_VIEWER_OR_OWNER = "QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    QUICKSIGHT_OWNER = "QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    ANALYSIS_NAME = "ANALYSIS_NAME"


class AnchorOption:
    """AnchorOption enum values."""

    NOW = "NOW"


class AnchorType:
    """AnchorType enum values."""

    TODAY = "TODAY"


class AnonymousUserDashboardEmbeddingConfigurationDisabledFeature:
    """AnonymousUserDashboardEmbeddingConfigurationDisabledFeature enum values."""

    SHARED_VIEW = "SHARED_VIEW"


class AnonymousUserDashboardEmbeddingConfigurationEnabledFeature:
    """AnonymousUserDashboardEmbeddingConfigurationEnabledFeature enum values."""

    SHARED_VIEW = "SHARED_VIEW"


class ArcThickness:
    """ArcThickness enum values."""

    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    WHOLE = "WHOLE"


class ArcThicknessOptions:
    """ArcThicknessOptions enum values."""

    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class AssetBundleExportFormat:
    """AssetBundleExportFormat enum values."""

    CLOUDFORMATION_JSON = "CLOUDFORMATION_JSON"
    QUICKSIGHT_JSON = "QUICKSIGHT_JSON"


class AssetBundleExportJobAnalysisPropertyToOverride:
    """AssetBundleExportJobAnalysisPropertyToOverride enum values."""

    NAME = "Name"


class AssetBundleExportJobDashboardPropertyToOverride:
    """AssetBundleExportJobDashboardPropertyToOverride enum values."""

    NAME = "Name"


class AssetBundleExportJobDataSetPropertyToOverride:
    """AssetBundleExportJobDataSetPropertyToOverride enum values."""

    NAME = "Name"
    REFRESHFAILUREEMAILALERTSTATUS = "RefreshFailureEmailAlertStatus"


class AssetBundleExportJobDataSourcePropertyToOverride:
    """AssetBundleExportJobDataSourcePropertyToOverride enum values."""

    NAME = "Name"
    DISABLESSL = "DisableSsl"
    SECRETARN = "SecretArn"
    USERNAME = "Username"
    PASSWORD = "Password"
    DOMAIN = "Domain"
    WORKGROUP = "WorkGroup"
    HOST = "Host"
    PORT = "Port"
    DATABASE = "Database"
    DATASETNAME = "DataSetName"
    CATALOG = "Catalog"
    INSTANCEID = "InstanceId"
    CLUSTERID = "ClusterId"
    MANIFESTFILELOCATION = "ManifestFileLocation"
    WAREHOUSE = "Warehouse"
    ROLEARN = "RoleArn"
    PRODUCTTYPE = "ProductType"


class AssetBundleExportJobFolderPropertyToOverride:
    """AssetBundleExportJobFolderPropertyToOverride enum values."""

    NAME = "Name"
    PARENTFOLDERARN = "ParentFolderArn"


class AssetBundleExportJobRefreshSchedulePropertyToOverride:
    """AssetBundleExportJobRefreshSchedulePropertyToOverride enum values."""

    STARTAFTERDATETIME = "StartAfterDateTime"


class AssetBundleExportJobStatus:
    """AssetBundleExportJobStatus enum values."""

    QUEUED_FOR_IMMEDIATE_EXECUTION = "QUEUED_FOR_IMMEDIATE_EXECUTION"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"


class AssetBundleExportJobThemePropertyToOverride:
    """AssetBundleExportJobThemePropertyToOverride enum values."""

    NAME = "Name"


class AssetBundleExportJobVPCConnectionPropertyToOverride:
    """AssetBundleExportJobVPCConnectionPropertyToOverride enum values."""

    NAME = "Name"
    DNSRESOLVERS = "DnsResolvers"
    ROLEARN = "RoleArn"


class AssetBundleImportFailureAction:
    """AssetBundleImportFailureAction enum values."""

    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"


class AssetBundleImportJobStatus:
    """AssetBundleImportJobStatus enum values."""

    QUEUED_FOR_IMMEDIATE_EXECUTION = "QUEUED_FOR_IMMEDIATE_EXECUTION"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    FAILED_ROLLBACK_IN_PROGRESS = "FAILED_ROLLBACK_IN_PROGRESS"
    FAILED_ROLLBACK_COMPLETED = "FAILED_ROLLBACK_COMPLETED"
    FAILED_ROLLBACK_ERROR = "FAILED_ROLLBACK_ERROR"


class AssignmentStatus:
    """AssignmentStatus enum values."""

    ENABLED = "ENABLED"
    DRAFT = "DRAFT"
    DISABLED = "DISABLED"


class AuthenticationMethodOption:
    """AuthenticationMethodOption enum values."""

    IAM_AND_QUICKSIGHT = "IAM_AND_QUICKSIGHT"
    IAM_ONLY = "IAM_ONLY"
    ACTIVE_DIRECTORY = "ACTIVE_DIRECTORY"
    IAM_IDENTITY_CENTER = "IAM_IDENTITY_CENTER"


class AuthenticationType:
    """AuthenticationType enum values."""

    PASSWORD = "PASSWORD"
    TOKEN = "TOKEN"
    X509 = "X509"


class AuthorSpecifiedAggregation:
    """AuthorSpecifiedAggregation enum values."""

    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    MIN = "MIN"
    MAX = "MAX"
    MEDIAN = "MEDIAN"
    SUM = "SUM"
    AVERAGE = "AVERAGE"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    VAR = "VAR"
    VARP = "VARP"
    PERCENTILE = "PERCENTILE"


class AuthorizationCodeGrantCredentialsSource:
    """AuthorizationCodeGrantCredentialsSource enum values."""

    PLAIN_CREDENTIALS = "PLAIN_CREDENTIALS"


class AxisBinding:
    """AxisBinding enum values."""

    PRIMARY_YAXIS = "PRIMARY_YAXIS"
    SECONDARY_YAXIS = "SECONDARY_YAXIS"


class BarChartOrientation:
    """BarChartOrientation enum values."""

    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"


class BarsArrangement:
    """BarsArrangement enum values."""

    CLUSTERED = "CLUSTERED"
    STACKED = "STACKED"
    STACKED_PERCENT = "STACKED_PERCENT"


class BaseMapStyleType:
    """BaseMapStyleType enum values."""

    LIGHT_GRAY = "LIGHT_GRAY"
    DARK_GRAY = "DARK_GRAY"
    STREET = "STREET"
    IMAGERY = "IMAGERY"


class BoxPlotFillStyle:
    """BoxPlotFillStyle enum values."""

    SOLID = "SOLID"
    TRANSPARENT = "TRANSPARENT"


class BrandStatus:
    """BrandStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_SUCCEEDED = "CREATE_SUCCEEDED"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class BrandVersionStatus:
    """BrandVersionStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_SUCCEEDED = "CREATE_SUCCEEDED"
    CREATE_FAILED = "CREATE_FAILED"


class CapabilityState:
    """CapabilityState enum values."""

    DENY = "DENY"


class CategoricalAggregationFunction:
    """CategoricalAggregationFunction enum values."""

    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"


class CategoryFilterFunction:
    """CategoryFilterFunction enum values."""

    EXACT = "EXACT"
    CONTAINS = "CONTAINS"


class CategoryFilterMatchOperator:
    """CategoryFilterMatchOperator enum values."""

    EQUALS = "EQUALS"
    DOES_NOT_EQUAL = "DOES_NOT_EQUAL"
    CONTAINS = "CONTAINS"
    DOES_NOT_CONTAIN = "DOES_NOT_CONTAIN"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"


class CategoryFilterSelectAllOptions:
    """CategoryFilterSelectAllOptions enum values."""

    FILTER_ALL_VALUES = "FILTER_ALL_VALUES"


class CategoryFilterType:
    """CategoryFilterType enum values."""

    CUSTOM_FILTER = "CUSTOM_FILTER"
    CUSTOM_FILTER_LIST = "CUSTOM_FILTER_LIST"
    FILTER_LIST = "FILTER_LIST"


class ClientCredentialsSource:
    """ClientCredentialsSource enum values."""

    PLAIN_CREDENTIALS = "PLAIN_CREDENTIALS"


class ColorFillType:
    """ColorFillType enum values."""

    DISCRETE = "DISCRETE"
    GRADIENT = "GRADIENT"


class ColumnDataRole:
    """ColumnDataRole enum values."""

    DIMENSION = "DIMENSION"
    MEASURE = "MEASURE"


class ColumnDataSubType:
    """ColumnDataSubType enum values."""

    FLOAT = "FLOAT"
    FIXED = "FIXED"


class ColumnDataType:
    """ColumnDataType enum values."""

    STRING = "STRING"
    INTEGER = "INTEGER"
    DECIMAL = "DECIMAL"
    DATETIME = "DATETIME"


class ColumnOrderingType:
    """ColumnOrderingType enum values."""

    GREATER_IS_BETTER = "GREATER_IS_BETTER"
    LESSER_IS_BETTER = "LESSER_IS_BETTER"
    SPECIFIED = "SPECIFIED"


class ColumnRole:
    """ColumnRole enum values."""

    DIMENSION = "DIMENSION"
    MEASURE = "MEASURE"


class ColumnTagName:
    """ColumnTagName enum values."""

    COLUMN_GEOGRAPHIC_ROLE = "COLUMN_GEOGRAPHIC_ROLE"
    COLUMN_DESCRIPTION = "COLUMN_DESCRIPTION"


class CommitMode:
    """CommitMode enum values."""

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class ComparisonMethod:
    """ComparisonMethod enum values."""

    DIFFERENCE = "DIFFERENCE"
    PERCENT_DIFFERENCE = "PERCENT_DIFFERENCE"
    PERCENT = "PERCENT"


class ComparisonMethodType:
    """ComparisonMethodType enum values."""

    DIFF = "DIFF"
    PERC_DIFF = "PERC_DIFF"
    DIFF_AS_PERC = "DIFF_AS_PERC"
    POP_CURRENT_DIFF_AS_PERC = "POP_CURRENT_DIFF_AS_PERC"
    POP_CURRENT_DIFF = "POP_CURRENT_DIFF"
    POP_OVERTIME_DIFF_AS_PERC = "POP_OVERTIME_DIFF_AS_PERC"
    POP_OVERTIME_DIFF = "POP_OVERTIME_DIFF"
    PERCENT_OF_TOTAL = "PERCENT_OF_TOTAL"
    RUNNING_SUM = "RUNNING_SUM"
    MOVING_AVERAGE = "MOVING_AVERAGE"


class ConditionalFormattingIconDisplayOption:
    """ConditionalFormattingIconDisplayOption enum values."""

    ICON_ONLY = "ICON_ONLY"


class ConditionalFormattingIconSetType:
    """ConditionalFormattingIconSetType enum values."""

    PLUS_MINUS = "PLUS_MINUS"
    CHECK_X = "CHECK_X"
    THREE_COLOR_ARROW = "THREE_COLOR_ARROW"
    THREE_GRAY_ARROW = "THREE_GRAY_ARROW"
    CARET_UP_MINUS_DOWN = "CARET_UP_MINUS_DOWN"
    THREE_SHAPE = "THREE_SHAPE"
    THREE_CIRCLE = "THREE_CIRCLE"
    FLAGS = "FLAGS"
    BARS = "BARS"
    FOUR_COLOR_ARROW = "FOUR_COLOR_ARROW"
    FOUR_GRAY_ARROW = "FOUR_GRAY_ARROW"


class ConnectionAuthType:
    """ConnectionAuthType enum values."""

    BASIC = "BASIC"
    API_KEY = "API_KEY"
    OAUTH2_CLIENT_CREDENTIALS = "OAUTH2_CLIENT_CREDENTIALS"
    NONE = "NONE"
    IAM = "IAM"
    OAUTH2_AUTHORIZATION_CODE = "OAUTH2_AUTHORIZATION_CODE"


class ConstantType:
    """ConstantType enum values."""

    SINGULAR = "SINGULAR"
    RANGE = "RANGE"
    COLLECTIVE = "COLLECTIVE"


class ContributionAnalysisDirection:
    """ContributionAnalysisDirection enum values."""

    INCREASE = "INCREASE"
    DECREASE = "DECREASE"
    NEUTRAL = "NEUTRAL"


class ContributionAnalysisSortType:
    """ContributionAnalysisSortType enum values."""

    ABSOLUTE_DIFFERENCE = "ABSOLUTE_DIFFERENCE"
    CONTRIBUTION_PERCENTAGE = "CONTRIBUTION_PERCENTAGE"
    DEVIATION_FROM_EXPECTED = "DEVIATION_FROM_EXPECTED"
    PERCENTAGE_DIFFERENCE = "PERCENTAGE_DIFFERENCE"


class CrossDatasetTypes:
    """CrossDatasetTypes enum values."""

    ALL_DATASETS = "ALL_DATASETS"
    SINGLE_DATASET = "SINGLE_DATASET"


class CustomContentImageScalingConfiguration:
    """CustomContentImageScalingConfiguration enum values."""

    FIT_TO_HEIGHT = "FIT_TO_HEIGHT"
    FIT_TO_WIDTH = "FIT_TO_WIDTH"
    DO_NOT_SCALE = "DO_NOT_SCALE"
    SCALE_TO_VISUAL = "SCALE_TO_VISUAL"


class CustomContentType:
    """CustomContentType enum values."""

    IMAGE = "IMAGE"
    OTHER_EMBEDDED_CONTENT = "OTHER_EMBEDDED_CONTENT"


class DashboardBehavior:
    """DashboardBehavior enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DashboardCustomizationStatus:
    """DashboardCustomizationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DashboardErrorType:
    """DashboardErrorType enum values."""

    ACCESS_DENIED = "ACCESS_DENIED"
    SOURCE_NOT_FOUND = "SOURCE_NOT_FOUND"
    DATA_SET_NOT_FOUND = "DATA_SET_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    PARAMETER_VALUE_INCOMPATIBLE = "PARAMETER_VALUE_INCOMPATIBLE"
    PARAMETER_TYPE_INVALID = "PARAMETER_TYPE_INVALID"
    PARAMETER_NOT_FOUND = "PARAMETER_NOT_FOUND"
    COLUMN_TYPE_MISMATCH = "COLUMN_TYPE_MISMATCH"
    COLUMN_GEOGRAPHIC_ROLE_MISMATCH = "COLUMN_GEOGRAPHIC_ROLE_MISMATCH"
    COLUMN_REPLACEMENT_MISSING = "COLUMN_REPLACEMENT_MISSING"


class DashboardFilterAttribute:
    """DashboardFilterAttribute enum values."""

    QUICKSIGHT_USER = "QUICKSIGHT_USER"
    QUICKSIGHT_VIEWER_OR_OWNER = "QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    QUICKSIGHT_OWNER = "QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    DASHBOARD_NAME = "DASHBOARD_NAME"


class DashboardUIState:
    """DashboardUIState enum values."""

    EXPANDED = "EXPANDED"
    COLLAPSED = "COLLAPSED"


class DashboardsQAStatus:
    """DashboardsQAStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DataLabelContent:
    """DataLabelContent enum values."""

    VALUE = "VALUE"
    PERCENT = "PERCENT"
    VALUE_AND_PERCENT = "VALUE_AND_PERCENT"


class DataLabelOverlap:
    """DataLabelOverlap enum values."""

    DISABLE_OVERLAP = "DISABLE_OVERLAP"
    ENABLE_OVERLAP = "ENABLE_OVERLAP"


class DataLabelPosition:
    """DataLabelPosition enum values."""

    INSIDE = "INSIDE"
    OUTSIDE = "OUTSIDE"
    LEFT = "LEFT"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    RIGHT = "RIGHT"


class DataPrepSimpleAggregationFunctionType:
    """DataPrepSimpleAggregationFunctionType enum values."""

    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    SUM = "SUM"
    AVERAGE = "AVERAGE"
    MAX = "MAX"
    MIN = "MIN"


class DataSetDateComparisonFilterOperator:
    """DataSetDateComparisonFilterOperator enum values."""

    BEFORE = "BEFORE"
    BEFORE_OR_EQUALS_TO = "BEFORE_OR_EQUALS_TO"
    AFTER = "AFTER"
    AFTER_OR_EQUALS_TO = "AFTER_OR_EQUALS_TO"


class DataSetFilterAttribute:
    """DataSetFilterAttribute enum values."""

    QUICKSIGHT_VIEWER_OR_OWNER = "QUICKSIGHT_VIEWER_OR_OWNER"
    QUICKSIGHT_OWNER = "QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    DATASET_NAME = "DATASET_NAME"


class DataSetImportMode:
    """DataSetImportMode enum values."""

    SPICE = "SPICE"
    DIRECT_QUERY = "DIRECT_QUERY"


class DataSetNumericComparisonFilterOperator:
    """DataSetNumericComparisonFilterOperator enum values."""

    EQUALS = "EQUALS"
    DOES_NOT_EQUAL = "DOES_NOT_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUALS_TO = "GREATER_THAN_OR_EQUALS_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUALS_TO = "LESS_THAN_OR_EQUALS_TO"


class DataSetStringComparisonFilterOperator:
    """DataSetStringComparisonFilterOperator enum values."""

    EQUALS = "EQUALS"
    DOES_NOT_EQUAL = "DOES_NOT_EQUAL"
    CONTAINS = "CONTAINS"
    DOES_NOT_CONTAIN = "DOES_NOT_CONTAIN"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"


class DataSetStringListFilterOperator:
    """DataSetStringListFilterOperator enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class DataSetUseAs:
    """DataSetUseAs enum values."""

    RLS_RULES = "RLS_RULES"


class DataSourceErrorInfoType:
    """DataSourceErrorInfoType enum values."""

    ACCESS_DENIED = "ACCESS_DENIED"
    COPY_SOURCE_NOT_FOUND = "COPY_SOURCE_NOT_FOUND"
    TIMEOUT = "TIMEOUT"
    ENGINE_VERSION_NOT_SUPPORTED = "ENGINE_VERSION_NOT_SUPPORTED"
    UNKNOWN_HOST = "UNKNOWN_HOST"
    GENERIC_SQL_FAILURE = "GENERIC_SQL_FAILURE"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"


class DataSourceFilterAttribute:
    """DataSourceFilterAttribute enum values."""

    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    DATASOURCE_NAME = "DATASOURCE_NAME"


class DataSourceType:
    """DataSourceType enum values."""

    ADOBE_ANALYTICS = "ADOBE_ANALYTICS"
    AMAZON_ELASTICSEARCH = "AMAZON_ELASTICSEARCH"
    ATHENA = "ATHENA"
    AURORA = "AURORA"
    AURORA_POSTGRESQL = "AURORA_POSTGRESQL"
    AWS_IOT_ANALYTICS = "AWS_IOT_ANALYTICS"
    GITHUB = "GITHUB"
    JIRA = "JIRA"
    MARIADB = "MARIADB"
    MYSQL = "MYSQL"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    PRESTO = "PRESTO"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SALESFORCE = "SALESFORCE"
    SERVICENOW = "SERVICENOW"
    SNOWFLAKE = "SNOWFLAKE"
    SPARK = "SPARK"
    SQLSERVER = "SQLSERVER"
    TERADATA = "TERADATA"
    TWITTER = "TWITTER"
    TIMESTREAM = "TIMESTREAM"
    AMAZON_OPENSEARCH = "AMAZON_OPENSEARCH"
    EXASOL = "EXASOL"
    DATABRICKS = "DATABRICKS"
    STARBURST = "STARBURST"
    TRINO = "TRINO"
    BIGQUERY = "BIGQUERY"
    GOOGLESHEETS = "GOOGLESHEETS"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    CONFLUENCE = "CONFLUENCE"
    SHAREPOINT = "SHAREPOINT"
    ONE_DRIVE = "ONE_DRIVE"
    WEB_CRAWLER = "WEB_CRAWLER"
    S3_KNOWLEDGE_BASE = "S3_KNOWLEDGE_BASE"
    QBUSINESS = "QBUSINESS"


class DatasetParameterValueType:
    """DatasetParameterValueType enum values."""

    MULTI_VALUED = "MULTI_VALUED"
    SINGLE_VALUED = "SINGLE_VALUED"


class DateAggregationFunction:
    """DateAggregationFunction enum values."""

    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    MIN = "MIN"
    MAX = "MAX"


class DayOfTheWeek:
    """DayOfTheWeek enum values."""

    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class DayOfWeek:
    """DayOfWeek enum values."""

    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class DecalPatternType:
    """DecalPatternType enum values."""

    SOLID = "SOLID"
    DIAGONAL_MEDIUM = "DIAGONAL_MEDIUM"
    CIRCLE_MEDIUM = "CIRCLE_MEDIUM"
    DIAMOND_GRID_MEDIUM = "DIAMOND_GRID_MEDIUM"
    CHECKERBOARD_MEDIUM = "CHECKERBOARD_MEDIUM"
    TRIANGLE_MEDIUM = "TRIANGLE_MEDIUM"
    DIAGONAL_OPPOSITE_MEDIUM = "DIAGONAL_OPPOSITE_MEDIUM"
    DIAMOND_MEDIUM = "DIAMOND_MEDIUM"
    DIAGONAL_LARGE = "DIAGONAL_LARGE"
    CIRCLE_LARGE = "CIRCLE_LARGE"
    DIAMOND_GRID_LARGE = "DIAMOND_GRID_LARGE"
    CHECKERBOARD_LARGE = "CHECKERBOARD_LARGE"
    TRIANGLE_LARGE = "TRIANGLE_LARGE"
    DIAGONAL_OPPOSITE_LARGE = "DIAGONAL_OPPOSITE_LARGE"
    DIAMOND_LARGE = "DIAMOND_LARGE"
    DIAGONAL_SMALL = "DIAGONAL_SMALL"
    CIRCLE_SMALL = "CIRCLE_SMALL"
    DIAMOND_GRID_SMALL = "DIAMOND_GRID_SMALL"
    CHECKERBOARD_SMALL = "CHECKERBOARD_SMALL"
    TRIANGLE_SMALL = "TRIANGLE_SMALL"
    DIAGONAL_OPPOSITE_SMALL = "DIAGONAL_OPPOSITE_SMALL"
    DIAMOND_SMALL = "DIAMOND_SMALL"


class DecalStyleType:
    """DecalStyleType enum values."""

    MANUAL = "Manual"
    AUTO = "Auto"


class DefaultAggregation:
    """DefaultAggregation enum values."""

    SUM = "SUM"
    MAX = "MAX"
    MIN = "MIN"
    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    AVERAGE = "AVERAGE"
    MEDIAN = "MEDIAN"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    VAR = "VAR"
    VARP = "VARP"


class DigitGroupingStyle:
    """DigitGroupingStyle enum values."""

    DEFAULT = "DEFAULT"
    LAKHS = "LAKHS"


class DisplayFormat:
    """DisplayFormat enum values."""

    AUTO = "AUTO"
    PERCENT = "PERCENT"
    CURRENCY = "CURRENCY"
    NUMBER = "NUMBER"
    DATE = "DATE"
    STRING = "STRING"


class Edition:
    """Edition enum values."""

    STANDARD = "STANDARD"
    ENTERPRISE = "ENTERPRISE"
    ENTERPRISE_AND_Q = "ENTERPRISE_AND_Q"


class EmbeddingIdentityType:
    """EmbeddingIdentityType enum values."""

    IAM = "IAM"
    QUICKSIGHT = "QUICKSIGHT"
    ANONYMOUS = "ANONYMOUS"


class ExceptionResourceType:
    """ExceptionResourceType enum values."""

    USER = "USER"
    GROUP = "GROUP"
    NAMESPACE = "NAMESPACE"
    ACCOUNT_SETTINGS = "ACCOUNT_SETTINGS"
    IAMPOLICY_ASSIGNMENT = "IAMPOLICY_ASSIGNMENT"
    DATA_SOURCE = "DATA_SOURCE"
    DATA_SET = "DATA_SET"
    VPC_CONNECTION = "VPC_CONNECTION"
    INGESTION = "INGESTION"


class FieldName:
    """FieldName enum values."""

    ASSETNAME = "assetName"
    ASSETDESCRIPTION = "assetDescription"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"


class FileFormat:
    """FileFormat enum values."""

    CSV = "CSV"
    TSV = "TSV"
    CLF = "CLF"
    ELF = "ELF"
    XLSX = "XLSX"
    JSON = "JSON"


class FilterClass:
    """FilterClass enum values."""

    ENFORCED_VALUE_FILTER = "ENFORCED_VALUE_FILTER"
    CONDITIONAL_VALUE_FILTER = "CONDITIONAL_VALUE_FILTER"
    NAMED_VALUE_FILTER = "NAMED_VALUE_FILTER"


class FilterNullOption:
    """FilterNullOption enum values."""

    ALL_VALUES = "ALL_VALUES"
    NULLS_ONLY = "NULLS_ONLY"
    NON_NULLS_ONLY = "NON_NULLS_ONLY"


class FilterOperator:
    """FilterOperator enum values."""

    STRINGEQUALS = "StringEquals"
    STRINGLIKE = "StringLike"


class FilterVisualScope:
    """FilterVisualScope enum values."""

    ALL_VISUALS = "ALL_VISUALS"
    SELECTED_VISUALS = "SELECTED_VISUALS"


class FlowPublishState:
    """FlowPublishState enum values."""

    PUBLISHED = "PUBLISHED"
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"


class FolderFilterAttribute:
    """FolderFilterAttribute enum values."""

    PARENT_FOLDER_ARN = "PARENT_FOLDER_ARN"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    QUICKSIGHT_OWNER = "QUICKSIGHT_OWNER"
    QUICKSIGHT_VIEWER_OR_OWNER = "QUICKSIGHT_VIEWER_OR_OWNER"
    FOLDER_NAME = "FOLDER_NAME"


class FolderType:
    """FolderType enum values."""

    SHARED = "SHARED"
    RESTRICTED = "RESTRICTED"


class FontDecoration:
    """FontDecoration enum values."""

    UNDERLINE = "UNDERLINE"
    NONE = "NONE"


class FontStyle:
    """FontStyle enum values."""

    NORMAL = "NORMAL"
    ITALIC = "ITALIC"


class FontWeightName:
    """FontWeightName enum values."""

    NORMAL = "NORMAL"
    BOLD = "BOLD"


class ForecastComputationSeasonality:
    """ForecastComputationSeasonality enum values."""

    AUTOMATIC = "AUTOMATIC"
    CUSTOM = "CUSTOM"


class FunnelChartMeasureDataLabelStyle:
    """FunnelChartMeasureDataLabelStyle enum values."""

    VALUE_ONLY = "VALUE_ONLY"
    PERCENTAGE_BY_FIRST_STAGE = "PERCENTAGE_BY_FIRST_STAGE"
    PERCENTAGE_BY_PREVIOUS_STAGE = "PERCENTAGE_BY_PREVIOUS_STAGE"
    VALUE_AND_PERCENTAGE_BY_FIRST_STAGE = "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE"
    VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE = "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE"


class GeneratedAnswerStatus:
    """GeneratedAnswerStatus enum values."""

    ANSWER_GENERATED = "ANSWER_GENERATED"
    ANSWER_RETRIEVED = "ANSWER_RETRIEVED"
    ANSWER_DOWNGRADE = "ANSWER_DOWNGRADE"


class GeoSpatialCountryCode:
    """GeoSpatialCountryCode enum values."""

    US = "US"


class GeoSpatialDataRole:
    """GeoSpatialDataRole enum values."""

    COUNTRY = "COUNTRY"
    STATE = "STATE"
    COUNTY = "COUNTY"
    CITY = "CITY"
    POSTCODE = "POSTCODE"
    LONGITUDE = "LONGITUDE"
    LATITUDE = "LATITUDE"


class GeospatialColorState:
    """GeospatialColorState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GeospatialLayerType:
    """GeospatialLayerType enum values."""

    POINT = "POINT"
    LINE = "LINE"
    POLYGON = "POLYGON"


class GeospatialMapNavigation:
    """GeospatialMapNavigation enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GeospatialSelectedPointStyle:
    """GeospatialSelectedPointStyle enum values."""

    POINT = "POINT"
    CLUSTER = "CLUSTER"
    HEATMAP = "HEATMAP"


class GroupFilterAttribute:
    """GroupFilterAttribute enum values."""

    GROUP_NAME = "GROUP_NAME"


class GroupFilterOperator:
    """GroupFilterOperator enum values."""

    STARTSWITH = "StartsWith"


class HistogramBinType:
    """HistogramBinType enum values."""

    BIN_COUNT = "BIN_COUNT"
    BIN_WIDTH = "BIN_WIDTH"


class HorizontalTextAlignment:
    """HorizontalTextAlignment enum values."""

    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    AUTO = "AUTO"


class Icon:
    """Icon enum values."""

    CARET_UP = "CARET_UP"
    CARET_DOWN = "CARET_DOWN"
    PLUS = "PLUS"
    MINUS = "MINUS"
    ARROW_UP = "ARROW_UP"
    ARROW_DOWN = "ARROW_DOWN"
    ARROW_LEFT = "ARROW_LEFT"
    ARROW_UP_LEFT = "ARROW_UP_LEFT"
    ARROW_DOWN_LEFT = "ARROW_DOWN_LEFT"
    ARROW_RIGHT = "ARROW_RIGHT"
    ARROW_UP_RIGHT = "ARROW_UP_RIGHT"
    ARROW_DOWN_RIGHT = "ARROW_DOWN_RIGHT"
    FACE_UP = "FACE_UP"
    FACE_DOWN = "FACE_DOWN"
    FACE_FLAT = "FACE_FLAT"
    ONE_BAR = "ONE_BAR"
    TWO_BAR = "TWO_BAR"
    THREE_BAR = "THREE_BAR"
    CIRCLE = "CIRCLE"
    TRIANGLE = "TRIANGLE"
    SQUARE = "SQUARE"
    FLAG = "FLAG"
    THUMBS_UP = "THUMBS_UP"
    THUMBS_DOWN = "THUMBS_DOWN"
    CHECKMARK = "CHECKMARK"
    X = "X"


class IdentityStore:
    """IdentityStore enum values."""

    QUICKSIGHT = "QUICKSIGHT"


class IdentityType:
    """IdentityType enum values."""

    IAM = "IAM"
    QUICKSIGHT = "QUICKSIGHT"
    IAM_IDENTITY_CENTER = "IAM_IDENTITY_CENTER"


class ImageCustomActionTrigger:
    """ImageCustomActionTrigger enum values."""

    CLICK = "CLICK"
    MENU = "MENU"


class IncludeFolderMembers:
    """IncludeFolderMembers enum values."""

    RECURSE = "RECURSE"
    ONE_LEVEL = "ONE_LEVEL"
    NONE = "NONE"


class IncludeGeneratedAnswer:
    """IncludeGeneratedAnswer enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class IncludeQuickSightQIndex:
    """IncludeQuickSightQIndex enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class IngestionErrorType:
    """IngestionErrorType enum values."""

    FAILURE_TO_ASSUME_ROLE = "FAILURE_TO_ASSUME_ROLE"
    INGESTION_SUPERSEDED = "INGESTION_SUPERSEDED"
    INGESTION_CANCELED = "INGESTION_CANCELED"
    DATA_SET_DELETED = "DATA_SET_DELETED"
    DATA_SET_NOT_SPICE = "DATA_SET_NOT_SPICE"
    S3_UPLOADED_FILE_DELETED = "S3_UPLOADED_FILE_DELETED"
    S3_MANIFEST_ERROR = "S3_MANIFEST_ERROR"
    DATA_TOLERANCE_EXCEPTION = "DATA_TOLERANCE_EXCEPTION"
    SPICE_TABLE_NOT_FOUND = "SPICE_TABLE_NOT_FOUND"
    DATA_SET_SIZE_LIMIT_EXCEEDED = "DATA_SET_SIZE_LIMIT_EXCEEDED"
    ROW_SIZE_LIMIT_EXCEEDED = "ROW_SIZE_LIMIT_EXCEEDED"
    ACCOUNT_CAPACITY_LIMIT_EXCEEDED = "ACCOUNT_CAPACITY_LIMIT_EXCEEDED"
    CUSTOMER_ERROR = "CUSTOMER_ERROR"
    DATA_SOURCE_NOT_FOUND = "DATA_SOURCE_NOT_FOUND"
    IAM_ROLE_NOT_AVAILABLE = "IAM_ROLE_NOT_AVAILABLE"
    CONNECTION_FAILURE = "CONNECTION_FAILURE"
    SQL_TABLE_NOT_FOUND = "SQL_TABLE_NOT_FOUND"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    SSL_CERTIFICATE_VALIDATION_FAILURE = "SSL_CERTIFICATE_VALIDATION_FAILURE"
    OAUTH_TOKEN_FAILURE = "OAUTH_TOKEN_FAILURE"
    SOURCE_API_LIMIT_EXCEEDED_FAILURE = "SOURCE_API_LIMIT_EXCEEDED_FAILURE"
    PASSWORD_AUTHENTICATION_FAILURE = "PASSWORD_AUTHENTICATION_FAILURE"
    SQL_SCHEMA_MISMATCH_ERROR = "SQL_SCHEMA_MISMATCH_ERROR"
    INVALID_DATE_FORMAT = "INVALID_DATE_FORMAT"
    INVALID_DATAPREP_SYNTAX = "INVALID_DATAPREP_SYNTAX"
    SOURCE_RESOURCE_LIMIT_EXCEEDED = "SOURCE_RESOURCE_LIMIT_EXCEEDED"
    SQL_INVALID_PARAMETER_VALUE = "SQL_INVALID_PARAMETER_VALUE"
    QUERY_TIMEOUT = "QUERY_TIMEOUT"
    SQL_NUMERIC_OVERFLOW = "SQL_NUMERIC_OVERFLOW"
    UNRESOLVABLE_HOST = "UNRESOLVABLE_HOST"
    UNROUTABLE_HOST = "UNROUTABLE_HOST"
    SQL_EXCEPTION = "SQL_EXCEPTION"
    S3_FILE_INACCESSIBLE = "S3_FILE_INACCESSIBLE"
    IOT_FILE_NOT_FOUND = "IOT_FILE_NOT_FOUND"
    IOT_DATA_SET_FILE_EMPTY = "IOT_DATA_SET_FILE_EMPTY"
    INVALID_DATA_SOURCE_CONFIG = "INVALID_DATA_SOURCE_CONFIG"
    DATA_SOURCE_AUTH_FAILED = "DATA_SOURCE_AUTH_FAILED"
    DATA_SOURCE_CONNECTION_FAILED = "DATA_SOURCE_CONNECTION_FAILED"
    FAILURE_TO_PROCESS_JSON_FILE = "FAILURE_TO_PROCESS_JSON_FILE"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"
    REFRESH_SUPPRESSED_BY_EDIT = "REFRESH_SUPPRESSED_BY_EDIT"
    PERMISSION_NOT_FOUND = "PERMISSION_NOT_FOUND"
    ELASTICSEARCH_CURSOR_NOT_ENABLED = "ELASTICSEARCH_CURSOR_NOT_ENABLED"
    CURSOR_NOT_ENABLED = "CURSOR_NOT_ENABLED"
    DUPLICATE_COLUMN_NAMES_FOUND = "DUPLICATE_COLUMN_NAMES_FOUND"


class IngestionRequestSource:
    """IngestionRequestSource enum values."""

    MANUAL = "MANUAL"
    SCHEDULED = "SCHEDULED"


class IngestionRequestType:
    """IngestionRequestType enum values."""

    INITIAL_INGESTION = "INITIAL_INGESTION"
    EDIT = "EDIT"
    INCREMENTAL_REFRESH = "INCREMENTAL_REFRESH"
    FULL_REFRESH = "FULL_REFRESH"


class IngestionStatus:
    """IngestionStatus enum values."""

    INITIALIZED = "INITIALIZED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class IngestionType:
    """IngestionType enum values."""

    INCREMENTAL_REFRESH = "INCREMENTAL_REFRESH"
    FULL_REFRESH = "FULL_REFRESH"


class InputColumnDataType:
    """InputColumnDataType enum values."""

    STRING = "STRING"
    INTEGER = "INTEGER"
    DECIMAL = "DECIMAL"
    DATETIME = "DATETIME"
    BIT = "BIT"
    BOOLEAN = "BOOLEAN"
    JSON = "JSON"


class JoinOperationType:
    """JoinOperationType enum values."""

    INNER = "INNER"
    OUTER = "OUTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class JoinType:
    """JoinType enum values."""

    INNER = "INNER"
    OUTER = "OUTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class KPISparklineType:
    """KPISparklineType enum values."""

    LINE = "LINE"
    AREA = "AREA"


class KPIVisualStandardLayoutType:
    """KPIVisualStandardLayoutType enum values."""

    CLASSIC = "CLASSIC"
    VERTICAL = "VERTICAL"


class LayerCustomActionTrigger:
    """LayerCustomActionTrigger enum values."""

    DATA_POINT_CLICK = "DATA_POINT_CLICK"
    DATA_POINT_MENU = "DATA_POINT_MENU"


class LayoutElementType:
    """LayoutElementType enum values."""

    VISUAL = "VISUAL"
    FILTER_CONTROL = "FILTER_CONTROL"
    PARAMETER_CONTROL = "PARAMETER_CONTROL"
    TEXT_BOX = "TEXT_BOX"
    IMAGE = "IMAGE"


class LegendPosition:
    """LegendPosition enum values."""

    AUTO = "AUTO"
    RIGHT = "RIGHT"
    BOTTOM = "BOTTOM"
    TOP = "TOP"


class LineChartLineStyle:
    """LineChartLineStyle enum values."""

    SOLID = "SOLID"
    DOTTED = "DOTTED"
    DASHED = "DASHED"


class LineChartMarkerShape:
    """LineChartMarkerShape enum values."""

    CIRCLE = "CIRCLE"
    TRIANGLE = "TRIANGLE"
    SQUARE = "SQUARE"
    DIAMOND = "DIAMOND"
    ROUNDED_SQUARE = "ROUNDED_SQUARE"


class LineChartType:
    """LineChartType enum values."""

    LINE = "LINE"
    AREA = "AREA"
    STACKED_AREA = "STACKED_AREA"


class LineInterpolation:
    """LineInterpolation enum values."""

    LINEAR = "LINEAR"
    SMOOTH = "SMOOTH"
    STEPPED = "STEPPED"


class LookbackWindowSizeUnit:
    """LookbackWindowSizeUnit enum values."""

    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"


class MapZoomMode:
    """MapZoomMode enum values."""

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class MaximumMinimumComputationType:
    """MaximumMinimumComputationType enum values."""

    MAXIMUM = "MAXIMUM"
    MINIMUM = "MINIMUM"


class MemberType:
    """MemberType enum values."""

    DASHBOARD = "DASHBOARD"
    ANALYSIS = "ANALYSIS"
    DATASET = "DATASET"
    DATASOURCE = "DATASOURCE"
    TOPIC = "TOPIC"


class MissingDataTreatmentOption:
    """MissingDataTreatmentOption enum values."""

    INTERPOLATE = "INTERPOLATE"
    SHOW_AS_ZERO = "SHOW_AS_ZERO"
    SHOW_AS_BLANK = "SHOW_AS_BLANK"


class NamedEntityAggType:
    """NamedEntityAggType enum values."""

    SUM = "SUM"
    MIN = "MIN"
    MAX = "MAX"
    COUNT = "COUNT"
    AVERAGE = "AVERAGE"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    VAR = "VAR"
    VARP = "VARP"
    PERCENTILE = "PERCENTILE"
    MEDIAN = "MEDIAN"
    CUSTOM = "CUSTOM"


class NamedFilterAggType:
    """NamedFilterAggType enum values."""

    NO_AGGREGATION = "NO_AGGREGATION"
    SUM = "SUM"
    AVERAGE = "AVERAGE"
    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    MAX = "MAX"
    MEDIAN = "MEDIAN"
    MIN = "MIN"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    VAR = "VAR"
    VARP = "VARP"


class NamedFilterType:
    """NamedFilterType enum values."""

    CATEGORY_FILTER = "CATEGORY_FILTER"
    NUMERIC_EQUALITY_FILTER = "NUMERIC_EQUALITY_FILTER"
    NUMERIC_RANGE_FILTER = "NUMERIC_RANGE_FILTER"
    DATE_RANGE_FILTER = "DATE_RANGE_FILTER"
    RELATIVE_DATE_FILTER = "RELATIVE_DATE_FILTER"
    NULL_FILTER = "NULL_FILTER"


class NamespaceErrorType:
    """NamespaceErrorType enum values."""

    PERMISSION_DENIED = "PERMISSION_DENIED"
    INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"


class NamespaceStatus:
    """NamespaceStatus enum values."""

    CREATED = "CREATED"
    CREATING = "CREATING"
    DELETING = "DELETING"
    RETRYABLE_FAILURE = "RETRYABLE_FAILURE"
    NON_RETRYABLE_FAILURE = "NON_RETRYABLE_FAILURE"


class NegativeValueDisplayMode:
    """NegativeValueDisplayMode enum values."""

    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


class NetworkInterfaceStatus:
    """NetworkInterfaceStatus enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETION_FAILED = "DELETION_FAILED"
    DELETION_SCHEDULED = "DELETION_SCHEDULED"
    ATTACHMENT_FAILED_ROLLBACK_FAILED = "ATTACHMENT_FAILED_ROLLBACK_FAILED"


class NullFilterOption:
    """NullFilterOption enum values."""

    ALL_VALUES = "ALL_VALUES"
    NON_NULLS_ONLY = "NON_NULLS_ONLY"
    NULLS_ONLY = "NULLS_ONLY"


class NullFilterType:
    """NullFilterType enum values."""

    ALL_VALUES = "ALL_VALUES"
    NON_NULLS_ONLY = "NON_NULLS_ONLY"
    NULLS_ONLY = "NULLS_ONLY"


class NumberScale:
    """NumberScale enum values."""

    NONE = "NONE"
    AUTO = "AUTO"
    THOUSANDS = "THOUSANDS"
    MILLIONS = "MILLIONS"
    BILLIONS = "BILLIONS"
    TRILLIONS = "TRILLIONS"
    LAKHS = "LAKHS"
    CRORES = "CRORES"


class NumericEqualityMatchOperator:
    """NumericEqualityMatchOperator enum values."""

    EQUALS = "EQUALS"
    DOES_NOT_EQUAL = "DOES_NOT_EQUAL"


class NumericFilterSelectAllOptions:
    """NumericFilterSelectAllOptions enum values."""

    FILTER_ALL_VALUES = "FILTER_ALL_VALUES"


class NumericSeparatorSymbol:
    """NumericSeparatorSymbol enum values."""

    COMMA = "COMMA"
    DOT = "DOT"
    SPACE = "SPACE"


class OtherCategories:
    """OtherCategories enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class PanelBorderStyle:
    """PanelBorderStyle enum values."""

    SOLID = "SOLID"
    DASHED = "DASHED"
    DOTTED = "DOTTED"


class PaperOrientation:
    """PaperOrientation enum values."""

    PORTRAIT = "PORTRAIT"
    LANDSCAPE = "LANDSCAPE"


class PaperSize:
    """PaperSize enum values."""

    US_LETTER = "US_LETTER"
    US_LEGAL = "US_LEGAL"
    US_TABLOID_LEDGER = "US_TABLOID_LEDGER"
    A0 = "A0"
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    JIS_B4 = "JIS_B4"
    JIS_B5 = "JIS_B5"


class ParameterValueType:
    """ParameterValueType enum values."""

    MULTI_VALUED = "MULTI_VALUED"
    SINGLE_VALUED = "SINGLE_VALUED"


class PersonalizationMode:
    """PersonalizationMode enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PivotTableConditionalFormattingScopeRole:
    """PivotTableConditionalFormattingScopeRole enum values."""

    FIELD = "FIELD"
    FIELD_TOTAL = "FIELD_TOTAL"
    GRAND_TOTAL = "GRAND_TOTAL"


class PivotTableDataPathType:
    """PivotTableDataPathType enum values."""

    HIERARCHY_ROWS_LAYOUT_COLUMN = "HIERARCHY_ROWS_LAYOUT_COLUMN"
    MULTIPLE_ROW_METRICS_COLUMN = "MULTIPLE_ROW_METRICS_COLUMN"
    EMPTY_COLUMN_HEADER = "EMPTY_COLUMN_HEADER"
    COUNT_METRIC_COLUMN = "COUNT_METRIC_COLUMN"


class PivotTableFieldCollapseState:
    """PivotTableFieldCollapseState enum values."""

    COLLAPSED = "COLLAPSED"
    EXPANDED = "EXPANDED"


class PivotTableMetricPlacement:
    """PivotTableMetricPlacement enum values."""

    ROW = "ROW"
    COLUMN = "COLUMN"


class PivotTableRowsLayout:
    """PivotTableRowsLayout enum values."""

    TABULAR = "TABULAR"
    HIERARCHY = "HIERARCHY"


class PivotTableSubtotalLevel:
    """PivotTableSubtotalLevel enum values."""

    ALL = "ALL"
    CUSTOM = "CUSTOM"
    LAST = "LAST"


class PluginVisualAxisName:
    """PluginVisualAxisName enum values."""

    GROUP_BY = "GROUP_BY"
    VALUE = "VALUE"


class PrimaryValueDisplayType:
    """PrimaryValueDisplayType enum values."""

    HIDDEN = "HIDDEN"
    COMPARISON = "COMPARISON"
    ACTUAL = "ACTUAL"


class PropertyRole:
    """PropertyRole enum values."""

    PRIMARY = "PRIMARY"
    ID = "ID"


class PropertyUsage:
    """PropertyUsage enum values."""

    INHERIT = "INHERIT"
    DIMENSION = "DIMENSION"
    MEASURE = "MEASURE"


class PurchaseMode:
    """PurchaseMode enum values."""

    MANUAL = "MANUAL"
    AUTO_PURCHASE = "AUTO_PURCHASE"


class QAResultType:
    """QAResultType enum values."""

    DASHBOARD_VISUAL = "DASHBOARD_VISUAL"
    GENERATED_ANSWER = "GENERATED_ANSWER"
    NO_ANSWER = "NO_ANSWER"


class QBusinessInsightsStatus:
    """QBusinessInsightsStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class QDataKeyType:
    """QDataKeyType enum values."""

    AWS_OWNED = "AWS_OWNED"
    CMK = "CMK"


class QSearchStatus:
    """QSearchStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class QueryExecutionMode:
    """QueryExecutionMode enum values."""

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class RadarChartAxesRangeScale:
    """RadarChartAxesRangeScale enum values."""

    AUTO = "AUTO"
    INDEPENDENT = "INDEPENDENT"
    SHARED = "SHARED"


class RadarChartShape:
    """RadarChartShape enum values."""

    CIRCLE = "CIRCLE"
    POLYGON = "POLYGON"


class ReferenceLineLabelHorizontalPosition:
    """ReferenceLineLabelHorizontalPosition enum values."""

    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"


class ReferenceLineLabelVerticalPosition:
    """ReferenceLineLabelVerticalPosition enum values."""

    ABOVE = "ABOVE"
    BELOW = "BELOW"


class ReferenceLinePatternType:
    """ReferenceLinePatternType enum values."""

    SOLID = "SOLID"
    DASHED = "DASHED"
    DOTTED = "DOTTED"


class ReferenceLineSeriesType:
    """ReferenceLineSeriesType enum values."""

    BAR = "BAR"
    LINE = "LINE"


class ReferenceLineValueLabelRelativePosition:
    """ReferenceLineValueLabelRelativePosition enum values."""

    BEFORE_CUSTOM_LABEL = "BEFORE_CUSTOM_LABEL"
    AFTER_CUSTOM_LABEL = "AFTER_CUSTOM_LABEL"


class RefreshFailureAlertStatus:
    """RefreshFailureAlertStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RefreshInterval:
    """RefreshInterval enum values."""

    MINUTE15 = "MINUTE15"
    MINUTE30 = "MINUTE30"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class RelativeDateType:
    """RelativeDateType enum values."""

    PREVIOUS = "PREVIOUS"
    THIS = "THIS"
    LAST = "LAST"
    NOW = "NOW"
    NEXT = "NEXT"


class RelativeFontSize:
    """RelativeFontSize enum values."""

    EXTRA_SMALL = "EXTRA_SMALL"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    EXTRA_LARGE = "EXTRA_LARGE"


class ResizeOption:
    """ResizeOption enum values."""

    FIXED = "FIXED"
    RESPONSIVE = "RESPONSIVE"


class ResourceStatus:
    """ResourceStatus enum values."""

    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class ReviewedAnswerErrorCode:
    """ReviewedAnswerErrorCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    MISSING_ANSWER = "MISSING_ANSWER"
    DATASET_DOES_NOT_EXIST = "DATASET_DOES_NOT_EXIST"
    INVALID_DATASET_ARN = "INVALID_DATASET_ARN"
    DUPLICATED_ANSWER = "DUPLICATED_ANSWER"
    INVALID_DATA = "INVALID_DATA"
    MISSING_REQUIRED_FIELDS = "MISSING_REQUIRED_FIELDS"


class Role:
    """Role enum values."""

    ADMIN = "ADMIN"
    AUTHOR = "AUTHOR"
    READER = "READER"
    ADMIN_PRO = "ADMIN_PRO"
    AUTHOR_PRO = "AUTHOR_PRO"
    READER_PRO = "READER_PRO"


class RowLevelPermissionFormatVersion:
    """RowLevelPermissionFormatVersion enum values."""

    VERSION_1 = "VERSION_1"
    VERSION_2 = "VERSION_2"


class RowLevelPermissionPolicy:
    """RowLevelPermissionPolicy enum values."""

    GRANT_ACCESS = "GRANT_ACCESS"
    DENY_ACCESS = "DENY_ACCESS"


class SearchFilterOperator:
    """SearchFilterOperator enum values."""

    STRINGEQUALS = "StringEquals"
    STRINGLIKE = "StringLike"


class SectionPageBreakStatus:
    """SectionPageBreakStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SelectAllValueOptions:
    """SelectAllValueOptions enum values."""

    ALL_VALUES = "ALL_VALUES"


class SelectedFieldOptions:
    """SelectedFieldOptions enum values."""

    ALL_FIELDS = "ALL_FIELDS"


class SelectedTooltipType:
    """SelectedTooltipType enum values."""

    BASIC = "BASIC"
    DETAILED = "DETAILED"


class ServiceType:
    """ServiceType enum values."""

    REDSHIFT = "REDSHIFT"
    QBUSINESS = "QBUSINESS"
    ATHENA = "ATHENA"


class SharingModel:
    """SharingModel enum values."""

    ACCOUNT = "ACCOUNT"
    NAMESPACE = "NAMESPACE"


class SheetContentType:
    """SheetContentType enum values."""

    PAGINATED = "PAGINATED"
    INTERACTIVE = "INTERACTIVE"


class SheetControlDateTimePickerType:
    """SheetControlDateTimePickerType enum values."""

    SINGLE_VALUED = "SINGLE_VALUED"
    DATE_RANGE = "DATE_RANGE"


class SheetControlListType:
    """SheetControlListType enum values."""

    MULTI_SELECT = "MULTI_SELECT"
    SINGLE_SELECT = "SINGLE_SELECT"


class SheetControlSliderType:
    """SheetControlSliderType enum values."""

    SINGLE_POINT = "SINGLE_POINT"
    RANGE = "RANGE"


class SheetImageScalingType:
    """SheetImageScalingType enum values."""

    SCALE_TO_WIDTH = "SCALE_TO_WIDTH"
    SCALE_TO_HEIGHT = "SCALE_TO_HEIGHT"
    SCALE_TO_CONTAINER = "SCALE_TO_CONTAINER"
    SCALE_NONE = "SCALE_NONE"


class SimpleAttributeAggregationFunction:
    """SimpleAttributeAggregationFunction enum values."""

    UNIQUE_VALUE = "UNIQUE_VALUE"


class SimpleNumericalAggregationFunction:
    """SimpleNumericalAggregationFunction enum values."""

    SUM = "SUM"
    AVERAGE = "AVERAGE"
    MIN = "MIN"
    MAX = "MAX"
    COUNT = "COUNT"
    DISTINCT_COUNT = "DISTINCT_COUNT"
    VAR = "VAR"
    VARP = "VARP"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    MEDIAN = "MEDIAN"


class SimpleTotalAggregationFunction:
    """SimpleTotalAggregationFunction enum values."""

    DEFAULT = "DEFAULT"
    SUM = "SUM"
    AVERAGE = "AVERAGE"
    MIN = "MIN"
    MAX = "MAX"
    NONE = "NONE"


class SingleYAxisOption:
    """SingleYAxisOption enum values."""

    PRIMARY_Y_AXIS = "PRIMARY_Y_AXIS"


class SmallMultiplesAxisPlacement:
    """SmallMultiplesAxisPlacement enum values."""

    OUTSIDE = "OUTSIDE"
    INSIDE = "INSIDE"


class SmallMultiplesAxisScale:
    """SmallMultiplesAxisScale enum values."""

    SHARED = "SHARED"
    INDEPENDENT = "INDEPENDENT"


class SnapshotFileFormatType:
    """SnapshotFileFormatType enum values."""

    CSV = "CSV"
    PDF = "PDF"
    EXCEL = "EXCEL"


class SnapshotFileSheetSelectionScope:
    """SnapshotFileSheetSelectionScope enum values."""

    ALL_VISUALS = "ALL_VISUALS"
    SELECTED_VISUALS = "SELECTED_VISUALS"


class SnapshotJobStatus:
    """SnapshotJobStatus enum values."""

    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class SortDirection:
    """SortDirection enum values."""

    ASC = "ASC"
    DESC = "DESC"


class SpecialValue:
    """SpecialValue enum values."""

    EMPTY = "EMPTY"
    NULL = "NULL"
    OTHER = "OTHER"


class StarburstProductType:
    """StarburstProductType enum values."""

    GALAXY = "GALAXY"
    ENTERPRISE = "ENTERPRISE"


class Status:
    """Status enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class StyledCellType:
    """StyledCellType enum values."""

    TOTAL = "TOTAL"
    METRIC_HEADER = "METRIC_HEADER"
    VALUE = "VALUE"


class TableBorderStyle:
    """TableBorderStyle enum values."""

    NONE = "NONE"
    SOLID = "SOLID"


class TableCellImageScalingConfiguration:
    """TableCellImageScalingConfiguration enum values."""

    FIT_TO_CELL_HEIGHT = "FIT_TO_CELL_HEIGHT"
    FIT_TO_CELL_WIDTH = "FIT_TO_CELL_WIDTH"
    DO_NOT_SCALE = "DO_NOT_SCALE"


class TableFieldIconSetType:
    """TableFieldIconSetType enum values."""

    LINK = "LINK"


class TableOrientation:
    """TableOrientation enum values."""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class TableTotalsPlacement:
    """TableTotalsPlacement enum values."""

    START = "START"
    END = "END"
    AUTO = "AUTO"


class TableTotalsScrollStatus:
    """TableTotalsScrollStatus enum values."""

    PINNED = "PINNED"
    SCROLLED = "SCROLLED"


class TargetVisualOptions:
    """TargetVisualOptions enum values."""

    ALL_VISUALS = "ALL_VISUALS"


class TemplateErrorType:
    """TemplateErrorType enum values."""

    SOURCE_NOT_FOUND = "SOURCE_NOT_FOUND"
    DATA_SET_NOT_FOUND = "DATA_SET_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    ACCESS_DENIED = "ACCESS_DENIED"


class TextQualifier:
    """TextQualifier enum values."""

    DOUBLE_QUOTE = "DOUBLE_QUOTE"
    SINGLE_QUOTE = "SINGLE_QUOTE"


class TextTransform:
    """TextTransform enum values."""

    CAPITALIZE = "CAPITALIZE"


class TextWrap:
    """TextWrap enum values."""

    NONE = "NONE"
    WRAP = "WRAP"


class ThemeErrorType:
    """ThemeErrorType enum values."""

    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class ThemeType:
    """ThemeType enum values."""

    QUICKSIGHT = "QUICKSIGHT"
    CUSTOM = "CUSTOM"
    ALL = "ALL"


class TimeGranularity:
    """TimeGranularity enum values."""

    YEAR = "YEAR"
    QUARTER = "QUARTER"
    MONTH = "MONTH"
    WEEK = "WEEK"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
    MILLISECOND = "MILLISECOND"


class TooltipTarget:
    """TooltipTarget enum values."""

    BOTH = "BOTH"
    BAR = "BAR"
    LINE = "LINE"


class TooltipTitleType:
    """TooltipTitleType enum values."""

    NONE = "NONE"
    PRIMARY_VALUE = "PRIMARY_VALUE"


class TopBottomComputationType:
    """TopBottomComputationType enum values."""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class TopBottomSortOrder:
    """TopBottomSortOrder enum values."""

    PERCENT_DIFFERENCE = "PERCENT_DIFFERENCE"
    ABSOLUTE_DIFFERENCE = "ABSOLUTE_DIFFERENCE"


class TopicFilterAttribute:
    """TopicFilterAttribute enum values."""

    QUICKSIGHT_USER = "QUICKSIGHT_USER"
    QUICKSIGHT_VIEWER_OR_OWNER = "QUICKSIGHT_VIEWER_OR_OWNER"
    DIRECT_QUICKSIGHT_VIEWER_OR_OWNER = "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"
    QUICKSIGHT_OWNER = "QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_OWNER = "DIRECT_QUICKSIGHT_OWNER"
    DIRECT_QUICKSIGHT_SOLE_OWNER = "DIRECT_QUICKSIGHT_SOLE_OWNER"
    TOPIC_NAME = "TOPIC_NAME"


class TopicFilterOperator:
    """TopicFilterOperator enum values."""

    STRINGEQUALS = "StringEquals"
    STRINGLIKE = "StringLike"


class TopicIRFilterFunction:
    """TopicIRFilterFunction enum values."""

    CONTAINS = "CONTAINS"
    EXACT = "EXACT"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS_STRING = "CONTAINS_STRING"
    PREVIOUS = "PREVIOUS"
    THIS = "THIS"
    LAST = "LAST"
    NEXT = "NEXT"
    NOW = "NOW"


class TopicIRFilterType:
    """TopicIRFilterType enum values."""

    CATEGORY_FILTER = "CATEGORY_FILTER"
    NUMERIC_EQUALITY_FILTER = "NUMERIC_EQUALITY_FILTER"
    NUMERIC_RANGE_FILTER = "NUMERIC_RANGE_FILTER"
    DATE_RANGE_FILTER = "DATE_RANGE_FILTER"
    RELATIVE_DATE_FILTER = "RELATIVE_DATE_FILTER"
    TOP_BOTTOM_FILTER = "TOP_BOTTOM_FILTER"
    EQUALS = "EQUALS"
    RANK_LIMIT_FILTER = "RANK_LIMIT_FILTER"
    ACCEPT_ALL_FILTER = "ACCEPT_ALL_FILTER"


class TopicNumericSeparatorSymbol:
    """TopicNumericSeparatorSymbol enum values."""

    COMMA = "COMMA"
    DOT = "DOT"


class TopicRefreshStatus:
    """TopicRefreshStatus enum values."""

    INITIALIZED = "INITIALIZED"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class TopicRelativeDateFilterFunction:
    """TopicRelativeDateFilterFunction enum values."""

    PREVIOUS = "PREVIOUS"
    THIS = "THIS"
    LAST = "LAST"
    NEXT = "NEXT"
    NOW = "NOW"


class TopicScheduleType:
    """TopicScheduleType enum values."""

    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class TopicSortDirection:
    """TopicSortDirection enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class TopicTimeGranularity:
    """TopicTimeGranularity enum values."""

    SECOND = "SECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"


class TopicUserExperienceVersion:
    """TopicUserExperienceVersion enum values."""

    LEGACY = "LEGACY"
    NEW_READER_EXPERIENCE = "NEW_READER_EXPERIENCE"


class TransposedColumnType:
    """TransposedColumnType enum values."""

    ROW_HEADER_COLUMN = "ROW_HEADER_COLUMN"
    VALUE_COLUMN = "VALUE_COLUMN"


class URLTargetConfiguration:
    """URLTargetConfiguration enum values."""

    NEW_TAB = "NEW_TAB"
    NEW_WINDOW = "NEW_WINDOW"
    SAME_TAB = "SAME_TAB"


class UndefinedSpecifiedValueType:
    """UndefinedSpecifiedValueType enum values."""

    LEAST = "LEAST"
    MOST = "MOST"


class UserRole:
    """UserRole enum values."""

    ADMIN = "ADMIN"
    AUTHOR = "AUTHOR"
    READER = "READER"
    RESTRICTED_AUTHOR = "RESTRICTED_AUTHOR"
    RESTRICTED_READER = "RESTRICTED_READER"
    ADMIN_PRO = "ADMIN_PRO"
    AUTHOR_PRO = "AUTHOR_PRO"
    READER_PRO = "READER_PRO"


class VPCConnectionAvailabilityStatus:
    """VPCConnectionAvailabilityStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    PARTIALLY_AVAILABLE = "PARTIALLY_AVAILABLE"


class VPCConnectionResourceStatus:
    """VPCConnectionResourceStatus enum values."""

    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    DELETION_FAILED = "DELETION_FAILED"
    DELETED = "DELETED"


class ValidationStrategyMode:
    """ValidationStrategyMode enum values."""

    STRICT = "STRICT"
    LENIENT = "LENIENT"


class ValueWhenUnsetOption:
    """ValueWhenUnsetOption enum values."""

    RECOMMENDED_VALUE = "RECOMMENDED_VALUE"
    NULL = "NULL"


class VerticalTextAlignment:
    """VerticalTextAlignment enum values."""

    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"
    AUTO = "AUTO"


class Visibility:
    """Visibility enum values."""

    HIDDEN = "HIDDEN"
    VISIBLE = "VISIBLE"


class VisualCustomActionTrigger:
    """VisualCustomActionTrigger enum values."""

    DATA_POINT_CLICK = "DATA_POINT_CLICK"
    DATA_POINT_MENU = "DATA_POINT_MENU"


class VisualHighlightTrigger:
    """VisualHighlightTrigger enum values."""

    DATA_POINT_CLICK = "DATA_POINT_CLICK"
    DATA_POINT_HOVER = "DATA_POINT_HOVER"
    NONE = "NONE"


class VisualRole:
    """VisualRole enum values."""

    PRIMARY = "PRIMARY"
    COMPLIMENTARY = "COMPLIMENTARY"
    MULTI_INTENT = "MULTI_INTENT"
    FALLBACK = "FALLBACK"
    FRAGMENT = "FRAGMENT"


class WebCrawlerAuthType:
    """WebCrawlerAuthType enum values."""

    NO_AUTH = "NO_AUTH"
    BASIC_AUTH = "BASIC_AUTH"
    FORM = "FORM"
    SAML = "SAML"


class WidgetStatus:
    """WidgetStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class WordCloudCloudLayout:
    """WordCloudCloudLayout enum values."""

    FLUID = "FLUID"
    NORMAL = "NORMAL"


class WordCloudWordCasing:
    """WordCloudWordCasing enum values."""

    LOWER_CASE = "LOWER_CASE"
    EXISTING_CASE = "EXISTING_CASE"


class WordCloudWordOrientation:
    """WordCloudWordOrientation enum values."""

    HORIZONTAL = "HORIZONTAL"
    HORIZONTAL_AND_VERTICAL = "HORIZONTAL_AND_VERTICAL"


class WordCloudWordPadding:
    """WordCloudWordPadding enum values."""

    NONE = "NONE"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class WordCloudWordScaling:
    """WordCloudWordScaling enum values."""

    EMPHASIZE = "EMPHASIZE"
    NORMAL = "NORMAL"


@dataclass
class AggregateOperation(PropertyType):
    GROUP_BY_COLUMN_NAMES = "GroupByColumnNames"
    ALIAS = "Alias"
    AGGREGATIONS = "Aggregations"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_by_column_names": "GroupByColumnNames",
        "alias": "Alias",
        "aggregations": "Aggregations",
        "source": "Source",
    }

    group_by_column_names: Optional[Union[list[str], Ref]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aggregations: Optional[list[Aggregation]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class Aggregation(PropertyType):
    AGGREGATION_FUNCTION = "AggregationFunction"
    NEW_COLUMN_NAME = "NewColumnName"
    NEW_COLUMN_ID = "NewColumnId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
        "new_column_name": "NewColumnName",
        "new_column_id": "NewColumnId",
    }

    aggregation_function: Optional[DataPrepAggregationFunction] = None
    new_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AppendOperation(PropertyType):
    APPENDED_COLUMNS = "AppendedColumns"
    SECOND_SOURCE = "SecondSource"
    ALIAS = "Alias"
    FIRST_SOURCE = "FirstSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "appended_columns": "AppendedColumns",
        "second_source": "SecondSource",
        "alias": "Alias",
        "first_source": "FirstSource",
    }

    appended_columns: Optional[list[AppendedColumn]] = None
    second_source: Optional[TransformOperationSource] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_source: Optional[TransformOperationSource] = None


@dataclass
class AppendedColumn(PropertyType):
    COLUMN_NAME = "ColumnName"
    NEW_COLUMN_ID = "NewColumnId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "new_column_id": "NewColumnId",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CalculatedColumn(PropertyType):
    COLUMN_ID = "ColumnId"
    COLUMN_NAME = "ColumnName"
    EXPRESSION = "Expression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_id": "ColumnId",
        "column_name": "ColumnName",
        "expression": "Expression",
    }

    column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CastColumnTypeOperation(PropertyType):
    COLUMN_NAME = "ColumnName"
    SUB_TYPE = "SubType"
    FORMAT = "Format"
    NEW_COLUMN_TYPE = "NewColumnType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "sub_type": "SubType",
        "format": "Format",
        "new_column_type": "NewColumnType",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, ColumnDataSubType, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_type: Optional[Union[str, ColumnDataType, Ref, GetAtt, Sub]] = None


@dataclass
class CastColumnTypesOperation(PropertyType):
    CAST_COLUMN_TYPE_OPERATIONS = "CastColumnTypeOperations"
    ALIAS = "Alias"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cast_column_type_operations": "CastColumnTypeOperations",
        "alias": "Alias",
        "source": "Source",
    }

    cast_column_type_operations: Optional[list[CastColumnTypeOperation]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class ColumnGroup(PropertyType):
    GEO_SPATIAL_COLUMN_GROUP = "GeoSpatialColumnGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "geo_spatial_column_group": "GeoSpatialColumnGroup",
    }

    geo_spatial_column_group: Optional[GeoSpatialColumnGroup] = None


@dataclass
class ColumnLevelPermissionRule(PropertyType):
    COLUMN_NAMES = "ColumnNames"
    PRINCIPALS = "Principals"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_names": "ColumnNames",
        "principals": "Principals",
    }

    column_names: Optional[Union[list[str], Ref]] = None
    principals: Optional[Union[list[str], Ref]] = None


@dataclass
class ColumnToUnpivot(PropertyType):
    COLUMN_NAME = "ColumnName"
    NEW_VALUE = "NewValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "new_value": "NewValue",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CreateColumnsOperation(PropertyType):
    ALIAS = "Alias"
    COLUMNS = "Columns"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "columns": "Columns",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[CalculatedColumn]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class CustomSql(PropertyType):
    DATA_SOURCE_ARN = "DataSourceArn"
    SQL_QUERY = "SqlQuery"
    COLUMNS = "Columns"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "sql_query": "SqlQuery",
        "columns": "Columns",
        "name": "Name",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sql_query: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[list[InputColumn]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrepAggregationFunction(PropertyType):
    PERCENTILE_AGGREGATION = "PercentileAggregation"
    SIMPLE_AGGREGATION = "SimpleAggregation"
    LIST_AGGREGATION = "ListAggregation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "percentile_aggregation": "PercentileAggregation",
        "simple_aggregation": "SimpleAggregation",
        "list_aggregation": "ListAggregation",
    }

    percentile_aggregation: Optional[DataPrepPercentileAggregationFunction] = None
    simple_aggregation: Optional[DataPrepSimpleAggregationFunction] = None
    list_aggregation: Optional[DataPrepListAggregationFunction] = None


@dataclass
class DataPrepConfiguration(PropertyType):
    DESTINATION_TABLE_MAP = "DestinationTableMap"
    TRANSFORM_STEP_MAP = "TransformStepMap"
    SOURCE_TABLE_MAP = "SourceTableMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_table_map": "DestinationTableMap",
        "transform_step_map": "TransformStepMap",
        "source_table_map": "SourceTableMap",
    }

    destination_table_map: Optional[dict[str, Any]] = None
    transform_step_map: Optional[dict[str, Any]] = None
    source_table_map: Optional[dict[str, Any]] = None


@dataclass
class DataPrepListAggregationFunction(PropertyType):
    DISTINCT = "Distinct"
    INPUT_COLUMN_NAME = "InputColumnName"
    SEPARATOR = "Separator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "distinct": "Distinct",
        "input_column_name": "InputColumnName",
        "separator": "Separator",
    }

    distinct: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    input_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    separator: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrepPercentileAggregationFunction(PropertyType):
    INPUT_COLUMN_NAME = "InputColumnName"
    PERCENTILE_VALUE = "PercentileValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_column_name": "InputColumnName",
        "percentile_value": "PercentileValue",
    }

    input_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    percentile_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DataPrepSimpleAggregationFunction(PropertyType):
    FUNCTION_TYPE = "FunctionType"
    INPUT_COLUMN_NAME = "InputColumnName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function_type": "FunctionType",
        "input_column_name": "InputColumnName",
    }

    function_type: Optional[Union[str, DataPrepSimpleAggregationFunctionType, Ref, GetAtt, Sub]] = None
    input_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetColumnIdMapping(PropertyType):
    SOURCE_COLUMN_ID = "SourceColumnId"
    TARGET_COLUMN_ID = "TargetColumnId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_column_id": "SourceColumnId",
        "target_column_id": "TargetColumnId",
    }

    source_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetDateComparisonFilterCondition(PropertyType):
    OPERATOR = "Operator"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, DataSetDateComparisonFilterOperator, Ref, GetAtt, Sub]] = None
    value: Optional[DataSetDateFilterValue] = None


@dataclass
class DataSetDateFilterCondition(PropertyType):
    COLUMN_NAME = "ColumnName"
    RANGE_FILTER_CONDITION = "RangeFilterCondition"
    COMPARISON_FILTER_CONDITION = "ComparisonFilterCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "range_filter_condition": "RangeFilterCondition",
        "comparison_filter_condition": "ComparisonFilterCondition",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_filter_condition: Optional[DataSetDateRangeFilterCondition] = None
    comparison_filter_condition: Optional[DataSetDateComparisonFilterCondition] = None


@dataclass
class DataSetDateFilterValue(PropertyType):
    STATIC_VALUE = "StaticValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
    }

    static_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetDateRangeFilterCondition(PropertyType):
    INCLUDE_MAXIMUM = "IncludeMaximum"
    RANGE_MINIMUM = "RangeMinimum"
    RANGE_MAXIMUM = "RangeMaximum"
    INCLUDE_MINIMUM = "IncludeMinimum"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_maximum": "IncludeMaximum",
        "range_minimum": "RangeMinimum",
        "range_maximum": "RangeMaximum",
        "include_minimum": "IncludeMinimum",
    }

    include_maximum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    range_minimum: Optional[DataSetDateFilterValue] = None
    range_maximum: Optional[DataSetDateFilterValue] = None
    include_minimum: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetNumericComparisonFilterCondition(PropertyType):
    OPERATOR = "Operator"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, DataSetNumericComparisonFilterOperator, Ref, GetAtt, Sub]] = None
    value: Optional[DataSetNumericFilterValue] = None


@dataclass
class DataSetNumericFilterCondition(PropertyType):
    COLUMN_NAME = "ColumnName"
    RANGE_FILTER_CONDITION = "RangeFilterCondition"
    COMPARISON_FILTER_CONDITION = "ComparisonFilterCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "range_filter_condition": "RangeFilterCondition",
        "comparison_filter_condition": "ComparisonFilterCondition",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range_filter_condition: Optional[DataSetNumericRangeFilterCondition] = None
    comparison_filter_condition: Optional[DataSetNumericComparisonFilterCondition] = None


@dataclass
class DataSetNumericFilterValue(PropertyType):
    STATIC_VALUE = "StaticValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
    }

    static_value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetNumericRangeFilterCondition(PropertyType):
    INCLUDE_MAXIMUM = "IncludeMaximum"
    RANGE_MINIMUM = "RangeMinimum"
    RANGE_MAXIMUM = "RangeMaximum"
    INCLUDE_MINIMUM = "IncludeMinimum"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_maximum": "IncludeMaximum",
        "range_minimum": "RangeMinimum",
        "range_maximum": "RangeMaximum",
        "include_minimum": "IncludeMinimum",
    }

    include_maximum: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    range_minimum: Optional[DataSetNumericFilterValue] = None
    range_maximum: Optional[DataSetNumericFilterValue] = None
    include_minimum: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetRefreshProperties(PropertyType):
    REFRESH_CONFIGURATION = "RefreshConfiguration"
    FAILURE_CONFIGURATION = "FailureConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_configuration": "RefreshConfiguration",
        "failure_configuration": "FailureConfiguration",
    }

    refresh_configuration: Optional[RefreshConfiguration] = None
    failure_configuration: Optional[RefreshFailureConfiguration] = None


@dataclass
class DataSetStringComparisonFilterCondition(PropertyType):
    OPERATOR = "Operator"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "value": "Value",
    }

    operator: Optional[Union[str, DataSetStringComparisonFilterOperator, Ref, GetAtt, Sub]] = None
    value: Optional[DataSetStringFilterValue] = None


@dataclass
class DataSetStringFilterCondition(PropertyType):
    COLUMN_NAME = "ColumnName"
    COMPARISON_FILTER_CONDITION = "ComparisonFilterCondition"
    LIST_FILTER_CONDITION = "ListFilterCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "comparison_filter_condition": "ComparisonFilterCondition",
        "list_filter_condition": "ListFilterCondition",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    comparison_filter_condition: Optional[DataSetStringComparisonFilterCondition] = None
    list_filter_condition: Optional[DataSetStringListFilterCondition] = None


@dataclass
class DataSetStringFilterValue(PropertyType):
    STATIC_VALUE = "StaticValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_value": "StaticValue",
    }

    static_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSetStringListFilterCondition(PropertyType):
    OPERATOR = "Operator"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "values": "Values",
    }

    operator: Optional[Union[str, DataSetStringListFilterOperator, Ref, GetAtt, Sub]] = None
    values: Optional[DataSetStringListFilterValue] = None


@dataclass
class DataSetStringListFilterValue(PropertyType):
    STATIC_VALUES = "StaticValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class DataSetUsageConfiguration(PropertyType):
    DISABLE_USE_AS_IMPORTED_SOURCE = "DisableUseAsImportedSource"
    DISABLE_USE_AS_DIRECT_QUERY_SOURCE = "DisableUseAsDirectQuerySource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disable_use_as_imported_source": "DisableUseAsImportedSource",
        "disable_use_as_direct_query_source": "DisableUseAsDirectQuerySource",
    }

    disable_use_as_imported_source: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    disable_use_as_direct_query_source: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetParameter(PropertyType):
    INTEGER_DATASET_PARAMETER = "IntegerDatasetParameter"
    DATE_TIME_DATASET_PARAMETER = "DateTimeDatasetParameter"
    DECIMAL_DATASET_PARAMETER = "DecimalDatasetParameter"
    STRING_DATASET_PARAMETER = "StringDatasetParameter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "integer_dataset_parameter": "IntegerDatasetParameter",
        "date_time_dataset_parameter": "DateTimeDatasetParameter",
        "decimal_dataset_parameter": "DecimalDatasetParameter",
        "string_dataset_parameter": "StringDatasetParameter",
    }

    integer_dataset_parameter: Optional[IntegerDatasetParameter] = None
    date_time_dataset_parameter: Optional[DateTimeDatasetParameter] = None
    decimal_dataset_parameter: Optional[DecimalDatasetParameter] = None
    string_dataset_parameter: Optional[StringDatasetParameter] = None


@dataclass
class DateTimeDatasetParameter(PropertyType):
    VALUE_TYPE = "ValueType"
    TIME_GRANULARITY = "TimeGranularity"
    DEFAULT_VALUES = "DefaultValues"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "time_granularity": "TimeGranularity",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    time_granularity: Optional[Union[str, TimeGranularity, Ref, GetAtt, Sub]] = None
    default_values: Optional[DateTimeDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeDatasetParameterDefaultValues(PropertyType):
    STATIC_VALUES = "StaticValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class DecimalDatasetParameter(PropertyType):
    VALUE_TYPE = "ValueType"
    DEFAULT_VALUES = "DefaultValues"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    default_values: Optional[DecimalDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecimalDatasetParameterDefaultValues(PropertyType):
    STATIC_VALUES = "StaticValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[float], Ref]] = None


@dataclass
class DestinationTable(PropertyType):
    ALIAS = "Alias"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[DestinationTableSource] = None


@dataclass
class DestinationTableSource(PropertyType):
    TRANSFORM_OPERATION_ID = "TransformOperationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transform_operation_id": "TransformOperationId",
    }

    transform_operation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FieldFolder(PropertyType):
    DESCRIPTION = "Description"
    COLUMNS = "Columns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "columns": "Columns",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[Union[list[str], Ref]] = None


@dataclass
class FilterOperation(PropertyType):
    DATE_FILTER_CONDITION = "DateFilterCondition"
    STRING_FILTER_CONDITION = "StringFilterCondition"
    CONDITION_EXPRESSION = "ConditionExpression"
    NUMERIC_FILTER_CONDITION = "NumericFilterCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "date_filter_condition": "DateFilterCondition",
        "string_filter_condition": "StringFilterCondition",
        "condition_expression": "ConditionExpression",
        "numeric_filter_condition": "NumericFilterCondition",
    }

    date_filter_condition: Optional[DataSetDateFilterCondition] = None
    string_filter_condition: Optional[DataSetStringFilterCondition] = None
    condition_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    numeric_filter_condition: Optional[DataSetNumericFilterCondition] = None


@dataclass
class FiltersOperation(PropertyType):
    FILTER_OPERATIONS = "FilterOperations"
    ALIAS = "Alias"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_operations": "FilterOperations",
        "alias": "Alias",
        "source": "Source",
    }

    filter_operations: Optional[list[FilterOperation]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class GeoSpatialColumnGroup(PropertyType):
    COLUMNS = "Columns"
    COUNTRY_CODE = "CountryCode"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "columns": "Columns",
        "country_code": "CountryCode",
        "name": "Name",
    }

    columns: Optional[Union[list[str], Ref]] = None
    country_code: Optional[Union[str, GeoSpatialCountryCode, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImportTableOperation(PropertyType):
    ALIAS = "Alias"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[ImportTableOperationSource] = None


@dataclass
class ImportTableOperationSource(PropertyType):
    SOURCE_TABLE_ID = "SourceTableId"
    COLUMN_ID_MAPPINGS = "ColumnIdMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_table_id": "SourceTableId",
        "column_id_mappings": "ColumnIdMappings",
    }

    source_table_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_id_mappings: Optional[list[DataSetColumnIdMapping]] = None


@dataclass
class IncrementalRefresh(PropertyType):
    LOOKBACK_WINDOW = "LookbackWindow"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lookback_window": "LookbackWindow",
    }

    lookback_window: Optional[LookbackWindow] = None


@dataclass
class IngestionWaitPolicy(PropertyType):
    WAIT_FOR_SPICE_INGESTION = "WaitForSpiceIngestion"
    INGESTION_WAIT_TIME_IN_HOURS = "IngestionWaitTimeInHours"

    _property_mappings: ClassVar[dict[str, str]] = {
        "wait_for_spice_ingestion": "WaitForSpiceIngestion",
        "ingestion_wait_time_in_hours": "IngestionWaitTimeInHours",
    }

    wait_for_spice_ingestion: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ingestion_wait_time_in_hours: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class InputColumn(PropertyType):
    TYPE = "Type"
    SUB_TYPE = "SubType"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "sub_type": "SubType",
        "id": "Id",
        "name": "Name",
    }

    type_: Optional[Union[str, InputColumnDataType, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, ColumnDataSubType, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerDatasetParameter(PropertyType):
    VALUE_TYPE = "ValueType"
    DEFAULT_VALUES = "DefaultValues"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    default_values: Optional[IntegerDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegerDatasetParameterDefaultValues(PropertyType):
    STATIC_VALUES = "StaticValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[int], Ref]] = None


@dataclass
class JoinOperandProperties(PropertyType):
    OUTPUT_COLUMN_NAME_OVERRIDES = "OutputColumnNameOverrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_column_name_overrides": "OutputColumnNameOverrides",
    }

    output_column_name_overrides: Optional[list[OutputColumnNameOverride]] = None


@dataclass
class JoinOperation(PropertyType):
    ON_CLAUSE = "OnClause"
    TYPE = "Type"
    RIGHT_OPERAND_PROPERTIES = "RightOperandProperties"
    LEFT_OPERAND_PROPERTIES = "LeftOperandProperties"
    ALIAS = "Alias"
    LEFT_OPERAND = "LeftOperand"
    RIGHT_OPERAND = "RightOperand"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_clause": "OnClause",
        "type_": "Type",
        "right_operand_properties": "RightOperandProperties",
        "left_operand_properties": "LeftOperandProperties",
        "alias": "Alias",
        "left_operand": "LeftOperand",
        "right_operand": "RightOperand",
    }

    on_clause: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, JoinOperationType, Ref, GetAtt, Sub]] = None
    right_operand_properties: Optional[JoinOperandProperties] = None
    left_operand_properties: Optional[JoinOperandProperties] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    left_operand: Optional[TransformOperationSource] = None
    right_operand: Optional[TransformOperationSource] = None


@dataclass
class LookbackWindow(PropertyType):
    COLUMN_NAME = "ColumnName"
    SIZE_UNIT = "SizeUnit"
    SIZE = "Size"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "size_unit": "SizeUnit",
        "size": "Size",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_unit: Optional[Union[str, LookbackWindowSizeUnit, Ref, GetAtt, Sub]] = None
    size: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OutputColumn(PropertyType):
    TYPE = "Type"
    DESCRIPTION = "Description"
    SUB_TYPE = "SubType"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "sub_type": "SubType",
        "id": "Id",
        "name": "Name",
    }

    type_: Optional[Union[str, ColumnDataType, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sub_type: Optional[Union[str, ColumnDataSubType, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputColumnNameOverride(PropertyType):
    OUTPUT_COLUMN_NAME = "OutputColumnName"
    SOURCE_COLUMN_NAME = "SourceColumnName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_column_name": "OutputColumnName",
        "source_column_name": "SourceColumnName",
    }

    output_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParentDataSet(PropertyType):
    INPUT_COLUMNS = "InputColumns"
    DATA_SET_ARN = "DataSetArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_columns": "InputColumns",
        "data_set_arn": "DataSetArn",
    }

    input_columns: Optional[list[InputColumn]] = None
    data_set_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PerformanceConfiguration(PropertyType):
    UNIQUE_KEYS = "UniqueKeys"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unique_keys": "UniqueKeys",
    }

    unique_keys: Optional[list[UniqueKey]] = None


@dataclass
class PhysicalTable(PropertyType):
    SAA_S_TABLE = "SaaSTable"
    RELATIONAL_TABLE = "RelationalTable"
    CUSTOM_SQL = "CustomSql"
    S3_SOURCE = "S3Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "saa_s_table": "SaaSTable",
        "relational_table": "RelationalTable",
        "custom_sql": "CustomSql",
        "s3_source": "S3Source",
    }

    saa_s_table: Optional[SaaSTable] = None
    relational_table: Optional[RelationalTable] = None
    custom_sql: Optional[CustomSql] = None
    s3_source: Optional[S3Source] = None


@dataclass
class PivotConfiguration(PropertyType):
    LABEL_COLUMN_NAME = "LabelColumnName"
    PIVOTED_LABELS = "PivotedLabels"

    _property_mappings: ClassVar[dict[str, str]] = {
        "label_column_name": "LabelColumnName",
        "pivoted_labels": "PivotedLabels",
    }

    label_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pivoted_labels: Optional[list[PivotedLabel]] = None


@dataclass
class PivotOperation(PropertyType):
    PIVOT_CONFIGURATION = "PivotConfiguration"
    GROUP_BY_COLUMN_NAMES = "GroupByColumnNames"
    ALIAS = "Alias"
    VALUE_COLUMN_CONFIGURATION = "ValueColumnConfiguration"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pivot_configuration": "PivotConfiguration",
        "group_by_column_names": "GroupByColumnNames",
        "alias": "Alias",
        "value_column_configuration": "ValueColumnConfiguration",
        "source": "Source",
    }

    pivot_configuration: Optional[PivotConfiguration] = None
    group_by_column_names: Optional[Union[list[str], Ref]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_column_configuration: Optional[ValueColumnConfiguration] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class PivotedLabel(PropertyType):
    NEW_COLUMN_NAME = "NewColumnName"
    NEW_COLUMN_ID = "NewColumnId"
    LABEL_NAME = "LabelName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "new_column_name": "NewColumnName",
        "new_column_id": "NewColumnId",
        "label_name": "LabelName",
    }

    new_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    new_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    label_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProjectOperation(PropertyType):
    ALIAS = "Alias"
    PROJECTED_COLUMNS = "ProjectedColumns"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "projected_columns": "ProjectedColumns",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    projected_columns: Optional[Union[list[str], Ref]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class RefreshConfiguration(PropertyType):
    INCREMENTAL_REFRESH = "IncrementalRefresh"

    _property_mappings: ClassVar[dict[str, str]] = {
        "incremental_refresh": "IncrementalRefresh",
    }

    incremental_refresh: Optional[IncrementalRefresh] = None


@dataclass
class RefreshFailureConfiguration(PropertyType):
    EMAIL_ALERT = "EmailAlert"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email_alert": "EmailAlert",
    }

    email_alert: Optional[RefreshFailureEmailAlert] = None


@dataclass
class RefreshFailureEmailAlert(PropertyType):
    ALERT_STATUS = "AlertStatus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alert_status": "AlertStatus",
    }

    alert_status: Optional[Union[str, RefreshFailureAlertStatus, Ref, GetAtt, Sub]] = None


@dataclass
class RelationalTable(PropertyType):
    DATA_SOURCE_ARN = "DataSourceArn"
    INPUT_COLUMNS = "InputColumns"
    SCHEMA = "Schema"
    CATALOG = "Catalog"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "input_columns": "InputColumns",
        "schema": "Schema",
        "catalog": "Catalog",
        "name": "Name",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_columns: Optional[list[InputColumn]] = None
    schema: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenameColumnOperation(PropertyType):
    NEW_COLUMN_NAME = "NewColumnName"
    COLUMN_NAME = "ColumnName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "new_column_name": "NewColumnName",
        "column_name": "ColumnName",
    }

    new_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenameColumnsOperation(PropertyType):
    ALIAS = "Alias"
    RENAME_COLUMN_OPERATIONS = "RenameColumnOperations"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "rename_column_operations": "RenameColumnOperations",
        "source": "Source",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rename_column_operations: Optional[list[RenameColumnOperation]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class ResourcePermission(PropertyType):
    ACTIONS = "Actions"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "principal": "Principal",
    }

    actions: Optional[Union[list[str], Ref]] = None
    principal: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RowLevelPermissionConfiguration(PropertyType):
    TAG_CONFIGURATION = "TagConfiguration"
    ROW_LEVEL_PERMISSION_DATA_SET = "RowLevelPermissionDataSet"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_configuration": "TagConfiguration",
        "row_level_permission_data_set": "RowLevelPermissionDataSet",
    }

    tag_configuration: Optional[RowLevelPermissionTagConfiguration] = None
    row_level_permission_data_set: Optional[RowLevelPermissionDataSet] = None


@dataclass
class RowLevelPermissionDataSet(PropertyType):
    STATUS = "Status"
    FORMAT_VERSION = "FormatVersion"
    ARN = "Arn"
    NAMESPACE = "Namespace"
    PERMISSION_POLICY = "PermissionPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "format_version": "FormatVersion",
        "arn": "Arn",
        "namespace": "Namespace",
        "permission_policy": "PermissionPolicy",
    }

    status: Optional[Union[str, Status, Ref, GetAtt, Sub]] = None
    format_version: Optional[Union[str, RowLevelPermissionFormatVersion, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    permission_policy: Optional[Union[str, RowLevelPermissionPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class RowLevelPermissionTagConfiguration(PropertyType):
    STATUS = "Status"
    TAG_RULES = "TagRules"
    TAG_RULE_CONFIGURATIONS = "TagRuleConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "tag_rules": "TagRules",
        "tag_rule_configurations": "TagRuleConfigurations",
    }

    status: Optional[Union[str, Status, Ref, GetAtt, Sub]] = None
    tag_rules: Optional[list[RowLevelPermissionTagRule]] = None
    tag_rule_configurations: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class RowLevelPermissionTagRule(PropertyType):
    COLUMN_NAME = "ColumnName"
    TAG_KEY = "TagKey"
    MATCH_ALL_VALUE = "MatchAllValue"
    TAG_MULTI_VALUE_DELIMITER = "TagMultiValueDelimiter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "tag_key": "TagKey",
        "match_all_value": "MatchAllValue",
        "tag_multi_value_delimiter": "TagMultiValueDelimiter",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_all_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_multi_value_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Source(PropertyType):
    DATA_SOURCE_ARN = "DataSourceArn"
    INPUT_COLUMNS = "InputColumns"
    UPLOAD_SETTINGS = "UploadSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "input_columns": "InputColumns",
        "upload_settings": "UploadSettings",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_columns: Optional[list[InputColumn]] = None
    upload_settings: Optional[UploadSettings] = None


@dataclass
class SaaSTable(PropertyType):
    DATA_SOURCE_ARN = "DataSourceArn"
    INPUT_COLUMNS = "InputColumns"
    TABLE_PATH = "TablePath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_source_arn": "DataSourceArn",
        "input_columns": "InputColumns",
        "table_path": "TablePath",
    }

    data_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_columns: Optional[list[InputColumn]] = None
    table_path: Optional[list[TablePathElement]] = None


@dataclass
class SemanticModelConfiguration(PropertyType):
    TABLE_MAP = "TableMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_map": "TableMap",
    }

    table_map: Optional[dict[str, Any]] = None


@dataclass
class SemanticTable(PropertyType):
    ALIAS = "Alias"
    DESTINATION_TABLE_ID = "DestinationTableId"
    ROW_LEVEL_PERMISSION_CONFIGURATION = "RowLevelPermissionConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias": "Alias",
        "destination_table_id": "DestinationTableId",
        "row_level_permission_configuration": "RowLevelPermissionConfiguration",
    }

    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_table_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    row_level_permission_configuration: Optional[RowLevelPermissionConfiguration] = None


@dataclass
class SourceTable(PropertyType):
    PHYSICAL_TABLE_ID = "PhysicalTableId"
    DATA_SET = "DataSet"

    _property_mappings: ClassVar[dict[str, str]] = {
        "physical_table_id": "PhysicalTableId",
        "data_set": "DataSet",
    }

    physical_table_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_set: Optional[ParentDataSet] = None


@dataclass
class StringDatasetParameter(PropertyType):
    VALUE_TYPE = "ValueType"
    DEFAULT_VALUES = "DefaultValues"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "default_values": "DefaultValues",
        "id": "Id",
        "name": "Name",
    }

    value_type: Optional[Union[str, DatasetParameterValueType, Ref, GetAtt, Sub]] = None
    default_values: Optional[StringDatasetParameterDefaultValues] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StringDatasetParameterDefaultValues(PropertyType):
    STATIC_VALUES = "StaticValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static_values": "StaticValues",
    }

    static_values: Optional[Union[list[str], Ref]] = None


@dataclass
class TablePathElement(PropertyType):
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
        "name": "Name",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TransformOperationSource(PropertyType):
    TRANSFORM_OPERATION_ID = "TransformOperationId"
    COLUMN_ID_MAPPINGS = "ColumnIdMappings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transform_operation_id": "TransformOperationId",
        "column_id_mappings": "ColumnIdMappings",
    }

    transform_operation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_id_mappings: Optional[list[DataSetColumnIdMapping]] = None


@dataclass
class TransformStep(PropertyType):
    PROJECT_STEP = "ProjectStep"
    CREATE_COLUMNS_STEP = "CreateColumnsStep"
    RENAME_COLUMNS_STEP = "RenameColumnsStep"
    CAST_COLUMN_TYPES_STEP = "CastColumnTypesStep"
    IMPORT_TABLE_STEP = "ImportTableStep"
    UNPIVOT_STEP = "UnpivotStep"
    JOIN_STEP = "JoinStep"
    APPEND_STEP = "AppendStep"
    FILTERS_STEP = "FiltersStep"
    AGGREGATE_STEP = "AggregateStep"
    PIVOT_STEP = "PivotStep"

    _property_mappings: ClassVar[dict[str, str]] = {
        "project_step": "ProjectStep",
        "create_columns_step": "CreateColumnsStep",
        "rename_columns_step": "RenameColumnsStep",
        "cast_column_types_step": "CastColumnTypesStep",
        "import_table_step": "ImportTableStep",
        "unpivot_step": "UnpivotStep",
        "join_step": "JoinStep",
        "append_step": "AppendStep",
        "filters_step": "FiltersStep",
        "aggregate_step": "AggregateStep",
        "pivot_step": "PivotStep",
    }

    project_step: Optional[ProjectOperation] = None
    create_columns_step: Optional[CreateColumnsOperation] = None
    rename_columns_step: Optional[RenameColumnsOperation] = None
    cast_column_types_step: Optional[CastColumnTypesOperation] = None
    import_table_step: Optional[ImportTableOperation] = None
    unpivot_step: Optional[UnpivotOperation] = None
    join_step: Optional[JoinOperation] = None
    append_step: Optional[AppendOperation] = None
    filters_step: Optional[FiltersOperation] = None
    aggregate_step: Optional[AggregateOperation] = None
    pivot_step: Optional[PivotOperation] = None


@dataclass
class UniqueKey(PropertyType):
    COLUMN_NAMES = "ColumnNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_names": "ColumnNames",
    }

    column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class UnpivotOperation(PropertyType):
    UNPIVOTED_LABEL_COLUMN_NAME = "UnpivotedLabelColumnName"
    COLUMNS_TO_UNPIVOT = "ColumnsToUnpivot"
    UNPIVOTED_LABEL_COLUMN_ID = "UnpivotedLabelColumnId"
    ALIAS = "Alias"
    UNPIVOTED_VALUE_COLUMN_ID = "UnpivotedValueColumnId"
    UNPIVOTED_VALUE_COLUMN_NAME = "UnpivotedValueColumnName"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unpivoted_label_column_name": "UnpivotedLabelColumnName",
        "columns_to_unpivot": "ColumnsToUnpivot",
        "unpivoted_label_column_id": "UnpivotedLabelColumnId",
        "alias": "Alias",
        "unpivoted_value_column_id": "UnpivotedValueColumnId",
        "unpivoted_value_column_name": "UnpivotedValueColumnName",
        "source": "Source",
    }

    unpivoted_label_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns_to_unpivot: Optional[list[ColumnToUnpivot]] = None
    unpivoted_label_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unpivoted_value_column_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unpivoted_value_column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[TransformOperationSource] = None


@dataclass
class UploadSettings(PropertyType):
    CONTAINS_HEADER = "ContainsHeader"
    TEXT_QUALIFIER = "TextQualifier"
    FORMAT = "Format"
    START_FROM_ROW = "StartFromRow"
    DELIMITER = "Delimiter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contains_header": "ContainsHeader",
        "text_qualifier": "TextQualifier",
        "format": "Format",
        "start_from_row": "StartFromRow",
        "delimiter": "Delimiter",
    }

    contains_header: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    text_qualifier: Optional[Union[str, TextQualifier, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, FileFormat, Ref, GetAtt, Sub]] = None
    start_from_row: Optional[Union[float, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValueColumnConfiguration(PropertyType):
    AGGREGATION_FUNCTION = "AggregationFunction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregation_function": "AggregationFunction",
    }

    aggregation_function: Optional[DataPrepAggregationFunction] = None

