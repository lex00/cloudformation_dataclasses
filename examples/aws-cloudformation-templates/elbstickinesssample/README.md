# Elbstickinesssample

Imported from `NetworkLoadBalancerWithEIPs.yaml`.

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
uv run python -m elbstickinesssample
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
