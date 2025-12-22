"""SiteWebACL - AWS::WAFv2::WebACL resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteWebACLAllowAction:
    resource: wafv2.web_acl.AllowAction


@cloudformation_dataclass
class SiteWebACLDefaultAction:
    resource: wafv2.web_acl.DefaultAction
    allow = SiteWebACLAllowAction


@cloudformation_dataclass
class SiteWebACLVisibilityConfig:
    resource: wafv2.web_acl.VisibilityConfig
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForWebACLWithAMR'


@cloudformation_dataclass
class SiteWebACLOverrideAction:
    resource: wafv2.web_acl.OverrideAction
    none = {}


@cloudformation_dataclass
class SiteWebACLVisibilityConfig1:
    resource: wafv2.web_acl.VisibilityConfig
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForAMRCRS'


@cloudformation_dataclass
class SiteWebACLExcludedRule:
    resource: wafv2.web_acl.ExcludedRule
    name = 'NoUserAgent_HEADER'


@cloudformation_dataclass
class SiteWebACLManagedRuleGroupStatement:
    resource: wafv2.web_acl.ManagedRuleGroupStatement
    vendor_name = 'AWS'
    name = 'AWSManagedRulesCommonRuleSet'
    excluded_rules = [SiteWebACLExcludedRule]


@cloudformation_dataclass
class SiteWebACLStatement:
    resource: wafv2.web_acl.Statement
    managed_rule_group_statement = SiteWebACLManagedRuleGroupStatement


@cloudformation_dataclass
class SiteWebACLRule:
    resource: wafv2.web_acl.Rule
    name = 'AWS-AWSManagedRulesCommonRuleSet'
    priority = 0
    override_action = SiteWebACLOverrideAction
    visibility_config = SiteWebACLVisibilityConfig1
    statement = SiteWebACLStatement


@cloudformation_dataclass
class SiteWebACL:
    """AWS::WAFv2::WebACL resource."""

    resource: wafv2.WebACL
    name = Sub('${AppName}-WebACLWithAMR')
    scope = 'CLOUDFRONT'
    description = 'Web ACL with AWS Managed Rules'
    default_action = SiteWebACLDefaultAction
    visibility_config = SiteWebACLVisibilityConfig
    tags = [{
        'Key': 'Name',
        'Value': ref(AppName),
    }]
    rules = [SiteWebACLRule]
