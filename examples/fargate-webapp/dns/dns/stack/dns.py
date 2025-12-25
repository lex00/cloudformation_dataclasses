"""DNS resources - Route53 hosted zone and ACM certificate."""

from .. import *  # noqa: F403, F401


# =============================================================================
# Route53 Hosted Zone
# =============================================================================


@cloudformation_dataclass
class HostedZone:
    resource: route53.HostedZone
    name = ref(DomainNameParam)


# =============================================================================
# ACM Certificate with DNS Validation
# =============================================================================


@cloudformation_dataclass
class CertificateDomainValidation:
    resource: certificatemanager.certificate.DomainValidationOption
    domain_name = ref(DomainNameParam)
    hosted_zone_id = ref(HostedZone)


@cloudformation_dataclass
class Certificate:
    resource: certificatemanager.Certificate
    domain_name = ref(DomainNameParam)
    subject_alternative_names = [
        Sub("*.${DomainName}"),
    ]
    validation_method = "DNS"
    domain_validation_options = [CertificateDomainValidation]
