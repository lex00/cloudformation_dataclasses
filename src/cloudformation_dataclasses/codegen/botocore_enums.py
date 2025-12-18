"""
Botocore enum extraction for code generation.

This module extracts enum values from botocore service models and generates
Python constant classes for use in CloudFormation resource definitions.
"""

from __future__ import annotations

import re

try:
    from botocore.loaders import Loader
except ImportError:
    Loader = None  # type: ignore[misc, assignment]


# Mapping from CloudFormation service names to botocore service names
# CloudFormation uses PascalCase, botocore uses lowercase with hyphens
CF_TO_BOTOCORE_SERVICE: dict[str, str] = {
    "AccessAnalyzer": "accessanalyzer",
    "ACMPCA": "acm-pca",
    "AmazonMQ": "mq",
    "Amplify": "amplify",
    "ApiGateway": "apigateway",
    "ApiGatewayV2": "apigatewayv2",
    "AppConfig": "appconfig",
    "AppFlow": "appflow",
    "AppMesh": "appmesh",
    "AppRunner": "apprunner",
    "AppStream": "appstream",
    "AppSync": "appsync",
    "Athena": "athena",
    "AutoScaling": "autoscaling",
    "Backup": "backup",
    "Batch": "batch",
    "Budgets": "budgets",
    "CertificateManager": "acm",
    "Cloud9": "cloud9",
    "CloudFormation": "cloudformation",
    "CloudFront": "cloudfront",
    "CloudTrail": "cloudtrail",
    "CloudWatch": "cloudwatch",
    "CodeArtifact": "codeartifact",
    "CodeBuild": "codebuild",
    "CodeCommit": "codecommit",
    "CodeDeploy": "codedeploy",
    "CodePipeline": "codepipeline",
    "Cognito": "cognito-idp",
    "Comprehend": "comprehend",
    "Config": "config",
    "Connect": "connect",
    "DataBrew": "databrew",
    "DataPipeline": "datapipeline",
    "DAX": "dax",
    "Detective": "detective",
    "DirectoryService": "ds",
    "DLM": "dlm",
    "DMS": "dms",
    "DocDB": "docdb",
    "DynamoDB": "dynamodb",
    "EC2": "ec2",
    "ECR": "ecr",
    "ECS": "ecs",
    "EFS": "efs",
    "EKS": "eks",
    "ElastiCache": "elasticache",
    "ElasticBeanstalk": "elasticbeanstalk",
    "ElasticLoadBalancing": "elb",
    "ElasticLoadBalancingV2": "elbv2",
    "Elasticsearch": "es",
    "EMR": "emr",
    "Events": "events",
    "EventSchemas": "schemas",
    "Evidently": "evidently",
    "FinSpace": "finspace",
    "Firehose": "firehose",
    "FMS": "fms",
    "FraudDetector": "frauddetector",
    "FSx": "fsx",
    "GameLift": "gamelift",
    "GlobalAccelerator": "globalaccelerator",
    "Glue": "glue",
    "Greengrass": "greengrass",
    "GreengrassV2": "greengrassv2",
    "GuardDuty": "guardduty",
    "HealthLake": "healthlake",
    "IAM": "iam",
    "ImageBuilder": "imagebuilder",
    "Inspector": "inspector",
    "Inspector2": "inspector2",
    "IoT": "iot",
    "IoTAnalytics": "iotanalytics",
    "IoTEvents": "iotevents",
    "IoTFleetHub": "iotfleethub",
    "IoTSiteWise": "iotsitewise",
    "IoTThingsGraph": "iotthingsgraph",
    "IoTTwinMaker": "iottwinmaker",
    "IoTWireless": "iotwireless",
    "IVS": "ivs",
    "Kendra": "kendra",
    "Kinesis": "kinesis",
    "KinesisAnalytics": "kinesisanalytics",
    "KinesisAnalyticsV2": "kinesisanalyticsv2",
    "KinesisFirehose": "firehose",
    "KMS": "kms",
    "LakeFormation": "lakeformation",
    "Lambda": "lambda",
    "Lex": "lex-models",
    "LicenseManager": "license-manager",
    "Lightsail": "lightsail",
    "Location": "location",
    "Logs": "logs",
    "LookoutEquipment": "lookoutequipment",
    "LookoutMetrics": "lookoutmetrics",
    "LookoutVision": "lookoutvision",
    "Macie": "macie2",
    "ManagedBlockchain": "managedblockchain",
    "MediaConnect": "mediaconnect",
    "MediaConvert": "mediaconvert",
    "MediaLive": "medialive",
    "MediaPackage": "mediapackage",
    "MediaStore": "mediastore",
    "MemoryDB": "memorydb",
    "MSK": "kafka",
    "MWAA": "mwaa",
    "Neptune": "neptune",
    "NetworkFirewall": "network-firewall",
    "NetworkManager": "networkmanager",
    "NimbleStudio": "nimble",
    "OpenSearchService": "opensearch",
    "OpsWorks": "opsworks",
    "Organizations": "organizations",
    "Panorama": "panorama",
    "Personalize": "personalize",
    "Pinpoint": "pinpoint",
    "QLDB": "qldb",
    "QuickSight": "quicksight",
    "RAM": "ram",
    "RDS": "rds",
    "Redshift": "redshift",
    "RedshiftServerless": "redshift-serverless",
    "Rekognition": "rekognition",
    "ResilienceHub": "resiliencehub",
    "ResourceGroups": "resource-groups",
    "RoboMaker": "robomaker",
    "Route53": "route53",
    "Route53RecoveryControl": "route53-recovery-control-config",
    "Route53RecoveryReadiness": "route53-recovery-readiness",
    "Route53Resolver": "route53resolver",
    "S3": "s3",
    "S3ObjectLambda": "s3",
    "S3Outposts": "s3outposts",
    "SageMaker": "sagemaker",
    "Scheduler": "scheduler",
    "SecretsManager": "secretsmanager",
    "SecurityHub": "securityhub",
    "ServiceCatalog": "servicecatalog",
    "ServiceDiscovery": "servicediscovery",
    "SES": "ses",
    "SESv2": "sesv2",
    "Shield": "shield",
    "Signer": "signer",
    "SNS": "sns",
    "SQS": "sqs",
    "SSM": "ssm",
    "SSMContacts": "ssm-contacts",
    "SSMIncidents": "ssm-incidents",
    "SSO": "sso-admin",
    "StepFunctions": "stepfunctions",
    "StorageGateway": "storagegateway",
    "SupportApp": "support-app",
    "Synthetics": "synthetics",
    "Timestream": "timestream-write",
    "Transfer": "transfer",
    "WAF": "waf",
    "WAFRegional": "waf-regional",
    "WAFv2": "wafv2",
    "WorkSpaces": "workspaces",
    "XRay": "xray",
}


