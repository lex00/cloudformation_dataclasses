# Vpc

Migrated from [vpc.yml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m vpc
```

### Validate Template

```bash
python -m vpc --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `PublicSubnet1` | AWS::EC2::Subnet |
| `PublicSubnet1RouteTable` | AWS::EC2::RouteTable |
| `PublicSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnet1DefaultRoute` | AWS::EC2::Route |
| `PublicSubnet1EIP` | AWS::EC2::EIP |
| `PublicSubnet1NATGateway` | AWS::EC2::NatGateway |
| `PublicSubnet2` | AWS::EC2::Subnet |
| `PublicSubnet2RouteTable` | AWS::EC2::RouteTable |
| `PublicSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnet2DefaultRoute` | AWS::EC2::Route |
| `PublicSubnet2EIP` | AWS::EC2::EIP |
| `PublicSubnet2NATGateway` | AWS::EC2::NatGateway |
| `PrivateSubnet1Subnet` | AWS::EC2::Subnet |
| `PrivateSubnet1RouteTable` | AWS::EC2::RouteTable |
| `PrivateSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateSubnet1DefaultRoute` | AWS::EC2::Route |
| `PrivateSubnet2Subnet` | AWS::EC2::Subnet |
| `PrivateSubnet2RouteTable` | AWS::EC2::RouteTable |
| `PrivateSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateSubnet2DefaultRoute` | AWS::EC2::Route |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `VPCGW` | AWS::EC2::VPCGatewayAttachment |
