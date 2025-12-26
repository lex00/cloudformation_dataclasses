"""Stack resources."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DMSReplicationSubnetGroup:
    """AWS::DMS::ReplicationSubnetGroup resource."""

    resource: dms.ReplicationSubnetGroup
    replication_subnet_group_description = 'Subnets available for DMS'
    subnet_ids = [ref(DBSubnet1), ref(DBSubnet2)]


@cloudformation_dataclass
class DMSReplicationInstance:
    """AWS::DMS::ReplicationInstance resource."""

    resource: dms.ReplicationInstance
    availability_zone = get_att(DBSubnet1, "AvailabilityZone")
    publicly_accessible = False
    replication_instance_class = 'dms.t3.medium'
    replication_instance_identifier = 'aurora-s3-repinstance-sampledb'
    replication_subnet_group_identifier = ref(DMSReplicationSubnetGroup)
    vpc_security_group_ids = [ref(DMSSecurityGroup)]
    depends_on = [DMSReplicationSubnetGroup, DMSSecurityGroup]


@cloudformation_dataclass
class AuroraSourceEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: dms.Endpoint
    endpoint_type = 'source'
    engine_name = 'AURORA'
    password = '{{resolve:secretsmanager:aurora-source-enpoint-password:SecretString:password}}'
    port = 3306
    server_name = get_att(AuroraCluster, "Endpoint.Address")
    username = 'admin'
    depends_on = [DMSReplicationInstance, AuroraCluster, AuroraDB]


@cloudformation_dataclass
class S3TargetEndpointRedshiftSettings:
    resource: dms.endpoint.RedshiftSettings
    bucket_name = ref(S3Bucket)
    service_access_role_arn = get_att(S3TargetDMSRole, "Arn")


@cloudformation_dataclass
class S3TargetEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: dms.Endpoint
    endpoint_type = 'target'
    engine_name = 'S3'
    extra_connection_attributes = 'addColumnName=true'
    s3_settings = S3TargetEndpointRedshiftSettings
    depends_on = [DMSReplicationInstance, S3Bucket, S3TargetDMSRole]


@cloudformation_dataclass
class DMSReplicationTask:
    """AWS::DMS::ReplicationTask resource."""

    resource: dms.ReplicationTask
    migration_type = 'full-load-and-cdc'
    replication_instance_arn = ref(DMSReplicationInstance)
    replication_task_settings = '{ "Logging" : { "EnableLogging" : true, "LogComponents": [ { "Id" : "SOURCE_UNLOAD", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "SOURCE_CAPTURE", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "TARGET_LOAD", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "TARGET_APPLY", "Severity" : "LOGGER_SEVERITY_DEFAULT" } ] } }'
    source_endpoint_arn = ref(AuroraSourceEndpoint)
    table_mappings = '{ "rules": [ { "rule-type" : "selection", "rule-id" : "1", "rule-name" : "1", "object-locator" : { "schema-name" : "dms_sample", "table-name" : "%" }, "rule-action" : "include" } ] }'
    target_endpoint_arn = ref(S3TargetEndpoint)
    depends_on = [AuroraSourceEndpoint, S3TargetEndpoint, DMSReplicationInstance]
