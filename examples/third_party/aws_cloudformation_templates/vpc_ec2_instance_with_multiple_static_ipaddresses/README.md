# VpcEc2InstanceWithMultipleStaticIpaddresses

Imported from `VPC_EC2_Instance_With_Multiple_Static_IPAddresses.yaml`.

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
uv run python -m vpc_ec2_instance_with_multiple_static_ipaddresses
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EIP1` | AWS::EC2::EIP |
| `EIPAssoc1` | AWS::EC2::EIPAssociation |
| `SSHSecurityGroup` | AWS::EC2::SecurityGroup |
| `EC2Instance` | AWS::EC2::Instance |
| `Eth0` | AWS::EC2::NetworkInterface |
