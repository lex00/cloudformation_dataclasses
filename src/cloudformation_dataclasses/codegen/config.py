"""
Code generation configuration.

This module defines the pinned CloudFormation specification version and generator version
used for code generation. All generated code is based on these exact versions.

Version History:
  CloudFormation Spec v227.0.0 (Dec 2024):
    - Generator v1.0.0 (2024-12-15): Initial implementation
      * 1,502 resource types, 8,117 property types
      * S3 service generated and tested
      * Declarative wrapper pattern implemented

When to bump versions:
  CLOUDFORMATION_SPEC_VERSION:
    - When AWS releases a new CloudFormation spec
    - This is a major change affecting all resources

  GENERATOR_VERSION:
    - MAJOR: Breaking changes to generated code structure
    - MINOR: New features in generator (new code patterns, optimizations)
    - PATCH: Bug fixes in generator that don't change code structure
"""

# CloudFormation spec version from AWS
# UPDATE THIS when upgrading to a new AWS spec version
CLOUDFORMATION_SPEC_VERSION = "227.0.0"

# Generator version (semantic versioning)
# UPDATE THIS when fixing generator bugs or adding generator features
# This is independent of the CloudFormation spec version
GENERATOR_VERSION = "1.0.0"

# Combined version string for display
COMBINED_VERSION = f"spec-{CLOUDFORMATION_SPEC_VERSION}_gen-{GENERATOR_VERSION}"

# Spec URL - AWS provides "latest" which updates frequently
SPEC_URL = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"

# Note: AWS does not provide stable versioned URLs like:
# https://d1uauaxba7bl26.cloudfront.net/v227.0.0/gzip/CloudFormationResourceSpecification.json
# So we download "latest" but verify it matches our pinned version.
# This ensures we catch unexpected spec updates early.
