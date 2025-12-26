# PrivateSubnetPublicService

Migrated from [private-subnet-public-service.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m private_subnet_public_service
```

### Validate Template

```bash
python -m private_subnet_public_service --validate
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
