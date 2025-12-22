"""PropertyTypes for AWS::Invoicing::InvoiceUnit."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BuyerDomain:
    """BuyerDomain enum values."""

    NETWORKID = "NetworkID"


class ConnectionTestingMethod:
    """ConnectionTestingMethod enum values."""

    PROD_ENV_DOLLAR_TEST = "PROD_ENV_DOLLAR_TEST"
    TEST_ENV_REPLAY_TEST = "TEST_ENV_REPLAY_TEST"


class EinvoiceDeliveryAttachmentType:
    """EinvoiceDeliveryAttachmentType enum values."""

    INVOICE_PDF = "INVOICE_PDF"
    RFP_PDF = "RFP_PDF"


class EinvoiceDeliveryDocumentType:
    """EinvoiceDeliveryDocumentType enum values."""

    AWS_CLOUD_INVOICE = "AWS_CLOUD_INVOICE"
    AWS_CLOUD_CREDIT_MEMO = "AWS_CLOUD_CREDIT_MEMO"
    AWS_MARKETPLACE_INVOICE = "AWS_MARKETPLACE_INVOICE"
    AWS_MARKETPLACE_CREDIT_MEMO = "AWS_MARKETPLACE_CREDIT_MEMO"
    AWS_REQUEST_FOR_PAYMENT = "AWS_REQUEST_FOR_PAYMENT"


class InvoiceType:
    """InvoiceType enum values."""

    INVOICE = "INVOICE"
    CREDIT_MEMO = "CREDIT_MEMO"


class ListInvoiceSummariesResourceType:
    """ListInvoiceSummariesResourceType enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    INVOICE_ID = "INVOICE_ID"


class ProcurementPortalName:
    """ProcurementPortalName enum values."""

    SAP_BUSINESS_NETWORK = "SAP_BUSINESS_NETWORK"
    COUPA = "COUPA"


class ProcurementPortalPreferenceStatus:
    """ProcurementPortalPreferenceStatus enum values."""

    PENDING_VERIFICATION = "PENDING_VERIFICATION"
    TEST_INITIALIZED = "TEST_INITIALIZED"
    TEST_INITIALIZATION_FAILED = "TEST_INITIALIZATION_FAILED"
    TEST_FAILED = "TEST_FAILED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"


class Protocol:
    """Protocol enum values."""

    CXML = "CXML"


class PurchaseOrderDataSourceType:
    """PurchaseOrderDataSourceType enum values."""

    ASSOCIATED_PURCHASE_ORDER_REQUIRED = "ASSOCIATED_PURCHASE_ORDER_REQUIRED"
    PURCHASE_ORDER_NOT_REQUIRED = "PURCHASE_ORDER_NOT_REQUIRED"


class SupplierDomain:
    """SupplierDomain enum values."""

    NETWORKID = "NetworkID"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    NONMEMBERPRESENT = "nonMemberPresent"
    MAXACCOUNTSEXCEEDED = "maxAccountsExceeded"
    MAXINVOICEUNITSEXCEEDED = "maxInvoiceUnitsExceeded"
    DUPLICATEINVOICEUNIT = "duplicateInvoiceUnit"
    MUTUALEXCLUSIONERROR = "mutualExclusionError"
    ACCOUNTMEMBERSHIPERROR = "accountMembershipError"
    TAXSETTINGSERROR = "taxSettingsError"
    EXPIREDNEXTTOKEN = "expiredNextToken"
    INVALIDNEXTTOKEN = "invalidNextToken"
    INVALIDINPUT = "invalidInput"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    CANNOTPARSE = "cannotParse"
    UNKNOWNOPERATION = "unknownOperation"
    OTHER = "other"


@dataclass
class ResourceTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    LINKED_ACCOUNTS = "LinkedAccounts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "linked_accounts": "LinkedAccounts",
    }

    linked_accounts: Optional[Union[list[str], Ref]] = None

