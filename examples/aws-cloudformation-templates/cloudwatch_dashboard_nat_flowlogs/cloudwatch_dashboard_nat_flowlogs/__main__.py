"""Allow running as: python -m cloudwatch_dashboard_nat_flowlogs."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Creates a CloudWatch Dashboard with four CloudWatch Logs Insights log widgets that query VPC flow logs for NAT Gateway, related to https://repost.aws/knowledge-center/vpc-find-traffic-sources-nat-gateway")
