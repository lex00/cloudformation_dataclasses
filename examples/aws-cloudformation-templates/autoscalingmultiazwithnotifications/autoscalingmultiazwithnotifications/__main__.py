"""Allow running as: python -m autoscalingmultiazwithnotifications."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Create a multi-az, load balanced and Auto Scaled sample web site running on\nan Apache Web Server. The application is configured to span all\nAvailability Zones in the region and is Auto-Scaled based on the CPU\nutilization of the web servers. Notifications will be sent to the operator\nemail address on scaling events. The instances are load balanced with a\nsimple health check against the default web page. **WARNING** This template\ncreates one or more Amazon EC2 instances and an Elastic Load Balancer. You\nwill be billed for the AWS resources used if you create a stack from this\ntemplate.\n")
