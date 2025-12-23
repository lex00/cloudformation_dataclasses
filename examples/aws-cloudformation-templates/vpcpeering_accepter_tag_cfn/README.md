# VpcpeeringAccepterTagCfn

Migrated from [VPCPeering-Accepter-Tag.cfn.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m vpcpeering_accepter_tag_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `TagVpcPeeringConnectionsLambdaLogsLogGroup` | AWS::Logs::LogGroup |
| `TagVpcPeeringConnectionsLambdaRole` | AWS::IAM::Role |
| `TagVpcPeeringConnectionsLambdaFunction` | AWS::Lambda::Function |
| `TagVpcPeeringConnectionsResource` | Custom::TagVpcPeeringConnection |
