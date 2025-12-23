# LoadBalancer

Migrated from [load-balancer.yml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Run Tests

```bash
uv run pytest tests/ -v
```

### Generate Template

```bash
uv run python -m load_balancer
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `LoadBalancer` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `LoadBalancerSecurityGroup` | AWS::EC2::SecurityGroup |
| `LoadBalancerEgress` | AWS::EC2::SecurityGroupEgress |
| `LoadBalancerListener` | AWS::ElasticLoadBalancingV2::Listener |
| `TargetGroup` | AWS::ElasticLoadBalancingV2::TargetGroup |
