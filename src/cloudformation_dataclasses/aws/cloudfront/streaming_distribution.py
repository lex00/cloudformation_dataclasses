"""PropertyTypes for AWS::CloudFront::StreamingDistribution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Logging(PropertyType):
    BUCKET = "Bucket"
    ENABLED = "Enabled"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "enabled": "Enabled",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Origin(PropertyType):
    DOMAIN_NAME = "DomainName"
    ORIGIN_ACCESS_IDENTITY = "OriginAccessIdentity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_name": "DomainName",
        "origin_access_identity": "OriginAccessIdentity",
    }

    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_access_identity: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamingDistributionConfig(PropertyType):
    LOGGING = "Logging"
    COMMENT = "Comment"
    PRICE_CLASS = "PriceClass"
    S3_ORIGIN = "S3Origin"
    ENABLED = "Enabled"
    ALIASES = "Aliases"
    TRUSTED_SIGNERS = "TrustedSigners"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logging": "Logging",
        "comment": "Comment",
        "price_class": "PriceClass",
        "s3_origin": "S3Origin",
        "enabled": "Enabled",
        "aliases": "Aliases",
        "trusted_signers": "TrustedSigners",
    }

    logging: Optional[Logging] = None
    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    price_class: Optional[Union[str, PriceClass, Ref, GetAtt, Sub]] = None
    s3_origin: Optional[S3Origin] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    aliases: Optional[Union[list[str], Ref]] = None
    trusted_signers: Optional[TrustedSigners] = None


@dataclass
class TrustedSigners(PropertyType):
    ENABLED = "Enabled"
    AWS_ACCOUNT_NUMBERS = "AwsAccountNumbers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "aws_account_numbers": "AwsAccountNumbers",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    aws_account_numbers: Optional[Union[list[str], Ref]] = None

