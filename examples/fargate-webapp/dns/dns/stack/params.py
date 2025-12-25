"""Parameters for DNS stack."""

from .. import *  # noqa: F403, F401


DomainNameParam = Parameter(
    type=STRING,
    description="Domain name for the hosted zone (e.g., example.com)",
)
