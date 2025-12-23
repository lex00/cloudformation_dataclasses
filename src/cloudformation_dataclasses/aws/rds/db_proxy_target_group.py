"""PropertyTypes for AWS::RDS::DBProxyTargetGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionPoolConfigurationInfoFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_idle_connections_percent": "MaxIdleConnectionsPercent",
        "max_connections_percent": "MaxConnectionsPercent",
        "init_query": "InitQuery",
        "connection_borrow_timeout": "ConnectionBorrowTimeout",
        "session_pinning_filters": "SessionPinningFilters",
    }

    max_idle_connections_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_connections_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    init_query: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_borrow_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    session_pinning_filters: Optional[Union[list[str], Ref]] = None

