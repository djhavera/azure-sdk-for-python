# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .control_activity_py3 import ControlActivity


class WebHookActivity(ControlActivity):
    """WebHook activity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :ivar method: Required. Rest API method for target endpoint. Default
     value: "POST" .
    :vartype method: str
    :param url: Required. WebHook activity target endpoint and path. Type:
     string (or Expression with resultType string).
    :type url: object
    :param timeout: Specifies the timeout within which the webhook should be
     called back. If there is no value specified, it takes the value of
     TimeSpan.FromMinutes(10) which is 10 minutes as default. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type timeout: object
    :param headers: Represents the headers that will be sent to the request.
     For example, to set the language and type on a request: "headers" : {
     "Accept-Language": "en-us", "Content-Type": "application/json" }. Type:
     string (or Expression with resultType string).
    :type headers: object
    :param body: Represents the payload that will be sent to the endpoint.
     Required for POST/PUT method, not allowed for GET method Type: string (or
     Expression with resultType string).
    :type body: object
    :param authentication: Authentication method used for calling the
     endpoint.
    :type authentication:
     ~azure.mgmt.datafactory.models.WebActivityAuthentication
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'method': {'required': True, 'constant': True},
        'url': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'method': {'key': 'typeProperties.method', 'type': 'str'},
        'url': {'key': 'typeProperties.url', 'type': 'object'},
        'timeout': {'key': 'typeProperties.timeout', 'type': 'object'},
        'headers': {'key': 'typeProperties.headers', 'type': 'object'},
        'body': {'key': 'typeProperties.body', 'type': 'object'},
        'authentication': {'key': 'typeProperties.authentication', 'type': 'WebActivityAuthentication'},
    }

    method = "POST"

    def __init__(self, *, name: str, url, additional_properties=None, description: str=None, depends_on=None, user_properties=None, timeout=None, headers=None, body=None, authentication=None, **kwargs) -> None:
        super(WebHookActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, **kwargs)
        self.url = url
        self.timeout = timeout
        self.headers = headers
        self.body = body
        self.authentication = authentication
        self.type = 'WebHook'
