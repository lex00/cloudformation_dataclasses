"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CertificateARN:
    """The Amazon Resource Name (ARN) of an existing AWS IoT certificate aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key"""

    resource: Parameter
    type = STRING
    description = 'The Amazon Resource Name (ARN) of an existing AWS IoT certificate aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key'
