"""PropertyTypes for AWS::Location::APIKey."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BatchItemErrorCode:
    """BatchItemErrorCode enum values."""

    ACCESSDENIEDERROR = "AccessDeniedError"
    CONFLICTERROR = "ConflictError"
    INTERNALSERVERERROR = "InternalServerError"
    RESOURCENOTFOUNDERROR = "ResourceNotFoundError"
    THROTTLINGERROR = "ThrottlingError"
    VALIDATIONERROR = "ValidationError"


class DimensionUnit:
    """DimensionUnit enum values."""

    METERS = "Meters"
    FEET = "Feet"


class DistanceUnit:
    """DistanceUnit enum values."""

    KILOMETERS = "Kilometers"
    MILES = "Miles"


class ForecastedGeofenceEventType:
    """ForecastedGeofenceEventType enum values."""

    ENTER = "ENTER"
    EXIT = "EXIT"
    IDLE = "IDLE"


class IntendedUse:
    """IntendedUse enum values."""

    SINGLEUSE = "SingleUse"
    STORAGE = "Storage"


class OptimizationMode:
    """OptimizationMode enum values."""

    FASTESTROUTE = "FastestRoute"
    SHORTESTROUTE = "ShortestRoute"


class PositionFiltering:
    """PositionFiltering enum values."""

    TIMEBASED = "TimeBased"
    DISTANCEBASED = "DistanceBased"
    ACCURACYBASED = "AccuracyBased"


class PricingPlan:
    """PricingPlan enum values."""

    REQUESTBASEDUSAGE = "RequestBasedUsage"
    MOBILEASSETTRACKING = "MobileAssetTracking"
    MOBILEASSETMANAGEMENT = "MobileAssetManagement"


class RouteMatrixErrorCode:
    """RouteMatrixErrorCode enum values."""

    ROUTENOTFOUND = "RouteNotFound"
    ROUTETOOLONG = "RouteTooLong"
    POSITIONSNOTFOUND = "PositionsNotFound"
    DESTINATIONPOSITIONNOTFOUND = "DestinationPositionNotFound"
    DEPARTUREPOSITIONNOTFOUND = "DeparturePositionNotFound"
    OTHERVALIDATIONERROR = "OtherValidationError"


class SpeedUnit:
    """SpeedUnit enum values."""

    KILOMETERSPERHOUR = "KilometersPerHour"
    MILESPERHOUR = "MilesPerHour"


class Status:
    """Status enum values."""

    ACTIVE = "Active"
    EXPIRED = "Expired"


class TravelMode:
    """TravelMode enum values."""

    CAR = "Car"
    TRUCK = "Truck"
    WALKING = "Walking"
    BICYCLE = "Bicycle"
    MOTORCYCLE = "Motorcycle"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "UnknownOperation"
    MISSING = "Missing"
    CANNOTPARSE = "CannotParse"
    FIELDVALIDATIONFAILED = "FieldValidationFailed"
    OTHER = "Other"
    UNKNOWNFIELD = "UnknownField"


class VehicleWeightUnit:
    """VehicleWeightUnit enum values."""

    KILOGRAMS = "Kilograms"
    POUNDS = "Pounds"


@dataclass
class AndroidApp(PropertyType):
    CERTIFICATE_FINGERPRINT = "CertificateFingerprint"
    PACKAGE = "Package"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_fingerprint": "CertificateFingerprint",
        "package": "Package",
    }

    certificate_fingerprint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    package: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApiKeyRestrictions(PropertyType):
    ALLOW_ACTIONS = "AllowActions"
    ALLOW_RESOURCES = "AllowResources"
    ALLOW_ANDROID_APPS = "AllowAndroidApps"
    ALLOW_REFERERS = "AllowReferers"
    ALLOW_APPLE_APPS = "AllowAppleApps"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_actions": "AllowActions",
        "allow_resources": "AllowResources",
        "allow_android_apps": "AllowAndroidApps",
        "allow_referers": "AllowReferers",
        "allow_apple_apps": "AllowAppleApps",
    }

    allow_actions: Optional[Union[list[str], Ref]] = None
    allow_resources: Optional[Union[list[str], Ref]] = None
    allow_android_apps: Optional[list[AndroidApp]] = None
    allow_referers: Optional[Union[list[str], Ref]] = None
    allow_apple_apps: Optional[list[AppleApp]] = None


@dataclass
class AppleApp(PropertyType):
    BUNDLE_ID = "BundleId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bundle_id": "BundleId",
    }

    bundle_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

