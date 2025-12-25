# VpcpeeringRequesterMainCfn

Migrated from [VPCPeering-Requester.main.cfn.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m vpcpeering_requester_main_cfn
```

### Validate Template

```bash
python -m vpcpeering_requester_main_cfn --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPCPeeringRequesterSetupStack` | AWS::CloudFormation::Stack |
| `VPCPeeringUpdatesStack` | AWS::CloudFormation::Stack |
