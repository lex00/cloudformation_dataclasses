"""DMSReplicationTask - AWS::DMS::ReplicationTask resource."""

from .. import *  # noqa: F403


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
    depends_on = ["AuroraSourceEndpoint", "S3TargetEndpoint", "DMSReplicationInstance"]
