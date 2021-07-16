#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, WafRule, WafIpset, WafIpsetIpSetDescriptors, WafRulePredicates


class DynamicAttributesStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here
        AwsProvider(self, 'Aws', region='us-east-1')

        wafRuleV2 = Wafv2RuleGroup(
            id="wafRuleGroup-0",
            name="tfWafRuleGroup",
            scope="REGIONAL",
            capacity=1,

        )


        ipSet = WafIpset(self,
                 id="tfIPSet-0",
                 name="tfIPSet",
                 ip_set_descriptors=[
                     WafIpsetIpSetDescriptors(type="IPV4", value="192.0.7.0/24")
                 ])

        WafRule(self,
                id="tfWAFRule-0",
                name="tfWAFRule",
                metric_name="tfWAFRule",
                predicates=[
                  WafRulePredicates(data_id=ipSet.id,negated=False,type="IPMatch")
                ],
                depends_on=[ipSet])


app = App()
DynamicAttributesStack(app, "dynamic-resource-attributes")

app.synth()
