"""PropertyTypes for AWS::Transfer::Server."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EndpointDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address_allocation_ids": "AddressAllocationIds",
        "vpc_id": "VpcId",
        "vpc_endpoint_id": "VpcEndpointId",
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    address_allocation_ids: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class IdentityProviderDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "directory_id": "DirectoryId",
        "invocation_role": "InvocationRole",
        "url": "Url",
        "sftp_authentication_methods": "SftpAuthenticationMethods",
    }

    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    directory_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invocation_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sftp_authentication_methods: Optional[Union[str, SftpAuthenticationMethods, Ref, GetAtt, Sub]] = None


@dataclass
class ProtocolDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "as2_transports": "As2Transports",
        "passive_ip": "PassiveIp",
        "set_stat_option": "SetStatOption",
        "tls_session_resumption_mode": "TlsSessionResumptionMode",
    }

    as2_transports: Optional[Union[list[str], Ref]] = None
    passive_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    set_stat_option: Optional[Union[str, SetStatOption, Ref, GetAtt, Sub]] = None
    tls_session_resumption_mode: Optional[Union[str, TlsSessionResumptionMode, Ref, GetAtt, Sub]] = None


@dataclass
class S3StorageOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "directory_listing_optimization": "DirectoryListingOptimization",
    }

    directory_listing_optimization: Optional[Union[str, DirectoryListingOptimization, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "workflow_id": "WorkflowId",
        "execution_role": "ExecutionRole",
    }

    workflow_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "on_upload": "OnUpload",
        "on_partial_upload": "OnPartialUpload",
    }

    on_upload: Optional[list[WorkflowDetail]] = None
    on_partial_upload: Optional[list[WorkflowDetail]] = None

