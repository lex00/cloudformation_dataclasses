"""PropertyTypes for AWS::GameLift::Alias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceptanceType:
    """AcceptanceType enum values."""

    ACCEPT = "ACCEPT"
    REJECT = "REJECT"


class BackfillMode:
    """BackfillMode enum values."""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"


class BalancingStrategy:
    """BalancingStrategy enum values."""

    SPOT_ONLY = "SPOT_ONLY"
    SPOT_PREFERRED = "SPOT_PREFERRED"
    ON_DEMAND_ONLY = "ON_DEMAND_ONLY"


class BuildStatus:
    """BuildStatus enum values."""

    INITIALIZED = "INITIALIZED"
    READY = "READY"
    FAILED = "FAILED"


class CertificateType:
    """CertificateType enum values."""

    DISABLED = "DISABLED"
    GENERATED = "GENERATED"


class ComparisonOperatorType:
    """ComparisonOperatorType enum values."""

    GREATERTHANOREQUALTOTHRESHOLD = "GreaterThanOrEqualToThreshold"
    GREATERTHANTHRESHOLD = "GreaterThanThreshold"
    LESSTHANTHRESHOLD = "LessThanThreshold"
    LESSTHANOREQUALTOTHRESHOLD = "LessThanOrEqualToThreshold"


class ComputeStatus:
    """ComputeStatus enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    TERMINATING = "TERMINATING"
    IMPAIRED = "IMPAIRED"


class ComputeType:
    """ComputeType enum values."""

    EC2 = "EC2"
    ANYWHERE = "ANYWHERE"


class ContainerDependencyCondition:
    """ContainerDependencyCondition enum values."""

    START = "START"
    COMPLETE = "COMPLETE"
    SUCCESS = "SUCCESS"
    HEALTHY = "HEALTHY"


class ContainerFleetBillingType:
    """ContainerFleetBillingType enum values."""

    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"


class ContainerFleetLocationStatus:
    """ContainerFleetLocationStatus enum values."""

    PENDING = "PENDING"
    CREATING = "CREATING"
    CREATED = "CREATED"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"


class ContainerFleetRemoveAttribute:
    """ContainerFleetRemoveAttribute enum values."""

    PER_INSTANCE_CONTAINER_GROUP_DEFINITION = "PER_INSTANCE_CONTAINER_GROUP_DEFINITION"


class ContainerFleetStatus:
    """ContainerFleetStatus enum values."""

    PENDING = "PENDING"
    CREATING = "CREATING"
    CREATED = "CREATED"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"


class ContainerGroupDefinitionStatus:
    """ContainerGroupDefinitionStatus enum values."""

    READY = "READY"
    COPYING = "COPYING"
    FAILED = "FAILED"


class ContainerGroupType:
    """ContainerGroupType enum values."""

    GAME_SERVER = "GAME_SERVER"
    PER_INSTANCE = "PER_INSTANCE"


class ContainerMountPointAccessLevel:
    """ContainerMountPointAccessLevel enum values."""

    READ_ONLY = "READ_ONLY"
    READ_AND_WRITE = "READ_AND_WRITE"


class ContainerOperatingSystem:
    """ContainerOperatingSystem enum values."""

    AMAZON_LINUX_2023 = "AMAZON_LINUX_2023"


class DeploymentImpairmentStrategy:
    """DeploymentImpairmentStrategy enum values."""

    MAINTAIN = "MAINTAIN"
    ROLLBACK = "ROLLBACK"


class DeploymentProtectionStrategy:
    """DeploymentProtectionStrategy enum values."""

    WITH_PROTECTION = "WITH_PROTECTION"
    IGNORE_PROTECTION = "IGNORE_PROTECTION"


