"""PropertyTypes for AWS::Location::Map."""

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
class MapConfiguration(PropertyType):
    POLITICAL_VIEW = "PoliticalView"
    STYLE = "Style"
    CUSTOM_LAYERS = "CustomLayers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "political_view": "PoliticalView",
        "style": "Style",
        "custom_layers": "CustomLayers",
    }

    political_view: Optional[Union[str, Ref, GetAtt, Sub]] = None
    style: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_layers: Optional[Union[list[str], Ref]] = None

