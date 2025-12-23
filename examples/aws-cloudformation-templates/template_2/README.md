# Template2

Migrated from [template_2.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m template_2
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
| `AttachGateway` | AWS::EC2::VPCGatewayAttachment |
| `PublicRouteTable` | AWS::EC2::RouteTable |
| `RouteInternetGateway` | AWS::EC2::Route |
| `PublicSubnet1` | AWS::EC2::Subnet |
| `PublicRouteTableAssociation1` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnet2` | AWS::EC2::Subnet |
| `PublicRouteTableAssociation2` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnet3` | AWS::EC2::Subnet |
| `PublicRouteTableAssociation3` | AWS::EC2::SubnetRouteTableAssociation |
| `EIP1` | AWS::EC2::EIP |
| `NATGateway1` | AWS::EC2::NatGateway |
| `EIP2` | AWS::EC2::EIP |
| `NATGateway2` | AWS::EC2::NatGateway |
| `EIP3` | AWS::EC2::EIP |
| `NATGateway3` | AWS::EC2::NatGateway |
| `PrivateSubnet1` | AWS::EC2::Subnet |
| `PrivateRouteTable1` | AWS::EC2::RouteTable |
| `PrivateRouteTableAssociation1` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRoute1` | AWS::EC2::Route |
| `PrivateSubnet2` | AWS::EC2::Subnet |
| `PrivateRouteTable2` | AWS::EC2::RouteTable |
| `PrivateRouteTableAssociation2` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRoute2` | AWS::EC2::Route |
| `PrivateSubnet3` | AWS::EC2::Subnet |
| `PrivateRouteTable3` | AWS::EC2::RouteTable |
| `PrivateRouteTableAssociation3` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRoute3` | AWS::EC2::Route |
| `ControlPlane` | AWS::EKS::Cluster |
| `EKSClusterRole` | AWS::IAM::Role |
| `ControlPlaneSecurityGroup` | AWS::EC2::SecurityGroup |
| `ControlPlaneSecurityGroupIngress` | AWS::EC2::SecurityGroupIngress |
| `LaunchTemplate` | AWS::EC2::LaunchTemplate |
| `ManagedNodeGroup` | AWS::EKS::Nodegroup |
| `NodeInstanceRole` | AWS::IAM::Role |
