# VpcpeeringUpdatesCfn

Migrated from [VPCPeering-Updates.cfn.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m vpcpeering_updates_cfn
```

### Validate Template

```bash
python -m vpcpeering_updates_cfn --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `PeerRoute1` | AWS::EC2::Route |
| `PeerRoute2` | AWS::EC2::Route |
| `PeerRoute3` | AWS::EC2::Route |
| `PeerRoute4` | AWS::EC2::Route |
| `PeerRoute5` | AWS::EC2::Route |
| `PeerRoute6` | AWS::EC2::Route |
| `PeerIngressRule1` | AWS::EC2::SecurityGroupIngress |
| `PeerIngressRule2` | AWS::EC2::SecurityGroupIngress |
| `PeerIngressRule3` | AWS::EC2::SecurityGroupIngress |
| `PeerIngressRule4` | AWS::EC2::SecurityGroupIngress |
| `PeerIngressRule5` | AWS::EC2::SecurityGroupIngress |
| `PeerIngressRule6` | AWS::EC2::SecurityGroupIngress |
