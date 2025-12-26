"""Allow running as: python -m ecs_schedule_example."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Amazon ECS Time and Event-Based Task Scheduling with CloudFormation. This will let you run tasks on a regular, scheduled basis and in response to CloudWatch Events. It easier to launch and stop container services that you need to run only at certain times. For example a backup/cleanup task.")
