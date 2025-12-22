"""PropertyTypes for AWS::Config::ConfigRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AggregateConformancePackComplianceSummaryGroupKey:
    """AggregateConformancePackComplianceSummaryGroupKey enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


class AggregatedSourceStatusType:
    """AggregatedSourceStatusType enum values."""

    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    OUTDATED = "OUTDATED"


class AggregatedSourceType:
    """AggregatedSourceType enum values."""

    ACCOUNT = "ACCOUNT"
    ORGANIZATION = "ORGANIZATION"


class AggregatorFilterType:
    """AggregatorFilterType enum values."""

    INCLUDE = "INCLUDE"


class ChronologicalOrder:
    """ChronologicalOrder enum values."""

    REVERSE = "Reverse"
    FORWARD = "Forward"


class ComplianceType:
    """ComplianceType enum values."""

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class ConfigRuleComplianceSummaryGroupKey:
    """ConfigRuleComplianceSummaryGroupKey enum values."""

    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


class ConfigRuleState:
    """ConfigRuleState enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETING_RESULTS = "DELETING_RESULTS"
    EVALUATING = "EVALUATING"


class ConfigurationItemStatus:
    """ConfigurationItemStatus enum values."""

    OK = "OK"
    RESOURCEDISCOVERED = "ResourceDiscovered"
    RESOURCENOTRECORDED = "ResourceNotRecorded"
    RESOURCEDELETED = "ResourceDeleted"
    RESOURCEDELETEDNOTRECORDED = "ResourceDeletedNotRecorded"


class ConfigurationRecorderFilterName:
    """ConfigurationRecorderFilterName enum values."""

    RECORDINGSCOPE = "recordingScope"


class ConformancePackComplianceType:
    """ConformancePackComplianceType enum values."""

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class ConformancePackState:
    """ConformancePackState enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"


class DeliveryStatus:
    """DeliveryStatus enum values."""

    SUCCESS = "Success"
    FAILURE = "Failure"
    NOT_APPLICABLE = "Not_Applicable"


class EvaluationMode:
    """EvaluationMode enum values."""

    DETECTIVE = "DETECTIVE"
    PROACTIVE = "PROACTIVE"


class EventSource:
    """EventSource enum values."""

    AWS_CONFIG = "aws.config"


class MaximumExecutionFrequency:
    """MaximumExecutionFrequency enum values."""

    ONE_HOUR = "One_Hour"
    THREE_HOURS = "Three_Hours"
    SIX_HOURS = "Six_Hours"
    TWELVE_HOURS = "Twelve_Hours"
    TWENTYFOUR_HOURS = "TwentyFour_Hours"


class MemberAccountRuleStatus:
    """MemberAccountRuleStatus enum values."""

    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class MessageType:
    """MessageType enum values."""

    CONFIGURATIONITEMCHANGENOTIFICATION = "ConfigurationItemChangeNotification"
    CONFIGURATIONSNAPSHOTDELIVERYCOMPLETED = "ConfigurationSnapshotDeliveryCompleted"
    SCHEDULEDNOTIFICATION = "ScheduledNotification"
    OVERSIZEDCONFIGURATIONITEMCHANGENOTIFICATION = "OversizedConfigurationItemChangeNotification"


class OrganizationConfigRuleTriggerType:
    """OrganizationConfigRuleTriggerType enum values."""

    CONFIGURATIONITEMCHANGENOTIFICATION = "ConfigurationItemChangeNotification"
    OVERSIZEDCONFIGURATIONITEMCHANGENOTIFICATION = "OversizedConfigurationItemChangeNotification"
    SCHEDULEDNOTIFICATION = "ScheduledNotification"


class OrganizationConfigRuleTriggerTypeNoSN:
    """OrganizationConfigRuleTriggerTypeNoSN enum values."""

    CONFIGURATIONITEMCHANGENOTIFICATION = "ConfigurationItemChangeNotification"
    OVERSIZEDCONFIGURATIONITEMCHANGENOTIFICATION = "OversizedConfigurationItemChangeNotification"


class OrganizationResourceDetailedStatus:
    """OrganizationResourceDetailedStatus enum values."""

    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class OrganizationResourceStatus:
    """OrganizationResourceStatus enum values."""

    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class OrganizationRuleStatus:
    """OrganizationRuleStatus enum values."""

    CREATE_SUCCESSFUL = "CREATE_SUCCESSFUL"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_SUCCESSFUL = "DELETE_SUCCESSFUL"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"


class Owner:
    """Owner enum values."""

    CUSTOM_LAMBDA = "CUSTOM_LAMBDA"
    AWS = "AWS"
    CUSTOM_POLICY = "CUSTOM_POLICY"


