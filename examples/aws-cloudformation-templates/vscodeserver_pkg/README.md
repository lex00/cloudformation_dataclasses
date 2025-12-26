# VscodeserverPkg

Imported from `VPC_With_Managed_NAT_And_Private_Subnet.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m vscodeserver_pkg
```

### Validate Template

```bash
python -m vscodeserver_pkg --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `PublicSubnet0` | AWS::EC2::Subnet |
| `PublicSubnet1` | AWS::EC2::Subnet |
| `PrivateSubnet0` | AWS::EC2::Subnet |
| `PrivateSubnet1` | AWS::EC2::Subnet |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `GatewayToInternet` | AWS::EC2::VPCGatewayAttachment |
| `PublicRouteTable` | AWS::EC2::RouteTable |
| `PublicRoute` | AWS::EC2::Route |
| `PublicSubnetRouteTableAssociation0` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnetRouteTableAssociation1` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicNetworkAcl` | AWS::EC2::NetworkAcl |
| `InboundHTTPPublicNetworkAclEntry` | AWS::EC2::NetworkAclEntry |
| `OutboundPublicNetworkAclEntry` | AWS::EC2::NetworkAclEntry |
| `PublicSubnetNetworkAclAssociation0` | AWS::EC2::SubnetNetworkAclAssociation |
| `PublicSubnetNetworkAclAssociation1` | AWS::EC2::SubnetNetworkAclAssociation |
| `ElasticIP0` | AWS::EC2::EIP |
| `ElasticIP1` | AWS::EC2::EIP |
| `NATGateway0` | AWS::EC2::NatGateway |
| `NATGateway1` | AWS::EC2::NatGateway |
| `PrivateRouteTable0` | AWS::EC2::RouteTable |
| `PrivateRouteTable1` | AWS::EC2::RouteTable |
| `PrivateRouteToInternet0` | AWS::EC2::Route |
| `PrivateRouteToInternet1` | AWS::EC2::Route |
| `PrivateSubnetRouteTableAssociation0` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateSubnetRouteTableAssociation1` | AWS::EC2::SubnetRouteTableAssociation |