class DeploymentStatus:
    """DeploymentStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    IMPAIRED = "IMPAIRED"
    COMPLETE = "COMPLETE"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    CANCELLED = "CANCELLED"
    PENDING = "PENDING"


class EC2InstanceType:
    """EC2InstanceType enum values."""

    T2_MICRO = "t2.micro"
    T2_SMALL = "t2.small"
    T2_MEDIUM = "t2.medium"
    T2_LARGE = "t2.large"
    C3_LARGE = "c3.large"
    C3_XLARGE = "c3.xlarge"
    C3_2XLARGE = "c3.2xlarge"
    C3_4XLARGE = "c3.4xlarge"
    C3_8XLARGE = "c3.8xlarge"
    C4_LARGE = "c4.large"
    C4_XLARGE = "c4.xlarge"
    C4_2XLARGE = "c4.2xlarge"
    C4_4XLARGE = "c4.4xlarge"
    C4_8XLARGE = "c4.8xlarge"
    C5_LARGE = "c5.large"
    C5_XLARGE = "c5.xlarge"
    C5_2XLARGE = "c5.2xlarge"
    C5_4XLARGE = "c5.4xlarge"
    C5_9XLARGE = "c5.9xlarge"
    C5_12XLARGE = "c5.12xlarge"
    C5_18XLARGE = "c5.18xlarge"
    C5_24XLARGE = "c5.24xlarge"
    C5A_LARGE = "c5a.large"
    C5A_XLARGE = "c5a.xlarge"
    C5A_2XLARGE = "c5a.2xlarge"
    C5A_4XLARGE = "c5a.4xlarge"
    C5A_8XLARGE = "c5a.8xlarge"
    C5A_12XLARGE = "c5a.12xlarge"
    C5A_16XLARGE = "c5a.16xlarge"
    C5A_24XLARGE = "c5a.24xlarge"
    R3_LARGE = "r3.large"
    R3_XLARGE = "r3.xlarge"
    R3_2XLARGE = "r3.2xlarge"
    R3_4XLARGE = "r3.4xlarge"
    R3_8XLARGE = "r3.8xlarge"
    R4_LARGE = "r4.large"
    R4_XLARGE = "r4.xlarge"
    R4_2XLARGE = "r4.2xlarge"
    R4_4XLARGE = "r4.4xlarge"
    R4_8XLARGE = "r4.8xlarge"
    R4_16XLARGE = "r4.16xlarge"
    R5_LARGE = "r5.large"
    R5_XLARGE = "r5.xlarge"
    R5_2XLARGE = "r5.2xlarge"
    R5_4XLARGE = "r5.4xlarge"
    R5_8XLARGE = "r5.8xlarge"
    R5_12XLARGE = "r5.12xlarge"
    R5_16XLARGE = "r5.16xlarge"
    R5_24XLARGE = "r5.24xlarge"
    R5A_LARGE = "r5a.large"
    R5A_XLARGE = "r5a.xlarge"
    R5A_2XLARGE = "r5a.2xlarge"
    R5A_4XLARGE = "r5a.4xlarge"
    R5A_8XLARGE = "r5a.8xlarge"
    R5A_12XLARGE = "r5a.12xlarge"
    R5A_16XLARGE = "r5a.16xlarge"
    R5A_24XLARGE = "r5a.24xlarge"
    M3_MEDIUM = "m3.medium"
    M3_LARGE = "m3.large"
    M3_XLARGE = "m3.xlarge"
    M3_2XLARGE = "m3.2xlarge"
    M4_LARGE = "m4.large"
    M4_XLARGE = "m4.xlarge"
    M4_2XLARGE = "m4.2xlarge"
    M4_4XLARGE = "m4.4xlarge"
    M4_10XLARGE = "m4.10xlarge"
    M5_LARGE = "m5.large"
    M5_XLARGE = "m5.xlarge"
    M5_2XLARGE = "m5.2xlarge"
    M5_4XLARGE = "m5.4xlarge"
    M5_8XLARGE = "m5.8xlarge"
    M5_12XLARGE = "m5.12xlarge"
    M5_16XLARGE = "m5.16xlarge"
    M5_24XLARGE = "m5.24xlarge"
    M5A_LARGE = "m5a.large"
    M5A_XLARGE = "m5a.xlarge"
    M5A_2XLARGE = "m5a.2xlarge"
    M5A_4XLARGE = "m5a.4xlarge"
    M5A_8XLARGE = "m5a.8xlarge"
    M5A_12XLARGE = "m5a.12xlarge"
    M5A_16XLARGE = "m5a.16xlarge"
    M5A_24XLARGE = "m5a.24xlarge"
    C5D_LARGE = "c5d.large"
    C5D_XLARGE = "c5d.xlarge"
    C5D_2XLARGE = "c5d.2xlarge"
    C5D_4XLARGE = "c5d.4xlarge"
    C5D_9XLARGE = "c5d.9xlarge"
    C5D_12XLARGE = "c5d.12xlarge"
    C5D_18XLARGE = "c5d.18xlarge"
    C5D_24XLARGE = "c5d.24xlarge"
    C6A_LARGE = "c6a.large"
    C6A_XLARGE = "c6a.xlarge"
    C6A_2XLARGE = "c6a.2xlarge"
    C6A_4XLARGE = "c6a.4xlarge"
    C6A_8XLARGE = "c6a.8xlarge"
    C6A_12XLARGE = "c6a.12xlarge"
    C6A_16XLARGE = "c6a.16xlarge"
    C6A_24XLARGE = "c6a.24xlarge"
    C6I_LARGE = "c6i.large"
    C6I_XLARGE = "c6i.xlarge"
    C6I_2XLARGE = "c6i.2xlarge"
    C6I_4XLARGE = "c6i.4xlarge"
    C6I_8XLARGE = "c6i.8xlarge"
    C6I_12XLARGE = "c6i.12xlarge"
    C6I_16XLARGE = "c6i.16xlarge"
    C6I_24XLARGE = "c6i.24xlarge"
    R5D_LARGE = "r5d.large"
    R5D_XLARGE = "r5d.xlarge"
    R5D_2XLARGE = "r5d.2xlarge"
    R5D_4XLARGE = "r5d.4xlarge"
    R5D_8XLARGE = "r5d.8xlarge"
    R5D_12XLARGE = "r5d.12xlarge"
    R5D_16XLARGE = "r5d.16xlarge"
    R5D_24XLARGE = "r5d.24xlarge"
    M6G_MEDIUM = "m6g.medium"
    M6G_LARGE = "m6g.large"
    M6G_XLARGE = "m6g.xlarge"
    M6G_2XLARGE = "m6g.2xlarge"
    M6G_4XLARGE = "m6g.4xlarge"
    M6G_8XLARGE = "m6g.8xlarge"
    M6G_12XLARGE = "m6g.12xlarge"
    M6G_16XLARGE = "m6g.16xlarge"
    C6G_MEDIUM = "c6g.medium"
    C6G_LARGE = "c6g.large"
    C6G_XLARGE = "c6g.xlarge"
    C6G_2XLARGE = "c6g.2xlarge"
    C6G_4XLARGE = "c6g.4xlarge"
    C6G_8XLARGE = "c6g.8xlarge"
    C6G_12XLARGE = "c6g.12xlarge"
    C6G_16XLARGE = "c6g.16xlarge"
    R6G_MEDIUM = "r6g.medium"
    R6G_LARGE = "r6g.large"
    R6G_XLARGE = "r6g.xlarge"
    R6G_2XLARGE = "r6g.2xlarge"
    R6G_4XLARGE = "r6g.4xlarge"
    R6G_8XLARGE = "r6g.8xlarge"
    R6G_12XLARGE = "r6g.12xlarge"
    R6G_16XLARGE = "r6g.16xlarge"
    C6GN_MEDIUM = "c6gn.medium"
    C6GN_LARGE = "c6gn.large"
    C6GN_XLARGE = "c6gn.xlarge"
    C6GN_2XLARGE = "c6gn.2xlarge"
    C6GN_4XLARGE = "c6gn.4xlarge"
    C6GN_8XLARGE = "c6gn.8xlarge"
    C6GN_12XLARGE = "c6gn.12xlarge"
    C6GN_16XLARGE = "c6gn.16xlarge"
    C7G_MEDIUM = "c7g.medium"
    C7G_LARGE = "c7g.large"
    C7G_XLARGE = "c7g.xlarge"
    C7G_2XLARGE = "c7g.2xlarge"
    C7G_4XLARGE = "c7g.4xlarge"
    C7G_8XLARGE = "c7g.8xlarge"
    C7G_12XLARGE = "c7g.12xlarge"
    C7G_16XLARGE = "c7g.16xlarge"
    R7G_MEDIUM = "r7g.medium"
    R7G_LARGE = "r7g.large"
    R7G_XLARGE = "r7g.xlarge"
    R7G_2XLARGE = "r7g.2xlarge"
    R7G_4XLARGE = "r7g.4xlarge"
    R7G_8XLARGE = "r7g.8xlarge"
    R7G_12XLARGE = "r7g.12xlarge"
    R7G_16XLARGE = "r7g.16xlarge"
    M7G_MEDIUM = "m7g.medium"
    M7G_LARGE = "m7g.large"
    M7G_XLARGE = "m7g.xlarge"
    M7G_2XLARGE = "m7g.2xlarge"
    M7G_4XLARGE = "m7g.4xlarge"
    M7G_8XLARGE = "m7g.8xlarge"
    M7G_12XLARGE = "m7g.12xlarge"
    M7G_16XLARGE = "m7g.16xlarge"
    G5G_XLARGE = "g5g.xlarge"
    G5G_2XLARGE = "g5g.2xlarge"
    G5G_4XLARGE = "g5g.4xlarge"
    G5G_8XLARGE = "g5g.8xlarge"
    G5G_16XLARGE = "g5g.16xlarge"
    R6I_LARGE = "r6i.large"
    R6I_XLARGE = "r6i.xlarge"
    R6I_2XLARGE = "r6i.2xlarge"
    R6I_4XLARGE = "r6i.4xlarge"
    R6I_8XLARGE = "r6i.8xlarge"
    R6I_12XLARGE = "r6i.12xlarge"
    R6I_16XLARGE = "r6i.16xlarge"
    C6GD_MEDIUM = "c6gd.medium"
    C6GD_LARGE = "c6gd.large"
    C6GD_XLARGE = "c6gd.xlarge"
    C6GD_2XLARGE = "c6gd.2xlarge"
    C6GD_4XLARGE = "c6gd.4xlarge"
    C6GD_8XLARGE = "c6gd.8xlarge"
    C6GD_12XLARGE = "c6gd.12xlarge"
    C6GD_16XLARGE = "c6gd.16xlarge"
    C6IN_LARGE = "c6in.large"
    C6IN_XLARGE = "c6in.xlarge"
    C6IN_2XLARGE = "c6in.2xlarge"
    C6IN_4XLARGE = "c6in.4xlarge"
    C6IN_8XLARGE = "c6in.8xlarge"
    C6IN_12XLARGE = "c6in.12xlarge"
    C6IN_16XLARGE = "c6in.16xlarge"
    C7A_MEDIUM = "c7a.medium"
    C7A_LARGE = "c7a.large"
    C7A_XLARGE = "c7a.xlarge"
    C7A_2XLARGE = "c7a.2xlarge"
    C7A_4XLARGE = "c7a.4xlarge"
    C7A_8XLARGE = "c7a.8xlarge"
    C7A_12XLARGE = "c7a.12xlarge"
    C7A_16XLARGE = "c7a.16xlarge"
    C7GD_MEDIUM = "c7gd.medium"
    C7GD_LARGE = "c7gd.large"
    C7GD_XLARGE = "c7gd.xlarge"
    C7GD_2XLARGE = "c7gd.2xlarge"
    C7GD_4XLARGE = "c7gd.4xlarge"
    C7GD_8XLARGE = "c7gd.8xlarge"
    C7GD_12XLARGE = "c7gd.12xlarge"
    C7GD_16XLARGE = "c7gd.16xlarge"
    C7GN_MEDIUM = "c7gn.medium"
    C7GN_LARGE = "c7gn.large"
    C7GN_XLARGE = "c7gn.xlarge"
    C7GN_2XLARGE = "c7gn.2xlarge"
    C7GN_4XLARGE = "c7gn.4xlarge"
    C7GN_8XLARGE = "c7gn.8xlarge"
    C7GN_12XLARGE = "c7gn.12xlarge"
    C7GN_16XLARGE = "c7gn.16xlarge"
    C7I_LARGE = "c7i.large"
    C7I_XLARGE = "c7i.xlarge"
    C7I_2XLARGE = "c7i.2xlarge"
    C7I_4XLARGE = "c7i.4xlarge"
    C7I_8XLARGE = "c7i.8xlarge"
    C7I_12XLARGE = "c7i.12xlarge"
    C7I_16XLARGE = "c7i.16xlarge"
    M6A_LARGE = "m6a.large"
    M6A_XLARGE = "m6a.xlarge"
    M6A_2XLARGE = "m6a.2xlarge"
    M6A_4XLARGE = "m6a.4xlarge"
    M6A_8XLARGE = "m6a.8xlarge"
    M6A_12XLARGE = "m6a.12xlarge"
    M6A_16XLARGE = "m6a.16xlarge"
    M6GD_MEDIUM = "m6gd.medium"
    M6GD_LARGE = "m6gd.large"
    M6GD_XLARGE = "m6gd.xlarge"
    M6GD_2XLARGE = "m6gd.2xlarge"
    M6GD_4XLARGE = "m6gd.4xlarge"
    M6GD_8XLARGE = "m6gd.8xlarge"
    M6GD_12XLARGE = "m6gd.12xlarge"
    M6GD_16XLARGE = "m6gd.16xlarge"
    M6I_LARGE = "m6i.large"
    M6I_XLARGE = "m6i.xlarge"
    M6I_2XLARGE = "m6i.2xlarge"
    M6I_4XLARGE = "m6i.4xlarge"
    M6I_8XLARGE = "m6i.8xlarge"
    M6I_12XLARGE = "m6i.12xlarge"
    M6I_16XLARGE = "m6i.16xlarge"
    M7A_MEDIUM = "m7a.medium"
    M7A_LARGE = "m7a.large"
    M7A_XLARGE = "m7a.xlarge"
    M7A_2XLARGE = "m7a.2xlarge"
    M7A_4XLARGE = "m7a.4xlarge"
    M7A_8XLARGE = "m7a.8xlarge"
    M7A_12XLARGE = "m7a.12xlarge"
    M7A_16XLARGE = "m7a.16xlarge"
    M7GD_MEDIUM = "m7gd.medium"
    M7GD_LARGE = "m7gd.large"
    M7GD_XLARGE = "m7gd.xlarge"
    M7GD_2XLARGE = "m7gd.2xlarge"
    M7GD_4XLARGE = "m7gd.4xlarge"
    M7GD_8XLARGE = "m7gd.8xlarge"
    M7GD_12XLARGE = "m7gd.12xlarge"
    M7GD_16XLARGE = "m7gd.16xlarge"
    M7I_LARGE = "m7i.large"
    M7I_XLARGE = "m7i.xlarge"
    M7I_2XLARGE = "m7i.2xlarge"
    M7I_4XLARGE = "m7i.4xlarge"
    M7I_8XLARGE = "m7i.8xlarge"
    M7I_12XLARGE = "m7i.12xlarge"
    M7I_16XLARGE = "m7i.16xlarge"
    R6GD_MEDIUM = "r6gd.medium"
    R6GD_LARGE = "r6gd.large"
    R6GD_XLARGE = "r6gd.xlarge"
    R6GD_2XLARGE = "r6gd.2xlarge"
    R6GD_4XLARGE = "r6gd.4xlarge"
    R6GD_8XLARGE = "r6gd.8xlarge"
    R6GD_12XLARGE = "r6gd.12xlarge"
    R6GD_16XLARGE = "r6gd.16xlarge"
    R7A_MEDIUM = "r7a.medium"
    R7A_LARGE = "r7a.large"
    R7A_XLARGE = "r7a.xlarge"
    R7A_2XLARGE = "r7a.2xlarge"
    R7A_4XLARGE = "r7a.4xlarge"
    R7A_8XLARGE = "r7a.8xlarge"
    R7A_12XLARGE = "r7a.12xlarge"
    R7A_16XLARGE = "r7a.16xlarge"
    R7GD_MEDIUM = "r7gd.medium"
    R7GD_LARGE = "r7gd.large"
    R7GD_XLARGE = "r7gd.xlarge"
    R7GD_2XLARGE = "r7gd.2xlarge"
    R7GD_4XLARGE = "r7gd.4xlarge"
    R7GD_8XLARGE = "r7gd.8xlarge"
    R7GD_12XLARGE = "r7gd.12xlarge"
    R7GD_16XLARGE = "r7gd.16xlarge"
    R7I_LARGE = "r7i.large"
    R7I_XLARGE = "r7i.xlarge"
    R7I_2XLARGE = "r7i.2xlarge"
    R7I_4XLARGE = "r7i.4xlarge"
    R7I_8XLARGE = "r7i.8xlarge"
    R7I_12XLARGE = "r7i.12xlarge"
    R7I_16XLARGE = "r7i.16xlarge"
    R7I_24XLARGE = "r7i.24xlarge"
    R7I_48XLARGE = "r7i.48xlarge"
    C5AD_LARGE = "c5ad.large"
    C5AD_XLARGE = "c5ad.xlarge"
    C5AD_2XLARGE = "c5ad.2xlarge"
    C5AD_4XLARGE = "c5ad.4xlarge"
    C5AD_8XLARGE = "c5ad.8xlarge"
    C5AD_12XLARGE = "c5ad.12xlarge"
    C5AD_16XLARGE = "c5ad.16xlarge"
    C5AD_24XLARGE = "c5ad.24xlarge"
    C5N_LARGE = "c5n.large"
    C5N_XLARGE = "c5n.xlarge"
    C5N_2XLARGE = "c5n.2xlarge"
    C5N_4XLARGE = "c5n.4xlarge"
    C5N_9XLARGE = "c5n.9xlarge"
    C5N_18XLARGE = "c5n.18xlarge"
    R5AD_LARGE = "r5ad.large"
    R5AD_XLARGE = "r5ad.xlarge"
    R5AD_2XLARGE = "r5ad.2xlarge"
    R5AD_4XLARGE = "r5ad.4xlarge"
    R5AD_8XLARGE = "r5ad.8xlarge"
    R5AD_12XLARGE = "r5ad.12xlarge"
    R5AD_16XLARGE = "r5ad.16xlarge"
    R5AD_24XLARGE = "r5ad.24xlarge"
    C6ID_LARGE = "c6id.large"
    C6ID_XLARGE = "c6id.xlarge"
    C6ID_2XLARGE = "c6id.2xlarge"
    C6ID_4XLARGE = "c6id.4xlarge"
    C6ID_8XLARGE = "c6id.8xlarge"
    C6ID_12XLARGE = "c6id.12xlarge"
    C6ID_16XLARGE = "c6id.16xlarge"
    C6ID_24XLARGE = "c6id.24xlarge"
    C6ID_32XLARGE = "c6id.32xlarge"
    C8G_MEDIUM = "c8g.medium"
    C8G_LARGE = "c8g.large"
    C8G_XLARGE = "c8g.xlarge"
    C8G_2XLARGE = "c8g.2xlarge"
    C8G_4XLARGE = "c8g.4xlarge"
    C8G_8XLARGE = "c8g.8xlarge"
    C8G_12XLARGE = "c8g.12xlarge"
    C8G_16XLARGE = "c8g.16xlarge"
    C8G_24XLARGE = "c8g.24xlarge"
    C8G_48XLARGE = "c8g.48xlarge"
    M5AD_LARGE = "m5ad.large"
    M5AD_XLARGE = "m5ad.xlarge"
    M5AD_2XLARGE = "m5ad.2xlarge"
    M5AD_4XLARGE = "m5ad.4xlarge"
    M5AD_8XLARGE = "m5ad.8xlarge"
    M5AD_12XLARGE = "m5ad.12xlarge"
    M5AD_16XLARGE = "m5ad.16xlarge"
    M5AD_24XLARGE = "m5ad.24xlarge"
    M5D_LARGE = "m5d.large"
    M5D_XLARGE = "m5d.xlarge"
    M5D_2XLARGE = "m5d.2xlarge"
    M5D_4XLARGE = "m5d.4xlarge"
    M5D_8XLARGE = "m5d.8xlarge"
    M5D_12XLARGE = "m5d.12xlarge"
    M5D_16XLARGE = "m5d.16xlarge"
    M5D_24XLARGE = "m5d.24xlarge"
    M5DN_LARGE = "m5dn.large"
    M5DN_XLARGE = "m5dn.xlarge"
    M5DN_2XLARGE = "m5dn.2xlarge"
    M5DN_4XLARGE = "m5dn.4xlarge"
    M5DN_8XLARGE = "m5dn.8xlarge"
    M5DN_12XLARGE = "m5dn.12xlarge"
    M5DN_16XLARGE = "m5dn.16xlarge"
    M5DN_24XLARGE = "m5dn.24xlarge"
    M5N_LARGE = "m5n.large"
    M5N_XLARGE = "m5n.xlarge"
    M5N_2XLARGE = "m5n.2xlarge"
    M5N_4XLARGE = "m5n.4xlarge"
    M5N_8XLARGE = "m5n.8xlarge"
    M5N_12XLARGE = "m5n.12xlarge"
    M5N_16XLARGE = "m5n.16xlarge"
    M5N_24XLARGE = "m5n.24xlarge"
    M6ID_LARGE = "m6id.large"
    M6ID_XLARGE = "m6id.xlarge"
    M6ID_2XLARGE = "m6id.2xlarge"
    M6ID_4XLARGE = "m6id.4xlarge"
    M6ID_8XLARGE = "m6id.8xlarge"
    M6ID_12XLARGE = "m6id.12xlarge"
    M6ID_16XLARGE = "m6id.16xlarge"
    M6ID_24XLARGE = "m6id.24xlarge"
    M6ID_32XLARGE = "m6id.32xlarge"
    M6IDN_LARGE = "m6idn.large"
    M6IDN_XLARGE = "m6idn.xlarge"
    M6IDN_2XLARGE = "m6idn.2xlarge"
    M6IDN_4XLARGE = "m6idn.4xlarge"
    M6IDN_8XLARGE = "m6idn.8xlarge"
    M6IDN_12XLARGE = "m6idn.12xlarge"
    M6IDN_16XLARGE = "m6idn.16xlarge"
    M6IDN_24XLARGE = "m6idn.24xlarge"
    M6IDN_32XLARGE = "m6idn.32xlarge"
    M6IN_LARGE = "m6in.large"
    M6IN_XLARGE = "m6in.xlarge"
    M6IN_2XLARGE = "m6in.2xlarge"
    M6IN_4XLARGE = "m6in.4xlarge"
    M6IN_8XLARGE = "m6in.8xlarge"
    M6IN_12XLARGE = "m6in.12xlarge"
    M6IN_16XLARGE = "m6in.16xlarge"
    M6IN_24XLARGE = "m6in.24xlarge"
    M6IN_32XLARGE = "m6in.32xlarge"
    M8G_MEDIUM = "m8g.medium"
    M8G_LARGE = "m8g.large"
    M8G_XLARGE = "m8g.xlarge"
    M8G_2XLARGE = "m8g.2xlarge"
    M8G_4XLARGE = "m8g.4xlarge"
    M8G_8XLARGE = "m8g.8xlarge"
    M8G_12XLARGE = "m8g.12xlarge"
    M8G_16XLARGE = "m8g.16xlarge"
    M8G_24XLARGE = "m8g.24xlarge"
    M8G_48XLARGE = "m8g.48xlarge"
    R5DN_LARGE = "r5dn.large"
    R5DN_XLARGE = "r5dn.xlarge"
    R5DN_2XLARGE = "r5dn.2xlarge"
    R5DN_4XLARGE = "r5dn.4xlarge"
    R5DN_8XLARGE = "r5dn.8xlarge"
    R5DN_12XLARGE = "r5dn.12xlarge"
    R5DN_16XLARGE = "r5dn.16xlarge"
    R5DN_24XLARGE = "r5dn.24xlarge"
    R5N_LARGE = "r5n.large"
    R5N_XLARGE = "r5n.xlarge"
    R5N_2XLARGE = "r5n.2xlarge"
    R5N_4XLARGE = "r5n.4xlarge"
    R5N_8XLARGE = "r5n.8xlarge"
    R5N_12XLARGE = "r5n.12xlarge"
    R5N_16XLARGE = "r5n.16xlarge"
    R5N_24XLARGE = "r5n.24xlarge"
    R6A_LARGE = "r6a.large"
    R6A_XLARGE = "r6a.xlarge"
    R6A_2XLARGE = "r6a.2xlarge"
    R6A_4XLARGE = "r6a.4xlarge"
    R6A_8XLARGE = "r6a.8xlarge"
    R6A_12XLARGE = "r6a.12xlarge"
    R6A_16XLARGE = "r6a.16xlarge"
    R6A_24XLARGE = "r6a.24xlarge"
    R6A_32XLARGE = "r6a.32xlarge"
    R6A_48XLARGE = "r6a.48xlarge"
    R6ID_LARGE = "r6id.large"
    R6ID_XLARGE = "r6id.xlarge"
    R6ID_2XLARGE = "r6id.2xlarge"
    R6ID_4XLARGE = "r6id.4xlarge"
    R6ID_8XLARGE = "r6id.8xlarge"
    R6ID_12XLARGE = "r6id.12xlarge"
    R6ID_16XLARGE = "r6id.16xlarge"
    R6ID_24XLARGE = "r6id.24xlarge"
    R6ID_32XLARGE = "r6id.32xlarge"
    R6IDN_LARGE = "r6idn.large"
    R6IDN_XLARGE = "r6idn.xlarge"
    R6IDN_2XLARGE = "r6idn.2xlarge"
    R6IDN_4XLARGE = "r6idn.4xlarge"
    R6IDN_8XLARGE = "r6idn.8xlarge"
    R6IDN_12XLARGE = "r6idn.12xlarge"
    R6IDN_16XLARGE = "r6idn.16xlarge"
    R6IDN_24XLARGE = "r6idn.24xlarge"
    R6IDN_32XLARGE = "r6idn.32xlarge"
    R6IN_LARGE = "r6in.large"
    R6IN_XLARGE = "r6in.xlarge"
    R6IN_2XLARGE = "r6in.2xlarge"
    R6IN_4XLARGE = "r6in.4xlarge"
    R6IN_8XLARGE = "r6in.8xlarge"
    R6IN_12XLARGE = "r6in.12xlarge"
    R6IN_16XLARGE = "r6in.16xlarge"
    R6IN_24XLARGE = "r6in.24xlarge"
    R6IN_32XLARGE = "r6in.32xlarge"
    R8G_MEDIUM = "r8g.medium"
    R8G_LARGE = "r8g.large"
    R8G_XLARGE = "r8g.xlarge"
    R8G_2XLARGE = "r8g.2xlarge"
    R8G_4XLARGE = "r8g.4xlarge"
    R8G_8XLARGE = "r8g.8xlarge"
    R8G_12XLARGE = "r8g.12xlarge"
    R8G_16XLARGE = "r8g.16xlarge"
    R8G_24XLARGE = "r8g.24xlarge"
    R8G_48XLARGE = "r8g.48xlarge"
    M4_16XLARGE = "m4.16xlarge"
    C6A_32XLARGE = "c6a.32xlarge"
    C6A_48XLARGE = "c6a.48xlarge"
    C6I_32XLARGE = "c6i.32xlarge"
    R6I_24XLARGE = "r6i.24xlarge"
    R6I_32XLARGE = "r6i.32xlarge"
    C6IN_24XLARGE = "c6in.24xlarge"
    C6IN_32XLARGE = "c6in.32xlarge"
    C7A_24XLARGE = "c7a.24xlarge"
    C7A_32XLARGE = "c7a.32xlarge"
    C7A_48XLARGE = "c7a.48xlarge"
    C7I_24XLARGE = "c7i.24xlarge"
    C7I_48XLARGE = "c7i.48xlarge"
    M6A_24XLARGE = "m6a.24xlarge"
    M6A_32XLARGE = "m6a.32xlarge"
    M6A_48XLARGE = "m6a.48xlarge"
    M6I_24XLARGE = "m6i.24xlarge"
    M6I_32XLARGE = "m6i.32xlarge"
    M7A_24XLARGE = "m7a.24xlarge"
    M7A_32XLARGE = "m7a.32xlarge"
    M7A_48XLARGE = "m7a.48xlarge"
    M7I_24XLARGE = "m7i.24xlarge"
    M7I_48XLARGE = "m7i.48xlarge"
    R7A_24XLARGE = "r7a.24xlarge"
    R7A_32XLARGE = "r7a.32xlarge"
    R7A_48XLARGE = "r7a.48xlarge"


class EventCode:
    """EventCode enum values."""

    GENERIC_EVENT = "GENERIC_EVENT"
    FLEET_CREATED = "FLEET_CREATED"
    FLEET_DELETED = "FLEET_DELETED"
    FLEET_SCALING_EVENT = "FLEET_SCALING_EVENT"
    FLEET_STATE_DOWNLOADING = "FLEET_STATE_DOWNLOADING"
    FLEET_STATE_VALIDATING = "FLEET_STATE_VALIDATING"
    FLEET_STATE_BUILDING = "FLEET_STATE_BUILDING"
    FLEET_STATE_ACTIVATING = "FLEET_STATE_ACTIVATING"
    FLEET_STATE_ACTIVE = "FLEET_STATE_ACTIVE"
    FLEET_STATE_ERROR = "FLEET_STATE_ERROR"
    FLEET_STATE_PENDING = "FLEET_STATE_PENDING"
    FLEET_STATE_CREATING = "FLEET_STATE_CREATING"
    FLEET_STATE_CREATED = "FLEET_STATE_CREATED"
    FLEET_STATE_UPDATING = "FLEET_STATE_UPDATING"
    FLEET_INITIALIZATION_FAILED = "FLEET_INITIALIZATION_FAILED"
    FLEET_BINARY_DOWNLOAD_FAILED = "FLEET_BINARY_DOWNLOAD_FAILED"
    FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND = "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND"
    FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE = "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE"
    FLEET_VALIDATION_TIMED_OUT = "FLEET_VALIDATION_TIMED_OUT"
    FLEET_ACTIVATION_FAILED = "FLEET_ACTIVATION_FAILED"
    FLEET_ACTIVATION_FAILED_NO_INSTANCES = "FLEET_ACTIVATION_FAILED_NO_INSTANCES"
    FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED = "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED"
    SERVER_PROCESS_INVALID_PATH = "SERVER_PROCESS_INVALID_PATH"
    SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT = "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT"
    SERVER_PROCESS_PROCESS_READY_TIMEOUT = "SERVER_PROCESS_PROCESS_READY_TIMEOUT"
    SERVER_PROCESS_CRASHED = "SERVER_PROCESS_CRASHED"
    SERVER_PROCESS_TERMINATED_UNHEALTHY = "SERVER_PROCESS_TERMINATED_UNHEALTHY"
    SERVER_PROCESS_FORCE_TERMINATED = "SERVER_PROCESS_FORCE_TERMINATED"
    SERVER_PROCESS_PROCESS_EXIT_TIMEOUT = "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT"
    SERVER_PROCESS_SDK_INITIALIZATION_FAILED = "SERVER_PROCESS_SDK_INITIALIZATION_FAILED"
    SERVER_PROCESS_MISCONFIGURED_CONTAINER_PORT = "SERVER_PROCESS_MISCONFIGURED_CONTAINER_PORT"
    GAME_SESSION_ACTIVATION_TIMEOUT = "GAME_SESSION_ACTIVATION_TIMEOUT"
    FLEET_CREATION_EXTRACTING_BUILD = "FLEET_CREATION_EXTRACTING_BUILD"
    FLEET_CREATION_RUNNING_INSTALLER = "FLEET_CREATION_RUNNING_INSTALLER"
    FLEET_CREATION_VALIDATING_RUNTIME_CONFIG = "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG"
    FLEET_VPC_PEERING_SUCCEEDED = "FLEET_VPC_PEERING_SUCCEEDED"
    FLEET_VPC_PEERING_FAILED = "FLEET_VPC_PEERING_FAILED"
    FLEET_VPC_PEERING_DELETED = "FLEET_VPC_PEERING_DELETED"
    INSTANCE_INTERRUPTED = "INSTANCE_INTERRUPTED"
    INSTANCE_RECYCLED = "INSTANCE_RECYCLED"
    INSTANCE_REPLACED_UNHEALTHY = "INSTANCE_REPLACED_UNHEALTHY"
    FLEET_CREATION_COMPLETED_INSTALLER = "FLEET_CREATION_COMPLETED_INSTALLER"
    FLEET_CREATION_FAILED_INSTALLER = "FLEET_CREATION_FAILED_INSTALLER"
    COMPUTE_LOG_UPLOAD_FAILED = "COMPUTE_LOG_UPLOAD_FAILED"
    GAME_SERVER_CONTAINER_GROUP_CRASHED = "GAME_SERVER_CONTAINER_GROUP_CRASHED"
    PER_INSTANCE_CONTAINER_GROUP_CRASHED = "PER_INSTANCE_CONTAINER_GROUP_CRASHED"
    GAME_SERVER_CONTAINER_GROUP_REPLACED_UNHEALTHY = "GAME_SERVER_CONTAINER_GROUP_REPLACED_UNHEALTHY"
    LOCATION_STATE_PENDING = "LOCATION_STATE_PENDING"
    LOCATION_STATE_CREATING = "LOCATION_STATE_CREATING"
    LOCATION_STATE_CREATED = "LOCATION_STATE_CREATED"
    LOCATION_STATE_ACTIVATING = "LOCATION_STATE_ACTIVATING"
    LOCATION_STATE_ACTIVE = "LOCATION_STATE_ACTIVE"
    LOCATION_STATE_UPDATING = "LOCATION_STATE_UPDATING"
    LOCATION_STATE_ERROR = "LOCATION_STATE_ERROR"
    LOCATION_STATE_DELETING = "LOCATION_STATE_DELETING"
    LOCATION_STATE_DELETED = "LOCATION_STATE_DELETED"


class FilterInstanceStatus:
    """FilterInstanceStatus enum values."""

    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"


class FleetAction:
    """FleetAction enum values."""

    AUTO_SCALING = "AUTO_SCALING"


class FleetStatus:
    """FleetStatus enum values."""

    NEW = "NEW"
    DOWNLOADING = "DOWNLOADING"
    VALIDATING = "VALIDATING"
    BUILDING = "BUILDING"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    ERROR = "ERROR"
    TERMINATED = "TERMINATED"
    NOT_FOUND = "NOT_FOUND"


class FleetType:
    """FleetType enum values."""

    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"


class FlexMatchMode:
    """FlexMatchMode enum values."""

    STANDALONE = "STANDALONE"
    WITH_QUEUE = "WITH_QUEUE"


class GameServerClaimStatus:
    """GameServerClaimStatus enum values."""

    CLAIMED = "CLAIMED"


class GameServerGroupAction:
    """GameServerGroupAction enum values."""

    REPLACE_INSTANCE_TYPES = "REPLACE_INSTANCE_TYPES"


class GameServerGroupDeleteOption:
    """GameServerGroupDeleteOption enum values."""

    SAFE_DELETE = "SAFE_DELETE"
    FORCE_DELETE = "FORCE_DELETE"
    RETAIN = "RETAIN"


class GameServerGroupInstanceType:
    """GameServerGroupInstanceType enum values."""

    C4_LARGE = "c4.large"
    C4_XLARGE = "c4.xlarge"
    C4_2XLARGE = "c4.2xlarge"
    C4_4XLARGE = "c4.4xlarge"
    C4_8XLARGE = "c4.8xlarge"
    C5_LARGE = "c5.large"
    C5_XLARGE = "c5.xlarge"
    C5_2XLARGE = "c5.2xlarge"
    C5_4XLARGE = "c5.4xlarge"
    C5_9XLARGE = "c5.9xlarge"
    C5_12XLARGE = "c5.12xlarge"
    C5_18XLARGE = "c5.18xlarge"
    C5_24XLARGE = "c5.24xlarge"
    C5A_LARGE = "c5a.large"
    C5A_XLARGE = "c5a.xlarge"
    C5A_2XLARGE = "c5a.2xlarge"
    C5A_4XLARGE = "c5a.4xlarge"
    C5A_8XLARGE = "c5a.8xlarge"
    C5A_12XLARGE = "c5a.12xlarge"
    C5A_16XLARGE = "c5a.16xlarge"
    C5A_24XLARGE = "c5a.24xlarge"
    C6G_MEDIUM = "c6g.medium"
    C6G_LARGE = "c6g.large"
    C6G_XLARGE = "c6g.xlarge"
    C6G_2XLARGE = "c6g.2xlarge"
    C6G_4XLARGE = "c6g.4xlarge"
    C6G_8XLARGE = "c6g.8xlarge"
    C6G_12XLARGE = "c6g.12xlarge"
    C6G_16XLARGE = "c6g.16xlarge"
    R4_LARGE = "r4.large"
    R4_XLARGE = "r4.xlarge"
    R4_2XLARGE = "r4.2xlarge"
    R4_4XLARGE = "r4.4xlarge"
    R4_8XLARGE = "r4.8xlarge"
    R4_16XLARGE = "r4.16xlarge"
    R5_LARGE = "r5.large"
    R5_XLARGE = "r5.xlarge"
    R5_2XLARGE = "r5.2xlarge"
    R5_4XLARGE = "r5.4xlarge"
    R5_8XLARGE = "r5.8xlarge"
    R5_12XLARGE = "r5.12xlarge"
    R5_16XLARGE = "r5.16xlarge"
    R5_24XLARGE = "r5.24xlarge"
    R5A_LARGE = "r5a.large"
    R5A_XLARGE = "r5a.xlarge"
    R5A_2XLARGE = "r5a.2xlarge"
    R5A_4XLARGE = "r5a.4xlarge"
    R5A_8XLARGE = "r5a.8xlarge"
    R5A_12XLARGE = "r5a.12xlarge"
    R5A_16XLARGE = "r5a.16xlarge"
    R5A_24XLARGE = "r5a.24xlarge"
    R6G_MEDIUM = "r6g.medium"
    R6G_LARGE = "r6g.large"
    R6G_XLARGE = "r6g.xlarge"
    R6G_2XLARGE = "r6g.2xlarge"
    R6G_4XLARGE = "r6g.4xlarge"
    R6G_8XLARGE = "r6g.8xlarge"
    R6G_12XLARGE = "r6g.12xlarge"
    R6G_16XLARGE = "r6g.16xlarge"
    M4_LARGE = "m4.large"
    M4_XLARGE = "m4.xlarge"
    M4_2XLARGE = "m4.2xlarge"
    M4_4XLARGE = "m4.4xlarge"
    M4_10XLARGE = "m4.10xlarge"
    M5_LARGE = "m5.large"
    M5_XLARGE = "m5.xlarge"
    M5_2XLARGE = "m5.2xlarge"
    M5_4XLARGE = "m5.4xlarge"
    M5_8XLARGE = "m5.8xlarge"
    M5_12XLARGE = "m5.12xlarge"
    M5_16XLARGE = "m5.16xlarge"
    M5_24XLARGE = "m5.24xlarge"
    M5A_LARGE = "m5a.large"
    M5A_XLARGE = "m5a.xlarge"
    M5A_2XLARGE = "m5a.2xlarge"
    M5A_4XLARGE = "m5a.4xlarge"
    M5A_8XLARGE = "m5a.8xlarge"
    M5A_12XLARGE = "m5a.12xlarge"
    M5A_16XLARGE = "m5a.16xlarge"
    M5A_24XLARGE = "m5a.24xlarge"
    M6G_MEDIUM = "m6g.medium"
    M6G_LARGE = "m6g.large"
    M6G_XLARGE = "m6g.xlarge"
    M6G_2XLARGE = "m6g.2xlarge"
    M6G_4XLARGE = "m6g.4xlarge"
    M6G_8XLARGE = "m6g.8xlarge"
    M6G_12XLARGE = "m6g.12xlarge"
    M6G_16XLARGE = "m6g.16xlarge"


class GameServerGroupStatus:
    """GameServerGroupStatus enum values."""

    NEW = "NEW"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DELETE_SCHEDULED = "DELETE_SCHEDULED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    ERROR = "ERROR"


class GameServerHealthCheck:
    """GameServerHealthCheck enum values."""

    HEALTHY = "HEALTHY"


class GameServerInstanceStatus:
    """GameServerInstanceStatus enum values."""

    ACTIVE = "ACTIVE"
    DRAINING = "DRAINING"
    SPOT_TERMINATING = "SPOT_TERMINATING"


class GameServerProtectionPolicy:
    """GameServerProtectionPolicy enum values."""

    NO_PROTECTION = "NO_PROTECTION"
    FULL_PROTECTION = "FULL_PROTECTION"


class GameServerUtilizationStatus:
    """GameServerUtilizationStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UTILIZED = "UTILIZED"


