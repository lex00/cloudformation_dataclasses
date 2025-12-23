# CloudwatchDashboardClientvpn

Migrated from [CloudWatch_Dashboard_ClientVPN.yml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m cloudwatch_dashboard_clientvpn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `TotalUsagePerClientVPNEndpoint` | AWS::Logs::QueryDefinition |
| `ADSAMLAuthTotalUsageReport` | AWS::Logs::QueryDefinition |
| `ADSAMLAuthDistinctUsersConnectionDuration` | AWS::Logs::QueryDefinition |
| `ADSAMLAuthDistinctUsers` | AWS::Logs::QueryDefinition |
| `ADSAMLAuthUsersConnectionDuration` | AWS::Logs::QueryDefinition |
| `MutualAuthTotalUsageReport` | AWS::Logs::QueryDefinition |
| `MutualAuthDistinctUsersConnectionDuration` | AWS::Logs::QueryDefinition |
| `MutualAuthDistinctUsers` | AWS::Logs::QueryDefinition |
| `MutualAuthUsersConnectionDuration` | AWS::Logs::QueryDefinition |
| `MixAuthTotalUsageReport` | AWS::Logs::QueryDefinition |
| `MixAuthDistinctUsersConnectionDuration` | AWS::Logs::QueryDefinition |
| `MixAuthDistinctUsers` | AWS::Logs::QueryDefinition |
| `MixAuthUsersConnectionDuration` | AWS::Logs::QueryDefinition |
| `Dashboard` | AWS::CloudWatch::Dashboard |
