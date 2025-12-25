"""Tests for fargate-webapp multi-stack example."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLE_DIR = Path(__file__).parent.parent.parent / "examples" / "fargate-webapp"
STACKS = ["vpc", "dns", "alb", "rds", "fargate"]


@pytest.fixture(scope="module")
def stack_outputs():
    """Build all stacks and return their JSON outputs."""
    outputs = {}
    for stack in STACKS:
        stack_dir = EXAMPLE_DIR / stack
        result = subprocess.run(
            [sys.executable, "-m", stack],
            cwd=stack_dir,
            capture_output=True,
            text=True,
            env={
                **dict(__import__("os").environ),
                "PYTHONPATH": str(
                    Path(__file__).parent.parent.parent / "src"
                ),
            },
        )
        assert result.returncode == 0, f"{stack} failed: {result.stderr}"
        outputs[stack] = json.loads(result.stdout)
    return outputs


class TestFargateWebappStacks:
    """Test that all stacks generate valid CloudFormation."""

    def test_vpc_has_required_resources(self, stack_outputs):
        """VPC stack has VPC, subnets, NAT gateways."""
        resources = stack_outputs["vpc"]["Resources"]
        types = {r["Type"] for r in resources.values()}

        assert "AWS::EC2::VPC" in types
        assert "AWS::EC2::Subnet" in types
        assert "AWS::EC2::NatGateway" in types
        assert "AWS::EC2::InternetGateway" in types

    def test_vpc_has_required_outputs(self, stack_outputs):
        """VPC stack exports VpcId, subnet IDs."""
        outputs = stack_outputs["vpc"].get("Outputs", {})
        assert "VpcId" in outputs
        assert "PublicSubnetIds" in outputs
        assert "PrivateSubnetIds" in outputs

    def test_dns_has_hosted_zone_and_cert(self, stack_outputs):
        """DNS stack has Route53 zone and ACM certificate."""
        resources = stack_outputs["dns"]["Resources"]
        types = {r["Type"] for r in resources.values()}

        assert "AWS::Route53::HostedZone" in types
        assert "AWS::CertificateManager::Certificate" in types

    def test_dns_has_required_outputs(self, stack_outputs):
        """DNS stack exports zone ID and certificate ARN."""
        outputs = stack_outputs["dns"].get("Outputs", {})
        assert "HostedZoneId" in outputs
        assert "CertificateArn" in outputs
        assert "NameServers" in outputs

    def test_alb_has_load_balancer(self, stack_outputs):
        """ALB stack has ALB, listeners, target group."""
        resources = stack_outputs["alb"]["Resources"]
        types = {r["Type"] for r in resources.values()}

        assert "AWS::ElasticLoadBalancingV2::LoadBalancer" in types
        assert "AWS::ElasticLoadBalancingV2::Listener" in types
        assert "AWS::ElasticLoadBalancingV2::TargetGroup" in types

    def test_alb_has_required_outputs(self, stack_outputs):
        """ALB stack exports ARN, security group, target group."""
        outputs = stack_outputs["alb"].get("Outputs", {})
        assert "AlbArn" in outputs
        assert "AlbSecurityGroupId" in outputs
        assert "TargetGroupArn" in outputs

    def test_rds_has_database(self, stack_outputs):
        """RDS stack has DB instance and subnet group."""
        resources = stack_outputs["rds"]["Resources"]
        types = {r["Type"] for r in resources.values()}

        assert "AWS::RDS::DBInstance" in types
        assert "AWS::RDS::DBSubnetGroup" in types
        assert "AWS::SecretsManager::Secret" in types

    def test_rds_has_required_outputs(self, stack_outputs):
        """RDS stack exports endpoint and secret ARN."""
        outputs = stack_outputs["rds"].get("Outputs", {})
        assert "DbEndpoint" in outputs
        assert "DbSecretArn" in outputs

    def test_fargate_has_ecs_service(self, stack_outputs):
        """Fargate stack has ECS cluster, service, task definition."""
        resources = stack_outputs["fargate"]["Resources"]
        types = {r["Type"] for r in resources.values()}

        assert "AWS::ECS::Cluster" in types
        assert "AWS::ECS::Service" in types
        assert "AWS::ECS::TaskDefinition" in types
        assert "AWS::Logs::LogGroup" in types

    def test_fargate_has_required_outputs(self, stack_outputs):
        """Fargate stack exports cluster and service info."""
        outputs = stack_outputs["fargate"].get("Outputs", {})
        assert "ClusterArn" in outputs
        assert "ServiceName" in outputs

    def test_all_stacks_have_version(self, stack_outputs):
        """All stacks have AWSTemplateFormatVersion."""
        for stack, output in stack_outputs.items():
            assert "AWSTemplateFormatVersion" in output, f"{stack} missing version"

    def test_all_stacks_have_description(self, stack_outputs):
        """All stacks have a Description."""
        for stack, output in stack_outputs.items():
            assert "Description" in output, f"{stack} missing description"

    def test_vpc_has_six_subnets(self, stack_outputs):
        """VPC stack has 3 public and 3 private subnets."""
        resources = stack_outputs["vpc"]["Resources"]
        subnet_count = sum(
            1 for r in resources.values() if r["Type"] == "AWS::EC2::Subnet"
        )
        assert subnet_count == 6, f"Expected 6 subnets, got {subnet_count}"

    def test_vpc_has_three_nat_gateways(self, stack_outputs):
        """VPC stack has 3 NAT gateways (one per AZ)."""
        resources = stack_outputs["vpc"]["Resources"]
        nat_count = sum(
            1 for r in resources.values() if r["Type"] == "AWS::EC2::NatGateway"
        )
        assert nat_count == 3, f"Expected 3 NAT gateways, got {nat_count}"

    def test_fargate_task_uses_awsvpc(self, stack_outputs):
        """Fargate task definition uses awsvpc network mode."""
        resources = stack_outputs["fargate"]["Resources"]
        task_def = next(
            r for r in resources.values()
            if r["Type"] == "AWS::ECS::TaskDefinition"
        )
        assert task_def["Properties"]["NetworkMode"] == "awsvpc"

    def test_fargate_task_is_fargate_compatible(self, stack_outputs):
        """Fargate task definition requires FARGATE compatibility."""
        resources = stack_outputs["fargate"]["Resources"]
        task_def = next(
            r for r in resources.values()
            if r["Type"] == "AWS::ECS::TaskDefinition"
        )
        assert "FARGATE" in task_def["Properties"]["RequiresCompatibilities"]

    def test_rds_uses_postgres(self, stack_outputs):
        """RDS instance uses PostgreSQL engine."""
        resources = stack_outputs["rds"]["Resources"]
        db_instance = next(
            r for r in resources.values()
            if r["Type"] == "AWS::RDS::DBInstance"
        )
        assert db_instance["Properties"]["Engine"] == "postgres"

    def test_alb_has_https_listener(self, stack_outputs):
        """ALB has an HTTPS listener on port 443."""
        resources = stack_outputs["alb"]["Resources"]
        listeners = [
            r for r in resources.values()
            if r["Type"] == "AWS::ElasticLoadBalancingV2::Listener"
        ]
        https_listeners = [
            l for l in listeners
            if l["Properties"].get("Port") == 443
        ]
        assert len(https_listeners) == 1, "Expected exactly one HTTPS listener"

    def test_alb_http_redirects_to_https(self, stack_outputs):
        """ALB HTTP listener redirects to HTTPS."""
        resources = stack_outputs["alb"]["Resources"]
        listeners = [
            r for r in resources.values()
            if r["Type"] == "AWS::ElasticLoadBalancingV2::Listener"
        ]
        http_listener = next(
            (l for l in listeners if l["Properties"].get("Port") == 80),
            None
        )
        assert http_listener is not None, "Expected HTTP listener"
        actions = http_listener["Properties"]["DefaultActions"]
        assert any(a["Type"] == "redirect" for a in actions)
