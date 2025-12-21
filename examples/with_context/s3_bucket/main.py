"""
S3 Bucket Example - Declarative Approach

Demonstrates the CloudFormation dataclass pattern with:
- Deployment context with automatic resource naming and base tags
- Custom resource-specific tags merged with context tags
- Declarative wrapper classes for bucket configuration (reusable)
- IAM policy document with type-safe policy statements
- Resource references using ref() for cross-resource dependencies
- Auto-registration with Template.from_registry()

Key pattern: Declarative wrapper classes for clean, reusable infrastructure code.
"""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .context import ctx


def build_template() -> Template:
    """Build the S3 bucket template using auto-registered resources."""
    return Template.from_registry(
        description="S3 bucket with encryption-required policy",
    )


def main() -> None:
    """Create and export CloudFormation template with deployment context."""
    # Create resources using block syntax - all config from dataclass fields!
    bucket = MyData()
    bucket_policy = MyDataPolicy()

    # Show context-driven naming and tag merging
    print("=" * 80)
    print("RESOURCES")
    print("=" * 80)
    print(f"Bucket:        {bucket.resource.resource_name}")
    print(f"  Class name:  MyData")
    print(f"  Pattern:     {{component}}-{{resource_name}}-{{stage}}-{{deployment_name}}-{{deployment_group}}-{{region}}")
    print(f"\nBucket Policy: {bucket_policy.resource.resource_name}")
    print(f"Environment:   {ctx.stage} ({ctx.region})")
    print(f"\nBucket Tags: {len(bucket.resource.all_tags)} total (3 from context + 1 resource-specific)")
    for tag in bucket.resource.all_tags:
        print(f"  • {tag.key}: {tag.value}")
    print()

    # Generate CloudFormation template using auto-registration
    template = build_template()

    # Validate template
    errors = template.validate()
    if errors:
        print(f"Validation errors: {errors}\n")
        return

    print("Template validation passed!\n")

    # Output CloudFormation JSON
    print("=" * 80)
    print("CLOUDFORMATION TEMPLATE (JSON)")
    print("=" * 80)
    print(template.to_json())
    print()

    # Output YAML if available
    try:
        print("=" * 80)
        print("CLOUDFORMATION TEMPLATE (YAML)")
        print("=" * 80)
        print(template.to_yaml())
    except ImportError:
        print("(Install pyyaml for YAML: pip install cloudformation_dataclasses[yaml])")


if __name__ == "__main__":
    main()
