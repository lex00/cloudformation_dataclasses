"""Allow running as: python -m template_1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="The Count macro is an iterator for creating multiple resources\n")
