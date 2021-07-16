'''
# cdktf

cdktf is a framework for defining cloud infrastructure using Terraform providers and modules. It allows for
users to define infrastructure resources using higher-level programming languages.

## Build

Install dependencies

```bash
yarn install
```

Build the package

```bash
yarn build
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import constructs


class App(constructs.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdktf.App"):
    '''(experimental) Represents a cdktf application.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        outdir: typing.Optional[builtins.str] = None,
        stack_traces: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Defines an app.

        :param context: (experimental) Additional context values for the application. Context set by the CLI or the ``context`` key in ``cdktf.json`` has precedence. Context can be read from any construct using ``node.getContext(key)``. Default: - no additional context
        :param outdir: (experimental) The directory to output Terraform resources. Default: - CDKTF_OUTDIR if defined, otherwise "cdktf.out"
        :param stack_traces: 

        :stability: experimental
        '''
        options = AppOptions(context=context, outdir=outdir, stack_traces=stack_traces)

        jsii.create(App, self, [options])

    @jsii.member(jsii_name="synth")
    def synth(self) -> None:
        '''(experimental) Synthesizes all resources to the output directory.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synth", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''(experimental) The output directory into which resources will be synthesized.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetStackId")
    def target_stack_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The stack which will be synthesized.

        If not set, all stacks will be synthesized.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetStackId"))


@jsii.data_type(
    jsii_type="cdktf.AppOptions",
    jsii_struct_bases=[],
    name_mapping={
        "context": "context",
        "outdir": "outdir",
        "stack_traces": "stackTraces",
    },
)
class AppOptions:
    def __init__(
        self,
        *,
        context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        outdir: typing.Optional[builtins.str] = None,
        stack_traces: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param context: (experimental) Additional context values for the application. Context set by the CLI or the ``context`` key in ``cdktf.json`` has precedence. Context can be read from any construct using ``node.getContext(key)``. Default: - no additional context
        :param outdir: (experimental) The directory to output Terraform resources. Default: - CDKTF_OUTDIR if defined, otherwise "cdktf.out"
        :param stack_traces: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if context is not None:
            self._values["context"] = context
        if outdir is not None:
            self._values["outdir"] = outdir
        if stack_traces is not None:
            self._values["stack_traces"] = stack_traces

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Additional context values for the application.

        Context set by the CLI or the ``context`` key in ``cdktf.json`` has precedence.

        Context can be read from any construct using ``node.getContext(key)``.

        :default: - no additional context

        :stability: experimental
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''(experimental) The directory to output Terraform resources.

        :default: - CDKTF_OUTDIR if defined, otherwise "cdktf.out"

        :stability: experimental
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stack_traces(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("stack_traces")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.ArtifactoryBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "repo": "repo",
        "subpath": "subpath",
        "url": "url",
        "username": "username",
    },
)
class ArtifactoryBackendProps:
    def __init__(
        self,
        *,
        password: builtins.str,
        repo: builtins.str,
        subpath: builtins.str,
        url: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: 
        :param repo: 
        :param subpath: 
        :param url: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "repo": repo,
            "subpath": subpath,
            "url": url,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subpath(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("subpath")
        assert result is not None, "Required property 'subpath' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArtifactoryBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdktf.AssetType")
class AssetType(enum.Enum):
    '''
    :stability: experimental
    '''

    FILE = "FILE"
    '''
    :stability: experimental
    '''
    DIRECTORY = "DIRECTORY"
    '''
    :stability: experimental
    '''
    ARCHIVE = "ARCHIVE"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="cdktf.AzurermBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "key": "key",
        "storage_account_name": "storageAccountName",
        "access_key": "accessKey",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "endpoint": "endpoint",
        "environment": "environment",
        "msi_endpoint": "msiEndpoint",
        "resource_group_name": "resourceGroupName",
        "sas_token": "sasToken",
        "subscription_id": "subscriptionId",
        "tenant_id": "tenantId",
        "use_msi": "useMsi",
    },
)
class AzurermBackendProps:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        key: builtins.str,
        storage_account_name: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        sas_token: typing.Optional[builtins.str] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param container_name: 
        :param key: 
        :param storage_account_name: 
        :param access_key: 
        :param client_id: 
        :param client_secret: 
        :param endpoint: 
        :param environment: 
        :param msi_endpoint: 
        :param resource_group_name: 
        :param sas_token: 
        :param subscription_id: 
        :param tenant_id: 
        :param use_msi: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
            "key": key,
            "storage_account_name": storage_account_name,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if environment is not None:
            self._values["environment"] = environment
        if msi_endpoint is not None:
            self._values["msi_endpoint"] = msi_endpoint
        if resource_group_name is not None:
            self._values["resource_group_name"] = resource_group_name
        if sas_token is not None:
            self._values["sas_token"] = sas_token
        if subscription_id is not None:
            self._values["subscription_id"] = subscription_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if use_msi is not None:
            self._values["use_msi"] = use_msi

    @builtins.property
    def container_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("storage_account_name")
        assert result is not None, "Required property 'storage_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("msi_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sas_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sas_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_msi(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_msi")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurermBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BooleanMap(metaclass=jsii.JSIIMeta, jsii_type="cdktf.BooleanMap"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        terraform_resource: "ITerraformResource",
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -

        :stability: experimental
        '''
        jsii.create(BooleanMap, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="lookup")
    def lookup(self, key: builtins.str) -> builtins.bool:
        '''
        :param key: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "lookup", [key]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> "ITerraformResource":
        '''
        :stability: experimental
        '''
        return typing.cast("ITerraformResource", jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: "ITerraformResource") -> None:
        jsii.set(self, "terraformResource", value)


class ComplexComputedList(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.ComplexComputedList",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        terraform_resource: "ITerraformResource",
        terraform_attribute: builtins.str,
        complex_computed_list_index: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -
        :param complex_computed_list_index: -

        :stability: experimental
        '''
        jsii.create(ComplexComputedList, self, [terraform_resource, terraform_attribute, complex_computed_list_index])

    @jsii.member(jsii_name="getBooleanAttribute")
    def get_boolean_attribute(self, terraform_attribute: builtins.str) -> builtins.bool:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "getBooleanAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getListAttribute")
    def get_list_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> typing.List[builtins.str]:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getListAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getNumberAttribute")
    def get_number_attribute(self, terraform_attribute: builtins.str) -> jsii.Number:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "getNumberAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getStringAttribute")
    def get_string_attribute(self, terraform_attribute: builtins.str) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getStringAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="interpolationForAttribute")
    def _interpolation_for_attribute(self, property: builtins.str) -> builtins.str:
        '''
        :param property: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "interpolationForAttribute", [property]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="complexComputedListIndex")
    def _complex_computed_list_index(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "complexComputedListIndex"))

    @_complex_computed_list_index.setter
    def _complex_computed_list_index(self, value: builtins.str) -> None:
        jsii.set(self, "complexComputedListIndex", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> "ITerraformResource":
        '''
        :stability: experimental
        '''
        return typing.cast("ITerraformResource", jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: "ITerraformResource") -> None:
        jsii.set(self, "terraformResource", value)


@jsii.data_type(
    jsii_type="cdktf.ConsulBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "path": "path",
        "address": "address",
        "ca_file": "caFile",
        "cert_file": "certFile",
        "datacenter": "datacenter",
        "gzip": "gzip",
        "http_auth": "httpAuth",
        "key_file": "keyFile",
        "lock": "lock",
        "scheme": "scheme",
    },
)
class ConsulBackendProps:
    def __init__(
        self,
        *,
        access_token: builtins.str,
        path: builtins.str,
        address: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        datacenter: typing.Optional[builtins.str] = None,
        gzip: typing.Optional[builtins.bool] = None,
        http_auth: typing.Optional[builtins.str] = None,
        key_file: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: 
        :param path: 
        :param address: 
        :param ca_file: 
        :param cert_file: 
        :param datacenter: 
        :param gzip: 
        :param http_auth: 
        :param key_file: 
        :param lock: 
        :param scheme: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "access_token": access_token,
            "path": path,
        }
        if address is not None:
            self._values["address"] = address
        if ca_file is not None:
            self._values["ca_file"] = ca_file
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if gzip is not None:
            self._values["gzip"] = gzip
        if http_auth is not None:
            self._values["http_auth"] = http_auth
        if key_file is not None:
            self._values["key_file"] = key_file
        if lock is not None:
            self._values["lock"] = lock
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def access_token(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_token")
        assert result is not None, "Required property 'access_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ca_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gzip(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("gzip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def http_auth(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("http_auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsulBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.CosBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "acl": "acl",
        "encrypt": "encrypt",
        "key": "key",
        "prefix": "prefix",
        "region": "region",
        "secret_id": "secretId",
        "secret_key": "secretKey",
    },
)
class CosBackendProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: 
        :param acl: 
        :param encrypt: 
        :param key: 
        :param prefix: 
        :param region: 
        :param secret_id: 
        :param secret_key: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if acl is not None:
            self._values["acl"] = acl
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if key is not None:
            self._values["key"] = key
        if prefix is not None:
            self._values["prefix"] = prefix
        if region is not None:
            self._values["region"] = region
        if secret_id is not None:
            self._values["secret_id"] = secret_id
        if secret_key is not None:
            self._values["secret_key"] = secret_key

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateConfig",
    jsii_struct_bases=[],
    name_mapping={"defaults": "defaults", "workspace": "workspace"},
)
class DataTerraformRemoteStateConfig:
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateConsulConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, ConsulBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "access_token": "accessToken",
        "path": "path",
        "address": "address",
        "ca_file": "caFile",
        "cert_file": "certFile",
        "datacenter": "datacenter",
        "gzip": "gzip",
        "http_auth": "httpAuth",
        "key_file": "keyFile",
        "lock": "lock",
        "scheme": "scheme",
    },
)
class DataTerraformRemoteStateConsulConfig(
    DataTerraformRemoteStateConfig,
    ConsulBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        access_token: builtins.str,
        path: builtins.str,
        address: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        datacenter: typing.Optional[builtins.str] = None,
        gzip: typing.Optional[builtins.bool] = None,
        http_auth: typing.Optional[builtins.str] = None,
        key_file: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param access_token: 
        :param path: 
        :param address: 
        :param ca_file: 
        :param cert_file: 
        :param datacenter: 
        :param gzip: 
        :param http_auth: 
        :param key_file: 
        :param lock: 
        :param scheme: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "access_token": access_token,
            "path": path,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if address is not None:
            self._values["address"] = address
        if ca_file is not None:
            self._values["ca_file"] = ca_file
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if gzip is not None:
            self._values["gzip"] = gzip
        if http_auth is not None:
            self._values["http_auth"] = http_auth
        if key_file is not None:
            self._values["key_file"] = key_file
        if lock is not None:
            self._values["lock"] = lock
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_token(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_token")
        assert result is not None, "Required property 'access_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ca_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gzip(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("gzip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def http_auth(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("http_auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateConsulConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateCosConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, CosBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "bucket": "bucket",
        "acl": "acl",
        "encrypt": "encrypt",
        "key": "key",
        "prefix": "prefix",
        "region": "region",
        "secret_id": "secretId",
        "secret_key": "secretKey",
    },
)
class DataTerraformRemoteStateCosConfig(
    DataTerraformRemoteStateConfig,
    CosBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param acl: 
        :param encrypt: 
        :param key: 
        :param prefix: 
        :param region: 
        :param secret_id: 
        :param secret_key: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if acl is not None:
            self._values["acl"] = acl
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if key is not None:
            self._values["key"] = key
        if prefix is not None:
            self._values["prefix"] = prefix
        if region is not None:
            self._values["region"] = region
        if secret_id is not None:
            self._values["secret_id"] = secret_id
        if secret_key is not None:
            self._values["secret_key"] = secret_key

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateCosConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.EncodingOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint"},
)
class EncodingOptions:
    def __init__(self, *, display_hint: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Properties to string encodings.

        :param display_hint: (experimental) A hint for the Token's purpose when stringifying it. Default: - no display hint

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''(experimental) A hint for the Token's purpose when stringifying it.

        :default: - no display hint

        :stability: experimental
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncodingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.EtcdBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints": "endpoints",
        "path": "path",
        "password": "password",
        "username": "username",
    },
)
class EtcdBackendProps:
    def __init__(
        self,
        *,
        endpoints: builtins.str,
        path: builtins.str,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoints: 
        :param path: 
        :param password: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoints": endpoints,
            "path": path,
        }
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def endpoints(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EtcdBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.EtcdV3BackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints": "endpoints",
        "cacert_path": "cacertPath",
        "cert_path": "certPath",
        "key_path": "keyPath",
        "lock": "lock",
        "password": "password",
        "prefix": "prefix",
        "username": "username",
    },
)
class EtcdV3BackendProps:
    def __init__(
        self,
        *,
        endpoints: typing.Sequence[builtins.str],
        cacert_path: typing.Optional[builtins.str] = None,
        cert_path: typing.Optional[builtins.str] = None,
        key_path: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        password: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoints: 
        :param cacert_path: 
        :param cert_path: 
        :param key_path: 
        :param lock: 
        :param password: 
        :param prefix: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoints": endpoints,
        }
        if cacert_path is not None:
            self._values["cacert_path"] = cacert_path
        if cert_path is not None:
            self._values["cert_path"] = cert_path
        if key_path is not None:
            self._values["key_path"] = key_path
        if lock is not None:
            self._values["lock"] = lock
        if password is not None:
            self._values["password"] = password
        if prefix is not None:
            self._values["prefix"] = prefix
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def endpoints(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cacert_path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cacert_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cert_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EtcdV3BackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.GcsBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "access_token": "accessToken",
        "credentials": "credentials",
        "encryption_key": "encryptionKey",
        "prefix": "prefix",
    },
)
class GcsBackendProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: 
        :param access_token: 
        :param credentials: 
        :param encryption_key: 
        :param prefix: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if credentials is not None:
            self._values["credentials"] = credentials
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcsBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.HttpBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "lock_address": "lockAddress",
        "lock_method": "lockMethod",
        "password": "password",
        "retry_max": "retryMax",
        "retry_wait_max": "retryWaitMax",
        "retry_wait_min": "retryWaitMin",
        "skip_cert_verification": "skipCertVerification",
        "unlock_address": "unlockAddress",
        "unlock_method": "unlockMethod",
        "update_method": "updateMethod",
        "username": "username",
    },
)
class HttpBackendProps:
    def __init__(
        self,
        *,
        address: builtins.str,
        lock_address: typing.Optional[builtins.str] = None,
        lock_method: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        retry_max: typing.Optional[jsii.Number] = None,
        retry_wait_max: typing.Optional[jsii.Number] = None,
        retry_wait_min: typing.Optional[jsii.Number] = None,
        skip_cert_verification: typing.Optional[builtins.bool] = None,
        unlock_address: typing.Optional[builtins.str] = None,
        unlock_method: typing.Optional[builtins.str] = None,
        update_method: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: 
        :param lock_address: 
        :param lock_method: 
        :param password: 
        :param retry_max: 
        :param retry_wait_max: 
        :param retry_wait_min: 
        :param skip_cert_verification: 
        :param unlock_address: 
        :param unlock_method: 
        :param update_method: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
        }
        if lock_address is not None:
            self._values["lock_address"] = lock_address
        if lock_method is not None:
            self._values["lock_method"] = lock_method
        if password is not None:
            self._values["password"] = password
        if retry_max is not None:
            self._values["retry_max"] = retry_max
        if retry_wait_max is not None:
            self._values["retry_wait_max"] = retry_wait_max
        if retry_wait_min is not None:
            self._values["retry_wait_min"] = retry_wait_min
        if skip_cert_verification is not None:
            self._values["skip_cert_verification"] = skip_cert_verification
        if unlock_address is not None:
            self._values["unlock_address"] = unlock_address
        if unlock_method is not None:
            self._values["unlock_method"] = unlock_method
        if update_method is not None:
            self._values["update_method"] = update_method
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def address(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lock_address(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock_method(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_max(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("retry_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_wait_max(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("retry_wait_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_wait_min(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("retry_wait_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_cert_verification(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_cert_verification")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def unlock_address(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("unlock_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unlock_method(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("unlock_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_method(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("update_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="cdktf.IAnyProducer")
class IAnyProducer(typing_extensions.Protocol):
    '''(experimental) Interface for lazy untyped value producers.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IAnyProducerProxy"]:
        return _IAnyProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Any:
        '''(experimental) Produce the value.

        :param context: -

        :stability: experimental
        '''
        ...


class _IAnyProducerProxy:
    '''(experimental) Interface for lazy untyped value producers.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IAnyProducer"

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Any:
        '''(experimental) Produce the value.

        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "produce", [context]))


@jsii.interface(jsii_type="cdktf.IFragmentConcatenator")
class IFragmentConcatenator(typing_extensions.Protocol):
    '''(experimental) Function used to concatenate symbols in the target document language.

    Interface so it could potentially be exposed over jsii.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IFragmentConcatenatorProxy"]:
        return _IFragmentConcatenatorProxy

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        '''(experimental) Join the fragment on the left and on the right.

        :param left: -
        :param right: -

        :stability: experimental
        '''
        ...


class _IFragmentConcatenatorProxy:
    '''(experimental) Function used to concatenate symbols in the target document language.

    Interface so it could potentially be exposed over jsii.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IFragmentConcatenator"

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        '''(experimental) Join the fragment on the left and on the right.

        :param left: -
        :param right: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "join", [left, right]))


@jsii.interface(jsii_type="cdktf.IListProducer")
class IListProducer(typing_extensions.Protocol):
    '''(experimental) Interface for lazy list producers.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IListProducerProxy"]:
        return _IListProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(
        self,
        context: "IResolveContext",
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Produce the list value.

        :param context: -

        :stability: experimental
        '''
        ...


class _IListProducerProxy:
    '''(experimental) Interface for lazy list producers.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IListProducer"

    @jsii.member(jsii_name="produce")
    def produce(
        self,
        context: "IResolveContext",
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Produce the list value.

        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.invoke(self, "produce", [context]))


@jsii.interface(jsii_type="cdktf.INumberProducer")
class INumberProducer(typing_extensions.Protocol):
    '''(experimental) Interface for lazy number producers.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_INumberProducerProxy"]:
        return _INumberProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[jsii.Number]:
        '''(experimental) Produce the number value.

        :param context: -

        :stability: experimental
        '''
        ...


class _INumberProducerProxy:
    '''(experimental) Interface for lazy number producers.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.INumberProducer"

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[jsii.Number]:
        '''(experimental) Produce the number value.

        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.invoke(self, "produce", [context]))


@jsii.interface(jsii_type="cdktf.IPostProcessor")
class IPostProcessor(typing_extensions.Protocol):
    '''(experimental) A Token that can post-process the complete resolved value, after resolve() has recursed over it.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IPostProcessorProxy"]:
        return _IPostProcessorProxy

    @jsii.member(jsii_name="postProcess")
    def post_process(self, input: typing.Any, context: "IResolveContext") -> typing.Any:
        '''(experimental) Process the completely resolved value, after full recursion/resolution has happened.

        :param input: -
        :param context: -

        :stability: experimental
        '''
        ...


class _IPostProcessorProxy:
    '''(experimental) A Token that can post-process the complete resolved value, after resolve() has recursed over it.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IPostProcessor"

    @jsii.member(jsii_name="postProcess")
    def post_process(self, input: typing.Any, context: "IResolveContext") -> typing.Any:
        '''(experimental) Process the completely resolved value, after full recursion/resolution has happened.

        :param input: -
        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "postProcess", [input, context]))


@jsii.interface(jsii_type="cdktf.IRemoteWorkspace")
class IRemoteWorkspace(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IRemoteWorkspaceProxy"]:
        return _IRemoteWorkspaceProxy


class _IRemoteWorkspaceProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IRemoteWorkspace"
    pass


@jsii.interface(jsii_type="cdktf.IResolvable")
class IResolvable(typing_extensions.Protocol):
    '''(experimental) Interface for values that can be resolvable later.

    Tokens are special objects that participate in synthesis.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IResolvableProxy"]:
        return _IResolvableProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''(experimental) The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array the stack will not be attached.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: "IResolveContext") -> typing.Any:
        '''(experimental) Produce the Token's value at resolution time.

        :param context: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Return a string representation of this resolvable object.

        Returns a reversible string representation.

        :stability: experimental
        '''
        ...


class _IResolvableProxy:
    '''(experimental) Interface for values that can be resolvable later.

    Tokens are special objects that participate in synthesis.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IResolvable"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''(experimental) The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array the stack will not be attached.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: "IResolveContext") -> typing.Any:
        '''(experimental) Produce the Token's value at resolution time.

        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [context]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Return a string representation of this resolvable object.

        Returns a reversible string representation.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))


@jsii.interface(jsii_type="cdktf.IResolveContext")
class IResolveContext(typing_extensions.Protocol):
    '''(experimental) Current resolution context for tokens.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IResolveContextProxy"]:
        return _IResolveContextProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preparing")
    def preparing(self) -> builtins.bool:
        '''(experimental) True when we are still preparing, false if we're rendering the final output.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> constructs.IConstruct:
        '''(experimental) The scope from which resolution has been initiated.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="registerPostProcessor")
    def register_post_processor(self, post_processor: IPostProcessor) -> None:
        '''(experimental) Use this postprocessor after the entire token structure has been resolved.

        :param post_processor: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="resolve")
    def resolve(self, x: typing.Any) -> typing.Any:
        '''(experimental) Resolve an inner object.

        :param x: -

        :stability: experimental
        '''
        ...


class _IResolveContextProxy:
    '''(experimental) Current resolution context for tokens.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IResolveContext"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preparing")
    def preparing(self) -> builtins.bool:
        '''(experimental) True when we are still preparing, false if we're rendering the final output.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "preparing"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> constructs.IConstruct:
        '''(experimental) The scope from which resolution has been initiated.

        :stability: experimental
        '''
        return typing.cast(constructs.IConstruct, jsii.get(self, "scope"))

    @jsii.member(jsii_name="registerPostProcessor")
    def register_post_processor(self, post_processor: IPostProcessor) -> None:
        '''(experimental) Use this postprocessor after the entire token structure has been resolved.

        :param post_processor: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "registerPostProcessor", [post_processor]))

    @jsii.member(jsii_name="resolve")
    def resolve(self, x: typing.Any) -> typing.Any:
        '''(experimental) Resolve an inner object.

        :param x: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [x]))


@jsii.interface(jsii_type="cdktf.IResource")
class IResource(constructs.IConstruct, typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IResourceProxy"]:
        return _IResourceProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> "TerraformStack":
        '''(experimental) The stack in which this resource is defined.

        :stability: experimental
        '''
        ...


class _IResourceProxy(
    jsii.proxy_for(constructs.IConstruct) # type: ignore[misc]
):
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IResource"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> "TerraformStack":
        '''(experimental) The stack in which this resource is defined.

        :stability: experimental
        '''
        return typing.cast("TerraformStack", jsii.get(self, "stack"))


@jsii.interface(jsii_type="cdktf.IStringProducer")
class IStringProducer(typing_extensions.Protocol):
    '''(experimental) Interface for lazy string producers.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_IStringProducerProxy"]:
        return _IStringProducerProxy

    @jsii.member(jsii_name="produce")
    def produce(self, context: IResolveContext) -> typing.Optional[builtins.str]:
        '''(experimental) Produce the string value.

        :param context: -

        :stability: experimental
        '''
        ...


class _IStringProducerProxy:
    '''(experimental) Interface for lazy string producers.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.IStringProducer"

    @jsii.member(jsii_name="produce")
    def produce(self, context: IResolveContext) -> typing.Optional[builtins.str]:
        '''(experimental) Produce the string value.

        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "produce", [context]))


@jsii.interface(jsii_type="cdktf.ITerraformDependable")
class ITerraformDependable(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_ITerraformDependableProxy"]:
        return _ITerraformDependableProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...


class _ITerraformDependableProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.ITerraformDependable"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqn"))


@jsii.interface(jsii_type="cdktf.ITerraformResource")
class ITerraformResource(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_ITerraformResourceProxy"]:
        return _ITerraformResourceProxy

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="friendlyUniqueId")
    def friendly_unique_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResourceType")
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        ...

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        ...

    @depends_on.setter
    def depends_on(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycle")
    def lifecycle(self) -> typing.Optional["TerraformResourceLifecycle"]:
        '''
        :stability: experimental
        '''
        ...

    @lifecycle.setter
    def lifecycle(self, value: typing.Optional["TerraformResourceLifecycle"]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional["TerraformProvider"]:
        '''
        :stability: experimental
        '''
        ...

    @provider.setter
    def provider(self, value: typing.Optional["TerraformProvider"]) -> None:
        ...

    @jsii.member(jsii_name="interpolationForAttribute")
    def interpolation_for_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        ...


class _ITerraformResourceProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.ITerraformResource"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="friendlyUniqueId")
    def friendly_unique_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "friendlyUniqueId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResourceType")
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "count"))

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "count", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dependsOn"))

    @depends_on.setter
    def depends_on(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "dependsOn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycle")
    def lifecycle(self) -> typing.Optional["TerraformResourceLifecycle"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional["TerraformResourceLifecycle"], jsii.get(self, "lifecycle"))

    @lifecycle.setter
    def lifecycle(self, value: typing.Optional["TerraformResourceLifecycle"]) -> None:
        jsii.set(self, "lifecycle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional["TerraformProvider"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional["TerraformProvider"], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional["TerraformProvider"]) -> None:
        jsii.set(self, "provider", value)

    @jsii.member(jsii_name="interpolationForAttribute")
    def interpolation_for_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "interpolationForAttribute", [terraform_attribute]))


@jsii.interface(jsii_type="cdktf.ITokenMapper")
class ITokenMapper(typing_extensions.Protocol):
    '''(experimental) Interface to apply operation to tokens in a string.

    Interface so it can be exported via jsii.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_ITokenMapperProxy"]:
        return _ITokenMapperProxy

    @jsii.member(jsii_name="mapToken")
    def map_token(self, t: IResolvable) -> typing.Any:
        '''(experimental) Replace a single token.

        :param t: -

        :stability: experimental
        '''
        ...


class _ITokenMapperProxy:
    '''(experimental) Interface to apply operation to tokens in a string.

    Interface so it can be exported via jsii.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.ITokenMapper"

    @jsii.member(jsii_name="mapToken")
    def map_token(self, t: IResolvable) -> typing.Any:
        '''(experimental) Replace a single token.

        :param t: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "mapToken", [t]))