class RecorderStatus:
    """RecorderStatus enum values."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILURE = "Failure"
    NOTAPPLICABLE = "NotApplicable"


class RecordingFrequency:
    """RecordingFrequency enum values."""

    CONTINUOUS = "CONTINUOUS"
    DAILY = "DAILY"


class RecordingScope:
    """RecordingScope enum values."""

    INTERNAL = "INTERNAL"
    PAID = "PAID"


class RecordingStrategyType:
    """RecordingStrategyType enum values."""

    ALL_SUPPORTED_RESOURCE_TYPES = "ALL_SUPPORTED_RESOURCE_TYPES"
    INCLUSION_BY_RESOURCE_TYPES = "INCLUSION_BY_RESOURCE_TYPES"
    EXCLUSION_BY_RESOURCE_TYPES = "EXCLUSION_BY_RESOURCE_TYPES"


class RemediationExecutionState:
    """RemediationExecutionState enum values."""

    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


class RemediationExecutionStepState:
    """RemediationExecutionStepState enum values."""

    SUCCEEDED = "SUCCEEDED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    EXITED = "EXITED"
    UNKNOWN = "UNKNOWN"


class RemediationTargetType:
    """RemediationTargetType enum values."""

    SSM_DOCUMENT = "SSM_DOCUMENT"


class ResourceConfigurationSchemaType:
    """ResourceConfigurationSchemaType enum values."""

    CFN_RESOURCE_SCHEMA = "CFN_RESOURCE_SCHEMA"


class ResourceCountGroupKey:
    """ResourceCountGroupKey enum values."""

    RESOURCE_TYPE = "RESOURCE_TYPE"
    ACCOUNT_ID = "ACCOUNT_ID"
    AWS_REGION = "AWS_REGION"


class ResourceEvaluationStatus:
    """ResourceEvaluationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class ResourceType:
    """ResourceType enum values."""

    AWS_EC2_CUSTOMERGATEWAY = "AWS::EC2::CustomerGateway"
    AWS_EC2_EIP = "AWS::EC2::EIP"
    AWS_EC2_HOST = "AWS::EC2::Host"
    AWS_EC2_INSTANCE = "AWS::EC2::Instance"
    AWS_EC2_INTERNETGATEWAY = "AWS::EC2::InternetGateway"
    AWS_EC2_NETWORKACL = "AWS::EC2::NetworkAcl"
    AWS_EC2_NETWORKINTERFACE = "AWS::EC2::NetworkInterface"
    AWS_EC2_ROUTETABLE = "AWS::EC2::RouteTable"
    AWS_EC2_SECURITYGROUP = "AWS::EC2::SecurityGroup"
    AWS_EC2_SUBNET = "AWS::EC2::Subnet"
    AWS_CLOUDTRAIL_TRAIL = "AWS::CloudTrail::Trail"
    AWS_EC2_VOLUME = "AWS::EC2::Volume"
    AWS_EC2_VPC = "AWS::EC2::VPC"
    AWS_EC2_VPNCONNECTION = "AWS::EC2::VPNConnection"
    AWS_EC2_VPNGATEWAY = "AWS::EC2::VPNGateway"
    AWS_EC2_REGISTEREDHAINSTANCE = "AWS::EC2::RegisteredHAInstance"
    AWS_EC2_NATGATEWAY = "AWS::EC2::NatGateway"
    AWS_EC2_EGRESSONLYINTERNETGATEWAY = "AWS::EC2::EgressOnlyInternetGateway"
    AWS_EC2_VPCENDPOINT = "AWS::EC2::VPCEndpoint"
    AWS_EC2_VPCENDPOINTSERVICE = "AWS::EC2::VPCEndpointService"
    AWS_EC2_FLOWLOG = "AWS::EC2::FlowLog"
    AWS_EC2_VPCPEERINGCONNECTION = "AWS::EC2::VPCPeeringConnection"
    AWS_ELASTICSEARCH_DOMAIN = "AWS::Elasticsearch::Domain"
    AWS_IAM_GROUP = "AWS::IAM::Group"
    AWS_IAM_POLICY = "AWS::IAM::Policy"
    AWS_IAM_ROLE = "AWS::IAM::Role"
    AWS_IAM_USER = "AWS::IAM::User"
    AWS_ELASTICLOADBALANCINGV2_LOADBALANCER = "AWS::ElasticLoadBalancingV2::LoadBalancer"
    AWS_ACM_CERTIFICATE = "AWS::ACM::Certificate"
    AWS_RDS_DBINSTANCE = "AWS::RDS::DBInstance"
    AWS_RDS_DBSUBNETGROUP = "AWS::RDS::DBSubnetGroup"
    AWS_RDS_DBSECURITYGROUP = "AWS::RDS::DBSecurityGroup"
    AWS_RDS_DBSNAPSHOT = "AWS::RDS::DBSnapshot"
    AWS_RDS_DBCLUSTER = "AWS::RDS::DBCluster"
    AWS_RDS_DBCLUSTERSNAPSHOT = "AWS::RDS::DBClusterSnapshot"
    AWS_RDS_EVENTSUBSCRIPTION = "AWS::RDS::EventSubscription"
    AWS_S3_BUCKET = "AWS::S3::Bucket"
    AWS_S3_ACCOUNTPUBLICACCESSBLOCK = "AWS::S3::AccountPublicAccessBlock"
    AWS_REDSHIFT_CLUSTER = "AWS::Redshift::Cluster"
    AWS_REDSHIFT_CLUSTERSNAPSHOT = "AWS::Redshift::ClusterSnapshot"
    AWS_REDSHIFT_CLUSTERPARAMETERGROUP = "AWS::Redshift::ClusterParameterGroup"
    AWS_REDSHIFT_CLUSTERSECURITYGROUP = "AWS::Redshift::ClusterSecurityGroup"
    AWS_REDSHIFT_CLUSTERSUBNETGROUP = "AWS::Redshift::ClusterSubnetGroup"
    AWS_REDSHIFT_EVENTSUBSCRIPTION = "AWS::Redshift::EventSubscription"
    AWS_SSM_MANAGEDINSTANCEINVENTORY = "AWS::SSM::ManagedInstanceInventory"
    AWS_CLOUDWATCH_ALARM = "AWS::CloudWatch::Alarm"
    AWS_CLOUDFORMATION_STACK = "AWS::CloudFormation::Stack"
    AWS_ELASTICLOADBALANCING_LOADBALANCER = "AWS::ElasticLoadBalancing::LoadBalancer"
    AWS_AUTOSCALING_AUTOSCALINGGROUP = "AWS::AutoScaling::AutoScalingGroup"
    AWS_AUTOSCALING_LAUNCHCONFIGURATION = "AWS::AutoScaling::LaunchConfiguration"
    AWS_AUTOSCALING_SCALINGPOLICY = "AWS::AutoScaling::ScalingPolicy"
    AWS_AUTOSCALING_SCHEDULEDACTION = "AWS::AutoScaling::ScheduledAction"
    AWS_DYNAMODB_TABLE = "AWS::DynamoDB::Table"
    AWS_CODEBUILD_PROJECT = "AWS::CodeBuild::Project"
    AWS_WAF_RATEBASEDRULE = "AWS::WAF::RateBasedRule"
    AWS_WAF_RULE = "AWS::WAF::Rule"
    AWS_WAF_RULEGROUP = "AWS::WAF::RuleGroup"
    AWS_WAF_WEBACL = "AWS::WAF::WebACL"
    AWS_WAFREGIONAL_RATEBASEDRULE = "AWS::WAFRegional::RateBasedRule"
    AWS_WAFREGIONAL_RULE = "AWS::WAFRegional::Rule"
    AWS_WAFREGIONAL_RULEGROUP = "AWS::WAFRegional::RuleGroup"
    AWS_WAFREGIONAL_WEBACL = "AWS::WAFRegional::WebACL"
    AWS_CLOUDFRONT_DISTRIBUTION = "AWS::CloudFront::Distribution"
    AWS_CLOUDFRONT_STREAMINGDISTRIBUTION = "AWS::CloudFront::StreamingDistribution"
    AWS_LAMBDA_FUNCTION = "AWS::Lambda::Function"
    AWS_NETWORKFIREWALL_FIREWALL = "AWS::NetworkFirewall::Firewall"
    AWS_NETWORKFIREWALL_FIREWALLPOLICY = "AWS::NetworkFirewall::FirewallPolicy"
    AWS_NETWORKFIREWALL_RULEGROUP = "AWS::NetworkFirewall::RuleGroup"
    AWS_ELASTICBEANSTALK_APPLICATION = "AWS::ElasticBeanstalk::Application"
    AWS_ELASTICBEANSTALK_APPLICATIONVERSION = "AWS::ElasticBeanstalk::ApplicationVersion"
    AWS_ELASTICBEANSTALK_ENVIRONMENT = "AWS::ElasticBeanstalk::Environment"
    AWS_WAFV2_WEBACL = "AWS::WAFv2::WebACL"
    AWS_WAFV2_RULEGROUP = "AWS::WAFv2::RuleGroup"
    AWS_WAFV2_IPSET = "AWS::WAFv2::IPSet"
    AWS_WAFV2_REGEXPATTERNSET = "AWS::WAFv2::RegexPatternSet"
    AWS_WAFV2_MANAGEDRULESET = "AWS::WAFv2::ManagedRuleSet"
    AWS_XRAY_ENCRYPTIONCONFIG = "AWS::XRay::EncryptionConfig"
    AWS_SSM_ASSOCIATIONCOMPLIANCE = "AWS::SSM::AssociationCompliance"
    AWS_SSM_PATCHCOMPLIANCE = "AWS::SSM::PatchCompliance"
    AWS_SHIELD_PROTECTION = "AWS::Shield::Protection"
    AWS_SHIELDREGIONAL_PROTECTION = "AWS::ShieldRegional::Protection"
    AWS_CONFIG_CONFORMANCEPACKCOMPLIANCE = "AWS::Config::ConformancePackCompliance"
    AWS_CONFIG_RESOURCECOMPLIANCE = "AWS::Config::ResourceCompliance"
    AWS_APIGATEWAY_STAGE = "AWS::ApiGateway::Stage"
    AWS_APIGATEWAY_RESTAPI = "AWS::ApiGateway::RestApi"
    AWS_APIGATEWAYV2_STAGE = "AWS::ApiGatewayV2::Stage"
    AWS_APIGATEWAYV2_API = "AWS::ApiGatewayV2::Api"
    AWS_CODEPIPELINE_PIPELINE = "AWS::CodePipeline::Pipeline"
    AWS_SERVICECATALOG_CLOUDFORMATIONPROVISIONEDPRODUCT = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"
    AWS_SERVICECATALOG_CLOUDFORMATIONPRODUCT = "AWS::ServiceCatalog::CloudFormationProduct"
    AWS_SERVICECATALOG_PORTFOLIO = "AWS::ServiceCatalog::Portfolio"
    AWS_SQS_QUEUE = "AWS::SQS::Queue"
    AWS_KMS_KEY = "AWS::KMS::Key"
    AWS_QLDB_LEDGER = "AWS::QLDB::Ledger"
    AWS_SECRETSMANAGER_SECRET = "AWS::SecretsManager::Secret"
    AWS_SNS_TOPIC = "AWS::SNS::Topic"
    AWS_SSM_FILEDATA = "AWS::SSM::FileData"
    AWS_BACKUP_BACKUPPLAN = "AWS::Backup::BackupPlan"
    AWS_BACKUP_BACKUPSELECTION = "AWS::Backup::BackupSelection"
    AWS_BACKUP_BACKUPVAULT = "AWS::Backup::BackupVault"
    AWS_BACKUP_RECOVERYPOINT = "AWS::Backup::RecoveryPoint"
    AWS_ECR_REPOSITORY = "AWS::ECR::Repository"
    AWS_ECS_CLUSTER = "AWS::ECS::Cluster"
    AWS_ECS_SERVICE = "AWS::ECS::Service"
    AWS_ECS_TASKDEFINITION = "AWS::ECS::TaskDefinition"
    AWS_EFS_ACCESSPOINT = "AWS::EFS::AccessPoint"
    AWS_EFS_FILESYSTEM = "AWS::EFS::FileSystem"
    AWS_EKS_CLUSTER = "AWS::EKS::Cluster"
    AWS_OPENSEARCH_DOMAIN = "AWS::OpenSearch::Domain"
    AWS_EC2_TRANSITGATEWAY = "AWS::EC2::TransitGateway"
    AWS_KINESIS_STREAM = "AWS::Kinesis::Stream"
    AWS_KINESIS_STREAMCONSUMER = "AWS::Kinesis::StreamConsumer"
    AWS_CODEDEPLOY_APPLICATION = "AWS::CodeDeploy::Application"
    AWS_CODEDEPLOY_DEPLOYMENTCONFIG = "AWS::CodeDeploy::DeploymentConfig"
    AWS_CODEDEPLOY_DEPLOYMENTGROUP = "AWS::CodeDeploy::DeploymentGroup"
    AWS_EC2_LAUNCHTEMPLATE = "AWS::EC2::LaunchTemplate"
    AWS_ECR_PUBLICREPOSITORY = "AWS::ECR::PublicRepository"
    AWS_GUARDDUTY_DETECTOR = "AWS::GuardDuty::Detector"
    AWS_EMR_SECURITYCONFIGURATION = "AWS::EMR::SecurityConfiguration"
    AWS_SAGEMAKER_CODEREPOSITORY = "AWS::SageMaker::CodeRepository"
    AWS_ROUTE53RESOLVER_RESOLVERENDPOINT = "AWS::Route53Resolver::ResolverEndpoint"
    AWS_ROUTE53RESOLVER_RESOLVERRULE = "AWS::Route53Resolver::ResolverRule"
    AWS_ROUTE53RESOLVER_RESOLVERRULEASSOCIATION = "AWS::Route53Resolver::ResolverRuleAssociation"
    AWS_DMS_REPLICATIONSUBNETGROUP = "AWS::DMS::ReplicationSubnetGroup"
    AWS_DMS_EVENTSUBSCRIPTION = "AWS::DMS::EventSubscription"
    AWS_MSK_CLUSTER = "AWS::MSK::Cluster"
    AWS_STEPFUNCTIONS_ACTIVITY = "AWS::StepFunctions::Activity"
    AWS_WORKSPACES_WORKSPACE = "AWS::WorkSpaces::Workspace"
    AWS_WORKSPACES_CONNECTIONALIAS = "AWS::WorkSpaces::ConnectionAlias"
    AWS_SAGEMAKER_MODEL = "AWS::SageMaker::Model"
    AWS_ELASTICLOADBALANCINGV2_LISTENER = "AWS::ElasticLoadBalancingV2::Listener"
    AWS_STEPFUNCTIONS_STATEMACHINE = "AWS::StepFunctions::StateMachine"
    AWS_BATCH_JOBQUEUE = "AWS::Batch::JobQueue"
    AWS_BATCH_COMPUTEENVIRONMENT = "AWS::Batch::ComputeEnvironment"
    AWS_ACCESSANALYZER_ANALYZER = "AWS::AccessAnalyzer::Analyzer"
    AWS_ATHENA_WORKGROUP = "AWS::Athena::WorkGroup"
    AWS_ATHENA_DATACATALOG = "AWS::Athena::DataCatalog"
    AWS_DETECTIVE_GRAPH = "AWS::Detective::Graph"
    AWS_GLOBALACCELERATOR_ACCELERATOR = "AWS::GlobalAccelerator::Accelerator"
    AWS_GLOBALACCELERATOR_ENDPOINTGROUP = "AWS::GlobalAccelerator::EndpointGroup"
    AWS_GLOBALACCELERATOR_LISTENER = "AWS::GlobalAccelerator::Listener"
    AWS_EC2_TRANSITGATEWAYATTACHMENT = "AWS::EC2::TransitGatewayAttachment"
    AWS_EC2_TRANSITGATEWAYROUTETABLE = "AWS::EC2::TransitGatewayRouteTable"
    AWS_DMS_CERTIFICATE = "AWS::DMS::Certificate"
    AWS_APPCONFIG_APPLICATION = "AWS::AppConfig::Application"
    AWS_APPSYNC_GRAPHQLAPI = "AWS::AppSync::GraphQLApi"
    AWS_DATASYNC_LOCATIONSMB = "AWS::DataSync::LocationSMB"
    AWS_DATASYNC_LOCATIONFSXLUSTRE = "AWS::DataSync::LocationFSxLustre"
    AWS_DATASYNC_LOCATIONS3 = "AWS::DataSync::LocationS3"
    AWS_DATASYNC_LOCATIONEFS = "AWS::DataSync::LocationEFS"
    AWS_DATASYNC_TASK = "AWS::DataSync::Task"
    AWS_DATASYNC_LOCATIONNFS = "AWS::DataSync::LocationNFS"
    AWS_EC2_NETWORKINSIGHTSACCESSSCOPEANALYSIS = "AWS::EC2::NetworkInsightsAccessScopeAnalysis"
    AWS_EKS_FARGATEPROFILE = "AWS::EKS::FargateProfile"
    AWS_GLUE_JOB = "AWS::Glue::Job"
    AWS_GUARDDUTY_THREATINTELSET = "AWS::GuardDuty::ThreatIntelSet"
    AWS_GUARDDUTY_IPSET = "AWS::GuardDuty::IPSet"
    AWS_SAGEMAKER_WORKTEAM = "AWS::SageMaker::Workteam"
    AWS_SAGEMAKER_NOTEBOOKINSTANCELIFECYCLECONFIG = "AWS::SageMaker::NotebookInstanceLifecycleConfig"
    AWS_SERVICEDISCOVERY_SERVICE = "AWS::ServiceDiscovery::Service"
    AWS_SERVICEDISCOVERY_PUBLICDNSNAMESPACE = "AWS::ServiceDiscovery::PublicDnsNamespace"
    AWS_SES_CONTACTLIST = "AWS::SES::ContactList"
    AWS_SES_CONFIGURATIONSET = "AWS::SES::ConfigurationSet"
    AWS_ROUTE53_HOSTEDZONE = "AWS::Route53::HostedZone"
    AWS_IOTEVENTS_INPUT = "AWS::IoTEvents::Input"
    AWS_IOTEVENTS_DETECTORMODEL = "AWS::IoTEvents::DetectorModel"
    AWS_IOTEVENTS_ALARMMODEL = "AWS::IoTEvents::AlarmModel"
    AWS_SERVICEDISCOVERY_HTTPNAMESPACE = "AWS::ServiceDiscovery::HttpNamespace"
    AWS_EVENTS_EVENTBUS = "AWS::Events::EventBus"
    AWS_IMAGEBUILDER_CONTAINERRECIPE = "AWS::ImageBuilder::ContainerRecipe"
    AWS_IMAGEBUILDER_DISTRIBUTIONCONFIGURATION = "AWS::ImageBuilder::DistributionConfiguration"
    AWS_IMAGEBUILDER_INFRASTRUCTURECONFIGURATION = "AWS::ImageBuilder::InfrastructureConfiguration"
    AWS_DATASYNC_LOCATIONOBJECTSTORAGE = "AWS::DataSync::LocationObjectStorage"
    AWS_DATASYNC_LOCATIONHDFS = "AWS::DataSync::LocationHDFS"
    AWS_GLUE_CLASSIFIER = "AWS::Glue::Classifier"
    AWS_ROUTE53RECOVERYREADINESS_CELL = "AWS::Route53RecoveryReadiness::Cell"
    AWS_ROUTE53RECOVERYREADINESS_READINESSCHECK = "AWS::Route53RecoveryReadiness::ReadinessCheck"
    AWS_ECR_REGISTRYPOLICY = "AWS::ECR::RegistryPolicy"
    AWS_BACKUP_REPORTPLAN = "AWS::Backup::ReportPlan"
    AWS_LIGHTSAIL_CERTIFICATE = "AWS::Lightsail::Certificate"
    AWS_RUM_APPMONITOR = "AWS::RUM::AppMonitor"
    AWS_EVENTS_ENDPOINT = "AWS::Events::Endpoint"
    AWS_SES_RECEIPTRULESET = "AWS::SES::ReceiptRuleSet"
    AWS_EVENTS_ARCHIVE = "AWS::Events::Archive"
    AWS_EVENTS_APIDESTINATION = "AWS::Events::ApiDestination"
    AWS_LIGHTSAIL_DISK = "AWS::Lightsail::Disk"
    AWS_FIS_EXPERIMENTTEMPLATE = "AWS::FIS::ExperimentTemplate"
    AWS_DATASYNC_LOCATIONFSXWINDOWS = "AWS::DataSync::LocationFSxWindows"
    AWS_SES_RECEIPTFILTER = "AWS::SES::ReceiptFilter"
    AWS_GUARDDUTY_FILTER = "AWS::GuardDuty::Filter"
    AWS_SES_TEMPLATE = "AWS::SES::Template"
    AWS_AMAZONMQ_BROKER = "AWS::AmazonMQ::Broker"
    AWS_APPCONFIG_ENVIRONMENT = "AWS::AppConfig::Environment"
    AWS_APPCONFIG_CONFIGURATIONPROFILE = "AWS::AppConfig::ConfigurationProfile"
    AWS_CLOUD9_ENVIRONMENTEC2 = "AWS::Cloud9::EnvironmentEC2"
    AWS_EVENTSCHEMAS_REGISTRY = "AWS::EventSchemas::Registry"
    AWS_EVENTSCHEMAS_REGISTRYPOLICY = "AWS::EventSchemas::RegistryPolicy"
    AWS_EVENTSCHEMAS_DISCOVERER = "AWS::EventSchemas::Discoverer"
    AWS_FRAUDDETECTOR_LABEL = "AWS::FraudDetector::Label"
    AWS_FRAUDDETECTOR_ENTITYTYPE = "AWS::FraudDetector::EntityType"
    AWS_FRAUDDETECTOR_VARIABLE = "AWS::FraudDetector::Variable"
    AWS_FRAUDDETECTOR_OUTCOME = "AWS::FraudDetector::Outcome"
    AWS_IOT_AUTHORIZER = "AWS::IoT::Authorizer"
    AWS_IOT_SECURITYPROFILE = "AWS::IoT::SecurityProfile"
    AWS_IOT_ROLEALIAS = "AWS::IoT::RoleAlias"
    AWS_IOT_DIMENSION = "AWS::IoT::Dimension"
    AWS_IOTANALYTICS_DATASTORE = "AWS::IoTAnalytics::Datastore"
    AWS_LIGHTSAIL_BUCKET = "AWS::Lightsail::Bucket"
    AWS_LIGHTSAIL_STATICIP = "AWS::Lightsail::StaticIp"
    AWS_MEDIAPACKAGE_PACKAGINGGROUP = "AWS::MediaPackage::PackagingGroup"
    AWS_ROUTE53RECOVERYREADINESS_RECOVERYGROUP = "AWS::Route53RecoveryReadiness::RecoveryGroup"
    AWS_RESILIENCEHUB_RESILIENCYPOLICY = "AWS::ResilienceHub::ResiliencyPolicy"
    AWS_TRANSFER_WORKFLOW = "AWS::Transfer::Workflow"
    AWS_EKS_IDENTITYPROVIDERCONFIG = "AWS::EKS::IdentityProviderConfig"
    AWS_EKS_ADDON = "AWS::EKS::Addon"
    AWS_GLUE_MLTRANSFORM = "AWS::Glue::MLTransform"
    AWS_IOT_POLICY = "AWS::IoT::Policy"
    AWS_IOT_MITIGATIONACTION = "AWS::IoT::MitigationAction"
    AWS_IOTTWINMAKER_WORKSPACE = "AWS::IoTTwinMaker::Workspace"
    AWS_IOTTWINMAKER_ENTITY = "AWS::IoTTwinMaker::Entity"
    AWS_IOTANALYTICS_DATASET = "AWS::IoTAnalytics::Dataset"
    AWS_IOTANALYTICS_PIPELINE = "AWS::IoTAnalytics::Pipeline"
    AWS_IOTANALYTICS_CHANNEL = "AWS::IoTAnalytics::Channel"
    AWS_IOTSITEWISE_DASHBOARD = "AWS::IoTSiteWise::Dashboard"
    AWS_IOTSITEWISE_PROJECT = "AWS::IoTSiteWise::Project"
    AWS_IOTSITEWISE_PORTAL = "AWS::IoTSiteWise::Portal"
    AWS_IOTSITEWISE_ASSETMODEL = "AWS::IoTSiteWise::AssetModel"
    AWS_IVS_CHANNEL = "AWS::IVS::Channel"
    AWS_IVS_RECORDINGCONFIGURATION = "AWS::IVS::RecordingConfiguration"
    AWS_IVS_PLAYBACKKEYPAIR = "AWS::IVS::PlaybackKeyPair"
    AWS_KINESISANALYTICSV2_APPLICATION = "AWS::KinesisAnalyticsV2::Application"
    AWS_RDS_GLOBALCLUSTER = "AWS::RDS::GlobalCluster"
    AWS_S3_MULTIREGIONACCESSPOINT = "AWS::S3::MultiRegionAccessPoint"
    AWS_DEVICEFARM_TESTGRIDPROJECT = "AWS::DeviceFarm::TestGridProject"
    AWS_BUDGETS_BUDGETSACTION = "AWS::Budgets::BudgetsAction"
    AWS_LEX_BOT = "AWS::Lex::Bot"
    AWS_CODEGURUREVIEWER_REPOSITORYASSOCIATION = "AWS::CodeGuruReviewer::RepositoryAssociation"
    AWS_IOT_CUSTOMMETRIC = "AWS::IoT::CustomMetric"
    AWS_ROUTE53RESOLVER_FIREWALLDOMAINLIST = "AWS::Route53Resolver::FirewallDomainList"
    AWS_ROBOMAKER_ROBOTAPPLICATIONVERSION = "AWS::RoboMaker::RobotApplicationVersion"
    AWS_EC2_TRAFFICMIRRORSESSION = "AWS::EC2::TrafficMirrorSession"
    AWS_IOTSITEWISE_GATEWAY = "AWS::IoTSiteWise::Gateway"
    AWS_LEX_BOTALIAS = "AWS::Lex::BotAlias"
    AWS_LOOKOUTMETRICS_ALERT = "AWS::LookoutMetrics::Alert"
    AWS_IOT_ACCOUNTAUDITCONFIGURATION = "AWS::IoT::AccountAuditConfiguration"
    AWS_EC2_TRAFFICMIRRORTARGET = "AWS::EC2::TrafficMirrorTarget"
    AWS_S3_STORAGELENS = "AWS::S3::StorageLens"
    AWS_IOT_SCHEDULEDAUDIT = "AWS::IoT::ScheduledAudit"
    AWS_EVENTS_CONNECTION = "AWS::Events::Connection"
    AWS_EVENTSCHEMAS_SCHEMA = "AWS::EventSchemas::Schema"
    AWS_MEDIAPACKAGE_PACKAGINGCONFIGURATION = "AWS::MediaPackage::PackagingConfiguration"
    AWS_KINESISVIDEO_SIGNALINGCHANNEL = "AWS::KinesisVideo::SignalingChannel"
    AWS_APPSTREAM_DIRECTORYCONFIG = "AWS::AppStream::DirectoryConfig"
    AWS_LOOKOUTVISION_PROJECT = "AWS::LookoutVision::Project"
    AWS_ROUTE53RECOVERYCONTROL_CLUSTER = "AWS::Route53RecoveryControl::Cluster"
    AWS_ROUTE53RECOVERYCONTROL_SAFETYRULE = "AWS::Route53RecoveryControl::SafetyRule"
    AWS_ROUTE53RECOVERYCONTROL_CONTROLPANEL = "AWS::Route53RecoveryControl::ControlPanel"
    AWS_ROUTE53RECOVERYCONTROL_ROUTINGCONTROL = "AWS::Route53RecoveryControl::RoutingControl"
    AWS_ROUTE53RECOVERYREADINESS_RESOURCESET = "AWS::Route53RecoveryReadiness::ResourceSet"
    AWS_ROBOMAKER_SIMULATIONAPPLICATION = "AWS::RoboMaker::SimulationApplication"
    AWS_ROBOMAKER_ROBOTAPPLICATION = "AWS::RoboMaker::RobotApplication"
    AWS_HEALTHLAKE_FHIRDATASTORE = "AWS::HealthLake::FHIRDatastore"
    AWS_PINPOINT_SEGMENT = "AWS::Pinpoint::Segment"
    AWS_PINPOINT_APPLICATIONSETTINGS = "AWS::Pinpoint::ApplicationSettings"
    AWS_EVENTS_RULE = "AWS::Events::Rule"
    AWS_EC2_DHCPOPTIONS = "AWS::EC2::DHCPOptions"
    AWS_EC2_NETWORKINSIGHTSPATH = "AWS::EC2::NetworkInsightsPath"
    AWS_EC2_TRAFFICMIRRORFILTER = "AWS::EC2::TrafficMirrorFilter"
    AWS_EC2_IPAM = "AWS::EC2::IPAM"
    AWS_IOTTWINMAKER_SCENE = "AWS::IoTTwinMaker::Scene"
    AWS_NETWORKMANAGER_TRANSITGATEWAYREGISTRATION = "AWS::NetworkManager::TransitGatewayRegistration"
    AWS_CUSTOMERPROFILES_DOMAIN = "AWS::CustomerProfiles::Domain"
    AWS_AUTOSCALING_WARMPOOL = "AWS::AutoScaling::WarmPool"
    AWS_CONNECT_PHONENUMBER = "AWS::Connect::PhoneNumber"
    AWS_APPCONFIG_DEPLOYMENTSTRATEGY = "AWS::AppConfig::DeploymentStrategy"
    AWS_APPFLOW_FLOW = "AWS::AppFlow::Flow"
    AWS_AUDITMANAGER_ASSESSMENT = "AWS::AuditManager::Assessment"
    AWS_CLOUDWATCH_METRICSTREAM = "AWS::CloudWatch::MetricStream"
    AWS_DEVICEFARM_INSTANCEPROFILE = "AWS::DeviceFarm::InstanceProfile"
    AWS_DEVICEFARM_PROJECT = "AWS::DeviceFarm::Project"
    AWS_EC2_EC2FLEET = "AWS::EC2::EC2Fleet"
    AWS_EC2_SUBNETROUTETABLEASSOCIATION = "AWS::EC2::SubnetRouteTableAssociation"
    AWS_ECR_PULLTHROUGHCACHERULE = "AWS::ECR::PullThroughCacheRule"
    AWS_GROUNDSTATION_CONFIG = "AWS::GroundStation::Config"
    AWS_IMAGEBUILDER_IMAGEPIPELINE = "AWS::ImageBuilder::ImagePipeline"
    AWS_IOT_FLEETMETRIC = "AWS::IoT::FleetMetric"
    AWS_IOTWIRELESS_SERVICEPROFILE = "AWS::IoTWireless::ServiceProfile"
    AWS_NETWORKMANAGER_DEVICE = "AWS::NetworkManager::Device"
    AWS_NETWORKMANAGER_GLOBALNETWORK = "AWS::NetworkManager::GlobalNetwork"
    AWS_NETWORKMANAGER_LINK = "AWS::NetworkManager::Link"
    AWS_NETWORKMANAGER_SITE = "AWS::NetworkManager::Site"
    AWS_PANORAMA_PACKAGE = "AWS::Panorama::Package"
    AWS_PINPOINT_APP = "AWS::Pinpoint::App"
    AWS_REDSHIFT_SCHEDULEDACTION = "AWS::Redshift::ScheduledAction"
    AWS_ROUTE53RESOLVER_FIREWALLRULEGROUPASSOCIATION = "AWS::Route53Resolver::FirewallRuleGroupAssociation"
    AWS_SAGEMAKER_APPIMAGECONFIG = "AWS::SageMaker::AppImageConfig"
    AWS_SAGEMAKER_IMAGE = "AWS::SageMaker::Image"
    AWS_ECS_TASKSET = "AWS::ECS::TaskSet"
    AWS_CASSANDRA_KEYSPACE = "AWS::Cassandra::Keyspace"
    AWS_SIGNER_SIGNINGPROFILE = "AWS::Signer::SigningProfile"
    AWS_AMPLIFY_APP = "AWS::Amplify::App"
    AWS_APPMESH_VIRTUALNODE = "AWS::AppMesh::VirtualNode"
    AWS_APPMESH_VIRTUALSERVICE = "AWS::AppMesh::VirtualService"
    AWS_APPRUNNER_VPCCONNECTOR = "AWS::AppRunner::VpcConnector"
    AWS_APPSTREAM_APPLICATION = "AWS::AppStream::Application"
    AWS_CODEARTIFACT_REPOSITORY = "AWS::CodeArtifact::Repository"
    AWS_EC2_PREFIXLIST = "AWS::EC2::PrefixList"
    AWS_EC2_SPOTFLEET = "AWS::EC2::SpotFleet"
    AWS_EVIDENTLY_PROJECT = "AWS::Evidently::Project"
    AWS_FORECAST_DATASET = "AWS::Forecast::Dataset"
    AWS_IAM_SAMLPROVIDER = "AWS::IAM::SAMLProvider"
    AWS_IAM_SERVERCERTIFICATE = "AWS::IAM::ServerCertificate"
    AWS_PINPOINT_CAMPAIGN = "AWS::Pinpoint::Campaign"
    AWS_PINPOINT_INAPPTEMPLATE = "AWS::Pinpoint::InAppTemplate"
    AWS_SAGEMAKER_DOMAIN = "AWS::SageMaker::Domain"
    AWS_TRANSFER_AGREEMENT = "AWS::Transfer::Agreement"
    AWS_TRANSFER_CONNECTOR = "AWS::Transfer::Connector"
    AWS_KINESISFIREHOSE_DELIVERYSTREAM = "AWS::KinesisFirehose::DeliveryStream"
    AWS_AMPLIFY_BRANCH = "AWS::Amplify::Branch"
    AWS_APPINTEGRATIONS_EVENTINTEGRATION = "AWS::AppIntegrations::EventIntegration"
    AWS_APPMESH_ROUTE = "AWS::AppMesh::Route"
    AWS_ATHENA_PREPAREDSTATEMENT = "AWS::Athena::PreparedStatement"
    AWS_EC2_IPAMSCOPE = "AWS::EC2::IPAMScope"
    AWS_EVIDENTLY_LAUNCH = "AWS::Evidently::Launch"
    AWS_FORECAST_DATASETGROUP = "AWS::Forecast::DatasetGroup"
    AWS_GREENGRASSV2_COMPONENTVERSION = "AWS::GreengrassV2::ComponentVersion"
    AWS_GROUNDSTATION_MISSIONPROFILE = "AWS::GroundStation::MissionProfile"
    AWS_MEDIACONNECT_FLOWENTITLEMENT = "AWS::MediaConnect::FlowEntitlement"
    AWS_MEDIACONNECT_FLOWVPCINTERFACE = "AWS::MediaConnect::FlowVpcInterface"
    AWS_MEDIATAILOR_PLAYBACKCONFIGURATION = "AWS::MediaTailor::PlaybackConfiguration"
    AWS_MSK_CONFIGURATION = "AWS::MSK::Configuration"
    AWS_PERSONALIZE_DATASET = "AWS::Personalize::Dataset"
    AWS_PERSONALIZE_SCHEMA = "AWS::Personalize::Schema"
    AWS_PERSONALIZE_SOLUTION = "AWS::Personalize::Solution"
    AWS_PINPOINT_EMAILTEMPLATE = "AWS::Pinpoint::EmailTemplate"
    AWS_PINPOINT_EVENTSTREAM = "AWS::Pinpoint::EventStream"
    AWS_RESILIENCEHUB_APP = "AWS::ResilienceHub::App"
    AWS_ACMPCA_CERTIFICATEAUTHORITY = "AWS::ACMPCA::CertificateAuthority"
    AWS_APPCONFIG_HOSTEDCONFIGURATIONVERSION = "AWS::AppConfig::HostedConfigurationVersion"
    AWS_APPMESH_VIRTUALGATEWAY = "AWS::AppMesh::VirtualGateway"
    AWS_APPMESH_VIRTUALROUTER = "AWS::AppMesh::VirtualRouter"
    AWS_APPRUNNER_SERVICE = "AWS::AppRunner::Service"
    AWS_CUSTOMERPROFILES_OBJECTTYPE = "AWS::CustomerProfiles::ObjectType"
    AWS_DMS_ENDPOINT = "AWS::DMS::Endpoint"
    AWS_EC2_CAPACITYRESERVATION = "AWS::EC2::CapacityReservation"
    AWS_EC2_CLIENTVPNENDPOINT = "AWS::EC2::ClientVpnEndpoint"
    AWS_KENDRA_INDEX = "AWS::Kendra::Index"
    AWS_KINESISVIDEO_STREAM = "AWS::KinesisVideo::Stream"
    AWS_LOGS_DESTINATION = "AWS::Logs::Destination"
    AWS_PINPOINT_EMAILCHANNEL = "AWS::Pinpoint::EmailChannel"
    AWS_S3_ACCESSPOINT = "AWS::S3::AccessPoint"
    AWS_NETWORKMANAGER_CUSTOMERGATEWAYASSOCIATION = "AWS::NetworkManager::CustomerGatewayAssociation"
    AWS_NETWORKMANAGER_LINKASSOCIATION = "AWS::NetworkManager::LinkAssociation"
    AWS_IOTWIRELESS_MULTICASTGROUP = "AWS::IoTWireless::MulticastGroup"
    AWS_PERSONALIZE_DATASETGROUP = "AWS::Personalize::DatasetGroup"
    AWS_IOTTWINMAKER_COMPONENTTYPE = "AWS::IoTTwinMaker::ComponentType"
    AWS_CODEBUILD_REPORTGROUP = "AWS::CodeBuild::ReportGroup"
    AWS_SAGEMAKER_FEATUREGROUP = "AWS::SageMaker::FeatureGroup"
    AWS_MSK_BATCHSCRAMSECRET = "AWS::MSK::BatchScramSecret"
    AWS_APPSTREAM_STACK = "AWS::AppStream::Stack"
    AWS_IOT_JOBTEMPLATE = "AWS::IoT::JobTemplate"
    AWS_IOTWIRELESS_FUOTATASK = "AWS::IoTWireless::FuotaTask"
    AWS_IOT_PROVISIONINGTEMPLATE = "AWS::IoT::ProvisioningTemplate"
    AWS_INSPECTORV2_FILTER = "AWS::InspectorV2::Filter"
    AWS_ROUTE53RESOLVER_RESOLVERQUERYLOGGINGCONFIGASSOCIATION = "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation"
    AWS_SERVICEDISCOVERY_INSTANCE = "AWS::ServiceDiscovery::Instance"
    AWS_TRANSFER_CERTIFICATE = "AWS::Transfer::Certificate"
    AWS_MEDIACONNECT_FLOWSOURCE = "AWS::MediaConnect::FlowSource"
    AWS_APS_RULEGROUPSNAMESPACE = "AWS::APS::RuleGroupsNamespace"
    AWS_CODEGURUPROFILER_PROFILINGGROUP = "AWS::CodeGuruProfiler::ProfilingGroup"
    AWS_ROUTE53RESOLVER_RESOLVERQUERYLOGGINGCONFIG = "AWS::Route53Resolver::ResolverQueryLoggingConfig"
    AWS_BATCH_SCHEDULINGPOLICY = "AWS::Batch::SchedulingPolicy"
    AWS_ACMPCA_CERTIFICATEAUTHORITYACTIVATION = "AWS::ACMPCA::CertificateAuthorityActivation"
    AWS_APPMESH_GATEWAYROUTE = "AWS::AppMesh::GatewayRoute"
    AWS_APPMESH_MESH = "AWS::AppMesh::Mesh"
    AWS_CONNECT_INSTANCE = "AWS::Connect::Instance"
    AWS_CONNECT_QUICKCONNECT = "AWS::Connect::QuickConnect"
    AWS_EC2_CARRIERGATEWAY = "AWS::EC2::CarrierGateway"
    AWS_EC2_IPAMPOOL = "AWS::EC2::IPAMPool"
    AWS_EC2_TRANSITGATEWAYCONNECT = "AWS::EC2::TransitGatewayConnect"
    AWS_EC2_TRANSITGATEWAYMULTICASTDOMAIN = "AWS::EC2::TransitGatewayMulticastDomain"
    AWS_ECS_CAPACITYPROVIDER = "AWS::ECS::CapacityProvider"
    AWS_IAM_INSTANCEPROFILE = "AWS::IAM::InstanceProfile"
    AWS_IOT_CACERTIFICATE = "AWS::IoT::CACertificate"
    AWS_IOTTWINMAKER_SYNCJOB = "AWS::IoTTwinMaker::SyncJob"
    AWS_KAFKACONNECT_CONNECTOR = "AWS::KafkaConnect::Connector"
    AWS_LAMBDA_CODESIGNINGCONFIG = "AWS::Lambda::CodeSigningConfig"
    AWS_NETWORKMANAGER_CONNECTPEER = "AWS::NetworkManager::ConnectPeer"
    AWS_RESOURCEEXPLORER2_INDEX = "AWS::ResourceExplorer2::Index"
    AWS_APPSTREAM_FLEET = "AWS::AppStream::Fleet"
    AWS_COGNITO_USERPOOL = "AWS::Cognito::UserPool"
    AWS_COGNITO_USERPOOLCLIENT = "AWS::Cognito::UserPoolClient"
    AWS_COGNITO_USERPOOLGROUP = "AWS::Cognito::UserPoolGroup"
    AWS_EC2_NETWORKINSIGHTSACCESSSCOPE = "AWS::EC2::NetworkInsightsAccessScope"
    AWS_EC2_NETWORKINSIGHTSANALYSIS = "AWS::EC2::NetworkInsightsAnalysis"
    AWS_GRAFANA_WORKSPACE = "AWS::Grafana::Workspace"
    AWS_GROUNDSTATION_DATAFLOWENDPOINTGROUP = "AWS::GroundStation::DataflowEndpointGroup"
    AWS_IMAGEBUILDER_IMAGERECIPE = "AWS::ImageBuilder::ImageRecipe"
    AWS_KMS_ALIAS = "AWS::KMS::Alias"
    AWS_M2_ENVIRONMENT = "AWS::M2::Environment"
    AWS_QUICKSIGHT_DATASOURCE = "AWS::QuickSight::DataSource"
    AWS_QUICKSIGHT_TEMPLATE = "AWS::QuickSight::Template"
    AWS_QUICKSIGHT_THEME = "AWS::QuickSight::Theme"
    AWS_RDS_OPTIONGROUP = "AWS::RDS::OptionGroup"
    AWS_REDSHIFT_ENDPOINTACCESS = "AWS::Redshift::EndpointAccess"
    AWS_ROUTE53RESOLVER_FIREWALLRULEGROUP = "AWS::Route53Resolver::FirewallRuleGroup"
    AWS_SSM_DOCUMENT = "AWS::SSM::Document"
    AWS_APPCONFIG_EXTENSIONASSOCIATION = "AWS::AppConfig::ExtensionAssociation"
    AWS_APPINTEGRATIONS_APPLICATION = "AWS::AppIntegrations::Application"
    AWS_APPSYNC_APICACHE = "AWS::AppSync::ApiCache"
    AWS_BEDROCK_GUARDRAIL = "AWS::Bedrock::Guardrail"
    AWS_BEDROCK_KNOWLEDGEBASE = "AWS::Bedrock::KnowledgeBase"
    AWS_COGNITO_IDENTITYPOOL = "AWS::Cognito::IdentityPool"
    AWS_CONNECT_RULE = "AWS::Connect::Rule"
    AWS_CONNECT_USER = "AWS::Connect::User"
    AWS_EC2_CLIENTVPNTARGETNETWORKASSOCIATION = "AWS::EC2::ClientVpnTargetNetworkAssociation"
    AWS_EC2_EIPASSOCIATION = "AWS::EC2::EIPAssociation"
    AWS_EC2_IPAMRESOURCEDISCOVERY = "AWS::EC2::IPAMResourceDiscovery"
    AWS_EC2_IPAMRESOURCEDISCOVERYASSOCIATION = "AWS::EC2::IPAMResourceDiscoveryAssociation"
    AWS_EC2_INSTANCECONNECTENDPOINT = "AWS::EC2::InstanceConnectEndpoint"
    AWS_EC2_SNAPSHOTBLOCKPUBLICACCESS = "AWS::EC2::SnapshotBlockPublicAccess"
    AWS_EC2_VPCBLOCKPUBLICACCESSEXCLUSION = "AWS::EC2::VPCBlockPublicAccessExclusion"
    AWS_EC2_VPCBLOCKPUBLICACCESSOPTIONS = "AWS::EC2::VPCBlockPublicAccessOptions"
    AWS_EC2_VPCENDPOINTCONNECTIONNOTIFICATION = "AWS::EC2::VPCEndpointConnectionNotification"
    AWS_EC2_VPNCONNECTIONROUTE = "AWS::EC2::VPNConnectionRoute"
    AWS_EVIDENTLY_SEGMENT = "AWS::Evidently::Segment"
    AWS_IAM_OIDCPROVIDER = "AWS::IAM::OIDCProvider"
    AWS_INSPECTORV2_ACTIVATION = "AWS::InspectorV2::Activation"
    AWS_MSK_CLUSTERPOLICY = "AWS::MSK::ClusterPolicy"
    AWS_MSK_VPCCONNECTION = "AWS::MSK::VpcConnection"
    AWS_MEDIACONNECT_GATEWAY = "AWS::MediaConnect::Gateway"
    AWS_MEMORYDB_SUBNETGROUP = "AWS::MemoryDB::SubnetGroup"
    AWS_OPENSEARCHSERVERLESS_COLLECTION = "AWS::OpenSearchServerless::Collection"
    AWS_OPENSEARCHSERVERLESS_VPCENDPOINT = "AWS::OpenSearchServerless::VpcEndpoint"
    AWS_REDSHIFT_ENDPOINTAUTHORIZATION = "AWS::Redshift::EndpointAuthorization"
    AWS_ROUTE53PROFILES_PROFILE = "AWS::Route53Profiles::Profile"
    AWS_S3_STORAGELENSGROUP = "AWS::S3::StorageLensGroup"
    AWS_S3EXPRESS_BUCKETPOLICY = "AWS::S3Express::BucketPolicy"
    AWS_S3EXPRESS_DIRECTORYBUCKET = "AWS::S3Express::DirectoryBucket"
    AWS_SAGEMAKER_INFERENCEEXPERIMENT = "AWS::SageMaker::InferenceExperiment"
    AWS_SECURITYHUB_STANDARD = "AWS::SecurityHub::Standard"
    AWS_TRANSFER_PROFILE = "AWS::Transfer::Profile"


