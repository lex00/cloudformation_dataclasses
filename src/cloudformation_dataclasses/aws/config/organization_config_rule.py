"""PropertyTypes for AWS::Config::OrganizationConfigRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OrganizationCustomPolicyRuleMetadata(PropertyType):
    TAG_KEY_SCOPE = "TagKeyScope"
    TAG_VALUE_SCOPE = "TagValueScope"
    RUNTIME = "Runtime"
    POLICY_TEXT = "PolicyText"
    DESCRIPTION = "Description"
    RESOURCE_ID_SCOPE = "ResourceIdScope"
    ORGANIZATION_CONFIG_RULE_TRIGGER_TYPES = "OrganizationConfigRuleTriggerTypes"
    DEBUG_LOG_DELIVERY_ACCOUNTS = "DebugLogDeliveryAccounts"
    RESOURCE_TYPES_SCOPE = "ResourceTypesScope"
    MAXIMUM_EXECUTION_FREQUENCY = "MaximumExecutionFrequency"
    INPUT_PARAMETERS = "InputParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key_scope": "TagKeyScope",
        "tag_value_scope": "TagValueScope",
        "runtime": "Runtime",
        "policy_text": "PolicyText",
        "description": "Description",
        "resource_id_scope": "ResourceIdScope",
        "organization_config_rule_trigger_types": "OrganizationConfigRuleTriggerTypes",
        "debug_log_delivery_accounts": "DebugLogDeliveryAccounts",
        "resource_types_scope": "ResourceTypesScope",
        "maximum_execution_frequency": "MaximumExecutionFrequency",
        "input_parameters": "InputParameters",
    }

    tag_key_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_value_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_id_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organization_config_rule_trigger_types: Optional[Union[list[str], Ref]] = None
    debug_log_delivery_accounts: Optional[Union[list[str], Ref]] = None
    resource_types_scope: Optional[Union[list[str], Ref]] = None
    maximum_execution_frequency: Optional[Union[str, MaximumExecutionFrequency, Ref, GetAtt, Sub]] = None
    input_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OrganizationCustomRuleMetadata(PropertyType):
    TAG_KEY_SCOPE = "TagKeyScope"
    TAG_VALUE_SCOPE = "TagValueScope"
    DESCRIPTION = "Description"
    RESOURCE_ID_SCOPE = "ResourceIdScope"
    LAMBDA_FUNCTION_ARN = "LambdaFunctionArn"
    ORGANIZATION_CONFIG_RULE_TRIGGER_TYPES = "OrganizationConfigRuleTriggerTypes"
    RESOURCE_TYPES_SCOPE = "ResourceTypesScope"
    MAXIMUM_EXECUTION_FREQUENCY = "MaximumExecutionFrequency"
    INPUT_PARAMETERS = "InputParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key_scope": "TagKeyScope",
        "tag_value_scope": "TagValueScope",
        "description": "Description",
        "resource_id_scope": "ResourceIdScope",
        "lambda_function_arn": "LambdaFunctionArn",
        "organization_config_rule_trigger_types": "OrganizationConfigRuleTriggerTypes",
        "resource_types_scope": "ResourceTypesScope",
        "maximum_execution_frequency": "MaximumExecutionFrequency",
        "input_parameters": "InputParameters",
    }

    tag_key_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_value_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_id_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organization_config_rule_trigger_types: Optional[Union[list[str], Ref]] = None
    resource_types_scope: Optional[Union[list[str], Ref]] = None
    maximum_execution_frequency: Optional[Union[str, MaximumExecutionFrequency, Ref, GetAtt, Sub]] = None
    input_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OrganizationManagedRuleMetadata(PropertyType):
    TAG_KEY_SCOPE = "TagKeyScope"
    TAG_VALUE_SCOPE = "TagValueScope"
    DESCRIPTION = "Description"
    RESOURCE_ID_SCOPE = "ResourceIdScope"
    RULE_IDENTIFIER = "RuleIdentifier"
    RESOURCE_TYPES_SCOPE = "ResourceTypesScope"
    MAXIMUM_EXECUTION_FREQUENCY = "MaximumExecutionFrequency"
    INPUT_PARAMETERS = "InputParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key_scope": "TagKeyScope",
        "tag_value_scope": "TagValueScope",
        "description": "Description",
        "resource_id_scope": "ResourceIdScope",
        "rule_identifier": "RuleIdentifier",
        "resource_types_scope": "ResourceTypesScope",
        "maximum_execution_frequency": "MaximumExecutionFrequency",
        "input_parameters": "InputParameters",
    }

    tag_key_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_value_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_id_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_types_scope: Optional[Union[list[str], Ref]] = None
    maximum_execution_frequency: Optional[Union[str, MaximumExecutionFrequency, Ref, GetAtt, Sub]] = None
    input_parameters: Optional[Union[str, Ref, GetAtt, Sub]] = None