@jsii.interface(jsii_type="cdktf.ITokenResolver")
class ITokenResolver(typing_extensions.Protocol):
    '''(experimental) How to resolve tokens.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_ITokenResolverProxy"]:
        return _ITokenResolverProxy

    @jsii.member(jsii_name="resolveList")
    def resolve_list(
        self,
        l: typing.Sequence[builtins.str],
        context: IResolveContext,
    ) -> typing.Any:
        '''(experimental) Resolve a tokenized list.

        :param l: -
        :param context: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="resolveString")
    def resolve_string(
        self,
        s: "TokenizedStringFragments",
        context: IResolveContext,
    ) -> typing.Any:
        '''(experimental) Resolve a string with at least one stringified token in it.

        (May use concatenation)

        :param s: -
        :param context: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(
        self,
        t: IResolvable,
        context: IResolveContext,
        post_processor: IPostProcessor,
    ) -> typing.Any:
        '''(experimental) Resolve a single token.

        :param t: -
        :param context: -
        :param post_processor: -

        :stability: experimental
        '''
        ...


class _ITokenResolverProxy:
    '''(experimental) How to resolve tokens.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdktf.ITokenResolver"

    @jsii.member(jsii_name="resolveList")
    def resolve_list(
        self,
        l: typing.Sequence[builtins.str],
        context: IResolveContext,
    ) -> typing.Any:
        '''(experimental) Resolve a tokenized list.

        :param l: -
        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveList", [l, context]))

    @jsii.member(jsii_name="resolveString")
    def resolve_string(
        self,
        s: "TokenizedStringFragments",
        context: IResolveContext,
    ) -> typing.Any:
        '''(experimental) Resolve a string with at least one stringified token in it.

        (May use concatenation)

        :param s: -
        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveString", [s, context]))

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(
        self,
        t: IResolvable,
        context: IResolveContext,
        post_processor: IPostProcessor,
    ) -> typing.Any:
        '''(experimental) Resolve a single token.

        :param t: -
        :param context: -
        :param post_processor: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveToken", [t, context, post_processor]))


class Lazy(metaclass=jsii.JSIIMeta, jsii_type="cdktf.Lazy"):
    '''(experimental) Lazily produce a value.

    Can be used to return a string, list or numeric value whose actual value
    will only be calculated later, during synthesis.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(Lazy, self, [])

    @jsii.member(jsii_name="anyValue") # type: ignore[misc]
    @builtins.classmethod
    def any_value(
        cls,
        producer: IAnyProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty_array: typing.Optional[builtins.bool] = None,
    ) -> IResolvable:
        '''(experimental) Produces a lazy token from an untyped value.

        :param producer: The lazy producer.
        :param display_hint: (experimental) Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: (experimental) If the produced value is an array and it is empty, return 'undefined' instead. Default: false

        :stability: experimental
        '''
        options = LazyAnyValueOptions(
            display_hint=display_hint, omit_empty_array=omit_empty_array
        )

        return typing.cast(IResolvable, jsii.sinvoke(cls, "anyValue", [producer, options]))

    @jsii.member(jsii_name="listValue") # type: ignore[misc]
    @builtins.classmethod
    def list_value(
        cls,
        producer: IListProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.List[builtins.str]:
        '''(experimental) Returns a list-ified token for a lazy value.

        :param producer: The producer.
        :param display_hint: (experimental) Use the given name as a display hint. Default: - No hint
        :param omit_empty: (experimental) If the produced list is empty, return 'undefined' instead. Default: false

        :stability: experimental
        '''
        options = LazyListValueOptions(
            display_hint=display_hint, omit_empty=omit_empty
        )

        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "listValue", [producer, options]))

    @jsii.member(jsii_name="numberValue") # type: ignore[misc]
    @builtins.classmethod
    def number_value(cls, producer: INumberProducer) -> jsii.Number:
        '''(experimental) Returns a numberified token for a lazy value.

        :param producer: The producer.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "numberValue", [producer]))

    @jsii.member(jsii_name="stringValue") # type: ignore[misc]
    @builtins.classmethod
    def string_value(
        cls,
        producer: IStringProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''(experimental) Returns a stringified token for a lazy value.

        :param producer: The producer.
        :param display_hint: (experimental) Use the given name as a display hint. Default: - No hint

        :stability: experimental
        '''
        options = LazyStringValueOptions(display_hint=display_hint)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "stringValue", [producer, options]))