class ResourceValueType:
    """ResourceValueType enum values."""

    RESOURCE_ID = "RESOURCE_ID"


class SortBy:
    """SortBy enum values."""

    SCORE = "SCORE"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


@dataclass
class Compliance(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPolicyDetails(PropertyType):
    ENABLE_DEBUG_LOG_DELIVERY = "EnableDebugLogDelivery"
    POLICY_TEXT = "PolicyText"
    POLICY_RUNTIME = "PolicyRuntime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_debug_log_delivery": "EnableDebugLogDelivery",
        "policy_text": "PolicyText",
        "policy_runtime": "PolicyRuntime",
    }

    enable_debug_log_delivery: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    policy_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationModeConfiguration(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, EvaluationMode, Ref, GetAtt, Sub]] = None


@dataclass
class Scope(PropertyType):
    COMPLIANCE_RESOURCE_ID = "ComplianceResourceId"
    TAG_KEY = "TagKey"
    COMPLIANCE_RESOURCE_TYPES = "ComplianceResourceTypes"
    TAG_VALUE = "TagValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compliance_resource_id": "ComplianceResourceId",
        "tag_key": "TagKey",
        "compliance_resource_types": "ComplianceResourceTypes",
        "tag_value": "TagValue",
    }

    compliance_resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    compliance_resource_types: Optional[Union[list[str], Ref]] = None
    tag_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    OWNER = "Owner"
    CUSTOM_POLICY_DETAILS = "CustomPolicyDetails"
    SOURCE_IDENTIFIER = "SourceIdentifier"
    SOURCE_DETAILS = "SourceDetails"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
        "custom_policy_details": "CustomPolicyDetails",
        "source_identifier": "SourceIdentifier",
        "source_details": "SourceDetails",
    }

    owner: Optional[Union[str, Owner, Ref, GetAtt, Sub]] = None
    custom_policy_details: Optional[CustomPolicyDetails] = None
    source_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_details: Optional[list[SourceDetail]] = None


@dataclass
class SourceDetail(PropertyType):
    EVENT_SOURCE = "EventSource"
    MAXIMUM_EXECUTION_FREQUENCY = "MaximumExecutionFrequency"
    MESSAGE_TYPE = "MessageType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_source": "EventSource",
        "maximum_execution_frequency": "MaximumExecutionFrequency",
        "message_type": "MessageType",
    }

    event_source: Optional[Union[str, EventSource, Ref, GetAtt, Sub]] = None
    maximum_execution_frequency: Optional[Union[str, MaximumExecutionFrequency, Ref, GetAtt, Sub]] = None
    message_type: Optional[Union[str, MessageType, Ref, GetAtt, Sub]] = None