class GameSessionPlacementState:
    """GameSessionPlacementState enum values."""

    PENDING = "PENDING"
    FULFILLED = "FULFILLED"
    CANCELLED = "CANCELLED"
    TIMED_OUT = "TIMED_OUT"
    FAILED = "FAILED"


class GameSessionStatus:
    """GameSessionStatus enum values."""

    ACTIVE = "ACTIVE"
    ACTIVATING = "ACTIVATING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    ERROR = "ERROR"


class GameSessionStatusReason:
    """GameSessionStatusReason enum values."""

    INTERRUPTED = "INTERRUPTED"
    TRIGGERED_ON_PROCESS_TERMINATE = "TRIGGERED_ON_PROCESS_TERMINATE"
    FORCE_TERMINATED = "FORCE_TERMINATED"


class InstanceRoleCredentialsProvider:
    """InstanceRoleCredentialsProvider enum values."""

    SHARED_CREDENTIAL_FILE = "SHARED_CREDENTIAL_FILE"


class InstanceStatus:
    """InstanceStatus enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    TERMINATING = "TERMINATING"


class IpProtocol:
    """IpProtocol enum values."""

    TCP = "TCP"
    UDP = "UDP"


class ListComputeInputStatus:
    """ListComputeInputStatus enum values."""

    ACTIVE = "ACTIVE"
    IMPAIRED = "IMPAIRED"


class LocationFilter:
    """LocationFilter enum values."""

    AWS = "AWS"
    CUSTOM = "CUSTOM"


class LocationUpdateStatus:
    """LocationUpdateStatus enum values."""

    PENDING_UPDATE = "PENDING_UPDATE"


class LogDestination:
    """LogDestination enum values."""

    NONE = "NONE"
    CLOUDWATCH = "CLOUDWATCH"
    S3 = "S3"


class MatchmakingConfigurationStatus:
    """MatchmakingConfigurationStatus enum values."""

    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PLACING = "PLACING"
    QUEUED = "QUEUED"
    REQUIRES_ACCEPTANCE = "REQUIRES_ACCEPTANCE"
    SEARCHING = "SEARCHING"
    TIMED_OUT = "TIMED_OUT"


class MetricName:
    """MetricName enum values."""

    ACTIVATINGGAMESESSIONS = "ActivatingGameSessions"
    ACTIVEGAMESESSIONS = "ActiveGameSessions"
    ACTIVEINSTANCES = "ActiveInstances"
    AVAILABLEGAMESESSIONS = "AvailableGameSessions"
    AVAILABLEPLAYERSESSIONS = "AvailablePlayerSessions"
    CURRENTPLAYERSESSIONS = "CurrentPlayerSessions"
    IDLEINSTANCES = "IdleInstances"
    PERCENTAVAILABLEGAMESESSIONS = "PercentAvailableGameSessions"
    PERCENTIDLEINSTANCES = "PercentIdleInstances"
    QUEUEDEPTH = "QueueDepth"
    WAITTIME = "WaitTime"
    CONCURRENTACTIVATABLEGAMESESSIONS = "ConcurrentActivatableGameSessions"


class OperatingSystem:
    """OperatingSystem enum values."""

    WINDOWS_2012 = "WINDOWS_2012"
    AMAZON_LINUX = "AMAZON_LINUX"
    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    WINDOWS_2016 = "WINDOWS_2016"
    AMAZON_LINUX_2023 = "AMAZON_LINUX_2023"
    WINDOWS_2022 = "WINDOWS_2022"


class PlacementFallbackStrategy:
    """PlacementFallbackStrategy enum values."""

    DEFAULT_AFTER_SINGLE_PASS = "DEFAULT_AFTER_SINGLE_PASS"
    NONE = "NONE"


class PlayerSessionCreationPolicy:
    """PlayerSessionCreationPolicy enum values."""

    ACCEPT_ALL = "ACCEPT_ALL"
    DENY_ALL = "DENY_ALL"


class PlayerSessionStatus:
    """PlayerSessionStatus enum values."""

    RESERVED = "RESERVED"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    TIMEDOUT = "TIMEDOUT"


class PolicyType:
    """PolicyType enum values."""

    RULEBASED = "RuleBased"
    TARGETBASED = "TargetBased"


class PriorityType:
    """PriorityType enum values."""

    LATENCY = "LATENCY"
    COST = "COST"
    DESTINATION = "DESTINATION"
    LOCATION = "LOCATION"


class ProtectionPolicy:
    """ProtectionPolicy enum values."""

    NOPROTECTION = "NoProtection"
    FULLPROTECTION = "FullProtection"


class RoutingStrategyType:
    """RoutingStrategyType enum values."""

    SIMPLE = "SIMPLE"
    TERMINAL = "TERMINAL"


class ScalingAdjustmentType:
    """ScalingAdjustmentType enum values."""

    CHANGEINCAPACITY = "ChangeInCapacity"
    EXACTCAPACITY = "ExactCapacity"
    PERCENTCHANGEINCAPACITY = "PercentChangeInCapacity"


class ScalingStatusType:
    """ScalingStatusType enum values."""

    ACTIVE = "ACTIVE"
    UPDATE_REQUESTED = "UPDATE_REQUESTED"
    UPDATING = "UPDATING"
    DELETE_REQUESTED = "DELETE_REQUESTED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    ERROR = "ERROR"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class TerminationMode:
    """TerminationMode enum values."""

    TRIGGER_ON_PROCESS_TERMINATE = "TRIGGER_ON_PROCESS_TERMINATE"
    FORCE_TERMINATE = "FORCE_TERMINATE"


@dataclass
class RoutingStrategy(PropertyType):
    TYPE = "Type"
    MESSAGE = "Message"
    FLEET_ID = "FleetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "message": "Message",
        "fleet_id": "FleetId",
    }

    type_: Optional[Union[str, RoutingStrategyType, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fleet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