@jsii.data_type(
    jsii_type="cdktf.LazyAnyValueOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint", "omit_empty_array": "omitEmptyArray"},
)
class LazyAnyValueOptions:
    def __init__(
        self,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty_array: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for creating lazy untyped tokens.

        :param display_hint: (experimental) Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: (experimental) If the produced value is an array and it is empty, return 'undefined' instead. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint
        if omit_empty_array is not None:
            self._values["omit_empty_array"] = omit_empty_array

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''(experimental) Use the given name as a display hint.

        :default: - No hint

        :stability: experimental
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def omit_empty_array(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If the produced value is an array and it is empty, return 'undefined' instead.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty_array")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyAnyValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.LazyListValueOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint", "omit_empty": "omitEmpty"},
)
class LazyListValueOptions:
    def __init__(
        self,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for creating a lazy list token.

        :param display_hint: (experimental) Use the given name as a display hint. Default: - No hint
        :param omit_empty: (experimental) If the produced list is empty, return 'undefined' instead. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''(experimental) Use the given name as a display hint.

        :default: - No hint

        :stability: experimental
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If the produced list is empty, return 'undefined' instead.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyListValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.LazyStringValueOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint"},
)
class LazyStringValueOptions:
    def __init__(self, *, display_hint: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Options for creating a lazy string token.

        :param display_hint: (experimental) Use the given name as a display hint. Default: - No hint

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''(experimental) Use the given name as a display hint.

        :default: - No hint

        :stability: experimental
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyStringValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.LocalBackendProps",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "workspace_dir": "workspaceDir"},
)
class LocalBackendProps:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        workspace_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: 
        :param workspace_dir: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if workspace_dir is not None:
            self._values["workspace_dir"] = workspace_dir

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_dir(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Manifest(metaclass=jsii.JSIIMeta, jsii_type="cdktf.Manifest"):
    '''
    :stability: experimental
    '''

    def __init__(self, version: builtins.str, outdir: builtins.str) -> None:
        '''
        :param version: -
        :param outdir: -

        :stability: experimental
        '''
        jsii.create(Manifest, self, [version, outdir])

    @jsii.member(jsii_name="buildManifest")
    def build_manifest(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "buildManifest", []))

    @jsii.member(jsii_name="forStack")
    def for_stack(self, stack: "TerraformStack") -> "StackManifest":
        '''
        :param stack: -

        :stability: experimental
        '''
        return typing.cast("StackManifest", jsii.invoke(self, "forStack", [stack]))

    @jsii.member(jsii_name="writeToFile")
    def write_to_file(self) -> None:
        '''
        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "writeToFile", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="fileName")
    def FILE_NAME(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "fileName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="stackFileName")
    def STACK_FILE_NAME(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "stackFileName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="stacksFolder")
    def STACKS_FOLDER(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "stacksFolder"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List["StackManifest"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List["StackManifest"], jsii.get(self, "stacks"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.data_type(
    jsii_type="cdktf.MantaBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "key_id": "keyId",
        "path": "path",
        "insecure_skip_tls_verify": "insecureSkipTlsVerify",
        "key_material": "keyMaterial",
        "object_name": "objectName",
        "url": "url",
        "user": "user",
    },
)
class MantaBackendProps:
    def __init__(
        self,
        *,
        account: builtins.str,
        key_id: builtins.str,
        path: builtins.str,
        insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
        key_material: typing.Optional[builtins.str] = None,
        object_name: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: 
        :param key_id: 
        :param path: 
        :param insecure_skip_tls_verify: 
        :param key_material: 
        :param object_name: 
        :param url: 
        :param user: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "account": account,
            "key_id": key_id,
            "path": path,
        }
        if insecure_skip_tls_verify is not None:
            self._values["insecure_skip_tls_verify"] = insecure_skip_tls_verify
        if key_material is not None:
            self._values["key_material"] = key_material
        if object_name is not None:
            self._values["object_name"] = object_name
        if url is not None:
            self._values["url"] = url
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def account(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def insecure_skip_tls_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("insecure_skip_tls_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key_material(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_material")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("object_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MantaBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRemoteWorkspace)
class NamedRemoteWorkspace(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.NamedRemoteWorkspace",
):
    '''
    :stability: experimental
    '''

    def __init__(self, name: builtins.str) -> None:
        '''
        :param name: -

        :stability: experimental
        '''
        jsii.create(NamedRemoteWorkspace, self, [name])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)


class NumberMap(metaclass=jsii.JSIIMeta, jsii_type="cdktf.NumberMap"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        terraform_resource: ITerraformResource,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -

        :stability: experimental
        '''
        jsii.create(NumberMap, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="lookup")
    def lookup(self, key: builtins.str) -> jsii.Number:
        '''
        :param key: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "lookup", [key]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> ITerraformResource:
        '''
        :stability: experimental
        '''
        return typing.cast(ITerraformResource, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: ITerraformResource) -> None:
        jsii.set(self, "terraformResource", value)


@jsii.data_type(
    jsii_type="cdktf.OssAssumeRole",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "policy": "policy",
        "session_expiration": "sessionExpiration",
        "session_name": "sessionName",
    },
)
class OssAssumeRole:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        policy: typing.Optional[builtins.str] = None,
        session_expiration: typing.Optional[jsii.Number] = None,
        session_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: 
        :param policy: 
        :param session_expiration: 
        :param session_name: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "role_arn": role_arn,
        }
        if policy is not None:
            self._values["policy"] = policy
        if session_expiration is not None:
            self._values["session_expiration"] = session_expiration
        if session_name is not None:
            self._values["session_name"] = session_name

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_expiration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("session_expiration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def session_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OssAssumeRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.OssBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "access_key": "accessKey",
        "acl": "acl",
        "assume_role": "assumeRole",
        "ecs_role_name": "ecsRoleName",
        "encrypt": "encrypt",
        "endpoint": "endpoint",
        "key": "key",
        "prefix": "prefix",
        "profile": "profile",
        "region": "region",
        "secret_key": "secretKey",
        "security_token": "securityToken",
        "shared_credentials_file": "sharedCredentialsFile",
        "tablestore_endpoint": "tablestoreEndpoint",
        "tablestore_table": "tablestoreTable",
    },
)
class OssBackendProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role: typing.Optional[OssAssumeRole] = None,
        ecs_role_name: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        security_token: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        tablestore_endpoint: typing.Optional[builtins.str] = None,
        tablestore_table: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: 
        :param access_key: 
        :param acl: 
        :param assume_role: 
        :param ecs_role_name: 
        :param encrypt: 
        :param endpoint: 
        :param key: 
        :param prefix: 
        :param profile: 
        :param region: 
        :param secret_key: 
        :param security_token: 
        :param shared_credentials_file: 
        :param tablestore_endpoint: 
        :param tablestore_table: 

        :stability: experimental
        '''
        if isinstance(assume_role, dict):
            assume_role = OssAssumeRole(**assume_role)
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if acl is not None:
            self._values["acl"] = acl
        if assume_role is not None:
            self._values["assume_role"] = assume_role
        if ecs_role_name is not None:
            self._values["ecs_role_name"] = ecs_role_name
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if key is not None:
            self._values["key"] = key
        if prefix is not None:
            self._values["prefix"] = prefix
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if security_token is not None:
            self._values["security_token"] = security_token
        if shared_credentials_file is not None:
            self._values["shared_credentials_file"] = shared_credentials_file
        if tablestore_endpoint is not None:
            self._values["tablestore_endpoint"] = tablestore_endpoint
        if tablestore_table is not None:
            self._values["tablestore_table"] = tablestore_table

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role(self) -> typing.Optional[OssAssumeRole]:
        '''
        :stability: experimental
        '''
        result = self._values.get("assume_role")
        return typing.cast(typing.Optional[OssAssumeRole], result)

    @builtins.property
    def ecs_role_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ecs_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("security_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_credentials_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("shared_credentials_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tablestore_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tablestore_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tablestore_table(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tablestore_table")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OssBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.PgBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "conn_str": "connStr",
        "schema_name": "schemaName",
        "skip_schema_creation": "skipSchemaCreation",
    },
)
class PgBackendProps:
    def __init__(
        self,
        *,
        conn_str: builtins.str,
        schema_name: typing.Optional[builtins.str] = None,
        skip_schema_creation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param conn_str: 
        :param schema_name: 
        :param skip_schema_creation: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "conn_str": conn_str,
        }
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if skip_schema_creation is not None:
            self._values["skip_schema_creation"] = skip_schema_creation

    @builtins.property
    def conn_str(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("conn_str")
        assert result is not None, "Required property 'conn_str' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_schema_creation(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_schema_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PgBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRemoteWorkspace)
class PrefixedRemoteWorkspaces(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.PrefixedRemoteWorkspaces",
):
    '''
    :stability: experimental
    '''

    def __init__(self, prefix: builtins.str) -> None:
        '''
        :param prefix: -

        :stability: experimental
        '''
        jsii.create(PrefixedRemoteWorkspaces, self, [prefix])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        jsii.set(self, "prefix", value)


@jsii.data_type(
    jsii_type="cdktf.RemoteBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "organization": "organization",
        "workspaces": "workspaces",
        "hostname": "hostname",
        "token": "token",
    },
)
class RemoteBackendProps:
    def __init__(
        self,
        *,
        organization: builtins.str,
        workspaces: IRemoteWorkspace,
        hostname: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param organization: 
        :param workspaces: 
        :param hostname: 
        :param token: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "organization": organization,
            "workspaces": workspaces,
        }
        if hostname is not None:
            self._values["hostname"] = hostname
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def organization(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspaces(self) -> IRemoteWorkspace:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspaces")
        assert result is not None, "Required property 'workspaces' is missing"
        return typing.cast(IRemoteWorkspace, result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemoteBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.ResolveOptions",
    jsii_struct_bases=[],
    name_mapping={"resolver": "resolver", "scope": "scope", "preparing": "preparing"},
)
class ResolveOptions:
    def __init__(
        self,
        *,
        resolver: ITokenResolver,
        scope: constructs.IConstruct,
        preparing: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options to the resolve() operation.

        NOT the same as the ResolveContext; ResolveContext is exposed to Token
        implementors and resolution hooks, whereas this struct is just to bundle
        a number of things that would otherwise be arguments to resolve() in a
        readable way.

        :param resolver: (experimental) The resolver to apply to any resolvable tokens found.
        :param scope: (experimental) The scope from which resolution is performed.
        :param preparing: (experimental) Whether the resolution is being executed during the prepare phase or not. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resolver": resolver,
            "scope": scope,
        }
        if preparing is not None:
            self._values["preparing"] = preparing

    @builtins.property
    def resolver(self) -> ITokenResolver:
        '''(experimental) The resolver to apply to any resolvable tokens found.

        :stability: experimental
        '''
        result = self._values.get("resolver")
        assert result is not None, "Required property 'resolver' is missing"
        return typing.cast(ITokenResolver, result)

    @builtins.property
    def scope(self) -> constructs.IConstruct:
        '''(experimental) The scope from which resolution is performed.

        :stability: experimental
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(constructs.IConstruct, result)

    @builtins.property
    def preparing(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the resolution is being executed during the prepare phase or not.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("preparing")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IResource)
class Resource(
    constructs.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdktf.Resource",
):
    '''(experimental) A construct which represents a resource.

    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_ResourceProxy"]:
        return _ResourceProxy

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        jsii.create(Resource, self, [scope, id])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> "TerraformStack":
        '''(experimental) The stack in which this resource is defined.

        :stability: experimental
        '''
        return typing.cast("TerraformStack", jsii.get(self, "stack"))


class _ResourceProxy(Resource):
    pass


@jsii.data_type(
    jsii_type="cdktf.S3BackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "key": "key",
        "access_key": "accessKey",
        "acl": "acl",
        "assume_role_policy": "assumeRolePolicy",
        "dynamodb_endpoint": "dynamodbEndpoint",
        "dynamodb_table": "dynamodbTable",
        "encrypt": "encrypt",
        "endpoint": "endpoint",
        "external_id": "externalId",
        "force_path_style": "forcePathStyle",
        "iam_endpoint": "iamEndpoint",
        "kms_key_id": "kmsKeyId",
        "max_retries": "maxRetries",
        "profile": "profile",
        "region": "region",
        "role_arn": "roleArn",
        "secret_key": "secretKey",
        "session_name": "sessionName",
        "shared_credentials_file": "sharedCredentialsFile",
        "skip_credentials_validation": "skipCredentialsValidation",
        "skip_metadata_api_check": "skipMetadataApiCheck",
        "sse_customer_key": "sseCustomerKey",
        "sts_endpoint": "stsEndpoint",
        "token": "token",
        "workspace_key_prefix": "workspaceKeyPrefix",
    },
)
class S3BackendProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        key: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role_policy: typing.Optional[builtins.str] = None,
        dynamodb_endpoint: typing.Optional[builtins.str] = None,
        dynamodb_table: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_path_style: typing.Optional[builtins.bool] = None,
        iam_endpoint: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        skip_credentials_validation: typing.Optional[builtins.bool] = None,
        skip_metadata_api_check: typing.Optional[builtins.bool] = None,
        sse_customer_key: typing.Optional[builtins.str] = None,
        sts_endpoint: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        workspace_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: 
        :param key: 
        :param access_key: 
        :param acl: 
        :param assume_role_policy: 
        :param dynamodb_endpoint: 
        :param dynamodb_table: 
        :param encrypt: 
        :param endpoint: 
        :param external_id: 
        :param force_path_style: 
        :param iam_endpoint: 
        :param kms_key_id: 
        :param max_retries: 
        :param profile: 
        :param region: 
        :param role_arn: 
        :param secret_key: 
        :param session_name: 
        :param shared_credentials_file: 
        :param skip_credentials_validation: 
        :param skip_metadata_api_check: 
        :param sse_customer_key: 
        :param sts_endpoint: 
        :param token: 
        :param workspace_key_prefix: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if acl is not None:
            self._values["acl"] = acl
        if assume_role_policy is not None:
            self._values["assume_role_policy"] = assume_role_policy
        if dynamodb_endpoint is not None:
            self._values["dynamodb_endpoint"] = dynamodb_endpoint
        if dynamodb_table is not None:
            self._values["dynamodb_table"] = dynamodb_table
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if external_id is not None:
            self._values["external_id"] = external_id
        if force_path_style is not None:
            self._values["force_path_style"] = force_path_style
        if iam_endpoint is not None:
            self._values["iam_endpoint"] = iam_endpoint
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if session_name is not None:
            self._values["session_name"] = session_name
        if shared_credentials_file is not None:
            self._values["shared_credentials_file"] = shared_credentials_file
        if skip_credentials_validation is not None:
            self._values["skip_credentials_validation"] = skip_credentials_validation
        if skip_metadata_api_check is not None:
            self._values["skip_metadata_api_check"] = skip_metadata_api_check
        if sse_customer_key is not None:
            self._values["sse_customer_key"] = sse_customer_key
        if sts_endpoint is not None:
            self._values["sts_endpoint"] = sts_endpoint
        if token is not None:
            self._values["token"] = token
        if workspace_key_prefix is not None:
            self._values["workspace_key_prefix"] = workspace_key_prefix

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_policy(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("assume_role_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dynamodb_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_table(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dynamodb_table")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_path_style(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("force_path_style")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def iam_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("iam_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_credentials_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("shared_credentials_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_credentials_validation(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_credentials_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def skip_metadata_api_check(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_metadata_api_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sse_customer_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sse_customer_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sts_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sts_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_key_prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.StackManifest",
    jsii_struct_bases=[],
    name_mapping={
        "construct_path": "constructPath",
        "name": "name",
        "synthesized_stack_path": "synthesizedStackPath",
        "working_directory": "workingDirectory",
    },
)
class StackManifest:
    def __init__(
        self,
        *,
        construct_path: builtins.str,
        name: builtins.str,
        synthesized_stack_path: builtins.str,
        working_directory: builtins.str,
    ) -> None:
        '''
        :param construct_path: 
        :param name: 
        :param synthesized_stack_path: 
        :param working_directory: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "construct_path": construct_path,
            "name": name,
            "synthesized_stack_path": synthesized_stack_path,
            "working_directory": working_directory,
        }

    @builtins.property
    def construct_path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("construct_path")
        assert result is not None, "Required property 'construct_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def synthesized_stack_path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("synthesized_stack_path")
        assert result is not None, "Required property 'synthesized_stack_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def working_directory(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("working_directory")
        assert result is not None, "Required property 'working_directory' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IFragmentConcatenator)
class StringConcat(metaclass=jsii.JSIIMeta, jsii_type="cdktf.StringConcat"):
    '''(experimental) Converts all fragments to strings and concats those.

    Drops 'undefined's.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(StringConcat, self, [])

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        '''(experimental) Join the fragment on the left and on the right.

        :param left: -
        :param right: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "join", [left, right]))


class StringMap(metaclass=jsii.JSIIMeta, jsii_type="cdktf.StringMap"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        terraform_resource: ITerraformResource,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: -
        :param terraform_attribute: -

        :stability: experimental
        '''
        jsii.create(StringMap, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="lookup")
    def lookup(self, key: builtins.str) -> builtins.str:
        '''
        :param key: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "lookup", [key]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        jsii.set(self, "terraformAttribute", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> ITerraformResource:
        '''
        :stability: experimental
        '''
        return typing.cast(ITerraformResource, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: ITerraformResource) -> None:
        jsii.set(self, "terraformResource", value)


@jsii.data_type(
    jsii_type="cdktf.SwiftBackendProps",
    jsii_struct_bases=[],
    name_mapping={
        "container": "container",
        "application_credential_id": "applicationCredentialId",
        "application_credential_name": "applicationCredentialName",
        "application_credential_secret": "applicationCredentialSecret",
        "archive_container": "archiveContainer",
        "auth_url": "authUrl",
        "cacert_file": "cacertFile",
        "cert": "cert",
        "cloud": "cloud",
        "default_domain": "defaultDomain",
        "domain_id": "domainId",
        "domain_name": "domainName",
        "expire_after": "expireAfter",
        "insecure": "insecure",
        "key": "key",
        "password": "password",
        "project_domain_id": "projectDomainId",
        "project_domain_name": "projectDomainName",
        "region_name": "regionName",
        "state_name": "stateName",
        "tenant_id": "tenantId",
        "tenant_name": "tenantName",
        "token": "token",
        "user_domain_id": "userDomainId",
        "user_domain_name": "userDomainName",
        "user_id": "userId",
        "user_name": "userName",
    },
)
class SwiftBackendProps:
    def __init__(
        self,
        *,
        container: builtins.str,
        application_credential_id: typing.Optional[builtins.str] = None,
        application_credential_name: typing.Optional[builtins.str] = None,
        application_credential_secret: typing.Optional[builtins.str] = None,
        archive_container: typing.Optional[builtins.str] = None,
        auth_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        cert: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        default_domain: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        expire_after: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        project_domain_id: typing.Optional[builtins.str] = None,
        project_domain_name: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        tenant_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        user_domain_id: typing.Optional[builtins.str] = None,
        user_domain_name: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container: 
        :param application_credential_id: 
        :param application_credential_name: 
        :param application_credential_secret: 
        :param archive_container: 
        :param auth_url: 
        :param cacert_file: 
        :param cert: 
        :param cloud: 
        :param default_domain: 
        :param domain_id: 
        :param domain_name: 
        :param expire_after: 
        :param insecure: 
        :param key: 
        :param password: 
        :param project_domain_id: 
        :param project_domain_name: 
        :param region_name: 
        :param state_name: 
        :param tenant_id: 
        :param tenant_name: 
        :param token: 
        :param user_domain_id: 
        :param user_domain_name: 
        :param user_id: 
        :param user_name: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
        }
        if application_credential_id is not None:
            self._values["application_credential_id"] = application_credential_id
        if application_credential_name is not None:
            self._values["application_credential_name"] = application_credential_name
        if application_credential_secret is not None:
            self._values["application_credential_secret"] = application_credential_secret
        if archive_container is not None:
            self._values["archive_container"] = archive_container
        if auth_url is not None:
            self._values["auth_url"] = auth_url
        if cacert_file is not None:
            self._values["cacert_file"] = cacert_file
        if cert is not None:
            self._values["cert"] = cert
        if cloud is not None:
            self._values["cloud"] = cloud
        if default_domain is not None:
            self._values["default_domain"] = default_domain
        if domain_id is not None:
            self._values["domain_id"] = domain_id
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if expire_after is not None:
            self._values["expire_after"] = expire_after
        if insecure is not None:
            self._values["insecure"] = insecure
        if key is not None:
            self._values["key"] = key
        if password is not None:
            self._values["password"] = password
        if project_domain_id is not None:
            self._values["project_domain_id"] = project_domain_id
        if project_domain_name is not None:
            self._values["project_domain_name"] = project_domain_name
        if region_name is not None:
            self._values["region_name"] = region_name
        if state_name is not None:
            self._values["state_name"] = state_name
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if tenant_name is not None:
            self._values["tenant_name"] = tenant_name
        if token is not None:
            self._values["token"] = token
        if user_domain_id is not None:
            self._values["user_domain_id"] = user_domain_id
        if user_domain_name is not None:
            self._values["user_domain_name"] = user_domain_name
        if user_id is not None:
            self._values["user_id"] = user_id
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def container(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_credential_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("application_credential_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("application_credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_credential_secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("application_credential_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def archive_container(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("archive_container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_url(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cacert_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cacert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cloud")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_domain(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("default_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expire_after(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("expire_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_domain_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("project_domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_domain_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("project_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tenant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_domain_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_domain_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SwiftBackendProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformAsset(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformAsset",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        path: builtins.str,
        asset_hash: typing.Optional[builtins.str] = None,
        type: typing.Optional[AssetType] = None,
    ) -> None:
        '''(experimental) A Terraform Asset takes a file or directory outside of the CDK for Terraform context and moves it into it.

        Assets copy referenced files into the stacks context for further usage in other resources.

        :param scope: -
        :param id: -
        :param path: 
        :param asset_hash: 
        :param type: 

        :stability: experimental
        '''
        config = TerraformAssetConfig(path=path, asset_hash=asset_hash, type=type)

        jsii.create(TerraformAsset, self, [scope, id, config])

    @jsii.member(jsii_name="onSynthesize")
    def _on_synthesize(self, session: constructs.ISynthesisSession) -> None:
        '''(experimental) Allows this construct to emit artifacts into the cloud assembly during synthesis.

        This method is usually implemented by framework-level constructs such as ``Stack`` and ``Asset``
        as they participate in synthesizing the cloud assembly.

        :param session: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "onSynthesize", [session]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileName")
    def file_name(self) -> builtins.str:
        '''(experimental) Name of the asset.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''(experimental) The path relative to the root of the terraform directory in posix format Use this property to reference the asset.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetHash")
    def asset_hash(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetHash"))

    @asset_hash.setter
    def asset_hash(self, value: builtins.str) -> None:
        jsii.set(self, "assetHash", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> AssetType:
        '''
        :stability: experimental
        '''
        return typing.cast(AssetType, jsii.get(self, "type"))

    @type.setter
    def type(self, value: AssetType) -> None:
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="cdktf.TerraformAssetConfig",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "asset_hash": "assetHash", "type": "type"},
)
class TerraformAssetConfig:
    def __init__(
        self,
        *,
        path: builtins.str,
        asset_hash: typing.Optional[builtins.str] = None,
        type: typing.Optional[AssetType] = None,
    ) -> None:
        '''
        :param path: 
        :param asset_hash: 
        :param type: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[AssetType]:
        '''
        :stability: experimental
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[AssetType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformAssetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformElement(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformElement",
):
    '''
    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        jsii.create(TerraformElement, self, [scope, id])

    @jsii.member(jsii_name="addOverride")
    def add_override(self, path: builtins.str, value: typing.Any) -> None:
        '''
        :param path: -
        :param value: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addOverride", [path, value]))

    @jsii.member(jsii_name="overrideLogicalId")
    def override_logical_id(self, new_logical_id: builtins.str) -> None:
        '''(experimental) Overrides the auto-generated logical ID with a specific ID.

        :param new_logical_id: The new logical ID to use for this stack element.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "overrideLogicalId", [new_logical_id]))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cdktfStack")
    def cdktf_stack(self) -> "TerraformStack":
        '''
        :stability: experimental
        '''
        return typing.cast("TerraformStack", jsii.get(self, "cdktfStack"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="constructNode")
    def construct_node(self) -> constructs.Node:
        '''
        :stability: experimental
        '''
        return typing.cast(constructs.Node, jsii.get(self, "constructNode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="constructNodeMetadata")
    def _construct_node_metadata(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "constructNodeMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="friendlyUniqueId")
    def friendly_unique_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "friendlyUniqueId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rawOverrides")
    def _raw_overrides(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "rawOverrides"))


@jsii.data_type(
    jsii_type="cdktf.TerraformElementMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "stack_trace": "stackTrace",
        "unique_id": "uniqueId",
    },
)
class TerraformElementMetadata:
    def __init__(
        self,
        *,
        path: builtins.str,
        stack_trace: typing.Sequence[builtins.str],
        unique_id: builtins.str,
    ) -> None:
        '''
        :param path: 
        :param stack_trace: 
        :param unique_id: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
            "stack_trace": stack_trace,
            "unique_id": unique_id,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_trace(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("stack_trace")
        assert result is not None, "Required property 'stack_trace' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def unique_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("unique_id")
        assert result is not None, "Required property 'unique_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformElementMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformLocal(
    TerraformElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformLocal",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        expression: typing.Any,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param expression: -

        :stability: experimental
        '''
        jsii.create(TerraformLocal, self, [scope, id, expression])

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="asBoolean")
    def as_boolean(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "asBoolean"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="asList")
    def as_list(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "asList"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="asNumber")
    def as_number(self) -> jsii.Number:
        '''
        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "asNumber"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="asString")
    def as_string(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "asString"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expression")
    def expression(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: typing.Any) -> None:
        jsii.set(self, "expression", value)


@jsii.data_type(
    jsii_type="cdktf.TerraformMetaArguments",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
    },
)
class TerraformMetaArguments:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        lifecycle: typing.Optional["TerraformResourceLifecycle"] = None,
        provider: typing.Optional["TerraformProvider"] = None,
    ) -> None:
        '''
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 

        :stability: experimental
        '''
        if isinstance(lifecycle, dict):
            lifecycle = TerraformResourceLifecycle(**lifecycle)
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional["TerraformResourceLifecycle"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional["TerraformResourceLifecycle"], result)

    @builtins.property
    def provider(self) -> typing.Optional["TerraformProvider"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional["TerraformProvider"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformMetaArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ITerraformDependable)
class TerraformModule(
    TerraformElement,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdktf.TerraformModule",
):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_TerraformModuleProxy"]:
        return _TerraformModuleProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        source: builtins.str,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        providers: typing.Optional[typing.Sequence[typing.Union["TerraformModuleProvider", "TerraformProvider"]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param source: 
        :param depends_on: 
        :param providers: 
        :param version: 

        :stability: experimental
        '''
        options = TerraformModuleOptions(
            source=source, depends_on=depends_on, providers=providers, version=version
        )

        jsii.create(TerraformModule, self, [scope, id, options])

    @jsii.member(jsii_name="addProvider")
    def add_provider(
        self,
        provider: typing.Union["TerraformModuleProvider", "TerraformProvider"],
    ) -> None:
        '''
        :param provider: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addProvider", [provider]))

    @jsii.member(jsii_name="interpolationForOutput")
    def interpolation_for_output(self, module_output: builtins.str) -> typing.Any:
        '''
        :param module_output: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "interpolationForOutput", [module_output]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="providers")
    def providers(
        self,
    ) -> typing.Optional[typing.List[typing.Union["TerraformModuleProvider", "TerraformProvider"]]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[typing.Union["TerraformModuleProvider", "TerraformProvider"]]], jsii.get(self, "providers"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dependsOn"))

    @depends_on.setter
    def depends_on(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "dependsOn", value)


class _TerraformModuleProxy(TerraformModule):
    pass


@jsii.data_type(
    jsii_type="cdktf.TerraformModuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "depends_on": "dependsOn",
        "providers": "providers",
        "version": "version",
    },
)
class TerraformModuleOptions:
    def __init__(
        self,
        *,
        source: builtins.str,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        providers: typing.Optional[typing.Sequence[typing.Union["TerraformModuleProvider", "TerraformProvider"]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: 
        :param depends_on: 
        :param providers: 
        :param version: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if providers is not None:
            self._values["providers"] = providers
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def source(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[ITerraformDependable]], result)

    @builtins.property
    def providers(
        self,
    ) -> typing.Optional[typing.List[typing.Union["TerraformModuleProvider", "TerraformProvider"]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List[typing.Union["TerraformModuleProvider", "TerraformProvider"]]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformModuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.TerraformModuleProvider",
    jsii_struct_bases=[],
    name_mapping={"module_alias": "moduleAlias", "provider": "provider"},
)
class TerraformModuleProvider:
    def __init__(
        self,
        *,
        module_alias: builtins.str,
        provider: "TerraformProvider",
    ) -> None:
        '''
        :param module_alias: 
        :param provider: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "module_alias": module_alias,
            "provider": provider,
        }

    @builtins.property
    def module_alias(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("module_alias")
        assert result is not None, "Required property 'module_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider(self) -> "TerraformProvider":
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast("TerraformProvider", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformModuleProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformOutput(
    TerraformElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformOutput",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        description: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[builtins.bool] = None,
        value: typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.Sequence[typing.Any], typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param depends_on: 
        :param description: 
        :param sensitive: 
        :param value: 

        :stability: experimental
        '''
        config = TerraformOutputConfig(
            depends_on=depends_on,
            description=description,
            sensitive=sensitive,
            value=value,
        )

        jsii.create(TerraformOutput, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.Optional[typing.List[ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[ITerraformDependable]], jsii.get(self, "dependsOn"))

    @depends_on.setter
    def depends_on(
        self,
        value: typing.Optional[typing.List[ITerraformDependable]],
    ) -> None:
        jsii.set(self, "dependsOn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sensitive")
    def sensitive(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "sensitive"))

    @sensitive.setter
    def sensitive(self, value: typing.Optional[builtins.bool]) -> None:
        jsii.set(self, "sensitive", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.List[typing.Any], typing.Mapping[builtins.str, typing.Any]]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.List[typing.Any], typing.Mapping[builtins.str, typing.Any]]], jsii.get(self, "value"))

    @value.setter
    def value(
        self,
        value: typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.List[typing.Any], typing.Mapping[builtins.str, typing.Any]]],
    ) -> None:
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="cdktf.TerraformOutputConfig",
    jsii_struct_bases=[],
    name_mapping={
        "depends_on": "dependsOn",
        "description": "description",
        "sensitive": "sensitive",
        "value": "value",
    },
)
class TerraformOutputConfig:
    def __init__(
        self,
        *,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        description: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[builtins.bool] = None,
        value: typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.Sequence[typing.Any], typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param depends_on: 
        :param description: 
        :param sensitive: 
        :param value: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if description is not None:
            self._values["description"] = description
        if sensitive is not None:
            self._values["sensitive"] = sensitive
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[ITerraformDependable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sensitive")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def value(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.List[typing.Any], typing.Mapping[builtins.str, typing.Any]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.List[typing.Any], typing.Mapping[builtins.str, typing.Any]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformOutputConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformProvider(
    TerraformElement,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdktf.TerraformProvider",
):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_TerraformProviderProxy"]:
        return _TerraformProviderProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        terraform_resource_type: builtins.str,
        terraform_generator_metadata: typing.Optional["TerraformProviderGeneratorMetadata"] = None,
        terraform_provider_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param terraform_resource_type: 
        :param terraform_generator_metadata: 
        :param terraform_provider_source: 

        :stability: experimental
        '''
        config = TerraformProviderConfig(
            terraform_resource_type=terraform_resource_type,
            terraform_generator_metadata=terraform_generator_metadata,
            terraform_provider_source=terraform_provider_source,
        )

        jsii.create(TerraformProvider, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''(experimental) Adds this resource to the terraform JSON output.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metaAttributes")
    def meta_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "metaAttributes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResourceType")
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformGeneratorMetadata")
    def terraform_generator_metadata(
        self,
    ) -> typing.Optional["TerraformProviderGeneratorMetadata"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional["TerraformProviderGeneratorMetadata"], jsii.get(self, "terraformGeneratorMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformProviderSource")
    def terraform_provider_source(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "terraformProviderSource"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "alias", value)


class _TerraformProviderProxy(TerraformProvider):
    pass


@jsii.data_type(
    jsii_type="cdktf.TerraformProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "terraform_resource_type": "terraformResourceType",
        "terraform_generator_metadata": "terraformGeneratorMetadata",
        "terraform_provider_source": "terraformProviderSource",
    },
)
class TerraformProviderConfig:
    def __init__(
        self,
        *,
        terraform_resource_type: builtins.str,
        terraform_generator_metadata: typing.Optional["TerraformProviderGeneratorMetadata"] = None,
        terraform_provider_source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param terraform_resource_type: 
        :param terraform_generator_metadata: 
        :param terraform_provider_source: 

        :stability: experimental
        '''
        if isinstance(terraform_generator_metadata, dict):
            terraform_generator_metadata = TerraformProviderGeneratorMetadata(**terraform_generator_metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "terraform_resource_type": terraform_resource_type,
        }
        if terraform_generator_metadata is not None:
            self._values["terraform_generator_metadata"] = terraform_generator_metadata
        if terraform_provider_source is not None:
            self._values["terraform_provider_source"] = terraform_provider_source

    @builtins.property
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("terraform_resource_type")
        assert result is not None, "Required property 'terraform_resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def terraform_generator_metadata(
        self,
    ) -> typing.Optional["TerraformProviderGeneratorMetadata"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("terraform_generator_metadata")
        return typing.cast(typing.Optional["TerraformProviderGeneratorMetadata"], result)

    @builtins.property
    def terraform_provider_source(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("terraform_provider_source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.TerraformProviderGeneratorMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "provider_name": "providerName",
        "provider_version_constraint": "providerVersionConstraint",
    },
)
class TerraformProviderGeneratorMetadata:
    def __init__(
        self,
        *,
        provider_name: builtins.str,
        provider_version_constraint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param provider_name: 
        :param provider_version_constraint: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "provider_name": provider_name,
        }
        if provider_version_constraint is not None:
            self._values["provider_version_constraint"] = provider_version_constraint

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_version_constraint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider_version_constraint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformProviderGeneratorMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformRemoteState(
    TerraformElement,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdktf.TerraformRemoteState",
):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_TerraformRemoteStateProxy"]:
        return _TerraformRemoteStateProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        backend: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param backend: -
        :param defaults: 
        :param workspace: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateConfig(defaults=defaults, workspace=workspace)

        jsii.create(TerraformRemoteState, self, [scope, id, backend, config])

    @jsii.member(jsii_name="get")
    def get(self, output: builtins.str) -> typing.Any:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "get", [output]))

    @jsii.member(jsii_name="getBoolean")
    def get_boolean(self, output: builtins.str) -> builtins.bool:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "getBoolean", [output]))

    @jsii.member(jsii_name="getList")
    def get_list(self, output: builtins.str) -> typing.List[builtins.str]:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getList", [output]))

    @jsii.member(jsii_name="getNumber")
    def get_number(self, output: builtins.str) -> jsii.Number:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "getNumber", [output]))

    @jsii.member(jsii_name="getString")
    def get_string(self, output: builtins.str) -> builtins.str:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getString", [output]))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''(experimental) Adds this resource to the terraform JSON output.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))


