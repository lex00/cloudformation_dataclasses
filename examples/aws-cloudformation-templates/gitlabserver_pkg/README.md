# GitlabserverPkg

Imported from `VPCPeering-Accepter.main.cfn.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m gitlabserver_pkg
```

### Validate Template

```bash
python -m gitlabserver_pkg --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPCPeeringAccepterTagStack` | AWS::CloudFormation::Stack |
| `VPCPeeringUpdatesStack` | AWS::CloudFormation::Stack |