def cf_to_botocore_service(cf_service_name: str) -> str | None:
    """
    Map CloudFormation service name to botocore service name.

    Args:
        cf_service_name: CloudFormation service name (e.g., "DynamoDB", "S3")

    Returns:
        Botocore service name (e.g., "dynamodb", "s3") or None if no mapping exists
    """
    # Check explicit mapping first
    if cf_service_name in CF_TO_BOTOCORE_SERVICE:
        return CF_TO_BOTOCORE_SERVICE[cf_service_name]

    # Try lowercase conversion as fallback
    botocore_name = cf_service_name.lower()

    # Check if this service exists in botocore
    if Loader is None:
        return None

    loader = Loader()
    available = loader.list_available_services("service-2")
    if botocore_name in available:
        return botocore_name

    return None


def get_service_enums(cf_service_name: str) -> dict[str, list[str]]:
    """
    Get all enums for a CloudFormation service from botocore.

    Args:
        cf_service_name: CloudFormation service name (e.g., "DynamoDB", "S3")

    Returns:
        Dict mapping shape name to list of enum values
        e.g., {"KeyType": ["HASH", "RANGE"], "ProjectionType": ["ALL", "KEYS_ONLY", "INCLUDE"]}
    """
    if Loader is None:
        return {}

    botocore_name = cf_to_botocore_service(cf_service_name)
    if botocore_name is None:
        return {}

    try:
        loader = Loader()
        data = loader.load_service_model(botocore_name, "service-2")
    except Exception:
        return {}

    enums: dict[str, list[str]] = {}
    for name, shape in data.get("shapes", {}).items():
        if "enum" in shape:
            enums[name] = shape["enum"]

    return enums


