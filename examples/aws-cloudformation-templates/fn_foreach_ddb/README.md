# FnForeachDdb

Imported from `DMSAuroraToS3FullLoadAndOngoingReplication.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m fn_foreach_ddb
```

### Validate Template

```bash
python -m fn_foreach_ddb --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `DBSubnet1` | AWS::EC2::Subnet |
| `DBSubnet2` | AWS::EC2::Subnet |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `AttachGateway` | AWS::EC2::VPCGatewayAttachment |
| `RouteTable` | AWS::EC2::RouteTable |
| `Route` | AWS::EC2::Route |
| `SubnetRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `SubnetRouteTableAssociation1` | AWS::EC2::SubnetRouteTableAssociation |
| `AuroraDBSubnetGroup` | AWS::RDS::DBSubnetGroup |
| `AuroraSecurityGroup` | AWS::EC2::SecurityGroup |
| `AuroraCluster` | AWS::RDS::DBCluster |
| `AuroraDB` | AWS::RDS::DBInstance |
| `S3Bucket` | AWS::S3::Bucket |
| `DMSCloudwatchRole` | AWS::IAM::Role |
| `DMSVpcRole` | AWS::IAM::Role |
| `S3TargetDMSRole` | AWS::IAM::Role |
| `DMSReplicationSubnetGroup` | AWS::DMS::ReplicationSubnetGroup |
| `DMSSecurityGroup` | AWS::EC2::SecurityGroup |
| `DMSReplicationInstance` | AWS::DMS::ReplicationInstance |
| `AuroraSourceEndpoint` | AWS::DMS::Endpoint |
| `S3TargetEndpoint` | AWS::DMS::Endpoint |
| `DMSReplicationTask` | AWS::DMS::ReplicationTask |
