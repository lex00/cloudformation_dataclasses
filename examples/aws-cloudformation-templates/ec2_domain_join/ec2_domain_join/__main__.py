"""Allow running as: python -m ec2_domain_join."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Join Windows instance to AWS-Active Directory or Microsoft AD (no powershell). Create SSM document, IAM Role, SSM doc and EC2 Instance. Attaches EC2 instance to AD. Will need to use Domain Logins to RDP in.")
