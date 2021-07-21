#!/usr/bin/env python
import json
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, WafRule, WafIpset, WafIpsetIpSetDescriptors, Wafv2RuleGroup, Wafv2RuleGroupRule, \
    Wafv2RuleGroupRuleAction, Wafv2RuleGroupVisibilityConfig, Wafv2RuleGroupRuleStatementGeoMatchStatement, Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig, Wafv2RuleGroupRuleStatement, \
    Wafv2RuleGroupRuleStatementOrStatementStatementGeoMatchStatement, Wafv2RuleGroupRuleStatementOrStatementStatementGeoMatchStatementForwardedIpConfig, \
    Wafv2RuleGroupRuleStatementOrStatement, Wafv2RuleGroupRuleStatementOrStatementStatement, Wafv2RuleGroupRuleVisibilityConfig \


def parse_waf_statement(statements_object):
    geo_match_statements = []
    or_statements = []
    for statement in statements_object:
        for key, value in statement.items():
            if key == "geo_match_statement":
                geo_match_statements.append(parse_geo_match_statement(value, "root"))
            elif key == "or_statement":
                or_statements.append(parse_or_statement(value))

    return Wafv2RuleGroupRuleStatement(
        geo_match_statement=geo_match_statements,
        or_statement=or_statements
    )

def parse_or_statement(statements):
    or_statements = []

    for statement in statements:
        geo_match_statements = []
        for keys, value in statement.items():
            if keys == "geo_match_statement":
                geo_match_statements.append(parse_geo_match_statement(value, "or"))

        or_statements.append(Wafv2RuleGroupRuleStatementOrStatementStatement(
            geo_match_statement=geo_match_statements
        ))

    return Wafv2RuleGroupRuleStatementOrStatement(
        statement=or_statements
    )

def parse_geo_match_statement(statements, parent_type):
    geo_match_statements = []

    for statement in statements:
        forwarded_ip_config= None
        if "forwarded_ip_config" in statement:
            forwarded_ip_config = parse_forward_ip_config(statement["forwarded_ip_config"], parent_type)

        if parent_type == "root":
            geo_match_statements.append(Wafv2RuleGroupRuleStatementGeoMatchStatement(
                country_codes=statement["country_codes"],
                forwarded_ip_config=forwarded_ip_config
            ))
        elif parent_type == "or":
            geo_match_statements.append(Wafv2RuleGroupRuleStatementOrStatementStatementGeoMatchStatement(
                country_codes=statement["country_codes"],
                forwarded_ip_config=forwarded_ip_config
            ))

    return geo_match_statements

def parse_forward_ip_config(configs, parent_type):
    forward_ip_configs = []
    for config in configs:
        if parent_type == "root":
            forward_ip_configs.append(Wafv2RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig(
                fallback_behavior=config["fallback_behavior"],
                header_name=config["header_name"]
            ))
        elif parent_type == "or":
            forward_ip_configs.append(Wafv2RuleGroupRuleStatementOrStatementStatementGeoMatchStatementForwardedIpConfig(
                fallback_behavior=config["fallback_behavior"],
                header_name=config["header_name"]
            ))

    return forward_ip_configs


class DynamicAttributesStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here
        AwsProvider(self, 'Aws', region='us-east-1')

        file = open("waf_data_complex.json", )
        objects = json.load(file)

        # Attempt 1
        # I wrote the recursive code to parse JSON objects to JSii objects. This ultimately did not work, I suspect due
        # to an issue with the mapping of attribute names from underscore to camelcase
        # statement = parse_waf_statement(objects["waf_v2_rules"][0]["statement"])

        # Attempt 2
        # Initially i was trying to parse json formatted keys with underscores. This expects the JSii names which are
        # camel case.
        # rule = Wafv2RuleGroupRule(
        #     name=objects["waf_v2_rules"][0]["name"],
        #     priority=objects["waf_v2_rules"][0]["priority"],
        #     action=objects["waf_v2_rules"][0]["action"],
        #     statement=objects["waf_v2_rules"][0]["statement"],
        #     visibility_config=objects["waf_v2_rules"][0]["visibility_config"],
        # )

        # Attempt 3
        rule = Wafv2RuleGroupRule(**objects["waf_v2_rules"][0])

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
