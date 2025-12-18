# VPC CloudFormation Examples

Migrated from [aws-cloudformation-templates/VPC](https://github.com/awslabs/aws-cloudformation-templates/tree/main/VPC).

## Examples

### vpc_with_nat.py

VPC with Managed NAT and Private Subnet.

**Original:** `VPC_With_Managed_NAT_And_Private_Subnet.yaml`

**Features demonstrated:**
- VPC with DNS support and hostnames enabled
- Public and private subnets across two availability zones
- Internet Gateway with VPC attachment
- NAT Gateways for private subnet internet access
- Route tables for public and private routing
- Network ACLs for subnet security
- `Mapping` for CIDR configuration
- `Select` and `GetAZs` intrinsics for AZ selection
- `FindInMap` for CIDR lookups
- `depends_on` for resource ordering
- Export outputs for cross-stack references

**Run tests:**
```bash
uv run pytest examples/aws_cloudformation_templates/VPC/tests/ -v
```

**Generate template:**
```bash
uv run python -m examples.aws_cloudformation_templates.VPC.vpc_with_nat
```
