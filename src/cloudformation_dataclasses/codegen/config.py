"""
Code generation configuration.

This module defines the pinned CloudFormation specification version and generator version
used for code generation. All generated code is based on these exact versions.

Version History:
  CloudFormation Spec 2025.12.11:
    - Generator v1.0.0 (2025-12-15): Initial implementation
      * 1,502 resource types, 8,117 property types
      * All 262 AWS services generated
      * Declarative wrapper pattern implemented

Versioning Strategy:
  CLOUDFORMATION_SPEC_DATE:
    - Date-based version (YYYY.MM.DD) from AWS Last-Modified header
    - The spec file is committed to the repo for reproducibility

  GENERATOR_VERSION:
    - MAJOR: Breaking changes to generated code structure
    - MINOR: New features in generator (new code patterns, optimizations)
    - PATCH: Bug fixes in generator that don't change code structure
"""

from pathlib import Path

# CloudFormation spec date-based version (from AWS Last-Modified header)
# Format: YYYY.MM.DD - represents when AWS last modified the spec
# UPDATE THIS when downloading a new spec from AWS
CLOUDFORMATION_SPEC_DATE = "2025.12.11"

# Generator version (semantic versioning)
# UPDATE THIS when fixing generator bugs or adding generator features
# This is independent of the CloudFormation spec version
GENERATOR_VERSION = "1.0.0"

# Combined version string for display
COMBINED_VERSION = f"spec-{CLOUDFORMATION_SPEC_DATE}_gen-{GENERATOR_VERSION}"

# Legacy alias for backwards compatibility
CLOUDFORMATION_SPEC_VERSION = CLOUDFORMATION_SPEC_DATE

# Spec file location - committed to repo for reproducibility
SPEC_DIR = Path(__file__).parent.parent.parent.parent / "specs"
SPEC_FILE = SPEC_DIR / "CloudFormationResourceSpecification.json"

# Spec URL - AWS provides "latest" which updates frequently
SPEC_URL = (
    "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
)
