#!/usr/bin/env python
import json
from constructs import Construct
from cdktf import App, TerraformStack, TerraformHclModule
from imports.aws import AwsProvider

class ModuleCompositionStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        release_file = open('release.json', )
        release = json.load(release_file)

        AwsProvider(self, 'Aws', region='us-east-1')

        # define resources here
        network = TerraformHclModule(self,
            id="base-network",
            source="app.terraform.io/peyton-dev/module-network/aws",
            version=release["network"]
        )

        firewall = TerraformHclModule(self,
            id="firewall",
            source="app.terraform.io/peyton-dev/module-firewall/aws",
            version=release["firewall"],
            variables = {
                "vpc_id": network.get_string("vpc_id")
            },
            depends_on=[network]
        )

        compute = TerraformHclModule(self,
            id="compute",
            source="app.terraform.io/peyton-dev/module-compute/aws",
            version=release["compute"],
            variables = {
                "security_group_ids": [firewall.get_string("security_group_id")],
                "subnet_id": network.get_string("subnet_id")
            },
            depends_on=[network,firewall]
        )
app = App()
ModuleCompositionStack(app, "dynamic-module-composition")

app.synth()
