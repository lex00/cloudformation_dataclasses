# Networkloadbalancerwitheips

Migrated from [NetworkLoadBalancerWithEIPs.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m networkloadbalancerwitheips
```

### Validate Template

```bash
python -m networkloadbalancerwitheips --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EIP1` | AWS::EC2::EIP |
| `EIP2` | AWS::EC2::EIP |
| `loadBalancer` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `FirstEIP` | AWS::EC2::EIP |
| `SecondEIP` | AWS::EC2::EIP |
| `TargetGroup` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `Listener` | AWS::ElasticLoadBalancingV2::Listener |
