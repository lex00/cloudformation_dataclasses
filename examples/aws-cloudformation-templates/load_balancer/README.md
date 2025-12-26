# LoadBalancer

Migrated from [load-balancer.yml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m load_balancer
```

### Validate Template

```bash
python -m load_balancer --validate
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
