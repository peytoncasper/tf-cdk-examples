#!/usr/bin/env python
import requests, subprocess
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, Instance


def get_activity():
    r = requests.get('https://www.boredapi.com/api/activity')
    response = r.json()

    return response["type"]



class BoredActivityStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, 'Aws', region='us-east-1')

        instanceName = get_activity()

        helloInstance = Instance(self, instanceName,
                                 ami="ami-03368e982f317ae48",
                                 instance_type="t2.micro",
                                 )


app = App()
BoredActivityStack(app, "external-configuration-integration")

app.synth()
