# PublicVpc

Imported from `public-service_2.yaml`.

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
uv run python -m public_vpc
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `TaskDefinition` | AWS::ECS::TaskDefinition |
| `Service` | AWS::ECS::Service |
| `TargetGroup` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `LoadBalancerRule` | AWS::ElasticLoadBalancingV2::ListenerRule |
