"""Allow running as: python -m adconnector_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template creates an AD Connector to connect to an on-premises directory. Tasks accomplished, (1) create AD Connector (2) option to create seamless domain join resources for Windows & Linux EC2 instances (3) option to create a domain members security group that allows all PrivateIP communications inbound (4) option to create DHCPOptionSet pointing to Domain DNS servers")
