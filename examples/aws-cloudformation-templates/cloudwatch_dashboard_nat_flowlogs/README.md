# CloudwatchDashboardNatFlowlogs

Migrated from [CloudWatch_Dashboard_NAT_FlowLogs.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m cloudwatch_dashboard_nat_flowlogs
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CloudWatchDashboard` | AWS::CloudWatch::Dashboard |