def get_property_enum_mappings(cf_service_name: str) -> dict[tuple[str, str], str]:
    """
    Get mappings from (struct_name, property_name) to enum type for a service.

    This allows the generator to know which properties accept enum values,
    enabling type-safe enum support in generated code.

    Args:
        cf_service_name: CloudFormation service name (e.g., "DynamoDB", "S3")

    Returns:
        Dict mapping (structure_name, property_name) to enum type name
        e.g., {("KeySchemaElement", "KeyType"): "KeyType",
               ("AttributeDefinition", "AttributeType"): "ScalarAttributeType"}
    """
    if Loader is None:
        return {}

    botocore_name = cf_to_botocore_service(cf_service_name)
    if botocore_name is None:
        return {}

    try:
        loader = Loader()
        data = loader.load_service_model(botocore_name, "service-2")
    except Exception:
        return {}

    shapes = data.get("shapes", {})
    mappings: dict[tuple[str, str], str] = {}

    for shape_name, shape_def in shapes.items():
        if shape_def.get("type") != "structure":
            continue

        for member_name, member_info in shape_def.get("members", {}).items():
            member_shape = member_info.get("shape", "")
            member_shape_def = shapes.get(member_shape, {})
            if "enum" in member_shape_def:
                # Map (StructureName, MemberName) -> EnumTypeName
                mappings[(shape_name, member_name)] = member_shape

    return mappings


def to_python_identifier(value: str) -> str:
    """
    Convert an enum value to a valid Python identifier.

    Examples:
        "HASH" -> "HASH"
        "email-json" -> "EMAIL_JSON"
        "s3:ObjectCreated:*" -> "S3_OBJECT_CREATED_STAR"
        "AWS::EC2::Instance" -> "AWS_EC2_INSTANCE"
    """
    # Replace common separators with underscores
    result = re.sub(r"[-:./\s]+", "_", value)
    # Replace * with STAR
    result = result.replace("*", "STAR")
    # Remove any remaining invalid characters
    result = re.sub(r"[^a-zA-Z0-9_]", "", result)
    # Ensure it doesn't start with a number
    if result and result[0].isdigit():
        result = "_" + result
    # Convert to uppercase for constants
    result = result.upper()
    return result


def generate_enum_class(class_name: str, values: list[str]) -> str:
    """
    Generate a Python class for an enum.

    Args:
        class_name: Name of the class (e.g., "KeyType")
        values: List of enum values (e.g., ["HASH", "RANGE"])

    Returns:
        Python class definition as a string
    """
    lines = [f"class {class_name}:", f'    """{class_name} enum values."""', ""]

    for value in values:
        identifier = to_python_identifier(value)
        lines.append(f'    {identifier} = "{value}"')

    return "\n".join(lines)


def generate_enum_aliases(class_name: str, values: list[str]) -> list[str]:
    """
    Generate module-level aliases for enum values.

    Args:
        class_name: Name of the class (e.g., "KeyType")
        values: List of enum values (e.g., ["HASH", "RANGE"])

    Returns:
        List of alias assignment lines
    """
    aliases = []
    for value in values:
        identifier = to_python_identifier(value)
        aliases.append(f"{identifier} = {class_name}.{identifier}")
    return aliases


# Class name aliases for backward compatibility or convenience
# Maps botocore shape name -> alias name
CLASS_ALIASES: dict[str, str] = {
    "ScalarAttributeType": "AttributeType",  # DynamoDB
}

# Mapping from CloudFormation struct names to botocore struct names
# Some CF names differ from botocore (e.g., KeySchema vs KeySchemaElement)
CF_TO_BOTOCORE_STRUCT: dict[str, str] = {
    "KeySchema": "KeySchemaElement",  # DynamoDB
}


def generate_service_enums(cf_service_name: str) -> tuple[str, str]:
    """
    Generate enum classes and aliases for a service.

    Args:
        cf_service_name: CloudFormation service name (e.g., "DynamoDB")

    Returns:
        Tuple of (classes_code, aliases_code)
    """
    enums = get_service_enums(cf_service_name)
    if not enums:
        return "", ""

    classes = []
    all_aliases = []
    class_aliases = []

    for name, values in sorted(enums.items()):
        # Generate class
        classes.append(generate_enum_class(name, values))

        # Generate aliases
        all_aliases.extend(generate_enum_aliases(name, values))

        # Add class alias if defined
        if name in CLASS_ALIASES:
            class_aliases.append(f"{CLASS_ALIASES[name]} = {name}")

    classes_code = "\n\n\n".join(classes)

    # Add class aliases before value aliases
    if class_aliases:
        all_aliases = class_aliases + [""] + all_aliases

    aliases_code = "\n".join(all_aliases)

    return classes_code, aliases_code
