#!/usr/bin/env python
import json
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, WafRule, WafIpset, WafIpsetIpSetDescriptors, Wafv2RuleGroup, Wafv2RuleGroupRule, \
    Wafv2RuleGroupRuleAction, Wafv2RuleGroupVisibilityConfig


class DynamicAttributesStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here
        AwsProvider(self, 'Aws', region='us-east-1')

        file = open("waf_data.json", )
        objects = json.load(file)

        Wafv2RuleGroup(self,
                       id="waf-rule-group",
                       name="waf-rule-group",
                       scope="REGIONAL",
                       capacity=1,
                       rule=[Wafv2RuleGroupRule(**objects["waf_v2_rules"][0])],
                       visibility_config=[Wafv2RuleGroupVisibilityConfig(
                           cloudwatch_metrics_enabled=False,
                           metric_name="name",
                           sampled_requests_enabled=False
                       )]
                       )

app = App()
DynamicAttributesStack(app, "dynamic-resource-attributes")
app.synth()
