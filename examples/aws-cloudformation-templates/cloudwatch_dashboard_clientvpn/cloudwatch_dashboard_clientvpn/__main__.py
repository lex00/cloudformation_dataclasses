"""Allow running as: python -m cloudwatch_dashboard_clientvpn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This CloudFormation template creates a set of CloudWatch Logs Insights queries and a corresponding dashboard  for comprehensive AWS Client VPN usage reporting. It provides detailed insights into VPN usage patterns,  connection durations, data transfer volumes, and user activities across different authentication methods  (AD/SAML, Mutual Auth, and Mixed Auth).\n")
