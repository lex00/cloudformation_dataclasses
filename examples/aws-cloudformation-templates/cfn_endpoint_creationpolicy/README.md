# CfnEndpointCreationpolicy

Migrated from [cfn-endpoint-creationpolicy.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cfn_endpoint_creationpolicy
```

### Validate Template

```bash
python -m cfn_endpoint_creationpolicy --validate
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
| `CfnEndpoint` | AWS::EC2::VPCEndpoint |
| `PublicSubnet1` | AWS::EC2::Subnet |
| `PublicSubnet2` | AWS::EC2::Subnet |
| `PrivateSubnet1` | AWS::EC2::Subnet |
| `PrivateSubnet2` | AWS::EC2::Subnet |
| `PublicRouteTable` | AWS::EC2::RouteTable |
| `DefaultPublicRoute` | AWS::EC2::Route |
| `PublicSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRouteTable1` | AWS::EC2::RouteTable |
| `PrivateSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRouteTable2` | AWS::EC2::RouteTable |
| `PrivateSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `RootRole` | AWS::IAM::Role |
| `BastionInstance` | AWS::EC2::Instance |
| `BastionSG` | AWS::EC2::SecurityGroup |
| `BastionProfile` | AWS::IAM::InstanceProfile |
| `PrivateInstance` | AWS::EC2::Instance |
| `PrivateSG` | AWS::EC2::SecurityGroup |
| `PrivateProfile` | AWS::IAM::InstanceProfile |
| `EndpointSG` | AWS::EC2::SecurityGroup |
