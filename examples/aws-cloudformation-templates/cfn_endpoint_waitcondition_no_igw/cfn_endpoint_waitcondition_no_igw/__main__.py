"""Allow running as: python -m cfn_endpoint_waitcondition_no_igw."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This templates updates the settings for an AD Connector or AWS Managed AD directory. Tasks accomplied, (1) enables directory monitoring (2) option to create a custom access url (alias) (3) option to enable SSO via directory services. Note, deleting the directory, will only remove directory monitoring, directory SSO or alias settings will not be touched.")
