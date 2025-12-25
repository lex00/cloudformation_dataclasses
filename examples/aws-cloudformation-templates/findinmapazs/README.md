# Findinmapazs

Migrated from [FindInMapAZs.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m findinmapazs
```

### Validate Template

```bash
python -m findinmapazs --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `InternetGatewayAttachment` | AWS::EC2::VPCGatewayAttachment |
| `PublicSubnet1` | AWS::EC2::Subnet |
| `PublicSubnet2` | AWS::EC2::Subnet |
| `PrivateSubnet1` | AWS::EC2::Subnet |
| `PrivateSubnet2` | AWS::EC2::Subnet |
| `NatGateway1EIP` | AWS::EC2::EIP |
| `NatGateway2EIP` | AWS::EC2::EIP |
| `NatGateway1` | AWS::EC2::NatGateway |
| `NatGateway2` | AWS::EC2::NatGateway |
| `PublicRouteTable` | AWS::EC2::RouteTable |
| `DefaultPublicRoute` | AWS::EC2::Route |
| `PublicSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRouteTable1` | AWS::EC2::RouteTable |
| `DefaultPrivateRoute1` | AWS::EC2::Route |
| `PrivateSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRouteTable2` | AWS::EC2::RouteTable |
| `DefaultPrivateRoute2` | AWS::EC2::Route |
| `PrivateSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `NoIngressSecurityGroup` | AWS::EC2::SecurityGroup |
