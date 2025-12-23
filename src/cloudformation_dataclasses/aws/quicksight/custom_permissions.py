"""PropertyTypes for AWS::QuickSight::CustomPermissions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Capabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_content_in_scheduled_reports_email": "IncludeContentInScheduledReportsEmail",
        "export_to_csv_in_scheduled_reports": "ExportToCsvInScheduledReports",
        "create_and_update_data_sources": "CreateAndUpdateDataSources",
        "view_account_spice_capacity": "ViewAccountSPICECapacity",
        "dashboard": "Dashboard",
        "export_to_pdf_in_scheduled_reports": "ExportToPdfInScheduledReports",
        "create_spice_dataset": "CreateSPICEDataset",
        "create_and_update_datasets": "CreateAndUpdateDatasets",
        "print_reports": "PrintReports",
        "share_datasets": "ShareDatasets",
        "export_to_excel_in_scheduled_reports": "ExportToExcelInScheduledReports",
        "create_and_update_dashboard_email_reports": "CreateAndUpdateDashboardEmailReports",
        "create_and_update_threshold_alerts": "CreateAndUpdateThresholdAlerts",
        "create_shared_folders": "CreateSharedFolders",
        "share_dashboards": "ShareDashboards",
        "rename_shared_folders": "RenameSharedFolders",
        "add_or_run_anomaly_detection_for_analyses": "AddOrRunAnomalyDetectionForAnalyses",
        "share_data_sources": "ShareDataSources",
        "export_to_excel": "ExportToExcel",
        "export_to_pdf": "ExportToPdf",
        "share_analyses": "ShareAnalyses",
        "subscribe_dashboard_email_reports": "SubscribeDashboardEmailReports",
        "analysis": "Analysis",
        "export_to_csv": "ExportToCsv",
        "create_and_update_themes": "CreateAndUpdateThemes",
    }

    include_content_in_scheduled_reports_email: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    export_to_csv_in_scheduled_reports: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_and_update_data_sources: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    view_account_spice_capacity: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    dashboard: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    export_to_pdf_in_scheduled_reports: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_spice_dataset: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_and_update_datasets: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    print_reports: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    share_datasets: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    export_to_excel_in_scheduled_reports: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_and_update_dashboard_email_reports: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_and_update_threshold_alerts: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_shared_folders: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    share_dashboards: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    rename_shared_folders: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    add_or_run_anomaly_detection_for_analyses: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    share_data_sources: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    export_to_excel: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    export_to_pdf: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    share_analyses: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    subscribe_dashboard_email_reports: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    analysis: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    export_to_csv: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None
    create_and_update_themes: Optional[Union[str, CapabilityState, Ref, GetAtt, Sub]] = None

