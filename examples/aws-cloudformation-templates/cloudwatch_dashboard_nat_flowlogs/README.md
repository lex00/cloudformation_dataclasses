# CloudwatchDashboardNatFlowlogs

Migrated from [CloudWatch_Dashboard_NAT_FlowLogs.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cloudwatch_dashboard_nat_flowlogs
```

### Validate Template

```bash
python -m cloudwatch_dashboard_nat_flowlogs --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CloudWatchDashboard` | AWS::CloudWatch::Dashboard |
