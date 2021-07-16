## Dynamic Resource Attributes

This example showcases the difference of building a AWS WAF v2 Rule Group which allows an infinitely nested set of `statement` blocks. These statement blocks for the basis for various firewall rules that allow and deny traffic. If you were to look in the `dynamic-resource-attributes/declarative/main.tf` file, you would see the difficulty in mapping a dynamic set of rules to a standard declarative TF resource.

Contrast this to the ability for the TF CDK to simply parse a JSON object into a Wafv2RuleGroupRule class via Python and leverage the CDK to generate the correct TF JSON output. If we extrapolate this out, we can base these highly dynamic resources on external records like DB rows or create simpler representations of these rules and build a mapping function to convert it into the appropriate class.


Deploy

```
cd dynamic-resource-attributes
cdktf deploy
```

## Dynamic Module Composition

Terraform does not allow module versions to be dynamically defined at runtime. Given the TF CDK's ability to render TF JSON, we can leverage this abstraction layer to parse a `release.json` file and dynamically set module version numbers which will be statically set when the CDK generates the underlying TF code.

Deploy

```
cd dynamic-module-composition
cdktf deploy
```

## External Configuration Integration

Terraform allows integration with any service that has a provider, but this excludes a massive number of external services that don't have a TF Provider or exist as a simple REST API. This example leverages the TF CDK to make a request to the `https://www.boredapi.com/api/activity` API and use the JSON result to dynamically set information about the AWS VM based on the response. 

This could easily be extended to any external service like Kafka, PostreSQL, Active Directory and more to dynamically create TF resources.

Deploy

```
cd external-configuration-integration
cdktf deploy
```

## Post Provision Steps

Terraform doesn't have an easy way to create post provision steps or even inter-apply steps. This usually requires wrapping it using some sort of pipeline tool. Uitlizing the TF CDK, we can dynamically generate a `Stack` and perform a `commit` operation at each step. The Palo Alto Provider is an example that does not have a built in way to perform a commit which means that TF doesn't actually apply any changes.

Leveraging the TF CDK in this way, allows us to dynamically queue our changes and interact with the Palo Alto API to perform a commit after every resource is added.

Deploy

```
cd post-provision-steps
cdktf deploy
```