class _TerraformRemoteStateProxy(TerraformRemoteState):
    pass


@jsii.implements(ITerraformResource, ITerraformDependable)
class TerraformResource(
    TerraformElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformResource",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        terraform_resource_type: builtins.str,
        terraform_generator_metadata: typing.Optional[TerraformProviderGeneratorMetadata] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        lifecycle: typing.Optional["TerraformResourceLifecycle"] = None,
        provider: typing.Optional[TerraformProvider] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param terraform_resource_type: 
        :param terraform_generator_metadata: 
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 

        :stability: experimental
        '''
        config = TerraformResourceConfig(
            terraform_resource_type=terraform_resource_type,
            terraform_generator_metadata=terraform_generator_metadata,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(TerraformResource, self, [scope, id, config])

    @jsii.member(jsii_name="getBooleanAttribute")
    def get_boolean_attribute(self, terraform_attribute: builtins.str) -> builtins.bool:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "getBooleanAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getListAttribute")
    def get_list_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> typing.List[builtins.str]:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getListAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getNumberAttribute")
    def get_number_attribute(self, terraform_attribute: builtins.str) -> jsii.Number:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "getNumberAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getStringAttribute")
    def get_string_attribute(self, terraform_attribute: builtins.str) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getStringAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="interpolationForAttribute")
    def interpolation_for_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "interpolationForAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''(experimental) Adds this resource to the terraform JSON output.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformMetaArguments")
    def terraform_meta_arguments(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "terraformMetaArguments"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResourceType")
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformGeneratorMetadata")
    def terraform_generator_metadata(
        self,
    ) -> typing.Optional[TerraformProviderGeneratorMetadata]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TerraformProviderGeneratorMetadata], jsii.get(self, "terraformGeneratorMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "count"))

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "count", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dependsOn"))

    @depends_on.setter
    def depends_on(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "dependsOn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycle")
    def lifecycle(self) -> typing.Optional["TerraformResourceLifecycle"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional["TerraformResourceLifecycle"], jsii.get(self, "lifecycle"))

    @lifecycle.setter
    def lifecycle(self, value: typing.Optional["TerraformResourceLifecycle"]) -> None:
        jsii.set(self, "lifecycle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[TerraformProvider]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TerraformProvider], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[TerraformProvider]) -> None:
        jsii.set(self, "provider", value)


@jsii.data_type(
    jsii_type="cdktf.TerraformResourceConfig",
    jsii_struct_bases=[TerraformMetaArguments],
    name_mapping={
        "count": "count",
        "depends_on": "dependsOn",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "terraform_resource_type": "terraformResourceType",
        "terraform_generator_metadata": "terraformGeneratorMetadata",
    },
)
class TerraformResourceConfig(TerraformMetaArguments):
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        lifecycle: typing.Optional["TerraformResourceLifecycle"] = None,
        provider: typing.Optional[TerraformProvider] = None,
        terraform_resource_type: builtins.str,
        terraform_generator_metadata: typing.Optional[TerraformProviderGeneratorMetadata] = None,
    ) -> None:
        '''
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 
        :param terraform_resource_type: 
        :param terraform_generator_metadata: 

        :stability: experimental
        '''
        if isinstance(lifecycle, dict):
            lifecycle = TerraformResourceLifecycle(**lifecycle)
        if isinstance(terraform_generator_metadata, dict):
            terraform_generator_metadata = TerraformProviderGeneratorMetadata(**terraform_generator_metadata)
        self._values: typing.Dict[str, typing.Any] = {
            "terraform_resource_type": terraform_resource_type,
        }
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if terraform_generator_metadata is not None:
            self._values["terraform_generator_metadata"] = terraform_generator_metadata

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[ITerraformDependable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional["TerraformResourceLifecycle"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional["TerraformResourceLifecycle"], result)

    @builtins.property
    def provider(self) -> typing.Optional[TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[TerraformProvider], result)

    @builtins.property
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("terraform_resource_type")
        assert result is not None, "Required property 'terraform_resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def terraform_generator_metadata(
        self,
    ) -> typing.Optional[TerraformProviderGeneratorMetadata]:
        '''
        :stability: experimental
        '''
        result = self._values.get("terraform_generator_metadata")
        return typing.cast(typing.Optional[TerraformProviderGeneratorMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformResourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.TerraformResourceLifecycle",
    jsii_struct_bases=[],
    name_mapping={
        "create_before_destroy": "createBeforeDestroy",
        "ignore_changes": "ignoreChanges",
        "prevent_destroy": "preventDestroy",
    },
)
class TerraformResourceLifecycle:
    def __init__(
        self,
        *,
        create_before_destroy: typing.Optional[builtins.bool] = None,
        ignore_changes: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_destroy: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param create_before_destroy: 
        :param ignore_changes: 
        :param prevent_destroy: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if create_before_destroy is not None:
            self._values["create_before_destroy"] = create_before_destroy
        if ignore_changes is not None:
            self._values["ignore_changes"] = ignore_changes
        if prevent_destroy is not None:
            self._values["prevent_destroy"] = prevent_destroy

    @builtins.property
    def create_before_destroy(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("create_before_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_changes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ignore_changes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prevent_destroy(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prevent_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformResourceLifecycle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformStack(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformStack",
):
    '''
    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        jsii.create(TerraformStack, self, [scope, id])

    @jsii.member(jsii_name="isStack") # type: ignore[misc]
    @builtins.classmethod
    def is_stack(cls, x: typing.Any) -> builtins.bool:
        '''
        :param x: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStack", [x]))

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, construct: constructs.IConstruct) -> "TerraformStack":
        '''
        :param construct: -

        :stability: experimental
        '''
        return typing.cast("TerraformStack", jsii.sinvoke(cls, "of", [construct]))

    @jsii.member(jsii_name="addOverride")
    def add_override(self, path: builtins.str, value: typing.Any) -> None:
        '''
        :param path: -
        :param value: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addOverride", [path, value]))

    @jsii.member(jsii_name="allocateLogicalId")
    def _allocate_logical_id(
        self,
        tf_element: typing.Union[TerraformElement, constructs.Node],
    ) -> builtins.str:
        '''(experimental) Returns the naming scheme used to allocate logical IDs.

        By default, uses
        the ``HashedAddressingScheme`` but this method can be overridden to customize
        this behavior.

        :param tf_element: The element for which the logical ID is allocated.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "allocateLogicalId", [tf_element]))

    @jsii.member(jsii_name="allProviders")
    def all_providers(self) -> typing.List[TerraformProvider]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[TerraformProvider], jsii.invoke(self, "allProviders", []))

    @jsii.member(jsii_name="getLogicalId")
    def get_logical_id(
        self,
        tf_element: typing.Union[TerraformElement, constructs.Node],
    ) -> builtins.str:
        '''
        :param tf_element: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getLogicalId", [tf_element]))

    @jsii.member(jsii_name="onSynthesize")
    def _on_synthesize(self, session: constructs.ISynthesisSession) -> None:
        '''(experimental) Allows this construct to emit artifacts into the cloud assembly during synthesis.

        This method is usually implemented by framework-level constructs such as ``Stack`` and ``Asset``
        as they participate in synthesizing the cloud assembly.

        :param session: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "onSynthesize", [session]))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))


@jsii.data_type(
    jsii_type="cdktf.TerraformStackMetadata",
    jsii_struct_bases=[],
    name_mapping={"stack_name": "stackName", "version": "version"},
)
class TerraformStackMetadata:
    def __init__(self, *, stack_name: builtins.str, version: builtins.str) -> None:
        '''
        :param stack_name: 
        :param version: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "stack_name": stack_name,
            "version": version,
        }

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformStackMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TerraformVariable(
    TerraformElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformVariable",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        default: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[builtins.bool] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default: 
        :param description: 
        :param sensitive: 
        :param type: (experimental) The type argument in a variable block allows you to restrict the type of value that will be accepted as the value for a variable. If no type constraint is set then a value of any type is accepted. While type constraints are optional, we recommend specifying them; they serve as easy reminders for users of the module, and allow Terraform to return a helpful error message if the wrong type is used. Type constraints are created from a mixture of type keywords and type constructors. The supported type keywords are: - string - number - bool The type constructors allow you to specify complex types such as collections: - list(<TYPE>) - set(<TYPE>) - map(<TYPE>) - object({<ATTR NAME> = <TYPE>, ... }) - tuple([<TYPE>, ...]) The keyword any may be used to indicate that any type is acceptable. For more information on the meaning and behavior of these different types, as well as detailed information about automatic conversion of complex types, see {@link https://www.terraform.io/docs/configuration/types.html|Type Constraints}. If both the type and default arguments are specified, the given default value must be convertible to the specified type.

        :stability: experimental
        '''
        config = TerraformVariableConfig(
            default=default, description=description, sensitive=sensitive, type=type
        )

        jsii.create(TerraformVariable, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="booleanValue")
    def boolean_value(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "booleanValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listValue")
    def list_value(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="numberValue")
    def number_value(self) -> jsii.Number:
        '''
        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "numberValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="default")
    def default(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "default"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sensitive")
    def sensitive(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "sensitive"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))


@jsii.data_type(
    jsii_type="cdktf.TerraformVariableConfig",
    jsii_struct_bases=[],
    name_mapping={
        "default": "default",
        "description": "description",
        "sensitive": "sensitive",
        "type": "type",
    },
)
class TerraformVariableConfig:
    def __init__(
        self,
        *,
        default: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        sensitive: typing.Optional[builtins.bool] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default: 
        :param description: 
        :param sensitive: 
        :param type: (experimental) The type argument in a variable block allows you to restrict the type of value that will be accepted as the value for a variable. If no type constraint is set then a value of any type is accepted. While type constraints are optional, we recommend specifying them; they serve as easy reminders for users of the module, and allow Terraform to return a helpful error message if the wrong type is used. Type constraints are created from a mixture of type keywords and type constructors. The supported type keywords are: - string - number - bool The type constructors allow you to specify complex types such as collections: - list(<TYPE>) - set(<TYPE>) - map(<TYPE>) - object({<ATTR NAME> = <TYPE>, ... }) - tuple([<TYPE>, ...]) The keyword any may be used to indicate that any type is acceptable. For more information on the meaning and behavior of these different types, as well as detailed information about automatic conversion of complex types, see {@link https://www.terraform.io/docs/configuration/types.html|Type Constraints}. If both the type and default arguments are specified, the given default value must be convertible to the specified type.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default
        if description is not None:
            self._values["description"] = description
        if sensitive is not None:
            self._values["sensitive"] = sensitive
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def default(self) -> typing.Any:
        '''
        :stability: experimental
        '''
        result = self._values.get("default")
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sensitive")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''(experimental) The type argument in a variable block allows you to restrict the type of value that will be accepted as the value for a variable.

        If no type constraint is set then a value of any type is accepted.

        While type constraints are optional, we recommend specifying them; they serve as easy reminders for users of the module, and allow Terraform to return a helpful error message if the wrong type is used.

        Type constraints are created from a mixture of type keywords and type constructors. The supported type keywords are:

        - string
        - number
        - bool

        The type constructors allow you to specify complex types such as collections:

        - list()
        - set()
        - map()
        - object({ = , ... })
        - tuple([, ...])

        The keyword any may be used to indicate that any type is acceptable. For more information on the meaning and behavior of these different types, as well as detailed information about automatic conversion of complex types, see {@link https://www.terraform.io/docs/configuration/types.html|Type Constraints}.

        If both the type and default arguments are specified, the given default value must be convertible to the specified type.

        :stability: experimental
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformVariableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Testing(metaclass=jsii.JSIIMeta, jsii_type="cdktf.Testing"):
    '''(experimental) Testing utilities for cdktf applications.

    :stability: experimental
    '''

    @jsii.member(jsii_name="app") # type: ignore[misc]
    @builtins.classmethod
    def app(cls) -> App:
        '''(experimental) Returns an app for testing with the following properties: - Output directory is a temp dir.

        :stability: experimental
        '''
        return typing.cast(App, jsii.sinvoke(cls, "app", []))

    @jsii.member(jsii_name="enableFutureFlags") # type: ignore[misc]
    @builtins.classmethod
    def enable_future_flags(cls, app: App) -> App:
        '''
        :param app: -

        :stability: experimental
        '''
        return typing.cast(App, jsii.sinvoke(cls, "enableFutureFlags", [app]))

    @jsii.member(jsii_name="stubVersion") # type: ignore[misc]
    @builtins.classmethod
    def stub_version(cls, app: App) -> App:
        '''
        :param app: -

        :stability: experimental
        '''
        return typing.cast(App, jsii.sinvoke(cls, "stubVersion", [app]))

    @jsii.member(jsii_name="synth") # type: ignore[misc]
    @builtins.classmethod
    def synth(cls, stack: TerraformStack) -> builtins.str:
        '''(experimental) Returns the Terraform synthesized JSON.

        :param stack: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "synth", [stack]))


class Token(metaclass=jsii.JSIIMeta, jsii_type="cdktf.Token"):
    '''(experimental) Represents a special or lazily-evaluated value.

    Can be used to delay evaluation of a certain value in case, for example,
    that it requires some context or late-bound data. Can also be used to
    mark values that need special processing at document rendering time.

    Tokens can be embedded into strings while retaining their original
    semantics.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(Token, self, [])

    @jsii.member(jsii_name="asAny") # type: ignore[misc]
    @builtins.classmethod
    def as_any(cls, value: typing.Any) -> IResolvable:
        '''(experimental) Return a resolvable representation of the given value.

        :param value: -

        :stability: experimental
        '''
        return typing.cast(IResolvable, jsii.sinvoke(cls, "asAny", [value]))

    @jsii.member(jsii_name="asList") # type: ignore[misc]
    @builtins.classmethod
    def as_list(
        cls,
        value: typing.Any,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''(experimental) Return a reversible list representation of this token.

        :param value: -
        :param display_hint: (experimental) A hint for the Token's purpose when stringifying it. Default: - no display hint

        :stability: experimental
        '''
        options = EncodingOptions(display_hint=display_hint)

        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "asList", [value, options]))

    @jsii.member(jsii_name="asNumber") # type: ignore[misc]
    @builtins.classmethod
    def as_number(cls, value: typing.Any) -> jsii.Number:
        '''(experimental) Return a reversible number representation of this token.

        :param value: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "asNumber", [value]))

    @jsii.member(jsii_name="asString") # type: ignore[misc]
    @builtins.classmethod
    def as_string(
        cls,
        value: typing.Any,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''(experimental) Return a reversible string representation of this token.

        If the Token is initialized with a literal, the stringified value of the
        literal is returned. Otherwise, a special quoted string representation
        of the Token is returned that can be embedded into other strings.

        Strings with quoted Tokens in them can be restored back into
        complex values with the Tokens restored by calling ``resolve()``
        on the string.

        :param value: -
        :param display_hint: (experimental) A hint for the Token's purpose when stringifying it. Default: - no display hint

        :stability: experimental
        '''
        options = EncodingOptions(display_hint=display_hint)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "asString", [value, options]))

    @jsii.member(jsii_name="isUnresolved") # type: ignore[misc]
    @builtins.classmethod
    def is_unresolved(cls, obj: typing.Any) -> builtins.bool:
        '''(experimental) Returns true if obj represents an unresolved value.

        One of these must be true:

        - ``obj`` is an IResolvable
        - ``obj`` is a string containing at least one encoded ``IResolvable``
        - ``obj`` is either an encoded number or list

        This does NOT recurse into lists or objects to see if they
        containing resolvables.

        :param obj: The object to test.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isUnresolved", [obj]))


class Tokenization(metaclass=jsii.JSIIMeta, jsii_type="cdktf.Tokenization"):
    '''(experimental) Less oft-needed functions to manipulate Tokens.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(Tokenization, self, [])

    @jsii.member(jsii_name="isResolvable") # type: ignore[misc]
    @builtins.classmethod
    def is_resolvable(cls, obj: typing.Any) -> builtins.bool:
        '''(experimental) Return whether the given object is an IResolvable object.

        This is different from Token.isUnresolved() which will also check for
        encoded Tokens, whereas this method will only do a type check on the given
        object.

        :param obj: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isResolvable", [obj]))

    @jsii.member(jsii_name="resolve") # type: ignore[misc]
    @builtins.classmethod
    def resolve(
        cls,
        obj: typing.Any,
        *,
        resolver: ITokenResolver,
        scope: constructs.IConstruct,
        preparing: typing.Optional[builtins.bool] = None,
    ) -> typing.Any:
        '''(experimental) Resolves an object by evaluating all tokens and removing any undefined or empty objects or arrays.

        Values can only be primitives, arrays or tokens. Other objects (i.e. with methods) will be rejected.

        :param obj: The object to resolve.
        :param resolver: (experimental) The resolver to apply to any resolvable tokens found.
        :param scope: (experimental) The scope from which resolution is performed.
        :param preparing: (experimental) Whether the resolution is being executed during the prepare phase or not. Default: false

        :stability: experimental
        '''
        options = ResolveOptions(resolver=resolver, scope=scope, preparing=preparing)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolve", [obj, options]))

    @jsii.member(jsii_name="reverseList") # type: ignore[misc]
    @builtins.classmethod
    def reverse_list(
        cls,
        l: typing.Sequence[builtins.str],
    ) -> typing.Optional[IResolvable]:
        '''(experimental) Un-encode a Tokenized value from a list.

        :param l: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IResolvable], jsii.sinvoke(cls, "reverseList", [l]))

    @jsii.member(jsii_name="reverseNumber") # type: ignore[misc]
    @builtins.classmethod
    def reverse_number(cls, n: jsii.Number) -> typing.Optional[IResolvable]:
        '''(experimental) Un-encode a Tokenized value from a number.

        :param n: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IResolvable], jsii.sinvoke(cls, "reverseNumber", [n]))

    @jsii.member(jsii_name="reverseString") # type: ignore[misc]
    @builtins.classmethod
    def reverse_string(cls, s: builtins.str) -> "TokenizedStringFragments":
        '''(experimental) Un-encode a string potentially containing encoded tokens.

        :param s: -

        :stability: experimental
        '''
        return typing.cast("TokenizedStringFragments", jsii.sinvoke(cls, "reverseString", [s]))

    @jsii.member(jsii_name="stringifyNumber") # type: ignore[misc]
    @builtins.classmethod
    def stringify_number(cls, x: jsii.Number) -> builtins.str:
        '''(experimental) Stringify a number directly or lazily if it's a Token.

        If it is an object (i.e., { Ref: 'SomeLogicalId' }), return it as-is.

        :param x: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "stringifyNumber", [x]))


class TokenizedStringFragments(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TokenizedStringFragments",
):
    '''(experimental) Fragments of a concatenated string containing stringified Tokens.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(TokenizedStringFragments, self, [])

    @jsii.member(jsii_name="addIntrinsic")
    def add_intrinsic(self, value: typing.Any) -> None:
        '''(experimental) Adds an intrinsic fragment.

        :param value: the intrinsic value to add.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addIntrinsic", [value]))

    @jsii.member(jsii_name="addLiteral")
    def add_literal(self, lit: typing.Any) -> None:
        '''(experimental) Adds a literal fragment.

        :param lit: the literal to add.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addLiteral", [lit]))

    @jsii.member(jsii_name="addToken")
    def add_token(self, token: IResolvable) -> None:
        '''(experimental) Adds a token fragment.

        :param token: the token to add.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addToken", [token]))

    @jsii.member(jsii_name="join")
    def join(self, concat: IFragmentConcatenator) -> typing.Any:
        '''(experimental) Combine the string fragments using the given joiner.

        If there are any

        :param concat: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "join", [concat]))

    @jsii.member(jsii_name="mapTokens")
    def map_tokens(self, mapper: ITokenMapper) -> "TokenizedStringFragments":
        '''(experimental) Apply a transformation function to all tokens in the string.

        :param mapper: -

        :stability: experimental
        '''
        return typing.cast("TokenizedStringFragments", jsii.invoke(self, "mapTokens", [mapper]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firstValue")
    def first_value(self) -> typing.Any:
        '''(experimental) Returns the first value.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "firstValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        '''(experimental) Returns the number of fragments.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokens")
    def tokens(self) -> typing.List[IResolvable]:
        '''(experimental) Return all Tokens from this string.

        :stability: experimental
        '''
        return typing.cast(typing.List[IResolvable], jsii.get(self, "tokens"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firstToken")
    def first_token(self) -> typing.Optional[IResolvable]:
        '''(experimental) Returns the first token.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IResolvable], jsii.get(self, "firstToken"))


class VariableType(metaclass=jsii.JSIIAbstractClass, jsii_type="cdktf.VariableType"):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_VariableTypeProxy"]:
        return _VariableTypeProxy

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(VariableType, self, [])

    @jsii.member(jsii_name="list") # type: ignore[misc]
    @builtins.classmethod
    def list(cls, type: builtins.str) -> builtins.str:
        '''
        :param type: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "list", [type]))

    @jsii.member(jsii_name="map") # type: ignore[misc]
    @builtins.classmethod
    def map(cls, type: builtins.str) -> builtins.str:
        '''
        :param type: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "map", [type]))

    @jsii.member(jsii_name="object") # type: ignore[misc]
    @builtins.classmethod
    def object(
        cls,
        attributes: typing.Mapping[builtins.str, builtins.str],
    ) -> builtins.str:
        '''
        :param attributes: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "object", [attributes]))

    @jsii.member(jsii_name="set") # type: ignore[misc]
    @builtins.classmethod
    def set(cls, type: builtins.str) -> builtins.str:
        '''
        :param type: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "set", [type]))

    @jsii.member(jsii_name="tuple") # type: ignore[misc]
    @builtins.classmethod
    def tuple(cls, *elements: builtins.str) -> builtins.str:
        '''
        :param elements: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "tuple", [*elements]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="ANY")
    def ANY(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ANY"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="BOOL")
    def BOOL(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BOOL"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="LIST")
    def LIST(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LIST"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="LIST_BOOL")
    def LIST_BOOL(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LIST_BOOL"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="LIST_NUMBER")
    def LIST_NUMBER(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LIST_NUMBER"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="LIST_STRING")
    def LIST_STRING(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LIST_STRING"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="MAP")
    def MAP(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MAP"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="MAP_BOOL")
    def MAP_BOOL(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MAP_BOOL"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="MAP_NUMBER")
    def MAP_NUMBER(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MAP_NUMBER"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="MAP_STRING")
    def MAP_STRING(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MAP_STRING"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="NUMBER")
    def NUMBER(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NUMBER"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="SET")
    def SET(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SET"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="SET_BOOL")
    def SET_BOOL(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SET_BOOL"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="SET_NUMBER")
    def SET_NUMBER(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SET_NUMBER"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="SET_STRING")
    def SET_STRING(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SET_STRING"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="STRING")
    def STRING(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "STRING"))


class _VariableTypeProxy(VariableType):
    pass


class DataTerraformRemoteState(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteState",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        organization: builtins.str,
        workspaces: IRemoteWorkspace,
        hostname: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param organization: 
        :param workspaces: 
        :param hostname: 
        :param token: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateRemoteConfig(
            defaults=defaults,
            workspace=workspace,
            organization=organization,
            workspaces=workspaces,
            hostname=hostname,
            token=token,
        )

        jsii.create(DataTerraformRemoteState, self, [scope, id, config])


class DataTerraformRemoteStateArtifactory(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateArtifactory",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        password: builtins.str,
        repo: builtins.str,
        subpath: builtins.str,
        url: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param password: 
        :param repo: 
        :param subpath: 
        :param url: 
        :param username: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateArtifactoryConfig(
            defaults=defaults,
            workspace=workspace,
            password=password,
            repo=repo,
            subpath=subpath,
            url=url,
            username=username,
        )

        jsii.create(DataTerraformRemoteStateArtifactory, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateArtifactoryConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, ArtifactoryBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "password": "password",
        "repo": "repo",
        "subpath": "subpath",
        "url": "url",
        "username": "username",
    },
)
class DataTerraformRemoteStateArtifactoryConfig(
    DataTerraformRemoteStateConfig,
    ArtifactoryBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        password: builtins.str,
        repo: builtins.str,
        subpath: builtins.str,
        url: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param password: 
        :param repo: 
        :param subpath: 
        :param url: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "repo": repo,
            "subpath": subpath,
            "url": url,
            "username": username,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("repo")
        assert result is not None, "Required property 'repo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subpath(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("subpath")
        assert result is not None, "Required property 'subpath' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateArtifactoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateAzurerm(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateAzurerm",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        container_name: builtins.str,
        key: builtins.str,
        storage_account_name: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        sas_token: typing.Optional[builtins.str] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param container_name: 
        :param key: 
        :param storage_account_name: 
        :param access_key: 
        :param client_id: 
        :param client_secret: 
        :param endpoint: 
        :param environment: 
        :param msi_endpoint: 
        :param resource_group_name: 
        :param sas_token: 
        :param subscription_id: 
        :param tenant_id: 
        :param use_msi: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateAzurermConfig(
            defaults=defaults,
            workspace=workspace,
            container_name=container_name,
            key=key,
            storage_account_name=storage_account_name,
            access_key=access_key,
            client_id=client_id,
            client_secret=client_secret,
            endpoint=endpoint,
            environment=environment,
            msi_endpoint=msi_endpoint,
            resource_group_name=resource_group_name,
            sas_token=sas_token,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            use_msi=use_msi,
        )

        jsii.create(DataTerraformRemoteStateAzurerm, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateAzurermConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, AzurermBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "container_name": "containerName",
        "key": "key",
        "storage_account_name": "storageAccountName",
        "access_key": "accessKey",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "endpoint": "endpoint",
        "environment": "environment",
        "msi_endpoint": "msiEndpoint",
        "resource_group_name": "resourceGroupName",
        "sas_token": "sasToken",
        "subscription_id": "subscriptionId",
        "tenant_id": "tenantId",
        "use_msi": "useMsi",
    },
)
class DataTerraformRemoteStateAzurermConfig(
    DataTerraformRemoteStateConfig,
    AzurermBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        container_name: builtins.str,
        key: builtins.str,
        storage_account_name: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        sas_token: typing.Optional[builtins.str] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param container_name: 
        :param key: 
        :param storage_account_name: 
        :param access_key: 
        :param client_id: 
        :param client_secret: 
        :param endpoint: 
        :param environment: 
        :param msi_endpoint: 
        :param resource_group_name: 
        :param sas_token: 
        :param subscription_id: 
        :param tenant_id: 
        :param use_msi: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
            "key": key,
            "storage_account_name": storage_account_name,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if access_key is not None:
            self._values["access_key"] = access_key
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if environment is not None:
            self._values["environment"] = environment
        if msi_endpoint is not None:
            self._values["msi_endpoint"] = msi_endpoint
        if resource_group_name is not None:
            self._values["resource_group_name"] = resource_group_name
        if sas_token is not None:
            self._values["sas_token"] = sas_token
        if subscription_id is not None:
            self._values["subscription_id"] = subscription_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if use_msi is not None:
            self._values["use_msi"] = use_msi

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("storage_account_name")
        assert result is not None, "Required property 'storage_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("msi_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sas_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sas_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_msi(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_msi")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateAzurermConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateConsul(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateConsul",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        access_token: builtins.str,
        path: builtins.str,
        address: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        datacenter: typing.Optional[builtins.str] = None,
        gzip: typing.Optional[builtins.bool] = None,
        http_auth: typing.Optional[builtins.str] = None,
        key_file: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param access_token: 
        :param path: 
        :param address: 
        :param ca_file: 
        :param cert_file: 
        :param datacenter: 
        :param gzip: 
        :param http_auth: 
        :param key_file: 
        :param lock: 
        :param scheme: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateConsulConfig(
            defaults=defaults,
            workspace=workspace,
            access_token=access_token,
            path=path,
            address=address,
            ca_file=ca_file,
            cert_file=cert_file,
            datacenter=datacenter,
            gzip=gzip,
            http_auth=http_auth,
            key_file=key_file,
            lock=lock,
            scheme=scheme,
        )

        jsii.create(DataTerraformRemoteStateConsul, self, [scope, id, config])


class DataTerraformRemoteStateCos(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateCos",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param acl: 
        :param encrypt: 
        :param key: 
        :param prefix: 
        :param region: 
        :param secret_id: 
        :param secret_key: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateCosConfig(
            defaults=defaults,
            workspace=workspace,
            bucket=bucket,
            acl=acl,
            encrypt=encrypt,
            key=key,
            prefix=prefix,
            region=region,
            secret_id=secret_id,
            secret_key=secret_key,
        )

        jsii.create(DataTerraformRemoteStateCos, self, [scope, id, config])


class DataTerraformRemoteStateEtcd(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateEtcd",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        endpoints: builtins.str,
        path: builtins.str,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param endpoints: 
        :param path: 
        :param password: 
        :param username: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateEtcdConfig(
            defaults=defaults,
            workspace=workspace,
            endpoints=endpoints,
            path=path,
            password=password,
            username=username,
        )

        jsii.create(DataTerraformRemoteStateEtcd, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateEtcdConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, EtcdBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "endpoints": "endpoints",
        "path": "path",
        "password": "password",
        "username": "username",
    },
)
class DataTerraformRemoteStateEtcdConfig(
    DataTerraformRemoteStateConfig,
    EtcdBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        endpoints: builtins.str,
        path: builtins.str,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param endpoints: 
        :param path: 
        :param password: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoints": endpoints,
            "path": path,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateEtcdConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateEtcdV3(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateEtcdV3",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        endpoints: typing.Sequence[builtins.str],
        cacert_path: typing.Optional[builtins.str] = None,
        cert_path: typing.Optional[builtins.str] = None,
        key_path: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        password: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param endpoints: 
        :param cacert_path: 
        :param cert_path: 
        :param key_path: 
        :param lock: 
        :param password: 
        :param prefix: 
        :param username: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateEtcdV3Config(
            defaults=defaults,
            workspace=workspace,
            endpoints=endpoints,
            cacert_path=cacert_path,
            cert_path=cert_path,
            key_path=key_path,
            lock=lock,
            password=password,
            prefix=prefix,
            username=username,
        )

        jsii.create(DataTerraformRemoteStateEtcdV3, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateEtcdV3Config",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, EtcdV3BackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "endpoints": "endpoints",
        "cacert_path": "cacertPath",
        "cert_path": "certPath",
        "key_path": "keyPath",
        "lock": "lock",
        "password": "password",
        "prefix": "prefix",
        "username": "username",
    },
)
class DataTerraformRemoteStateEtcdV3Config(
    DataTerraformRemoteStateConfig,
    EtcdV3BackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        endpoints: typing.Sequence[builtins.str],
        cacert_path: typing.Optional[builtins.str] = None,
        cert_path: typing.Optional[builtins.str] = None,
        key_path: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        password: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param endpoints: 
        :param cacert_path: 
        :param cert_path: 
        :param key_path: 
        :param lock: 
        :param password: 
        :param prefix: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoints": endpoints,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if cacert_path is not None:
            self._values["cacert_path"] = cacert_path
        if cert_path is not None:
            self._values["cert_path"] = cert_path
        if key_path is not None:
            self._values["key_path"] = key_path
        if lock is not None:
            self._values["lock"] = lock
        if password is not None:
            self._values["password"] = password
        if prefix is not None:
            self._values["prefix"] = prefix
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cacert_path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cacert_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cert_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateEtcdV3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateGcs(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateGcs",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param access_token: 
        :param credentials: 
        :param encryption_key: 
        :param prefix: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateGcsConfig(
            defaults=defaults,
            workspace=workspace,
            bucket=bucket,
            access_token=access_token,
            credentials=credentials,
            encryption_key=encryption_key,
            prefix=prefix,
        )

        jsii.create(DataTerraformRemoteStateGcs, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateGcsConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, GcsBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "bucket": "bucket",
        "access_token": "accessToken",
        "credentials": "credentials",
        "encryption_key": "encryptionKey",
        "prefix": "prefix",
    },
)
class DataTerraformRemoteStateGcsConfig(
    DataTerraformRemoteStateConfig,
    GcsBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param access_token: 
        :param credentials: 
        :param encryption_key: 
        :param prefix: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if access_token is not None:
            self._values["access_token"] = access_token
        if credentials is not None:
            self._values["credentials"] = credentials
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateGcsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateHttp(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateHttp",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        address: builtins.str,
        lock_address: typing.Optional[builtins.str] = None,
        lock_method: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        retry_max: typing.Optional[jsii.Number] = None,
        retry_wait_max: typing.Optional[jsii.Number] = None,
        retry_wait_min: typing.Optional[jsii.Number] = None,
        skip_cert_verification: typing.Optional[builtins.bool] = None,
        unlock_address: typing.Optional[builtins.str] = None,
        unlock_method: typing.Optional[builtins.str] = None,
        update_method: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param address: 
        :param lock_address: 
        :param lock_method: 
        :param password: 
        :param retry_max: 
        :param retry_wait_max: 
        :param retry_wait_min: 
        :param skip_cert_verification: 
        :param unlock_address: 
        :param unlock_method: 
        :param update_method: 
        :param username: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateHttpConfig(
            defaults=defaults,
            workspace=workspace,
            address=address,
            lock_address=lock_address,
            lock_method=lock_method,
            password=password,
            retry_max=retry_max,
            retry_wait_max=retry_wait_max,
            retry_wait_min=retry_wait_min,
            skip_cert_verification=skip_cert_verification,
            unlock_address=unlock_address,
            unlock_method=unlock_method,
            update_method=update_method,
            username=username,
        )

        jsii.create(DataTerraformRemoteStateHttp, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateHttpConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, HttpBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "address": "address",
        "lock_address": "lockAddress",
        "lock_method": "lockMethod",
        "password": "password",
        "retry_max": "retryMax",
        "retry_wait_max": "retryWaitMax",
        "retry_wait_min": "retryWaitMin",
        "skip_cert_verification": "skipCertVerification",
        "unlock_address": "unlockAddress",
        "unlock_method": "unlockMethod",
        "update_method": "updateMethod",
        "username": "username",
    },
)
class DataTerraformRemoteStateHttpConfig(
    DataTerraformRemoteStateConfig,
    HttpBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        address: builtins.str,
        lock_address: typing.Optional[builtins.str] = None,
        lock_method: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        retry_max: typing.Optional[jsii.Number] = None,
        retry_wait_max: typing.Optional[jsii.Number] = None,
        retry_wait_min: typing.Optional[jsii.Number] = None,
        skip_cert_verification: typing.Optional[builtins.bool] = None,
        unlock_address: typing.Optional[builtins.str] = None,
        unlock_method: typing.Optional[builtins.str] = None,
        update_method: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param address: 
        :param lock_address: 
        :param lock_method: 
        :param password: 
        :param retry_max: 
        :param retry_wait_max: 
        :param retry_wait_min: 
        :param skip_cert_verification: 
        :param unlock_address: 
        :param unlock_method: 
        :param update_method: 
        :param username: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if lock_address is not None:
            self._values["lock_address"] = lock_address
        if lock_method is not None:
            self._values["lock_method"] = lock_method
        if password is not None:
            self._values["password"] = password
        if retry_max is not None:
            self._values["retry_max"] = retry_max
        if retry_wait_max is not None:
            self._values["retry_wait_max"] = retry_wait_max
        if retry_wait_min is not None:
            self._values["retry_wait_min"] = retry_wait_min
        if skip_cert_verification is not None:
            self._values["skip_cert_verification"] = skip_cert_verification
        if unlock_address is not None:
            self._values["unlock_address"] = unlock_address
        if unlock_method is not None:
            self._values["unlock_method"] = unlock_method
        if update_method is not None:
            self._values["update_method"] = update_method
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def address(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lock_address(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock_method(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lock_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_max(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("retry_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_wait_max(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("retry_wait_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_wait_min(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("retry_wait_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_cert_verification(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_cert_verification")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def unlock_address(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("unlock_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unlock_method(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("unlock_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_method(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("update_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateHttpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateLocal(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateLocal",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        workspace_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param path: 
        :param workspace_dir: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateLocalConfig(
            defaults=defaults,
            workspace=workspace,
            path=path,
            workspace_dir=workspace_dir,
        )

        jsii.create(DataTerraformRemoteStateLocal, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateLocalConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, LocalBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "path": "path",
        "workspace_dir": "workspaceDir",
    },
)
class DataTerraformRemoteStateLocalConfig(
    DataTerraformRemoteStateConfig,
    LocalBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        workspace_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param path: 
        :param workspace_dir: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if path is not None:
            self._values["path"] = path
        if workspace_dir is not None:
            self._values["workspace_dir"] = workspace_dir

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_dir(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateLocalConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateManta(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateManta",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        account: builtins.str,
        key_id: builtins.str,
        path: builtins.str,
        insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
        key_material: typing.Optional[builtins.str] = None,
        object_name: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param account: 
        :param key_id: 
        :param path: 
        :param insecure_skip_tls_verify: 
        :param key_material: 
        :param object_name: 
        :param url: 
        :param user: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateMantaConfig(
            defaults=defaults,
            workspace=workspace,
            account=account,
            key_id=key_id,
            path=path,
            insecure_skip_tls_verify=insecure_skip_tls_verify,
            key_material=key_material,
            object_name=object_name,
            url=url,
            user=user,
        )

        jsii.create(DataTerraformRemoteStateManta, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateMantaConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, MantaBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "account": "account",
        "key_id": "keyId",
        "path": "path",
        "insecure_skip_tls_verify": "insecureSkipTlsVerify",
        "key_material": "keyMaterial",
        "object_name": "objectName",
        "url": "url",
        "user": "user",
    },
)
class DataTerraformRemoteStateMantaConfig(
    DataTerraformRemoteStateConfig,
    MantaBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        account: builtins.str,
        key_id: builtins.str,
        path: builtins.str,
        insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
        key_material: typing.Optional[builtins.str] = None,
        object_name: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param account: 
        :param key_id: 
        :param path: 
        :param insecure_skip_tls_verify: 
        :param key_material: 
        :param object_name: 
        :param url: 
        :param user: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "account": account,
            "key_id": key_id,
            "path": path,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if insecure_skip_tls_verify is not None:
            self._values["insecure_skip_tls_verify"] = insecure_skip_tls_verify
        if key_material is not None:
            self._values["key_material"] = key_material
        if object_name is not None:
            self._values["object_name"] = object_name
        if url is not None:
            self._values["url"] = url
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def insecure_skip_tls_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("insecure_skip_tls_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key_material(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key_material")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("object_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateMantaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateOss(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateOss",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role: typing.Optional[OssAssumeRole] = None,
        ecs_role_name: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        security_token: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        tablestore_endpoint: typing.Optional[builtins.str] = None,
        tablestore_table: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param access_key: 
        :param acl: 
        :param assume_role: 
        :param ecs_role_name: 
        :param encrypt: 
        :param endpoint: 
        :param key: 
        :param prefix: 
        :param profile: 
        :param region: 
        :param secret_key: 
        :param security_token: 
        :param shared_credentials_file: 
        :param tablestore_endpoint: 
        :param tablestore_table: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateOssConfig(
            defaults=defaults,
            workspace=workspace,
            bucket=bucket,
            access_key=access_key,
            acl=acl,
            assume_role=assume_role,
            ecs_role_name=ecs_role_name,
            encrypt=encrypt,
            endpoint=endpoint,
            key=key,
            prefix=prefix,
            profile=profile,
            region=region,
            secret_key=secret_key,
            security_token=security_token,
            shared_credentials_file=shared_credentials_file,
            tablestore_endpoint=tablestore_endpoint,
            tablestore_table=tablestore_table,
        )

        jsii.create(DataTerraformRemoteStateOss, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateOssConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, OssBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "bucket": "bucket",
        "access_key": "accessKey",
        "acl": "acl",
        "assume_role": "assumeRole",
        "ecs_role_name": "ecsRoleName",
        "encrypt": "encrypt",
        "endpoint": "endpoint",
        "key": "key",
        "prefix": "prefix",
        "profile": "profile",
        "region": "region",
        "secret_key": "secretKey",
        "security_token": "securityToken",
        "shared_credentials_file": "sharedCredentialsFile",
        "tablestore_endpoint": "tablestoreEndpoint",
        "tablestore_table": "tablestoreTable",
    },
)
class DataTerraformRemoteStateOssConfig(
    DataTerraformRemoteStateConfig,
    OssBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role: typing.Optional[OssAssumeRole] = None,
        ecs_role_name: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        security_token: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        tablestore_endpoint: typing.Optional[builtins.str] = None,
        tablestore_table: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param access_key: 
        :param acl: 
        :param assume_role: 
        :param ecs_role_name: 
        :param encrypt: 
        :param endpoint: 
        :param key: 
        :param prefix: 
        :param profile: 
        :param region: 
        :param secret_key: 
        :param security_token: 
        :param shared_credentials_file: 
        :param tablestore_endpoint: 
        :param tablestore_table: 

        :stability: experimental
        '''
        if isinstance(assume_role, dict):
            assume_role = OssAssumeRole(**assume_role)
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if access_key is not None:
            self._values["access_key"] = access_key
        if acl is not None:
            self._values["acl"] = acl
        if assume_role is not None:
            self._values["assume_role"] = assume_role
        if ecs_role_name is not None:
            self._values["ecs_role_name"] = ecs_role_name
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if key is not None:
            self._values["key"] = key
        if prefix is not None:
            self._values["prefix"] = prefix
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if security_token is not None:
            self._values["security_token"] = security_token
        if shared_credentials_file is not None:
            self._values["shared_credentials_file"] = shared_credentials_file
        if tablestore_endpoint is not None:
            self._values["tablestore_endpoint"] = tablestore_endpoint
        if tablestore_table is not None:
            self._values["tablestore_table"] = tablestore_table

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role(self) -> typing.Optional[OssAssumeRole]:
        '''
        :stability: experimental
        '''
        result = self._values.get("assume_role")
        return typing.cast(typing.Optional[OssAssumeRole], result)

    @builtins.property
    def ecs_role_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ecs_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("security_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_credentials_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("shared_credentials_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tablestore_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tablestore_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tablestore_table(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tablestore_table")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateOssConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStatePg(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStatePg",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        conn_str: builtins.str,
        schema_name: typing.Optional[builtins.str] = None,
        skip_schema_creation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param conn_str: 
        :param schema_name: 
        :param skip_schema_creation: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStatePgConfig(
            defaults=defaults,
            workspace=workspace,
            conn_str=conn_str,
            schema_name=schema_name,
            skip_schema_creation=skip_schema_creation,
        )

        jsii.create(DataTerraformRemoteStatePg, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStatePgConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, PgBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "conn_str": "connStr",
        "schema_name": "schemaName",
        "skip_schema_creation": "skipSchemaCreation",
    },
)
class DataTerraformRemoteStatePgConfig(DataTerraformRemoteStateConfig, PgBackendProps):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        conn_str: builtins.str,
        schema_name: typing.Optional[builtins.str] = None,
        skip_schema_creation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param conn_str: 
        :param schema_name: 
        :param skip_schema_creation: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "conn_str": conn_str,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if skip_schema_creation is not None:
            self._values["skip_schema_creation"] = skip_schema_creation

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conn_str(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("conn_str")
        assert result is not None, "Required property 'conn_str' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_schema_creation(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_schema_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStatePgConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateRemoteConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, RemoteBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "organization": "organization",
        "workspaces": "workspaces",
        "hostname": "hostname",
        "token": "token",
    },
)
class DataTerraformRemoteStateRemoteConfig(
    DataTerraformRemoteStateConfig,
    RemoteBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        organization: builtins.str,
        workspaces: IRemoteWorkspace,
        hostname: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param organization: 
        :param workspaces: 
        :param hostname: 
        :param token: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "organization": organization,
            "workspaces": workspaces,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if hostname is not None:
            self._values["hostname"] = hostname
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspaces(self) -> IRemoteWorkspace:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspaces")
        assert result is not None, "Required property 'workspaces' is missing"
        return typing.cast(IRemoteWorkspace, result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateRemoteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateS3(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateS3",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        key: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role_policy: typing.Optional[builtins.str] = None,
        dynamodb_endpoint: typing.Optional[builtins.str] = None,
        dynamodb_table: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_path_style: typing.Optional[builtins.bool] = None,
        iam_endpoint: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        skip_credentials_validation: typing.Optional[builtins.bool] = None,
        skip_metadata_api_check: typing.Optional[builtins.bool] = None,
        sse_customer_key: typing.Optional[builtins.str] = None,
        sts_endpoint: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        workspace_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param key: 
        :param access_key: 
        :param acl: 
        :param assume_role_policy: 
        :param dynamodb_endpoint: 
        :param dynamodb_table: 
        :param encrypt: 
        :param endpoint: 
        :param external_id: 
        :param force_path_style: 
        :param iam_endpoint: 
        :param kms_key_id: 
        :param max_retries: 
        :param profile: 
        :param region: 
        :param role_arn: 
        :param secret_key: 
        :param session_name: 
        :param shared_credentials_file: 
        :param skip_credentials_validation: 
        :param skip_metadata_api_check: 
        :param sse_customer_key: 
        :param sts_endpoint: 
        :param token: 
        :param workspace_key_prefix: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateS3Config(
            defaults=defaults,
            workspace=workspace,
            bucket=bucket,
            key=key,
            access_key=access_key,
            acl=acl,
            assume_role_policy=assume_role_policy,
            dynamodb_endpoint=dynamodb_endpoint,
            dynamodb_table=dynamodb_table,
            encrypt=encrypt,
            endpoint=endpoint,
            external_id=external_id,
            force_path_style=force_path_style,
            iam_endpoint=iam_endpoint,
            kms_key_id=kms_key_id,
            max_retries=max_retries,
            profile=profile,
            region=region,
            role_arn=role_arn,
            secret_key=secret_key,
            session_name=session_name,
            shared_credentials_file=shared_credentials_file,
            skip_credentials_validation=skip_credentials_validation,
            skip_metadata_api_check=skip_metadata_api_check,
            sse_customer_key=sse_customer_key,
            sts_endpoint=sts_endpoint,
            token=token,
            workspace_key_prefix=workspace_key_prefix,
        )

        jsii.create(DataTerraformRemoteStateS3, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateS3Config",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, S3BackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "bucket": "bucket",
        "key": "key",
        "access_key": "accessKey",
        "acl": "acl",
        "assume_role_policy": "assumeRolePolicy",
        "dynamodb_endpoint": "dynamodbEndpoint",
        "dynamodb_table": "dynamodbTable",
        "encrypt": "encrypt",
        "endpoint": "endpoint",
        "external_id": "externalId",
        "force_path_style": "forcePathStyle",
        "iam_endpoint": "iamEndpoint",
        "kms_key_id": "kmsKeyId",
        "max_retries": "maxRetries",
        "profile": "profile",
        "region": "region",
        "role_arn": "roleArn",
        "secret_key": "secretKey",
        "session_name": "sessionName",
        "shared_credentials_file": "sharedCredentialsFile",
        "skip_credentials_validation": "skipCredentialsValidation",
        "skip_metadata_api_check": "skipMetadataApiCheck",
        "sse_customer_key": "sseCustomerKey",
        "sts_endpoint": "stsEndpoint",
        "token": "token",
        "workspace_key_prefix": "workspaceKeyPrefix",
    },
)
class DataTerraformRemoteStateS3Config(DataTerraformRemoteStateConfig, S3BackendProps):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        bucket: builtins.str,
        key: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role_policy: typing.Optional[builtins.str] = None,
        dynamodb_endpoint: typing.Optional[builtins.str] = None,
        dynamodb_table: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_path_style: typing.Optional[builtins.bool] = None,
        iam_endpoint: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        skip_credentials_validation: typing.Optional[builtins.bool] = None,
        skip_metadata_api_check: typing.Optional[builtins.bool] = None,
        sse_customer_key: typing.Optional[builtins.str] = None,
        sts_endpoint: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        workspace_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param bucket: 
        :param key: 
        :param access_key: 
        :param acl: 
        :param assume_role_policy: 
        :param dynamodb_endpoint: 
        :param dynamodb_table: 
        :param encrypt: 
        :param endpoint: 
        :param external_id: 
        :param force_path_style: 
        :param iam_endpoint: 
        :param kms_key_id: 
        :param max_retries: 
        :param profile: 
        :param region: 
        :param role_arn: 
        :param secret_key: 
        :param session_name: 
        :param shared_credentials_file: 
        :param skip_credentials_validation: 
        :param skip_metadata_api_check: 
        :param sse_customer_key: 
        :param sts_endpoint: 
        :param token: 
        :param workspace_key_prefix: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if access_key is not None:
            self._values["access_key"] = access_key
        if acl is not None:
            self._values["acl"] = acl
        if assume_role_policy is not None:
            self._values["assume_role_policy"] = assume_role_policy
        if dynamodb_endpoint is not None:
            self._values["dynamodb_endpoint"] = dynamodb_endpoint
        if dynamodb_table is not None:
            self._values["dynamodb_table"] = dynamodb_table
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if external_id is not None:
            self._values["external_id"] = external_id
        if force_path_style is not None:
            self._values["force_path_style"] = force_path_style
        if iam_endpoint is not None:
            self._values["iam_endpoint"] = iam_endpoint
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if profile is not None:
            self._values["profile"] = profile
        if region is not None:
            self._values["region"] = region
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if session_name is not None:
            self._values["session_name"] = session_name
        if shared_credentials_file is not None:
            self._values["shared_credentials_file"] = shared_credentials_file
        if skip_credentials_validation is not None:
            self._values["skip_credentials_validation"] = skip_credentials_validation
        if skip_metadata_api_check is not None:
            self._values["skip_metadata_api_check"] = skip_metadata_api_check
        if sse_customer_key is not None:
            self._values["sse_customer_key"] = sse_customer_key
        if sts_endpoint is not None:
            self._values["sts_endpoint"] = sts_endpoint
        if token is not None:
            self._values["token"] = token
        if workspace_key_prefix is not None:
            self._values["workspace_key_prefix"] = workspace_key_prefix

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_policy(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("assume_role_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dynamodb_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_table(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dynamodb_table")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_path_style(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("force_path_style")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def iam_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("iam_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_credentials_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("shared_credentials_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_credentials_validation(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_credentials_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def skip_metadata_api_check(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_metadata_api_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sse_customer_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sse_customer_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sts_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sts_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_key_prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateS3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataTerraformRemoteStateSwift(
    TerraformRemoteState,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DataTerraformRemoteStateSwift",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        container: builtins.str,
        application_credential_id: typing.Optional[builtins.str] = None,
        application_credential_name: typing.Optional[builtins.str] = None,
        application_credential_secret: typing.Optional[builtins.str] = None,
        archive_container: typing.Optional[builtins.str] = None,
        auth_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        cert: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        default_domain: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        expire_after: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        project_domain_id: typing.Optional[builtins.str] = None,
        project_domain_name: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        tenant_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        user_domain_id: typing.Optional[builtins.str] = None,
        user_domain_name: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param defaults: 
        :param workspace: 
        :param container: 
        :param application_credential_id: 
        :param application_credential_name: 
        :param application_credential_secret: 
        :param archive_container: 
        :param auth_url: 
        :param cacert_file: 
        :param cert: 
        :param cloud: 
        :param default_domain: 
        :param domain_id: 
        :param domain_name: 
        :param expire_after: 
        :param insecure: 
        :param key: 
        :param password: 
        :param project_domain_id: 
        :param project_domain_name: 
        :param region_name: 
        :param state_name: 
        :param tenant_id: 
        :param tenant_name: 
        :param token: 
        :param user_domain_id: 
        :param user_domain_name: 
        :param user_id: 
        :param user_name: 

        :stability: experimental
        '''
        config = DataTerraformRemoteStateSwiftConfig(
            defaults=defaults,
            workspace=workspace,
            container=container,
            application_credential_id=application_credential_id,
            application_credential_name=application_credential_name,
            application_credential_secret=application_credential_secret,
            archive_container=archive_container,
            auth_url=auth_url,
            cacert_file=cacert_file,
            cert=cert,
            cloud=cloud,
            default_domain=default_domain,
            domain_id=domain_id,
            domain_name=domain_name,
            expire_after=expire_after,
            insecure=insecure,
            key=key,
            password=password,
            project_domain_id=project_domain_id,
            project_domain_name=project_domain_name,
            region_name=region_name,
            state_name=state_name,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            token=token,
            user_domain_id=user_domain_id,
            user_domain_name=user_domain_name,
            user_id=user_id,
            user_name=user_name,
        )

        jsii.create(DataTerraformRemoteStateSwift, self, [scope, id, config])


@jsii.data_type(
    jsii_type="cdktf.DataTerraformRemoteStateSwiftConfig",
    jsii_struct_bases=[DataTerraformRemoteStateConfig, SwiftBackendProps],
    name_mapping={
        "defaults": "defaults",
        "workspace": "workspace",
        "container": "container",
        "application_credential_id": "applicationCredentialId",
        "application_credential_name": "applicationCredentialName",
        "application_credential_secret": "applicationCredentialSecret",
        "archive_container": "archiveContainer",
        "auth_url": "authUrl",
        "cacert_file": "cacertFile",
        "cert": "cert",
        "cloud": "cloud",
        "default_domain": "defaultDomain",
        "domain_id": "domainId",
        "domain_name": "domainName",
        "expire_after": "expireAfter",
        "insecure": "insecure",
        "key": "key",
        "password": "password",
        "project_domain_id": "projectDomainId",
        "project_domain_name": "projectDomainName",
        "region_name": "regionName",
        "state_name": "stateName",
        "tenant_id": "tenantId",
        "tenant_name": "tenantName",
        "token": "token",
        "user_domain_id": "userDomainId",
        "user_domain_name": "userDomainName",
        "user_id": "userId",
        "user_name": "userName",
    },
)
class DataTerraformRemoteStateSwiftConfig(
    DataTerraformRemoteStateConfig,
    SwiftBackendProps,
):
    def __init__(
        self,
        *,
        defaults: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        workspace: typing.Optional[builtins.str] = None,
        container: builtins.str,
        application_credential_id: typing.Optional[builtins.str] = None,
        application_credential_name: typing.Optional[builtins.str] = None,
        application_credential_secret: typing.Optional[builtins.str] = None,
        archive_container: typing.Optional[builtins.str] = None,
        auth_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        cert: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        default_domain: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        expire_after: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        project_domain_id: typing.Optional[builtins.str] = None,
        project_domain_name: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        tenant_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        user_domain_id: typing.Optional[builtins.str] = None,
        user_domain_name: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param defaults: 
        :param workspace: 
        :param container: 
        :param application_credential_id: 
        :param application_credential_name: 
        :param application_credential_secret: 
        :param archive_container: 
        :param auth_url: 
        :param cacert_file: 
        :param cert: 
        :param cloud: 
        :param default_domain: 
        :param domain_id: 
        :param domain_name: 
        :param expire_after: 
        :param insecure: 
        :param key: 
        :param password: 
        :param project_domain_id: 
        :param project_domain_name: 
        :param region_name: 
        :param state_name: 
        :param tenant_id: 
        :param tenant_name: 
        :param token: 
        :param user_domain_id: 
        :param user_domain_name: 
        :param user_id: 
        :param user_name: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
        }
        if defaults is not None:
            self._values["defaults"] = defaults
        if workspace is not None:
            self._values["workspace"] = workspace
        if application_credential_id is not None:
            self._values["application_credential_id"] = application_credential_id
        if application_credential_name is not None:
            self._values["application_credential_name"] = application_credential_name
        if application_credential_secret is not None:
            self._values["application_credential_secret"] = application_credential_secret
        if archive_container is not None:
            self._values["archive_container"] = archive_container
        if auth_url is not None:
            self._values["auth_url"] = auth_url
        if cacert_file is not None:
            self._values["cacert_file"] = cacert_file
        if cert is not None:
            self._values["cert"] = cert
        if cloud is not None:
            self._values["cloud"] = cloud
        if default_domain is not None:
            self._values["default_domain"] = default_domain
        if domain_id is not None:
            self._values["domain_id"] = domain_id
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if expire_after is not None:
            self._values["expire_after"] = expire_after
        if insecure is not None:
            self._values["insecure"] = insecure
        if key is not None:
            self._values["key"] = key
        if password is not None:
            self._values["password"] = password
        if project_domain_id is not None:
            self._values["project_domain_id"] = project_domain_id
        if project_domain_name is not None:
            self._values["project_domain_name"] = project_domain_name
        if region_name is not None:
            self._values["region_name"] = region_name
        if state_name is not None:
            self._values["state_name"] = state_name
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if tenant_name is not None:
            self._values["tenant_name"] = tenant_name
        if token is not None:
            self._values["token"] = token
        if user_domain_id is not None:
            self._values["user_domain_id"] = user_domain_id
        if user_domain_name is not None:
            self._values["user_domain_name"] = user_domain_name
        if user_id is not None:
            self._values["user_id"] = user_id
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def defaults(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def workspace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("workspace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_credential_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("application_credential_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("application_credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_credential_secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("application_credential_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def archive_container(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("archive_container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_url(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cacert_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cacert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cloud")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_domain(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("default_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expire_after(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("expire_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_domain_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("project_domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_domain_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("project_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tenant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_domain_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_domain_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTerraformRemoteStateSwiftConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ITokenResolver)
class DefaultTokenResolver(
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.DefaultTokenResolver",
):
    '''(experimental) Default resolver implementation.

    :stability: experimental
    '''

    def __init__(self, concat: IFragmentConcatenator) -> None:
        '''
        :param concat: -

        :stability: experimental
        '''
        jsii.create(DefaultTokenResolver, self, [concat])

    @jsii.member(jsii_name="resolveList")
    def resolve_list(
        self,
        xs: typing.Sequence[builtins.str],
        context: IResolveContext,
    ) -> typing.Any:
        '''(experimental) Resolve a tokenized list.

        :param xs: -
        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveList", [xs, context]))

    @jsii.member(jsii_name="resolveString")
    def resolve_string(
        self,
        fragments: TokenizedStringFragments,
        context: IResolveContext,
    ) -> typing.Any:
        '''(experimental) Resolve string fragments to Tokens.

        :param fragments: -
        :param context: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveString", [fragments, context]))

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(
        self,
        t: IResolvable,
        context: IResolveContext,
        post_processor: IPostProcessor,
    ) -> typing.Any:
        '''(experimental) Default Token resolution.

        Resolve the Token, recurse into whatever it returns,
        then finally post-process it.

        :param t: -
        :param context: -
        :param post_processor: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveToken", [t, context, post_processor]))


class TerraformBackend(
    TerraformElement,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdktf.TerraformBackend",
):
    '''
    :stability: experimental
    '''

    @builtins.staticmethod
    def __jsii_proxy_class__() -> typing.Type["_TerraformBackendProxy"]:
        return _TerraformBackendProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name: -

        :stability: experimental
        '''
        jsii.create(TerraformBackend, self, [scope, id, name])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''(experimental) Adds this resource to the terraform JSON output.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def _name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


class _TerraformBackendProxy(TerraformBackend):
    pass


@jsii.implements(ITerraformResource, ITerraformDependable)
class TerraformDataSource(
    TerraformElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformDataSource",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        terraform_resource_type: builtins.str,
        terraform_generator_metadata: typing.Optional[TerraformProviderGeneratorMetadata] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        lifecycle: typing.Optional[TerraformResourceLifecycle] = None,
        provider: typing.Optional[TerraformProvider] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param terraform_resource_type: 
        :param terraform_generator_metadata: 
        :param count: 
        :param depends_on: 
        :param lifecycle: 
        :param provider: 

        :stability: experimental
        '''
        config = TerraformResourceConfig(
            terraform_resource_type=terraform_resource_type,
            terraform_generator_metadata=terraform_generator_metadata,
            count=count,
            depends_on=depends_on,
            lifecycle=lifecycle,
            provider=provider,
        )

        jsii.create(TerraformDataSource, self, [scope, id, config])

    @jsii.member(jsii_name="getBooleanAttribute")
    def get_boolean_attribute(self, terraform_attribute: builtins.str) -> builtins.bool:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "getBooleanAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getListAttribute")
    def get_list_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> typing.List[builtins.str]:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getListAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getNumberAttribute")
    def get_number_attribute(self, terraform_attribute: builtins.str) -> jsii.Number:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "getNumberAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="getStringAttribute")
    def get_string_attribute(self, terraform_attribute: builtins.str) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getStringAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="interpolationForAttribute")
    def interpolation_for_attribute(
        self,
        terraform_attribute: builtins.str,
    ) -> builtins.str:
        '''
        :param terraform_attribute: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "interpolationForAttribute", [terraform_attribute]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        '''(experimental) Adds this resource to the terraform JSON output.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fqn")
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformMetaArguments")
    def terraform_meta_arguments(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "terraformMetaArguments"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformResourceType")
    def terraform_resource_type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "terraformResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terraformGeneratorMetadata")
    def terraform_generator_metadata(
        self,
    ) -> typing.Optional[TerraformProviderGeneratorMetadata]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TerraformProviderGeneratorMetadata], jsii.get(self, "terraformGeneratorMetadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "count"))

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "count", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dependsOn"))

    @depends_on.setter
    def depends_on(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "dependsOn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycle")
    def lifecycle(self) -> typing.Optional[TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TerraformResourceLifecycle], jsii.get(self, "lifecycle"))

    @lifecycle.setter
    def lifecycle(self, value: typing.Optional[TerraformResourceLifecycle]) -> None:
        jsii.set(self, "lifecycle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[TerraformProvider]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TerraformProvider], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[TerraformProvider]) -> None:
        jsii.set(self, "provider", value)


class TerraformHclModule(
    TerraformModule,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.TerraformHclModule",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        variables: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        source: builtins.str,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        providers: typing.Optional[typing.Sequence[typing.Union[TerraformModuleProvider, TerraformProvider]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param variables: 
        :param source: 
        :param depends_on: 
        :param providers: 
        :param version: 

        :stability: experimental
        '''
        options = TerraformHclModuleOptions(
            variables=variables,
            source=source,
            depends_on=depends_on,
            providers=providers,
            version=version,
        )

        jsii.create(TerraformHclModule, self, [scope, id, options])

    @jsii.member(jsii_name="get")
    def get(self, output: builtins.str) -> typing.Any:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "get", [output]))

    @jsii.member(jsii_name="getBoolean")
    def get_boolean(self, output: builtins.str) -> builtins.bool:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "getBoolean", [output]))

    @jsii.member(jsii_name="getList")
    def get_list(self, output: builtins.str) -> typing.List[builtins.str]:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getList", [output]))

    @jsii.member(jsii_name="getNumber")
    def get_number(self, output: builtins.str) -> jsii.Number:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "getNumber", [output]))

    @jsii.member(jsii_name="getString")
    def get_string(self, output: builtins.str) -> builtins.str:
        '''
        :param output: -

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getString", [output]))

    @jsii.member(jsii_name="set")
    def set(self, variable: builtins.str, value: typing.Any) -> None:
        '''
        :param variable: -
        :param value: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "set", [variable, value]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="variables")
    def variables(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "variables"))


@jsii.data_type(
    jsii_type="cdktf.TerraformHclModuleOptions",
    jsii_struct_bases=[TerraformModuleOptions],
    name_mapping={
        "source": "source",
        "depends_on": "dependsOn",
        "providers": "providers",
        "version": "version",
        "variables": "variables",
    },
)
class TerraformHclModuleOptions(TerraformModuleOptions):
    def __init__(
        self,
        *,
        source: builtins.str,
        depends_on: typing.Optional[typing.Sequence[ITerraformDependable]] = None,
        providers: typing.Optional[typing.Sequence[typing.Union[TerraformModuleProvider, TerraformProvider]]] = None,
        version: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param source: 
        :param depends_on: 
        :param providers: 
        :param version: 
        :param variables: 

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if providers is not None:
            self._values["providers"] = providers
        if version is not None:
            self._values["version"] = version
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def source(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[ITerraformDependable]], result)

    @builtins.property
    def providers(
        self,
    ) -> typing.Optional[typing.List[typing.Union[TerraformModuleProvider, TerraformProvider]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List[typing.Union[TerraformModuleProvider, TerraformProvider]]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TerraformHclModuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ArtifactoryBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.ArtifactoryBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        password: builtins.str,
        repo: builtins.str,
        subpath: builtins.str,
        url: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param password: 
        :param repo: 
        :param subpath: 
        :param url: 
        :param username: 

        :stability: experimental
        '''
        props = ArtifactoryBackendProps(
            password=password, repo=repo, subpath=subpath, url=url, username=username
        )

        jsii.create(ArtifactoryBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class AzurermBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.AzurermBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        container_name: builtins.str,
        key: builtins.str,
        storage_account_name: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        resource_group_name: typing.Optional[builtins.str] = None,
        sas_token: typing.Optional[builtins.str] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param container_name: 
        :param key: 
        :param storage_account_name: 
        :param access_key: 
        :param client_id: 
        :param client_secret: 
        :param endpoint: 
        :param environment: 
        :param msi_endpoint: 
        :param resource_group_name: 
        :param sas_token: 
        :param subscription_id: 
        :param tenant_id: 
        :param use_msi: 

        :stability: experimental
        '''
        props = AzurermBackendProps(
            container_name=container_name,
            key=key,
            storage_account_name=storage_account_name,
            access_key=access_key,
            client_id=client_id,
            client_secret=client_secret,
            endpoint=endpoint,
            environment=environment,
            msi_endpoint=msi_endpoint,
            resource_group_name=resource_group_name,
            sas_token=sas_token,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            use_msi=use_msi,
        )

        jsii.create(AzurermBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class ConsulBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.ConsulBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        access_token: builtins.str,
        path: builtins.str,
        address: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        datacenter: typing.Optional[builtins.str] = None,
        gzip: typing.Optional[builtins.bool] = None,
        http_auth: typing.Optional[builtins.str] = None,
        key_file: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param access_token: 
        :param path: 
        :param address: 
        :param ca_file: 
        :param cert_file: 
        :param datacenter: 
        :param gzip: 
        :param http_auth: 
        :param key_file: 
        :param lock: 
        :param scheme: 

        :stability: experimental
        '''
        props = ConsulBackendProps(
            access_token=access_token,
            path=path,
            address=address,
            ca_file=ca_file,
            cert_file=cert_file,
            datacenter=datacenter,
            gzip=gzip,
            http_auth=http_auth,
            key_file=key_file,
            lock=lock,
            scheme=scheme,
        )

        jsii.create(ConsulBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class CosBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.CosBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        bucket: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param bucket: 
        :param acl: 
        :param encrypt: 
        :param key: 
        :param prefix: 
        :param region: 
        :param secret_id: 
        :param secret_key: 

        :stability: experimental
        '''
        props = CosBackendProps(
            bucket=bucket,
            acl=acl,
            encrypt=encrypt,
            key=key,
            prefix=prefix,
            region=region,
            secret_id=secret_id,
            secret_key=secret_key,
        )

        jsii.create(CosBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class EtcdBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.EtcdBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        endpoints: builtins.str,
        path: builtins.str,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param endpoints: 
        :param path: 
        :param password: 
        :param username: 

        :stability: experimental
        '''
        props = EtcdBackendProps(
            endpoints=endpoints, path=path, password=password, username=username
        )

        jsii.create(EtcdBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class EtcdV3Backend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.EtcdV3Backend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        endpoints: typing.Sequence[builtins.str],
        cacert_path: typing.Optional[builtins.str] = None,
        cert_path: typing.Optional[builtins.str] = None,
        key_path: typing.Optional[builtins.str] = None,
        lock: typing.Optional[builtins.bool] = None,
        password: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param endpoints: 
        :param cacert_path: 
        :param cert_path: 
        :param key_path: 
        :param lock: 
        :param password: 
        :param prefix: 
        :param username: 

        :stability: experimental
        '''
        props = EtcdV3BackendProps(
            endpoints=endpoints,
            cacert_path=cacert_path,
            cert_path=cert_path,
            key_path=key_path,
            lock=lock,
            password=password,
            prefix=prefix,
            username=username,
        )

        jsii.create(EtcdV3Backend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class GcsBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.GcsBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        bucket: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param bucket: 
        :param access_token: 
        :param credentials: 
        :param encryption_key: 
        :param prefix: 

        :stability: experimental
        '''
        props = GcsBackendProps(
            bucket=bucket,
            access_token=access_token,
            credentials=credentials,
            encryption_key=encryption_key,
            prefix=prefix,
        )

        jsii.create(GcsBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class HttpBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.HttpBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        address: builtins.str,
        lock_address: typing.Optional[builtins.str] = None,
        lock_method: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        retry_max: typing.Optional[jsii.Number] = None,
        retry_wait_max: typing.Optional[jsii.Number] = None,
        retry_wait_min: typing.Optional[jsii.Number] = None,
        skip_cert_verification: typing.Optional[builtins.bool] = None,
        unlock_address: typing.Optional[builtins.str] = None,
        unlock_method: typing.Optional[builtins.str] = None,
        update_method: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param address: 
        :param lock_address: 
        :param lock_method: 
        :param password: 
        :param retry_max: 
        :param retry_wait_max: 
        :param retry_wait_min: 
        :param skip_cert_verification: 
        :param unlock_address: 
        :param unlock_method: 
        :param update_method: 
        :param username: 

        :stability: experimental
        '''
        props = HttpBackendProps(
            address=address,
            lock_address=lock_address,
            lock_method=lock_method,
            password=password,
            retry_max=retry_max,
            retry_wait_max=retry_wait_max,
            retry_wait_min=retry_wait_min,
            skip_cert_verification=skip_cert_verification,
            unlock_address=unlock_address,
            unlock_method=unlock_method,
            update_method=update_method,
            username=username,
        )

        jsii.create(HttpBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class LocalBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.LocalBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        path: typing.Optional[builtins.str] = None,
        workspace_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param path: 
        :param workspace_dir: 

        :stability: experimental
        '''
        props = LocalBackendProps(path=path, workspace_dir=workspace_dir)

        jsii.create(LocalBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class MantaBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.MantaBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        account: builtins.str,
        key_id: builtins.str,
        path: builtins.str,
        insecure_skip_tls_verify: typing.Optional[builtins.bool] = None,
        key_material: typing.Optional[builtins.str] = None,
        object_name: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param account: 
        :param key_id: 
        :param path: 
        :param insecure_skip_tls_verify: 
        :param key_material: 
        :param object_name: 
        :param url: 
        :param user: 

        :stability: experimental
        '''
        props = MantaBackendProps(
            account=account,
            key_id=key_id,
            path=path,
            insecure_skip_tls_verify=insecure_skip_tls_verify,
            key_material=key_material,
            object_name=object_name,
            url=url,
            user=user,
        )

        jsii.create(MantaBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class OssBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.OssBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        bucket: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role: typing.Optional[OssAssumeRole] = None,
        ecs_role_name: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        security_token: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        tablestore_endpoint: typing.Optional[builtins.str] = None,
        tablestore_table: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param bucket: 
        :param access_key: 
        :param acl: 
        :param assume_role: 
        :param ecs_role_name: 
        :param encrypt: 
        :param endpoint: 
        :param key: 
        :param prefix: 
        :param profile: 
        :param region: 
        :param secret_key: 
        :param security_token: 
        :param shared_credentials_file: 
        :param tablestore_endpoint: 
        :param tablestore_table: 

        :stability: experimental
        '''
        props = OssBackendProps(
            bucket=bucket,
            access_key=access_key,
            acl=acl,
            assume_role=assume_role,
            ecs_role_name=ecs_role_name,
            encrypt=encrypt,
            endpoint=endpoint,
            key=key,
            prefix=prefix,
            profile=profile,
            region=region,
            secret_key=secret_key,
            security_token=security_token,
            shared_credentials_file=shared_credentials_file,
            tablestore_endpoint=tablestore_endpoint,
            tablestore_table=tablestore_table,
        )

        jsii.create(OssBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class PgBackend(TerraformBackend, metaclass=jsii.JSIIMeta, jsii_type="cdktf.PgBackend"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        conn_str: builtins.str,
        schema_name: typing.Optional[builtins.str] = None,
        skip_schema_creation: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param conn_str: 
        :param schema_name: 
        :param skip_schema_creation: 

        :stability: experimental
        '''
        props = PgBackendProps(
            conn_str=conn_str,
            schema_name=schema_name,
            skip_schema_creation=skip_schema_creation,
        )

        jsii.create(PgBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class RemoteBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.RemoteBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        organization: builtins.str,
        workspaces: IRemoteWorkspace,
        hostname: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param organization: 
        :param workspaces: 
        :param hostname: 
        :param token: 

        :stability: experimental
        '''
        props = RemoteBackendProps(
            organization=organization,
            workspaces=workspaces,
            hostname=hostname,
            token=token,
        )

        jsii.create(RemoteBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class S3Backend(TerraformBackend, metaclass=jsii.JSIIMeta, jsii_type="cdktf.S3Backend"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        bucket: builtins.str,
        key: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        acl: typing.Optional[builtins.str] = None,
        assume_role_policy: typing.Optional[builtins.str] = None,
        dynamodb_endpoint: typing.Optional[builtins.str] = None,
        dynamodb_table: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.bool] = None,
        endpoint: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        force_path_style: typing.Optional[builtins.bool] = None,
        iam_endpoint: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        session_name: typing.Optional[builtins.str] = None,
        shared_credentials_file: typing.Optional[builtins.str] = None,
        skip_credentials_validation: typing.Optional[builtins.bool] = None,
        skip_metadata_api_check: typing.Optional[builtins.bool] = None,
        sse_customer_key: typing.Optional[builtins.str] = None,
        sts_endpoint: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        workspace_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param bucket: 
        :param key: 
        :param access_key: 
        :param acl: 
        :param assume_role_policy: 
        :param dynamodb_endpoint: 
        :param dynamodb_table: 
        :param encrypt: 
        :param endpoint: 
        :param external_id: 
        :param force_path_style: 
        :param iam_endpoint: 
        :param kms_key_id: 
        :param max_retries: 
        :param profile: 
        :param region: 
        :param role_arn: 
        :param secret_key: 
        :param session_name: 
        :param shared_credentials_file: 
        :param skip_credentials_validation: 
        :param skip_metadata_api_check: 
        :param sse_customer_key: 
        :param sts_endpoint: 
        :param token: 
        :param workspace_key_prefix: 

        :stability: experimental
        '''
        props = S3BackendProps(
            bucket=bucket,
            key=key,
            access_key=access_key,
            acl=acl,
            assume_role_policy=assume_role_policy,
            dynamodb_endpoint=dynamodb_endpoint,
            dynamodb_table=dynamodb_table,
            encrypt=encrypt,
            endpoint=endpoint,
            external_id=external_id,
            force_path_style=force_path_style,
            iam_endpoint=iam_endpoint,
            kms_key_id=kms_key_id,
            max_retries=max_retries,
            profile=profile,
            region=region,
            role_arn=role_arn,
            secret_key=secret_key,
            session_name=session_name,
            shared_credentials_file=shared_credentials_file,
            skip_credentials_validation=skip_credentials_validation,
            skip_metadata_api_check=skip_metadata_api_check,
            sse_customer_key=sse_customer_key,
            sts_endpoint=sts_endpoint,
            token=token,
            workspace_key_prefix=workspace_key_prefix,
        )

        jsii.create(S3Backend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


class SwiftBackend(
    TerraformBackend,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf.SwiftBackend",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        *,
        container: builtins.str,
        application_credential_id: typing.Optional[builtins.str] = None,
        application_credential_name: typing.Optional[builtins.str] = None,
        application_credential_secret: typing.Optional[builtins.str] = None,
        archive_container: typing.Optional[builtins.str] = None,
        auth_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        cert: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        default_domain: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        expire_after: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[builtins.bool] = None,
        key: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        project_domain_id: typing.Optional[builtins.str] = None,
        project_domain_name: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        tenant_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        user_domain_id: typing.Optional[builtins.str] = None,
        user_domain_name: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param container: 
        :param application_credential_id: 
        :param application_credential_name: 
        :param application_credential_secret: 
        :param archive_container: 
        :param auth_url: 
        :param cacert_file: 
        :param cert: 
        :param cloud: 
        :param default_domain: 
        :param domain_id: 
        :param domain_name: 
        :param expire_after: 
        :param insecure: 
        :param key: 
        :param password: 
        :param project_domain_id: 
        :param project_domain_name: 
        :param region_name: 
        :param state_name: 
        :param tenant_id: 
        :param tenant_name: 
        :param token: 
        :param user_domain_id: 
        :param user_domain_name: 
        :param user_id: 
        :param user_name: 

        :stability: experimental
        '''
        props = SwiftBackendProps(
            container=container,
            application_credential_id=application_credential_id,
            application_credential_name=application_credential_name,
            application_credential_secret=application_credential_secret,
            archive_container=archive_container,
            auth_url=auth_url,
            cacert_file=cacert_file,
            cert=cert,
            cloud=cloud,
            default_domain=default_domain,
            domain_id=domain_id,
            domain_name=domain_name,
            expire_after=expire_after,
            insecure=insecure,
            key=key,
            password=password,
            project_domain_id=project_domain_id,
            project_domain_name=project_domain_name,
            region_name=region_name,
            state_name=state_name,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            token=token,
            user_domain_id=user_domain_id,
            user_domain_name=user_domain_name,
            user_id=user_id,
            user_name=user_name,
        )

        jsii.create(SwiftBackend, self, [scope, props])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))


__all__ = [
    "App",
    "AppOptions",
    "ArtifactoryBackend",
    "ArtifactoryBackendProps",
    "AssetType",
    "AzurermBackend",
    "AzurermBackendProps",
    "BooleanMap",
    "ComplexComputedList",
    "ConsulBackend",
    "ConsulBackendProps",
    "CosBackend",
    "CosBackendProps",
    "DataTerraformRemoteState",
    "DataTerraformRemoteStateArtifactory",
    "DataTerraformRemoteStateArtifactoryConfig",
    "DataTerraformRemoteStateAzurerm",
    "DataTerraformRemoteStateAzurermConfig",
    "DataTerraformRemoteStateConfig",
    "DataTerraformRemoteStateConsul",
    "DataTerraformRemoteStateConsulConfig",
    "DataTerraformRemoteStateCos",
    "DataTerraformRemoteStateCosConfig",
    "DataTerraformRemoteStateEtcd",
    "DataTerraformRemoteStateEtcdConfig",
    "DataTerraformRemoteStateEtcdV3",
    "DataTerraformRemoteStateEtcdV3Config",
    "DataTerraformRemoteStateGcs",
    "DataTerraformRemoteStateGcsConfig",
    "DataTerraformRemoteStateHttp",
    "DataTerraformRemoteStateHttpConfig",
    "DataTerraformRemoteStateLocal",
    "DataTerraformRemoteStateLocalConfig",
    "DataTerraformRemoteStateManta",
    "DataTerraformRemoteStateMantaConfig",
    "DataTerraformRemoteStateOss",
    "DataTerraformRemoteStateOssConfig",
    "DataTerraformRemoteStatePg",
    "DataTerraformRemoteStatePgConfig",
    "DataTerraformRemoteStateRemoteConfig",
    "DataTerraformRemoteStateS3",
    "DataTerraformRemoteStateS3Config",
    "DataTerraformRemoteStateSwift",
    "DataTerraformRemoteStateSwiftConfig",
    "DefaultTokenResolver",
    "EncodingOptions",
    "EtcdBackend",
    "EtcdBackendProps",
    "EtcdV3Backend",
    "EtcdV3BackendProps",
    "GcsBackend",
    "GcsBackendProps",
    "HttpBackend",
    "HttpBackendProps",
    "IAnyProducer",
    "IFragmentConcatenator",
    "IListProducer",
    "INumberProducer",
    "IPostProcessor",
    "IRemoteWorkspace",
    "IResolvable",
    "IResolveContext",
    "IResource",
    "IStringProducer",
    "ITerraformDependable",
    "ITerraformResource",
    "ITokenMapper",
    "ITokenResolver",
    "Lazy",
    "LazyAnyValueOptions",
    "LazyListValueOptions",
    "LazyStringValueOptions",
    "LocalBackend",
    "LocalBackendProps",
    "Manifest",
    "MantaBackend",
    "MantaBackendProps",
    "NamedRemoteWorkspace",
    "NumberMap",
    "OssAssumeRole",
    "OssBackend",
    "OssBackendProps",
    "PgBackend",
    "PgBackendProps",
    "PrefixedRemoteWorkspaces",
    "RemoteBackend",
    "RemoteBackendProps",
    "ResolveOptions",
    "Resource",
    "S3Backend",
    "S3BackendProps",
    "StackManifest",
    "StringConcat",
    "StringMap",
    "SwiftBackend",
    "SwiftBackendProps",
    "TerraformAsset",
    "TerraformAssetConfig",
    "TerraformBackend",
    "TerraformDataSource",
    "TerraformElement",
    "TerraformElementMetadata",
    "TerraformHclModule",
    "TerraformHclModuleOptions",
    "TerraformLocal",
    "TerraformMetaArguments",
    "TerraformModule",
    "TerraformModuleOptions",
    "TerraformModuleProvider",
    "TerraformOutput",
    "TerraformOutputConfig",
    "TerraformProvider",
    "TerraformProviderConfig",
    "TerraformProviderGeneratorMetadata",
    "TerraformRemoteState",
    "TerraformResource",
    "TerraformResourceConfig",
    "TerraformResourceLifecycle",
    "TerraformStack",
    "TerraformStackMetadata",
    "TerraformVariable",
    "TerraformVariableConfig",
    "Testing",
    "Token",
    "Tokenization",
    "TokenizedStringFragments",
    "VariableType",
]

publication.publish()
