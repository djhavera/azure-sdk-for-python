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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class AlertsOperations(object):
    """AlertsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: API version. Constant value: "2018-05-05".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-05-05"

        self.config = config

    def get_all(
            self, target_resource=None, target_resource_type=None, target_resource_group=None, monitor_service=None, monitor_condition=None, severity=None, alert_state=None, alert_rule=None, smart_group_id=None, include_context=None, include_egress_config=None, page_count=None, sort_by=None, sort_order=None, select=None, time_range=None, custom_time_range=None, custom_headers=None, raw=False, **operation_config):
        """List all the existing alerts, where the results can be selective by
        passing multiple filter parameters including time range and sorted on
        specific fields. .

        :param target_resource: Filter by target resource( which is full ARM
         ID) Default value is select all.
        :type target_resource: str
        :param target_resource_type: Filter by target resource type. Default
         value is select all.
        :type target_resource_type: str
        :param target_resource_group: Filter by target resource group name.
         Default value is select all.
        :type target_resource_group: str
        :param monitor_service: Filter by monitor service which is the source
         of the alert instance. Default value is select all. Possible values
         include: 'Application Insights', 'ActivityLog Administrative',
         'ActivityLog Security', 'ActivityLog Recommendation', 'ActivityLog
         Policy', 'ActivityLog Autoscale', 'Log Analytics', 'Nagios',
         'Platform', 'SCOM', 'ServiceHealth', 'SmartDetector', 'VM Insights',
         'Zabbix'
        :type monitor_service: str or
         ~azure.mgmt.alertsmanagement.models.MonitorService
        :param monitor_condition: Filter by monitor condition which is the
         state of the  monitor(alertRule) at monitor service. Default value is
         to select all. Possible values include: 'Fired', 'Resolved'
        :type monitor_condition: str or
         ~azure.mgmt.alertsmanagement.models.MonitorCondition
        :param severity: Filter by severity.  Defaut value is select all.
         Possible values include: 'Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4'
        :type severity: str or ~azure.mgmt.alertsmanagement.models.Severity
        :param alert_state: Filter by state of the alert instance. Default
         value is to select all. Possible values include: 'New',
         'Acknowledged', 'Closed'
        :type alert_state: str or
         ~azure.mgmt.alertsmanagement.models.AlertState
        :param alert_rule: Filter by alert rule(monitor) which fired alert
         instance.  Default value is to select all.
        :type alert_rule: str
        :param smart_group_id: Filter the alerts list by the Smart Group Id.
         Default value is none.
        :type smart_group_id: str
        :param include_context: Include context which has data contextual to
         the monitor service. Default value is false'
        :type include_context: bool
        :param include_egress_config: Include egress config which would be
         used for displaying the content in portal.  Default value is 'false'.
        :type include_egress_config: bool
        :param page_count: Determines number of alerts returned per page in
         response. Permissible value is between 1 to 250. When the
         "includeContent"  filter is selected, maximum value allowed is 25.
         Default value is 25.
        :type page_count: int
        :param sort_by: Sort the query results by input field,  Default value
         is 'lastModifiedDateTime'. Possible values include: 'name',
         'severity', 'alertState', 'monitorCondition', 'targetResource',
         'targetResourceName', 'targetResourceGroup', 'targetResourceType',
         'startDateTime', 'lastModifiedDateTime'
        :type sort_by: str or
         ~azure.mgmt.alertsmanagement.models.AlertsSortByFields
        :param sort_order: Sort the query results order in either ascending or
         descending.  Default value is 'desc' for time fields and 'asc' for
         others. Possible values include: 'asc', 'desc'
        :type sort_order: str
        :param select: This filter allows to selection of the fields(comma
         seperated) which would  be part of the the essential section. This
         would allow to project only the  required fields rather than getting
         entire content.  Default is to fetch all the fields in the essentials
         section.
        :type select: str
        :param time_range: Filter by time range by below listed values.
         Default value is 1 day. Possible values include: '1h', '1d', '7d',
         '30d'
        :type time_range: str or ~azure.mgmt.alertsmanagement.models.TimeRange
        :param custom_time_range: Filter by custom time range in the format
         <start-time>/<end-time>  where time is in (ISO-8601 format)'.
         Permissible values is within 30 days from  query time. Either
         timeRange or customTimeRange could be used but not both. Default is
         none.
        :type custom_time_range: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Alert
        :rtype:
         ~azure.mgmt.alertsmanagement.models.AlertPaged[~azure.mgmt.alertsmanagement.models.Alert]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.get_all.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if target_resource is not None:
                    query_parameters['targetResource'] = self._serialize.query("target_resource", target_resource, 'str')
                if target_resource_type is not None:
                    query_parameters['targetResourceType'] = self._serialize.query("target_resource_type", target_resource_type, 'str')
                if target_resource_group is not None:
                    query_parameters['targetResourceGroup'] = self._serialize.query("target_resource_group", target_resource_group, 'str')
                if monitor_service is not None:
                    query_parameters['monitorService'] = self._serialize.query("monitor_service", monitor_service, 'str')
                if monitor_condition is not None:
                    query_parameters['monitorCondition'] = self._serialize.query("monitor_condition", monitor_condition, 'str')
                if severity is not None:
                    query_parameters['severity'] = self._serialize.query("severity", severity, 'str')
                if alert_state is not None:
                    query_parameters['alertState'] = self._serialize.query("alert_state", alert_state, 'str')
                if alert_rule is not None:
                    query_parameters['alertRule'] = self._serialize.query("alert_rule", alert_rule, 'str')
                if smart_group_id is not None:
                    query_parameters['smartGroupId'] = self._serialize.query("smart_group_id", smart_group_id, 'str')
                if include_context is not None:
                    query_parameters['includeContext'] = self._serialize.query("include_context", include_context, 'bool')
                if include_egress_config is not None:
                    query_parameters['includeEgressConfig'] = self._serialize.query("include_egress_config", include_egress_config, 'bool')
                if page_count is not None:
                    query_parameters['pageCount'] = self._serialize.query("page_count", page_count, 'int')
                if sort_by is not None:
                    query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, 'str')
                if sort_order is not None:
                    query_parameters['sortOrder'] = self._serialize.query("sort_order", sort_order, 'str')
                if select is not None:
                    query_parameters['select'] = self._serialize.query("select", select, 'str')
                if time_range is not None:
                    query_parameters['timeRange'] = self._serialize.query("time_range", time_range, 'str')
                if custom_time_range is not None:
                    query_parameters['customTimeRange'] = self._serialize.query("custom_time_range", custom_time_range, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.AlertPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.AlertPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    get_all.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts'}

    def get_by_id(
            self, alert_id, custom_headers=None, raw=False, **operation_config):
        """Get a specific alert.

        Get information related to a specific alert.

        :param alert_id: Unique ID of an alert instance.
        :type alert_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Alert or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.Alert or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'alertId': self._serialize.url("alert_id", alert_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Alert', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_id.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}'}

    def change_state(
            self, alert_id, new_state, custom_headers=None, raw=False, **operation_config):
        """Change the state of the alert.

        :param alert_id: Unique ID of an alert instance.
        :type alert_id: str
        :param new_state: New state of the alert. Possible values include:
         'New', 'Acknowledged', 'Closed'
        :type new_state: str or ~azure.mgmt.alertsmanagement.models.AlertState
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Alert or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.Alert or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.change_state.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'alertId': self._serialize.url("alert_id", alert_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['newState'] = self._serialize.query("new_state", new_state, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Alert', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    change_state.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}/changestate'}

    def get_history(
            self, alert_id, custom_headers=None, raw=False, **operation_config):
        """Get the history of the changes of an alert.

        :param alert_id: Unique ID of an alert instance.
        :type alert_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AlertModification or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.AlertModification or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_history.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'alertId': self._serialize.url("alert_id", alert_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AlertModification', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_history.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}/history'}

    def get_summary(
            self, groupby, include_smart_groups_count=None, target_resource=None, target_resource_type=None, target_resource_group=None, monitor_service=None, monitor_condition=None, severity=None, alert_state=None, alert_rule=None, time_range=None, custom_time_range=None, custom_headers=None, raw=False, **operation_config):
        """Summary of alerts with the count each severity.

        :param groupby: This parameter allows the result set to be aggregated
         by input fields. For example, groupby=severity,alertstate. Possible
         values include: 'severity', 'alertState', 'monitorCondition',
         'monitorService', 'signalType', 'alertRule'
        :type groupby: str or
         ~azure.mgmt.alertsmanagement.models.AlertsSummaryGroupByFields
        :param include_smart_groups_count: Include count of the SmartGroups as
         part of the summary. Default value is 'false'.
        :type include_smart_groups_count: bool
        :param target_resource: Filter by target resource( which is full ARM
         ID) Default value is select all.
        :type target_resource: str
        :param target_resource_type: Filter by target resource type. Default
         value is select all.
        :type target_resource_type: str
        :param target_resource_group: Filter by target resource group name.
         Default value is select all.
        :type target_resource_group: str
        :param monitor_service: Filter by monitor service which is the source
         of the alert instance. Default value is select all. Possible values
         include: 'Application Insights', 'ActivityLog Administrative',
         'ActivityLog Security', 'ActivityLog Recommendation', 'ActivityLog
         Policy', 'ActivityLog Autoscale', 'Log Analytics', 'Nagios',
         'Platform', 'SCOM', 'ServiceHealth', 'SmartDetector', 'VM Insights',
         'Zabbix'
        :type monitor_service: str or
         ~azure.mgmt.alertsmanagement.models.MonitorService
        :param monitor_condition: Filter by monitor condition which is the
         state of the  monitor(alertRule) at monitor service. Default value is
         to select all. Possible values include: 'Fired', 'Resolved'
        :type monitor_condition: str or
         ~azure.mgmt.alertsmanagement.models.MonitorCondition
        :param severity: Filter by severity.  Defaut value is select all.
         Possible values include: 'Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4'
        :type severity: str or ~azure.mgmt.alertsmanagement.models.Severity
        :param alert_state: Filter by state of the alert instance. Default
         value is to select all. Possible values include: 'New',
         'Acknowledged', 'Closed'
        :type alert_state: str or
         ~azure.mgmt.alertsmanagement.models.AlertState
        :param alert_rule: Filter by alert rule(monitor) which fired alert
         instance.  Default value is to select all.
        :type alert_rule: str
        :param time_range: Filter by time range by below listed values.
         Default value is 1 day. Possible values include: '1h', '1d', '7d',
         '30d'
        :type time_range: str or ~azure.mgmt.alertsmanagement.models.TimeRange
        :param custom_time_range: Filter by custom time range in the format
         <start-time>/<end-time>  where time is in (ISO-8601 format)'.
         Permissible values is within 30 days from  query time. Either
         timeRange or customTimeRange could be used but not both. Default is
         none.
        :type custom_time_range: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AlertsSummary or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.alertsmanagement.models.AlertsSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.alertsmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_summary.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['groupby'] = self._serialize.query("groupby", groupby, 'str')
        if include_smart_groups_count is not None:
            query_parameters['includeSmartGroupsCount'] = self._serialize.query("include_smart_groups_count", include_smart_groups_count, 'bool')
        if target_resource is not None:
            query_parameters['targetResource'] = self._serialize.query("target_resource", target_resource, 'str')
        if target_resource_type is not None:
            query_parameters['targetResourceType'] = self._serialize.query("target_resource_type", target_resource_type, 'str')
        if target_resource_group is not None:
            query_parameters['targetResourceGroup'] = self._serialize.query("target_resource_group", target_resource_group, 'str')
        if monitor_service is not None:
            query_parameters['monitorService'] = self._serialize.query("monitor_service", monitor_service, 'str')
        if monitor_condition is not None:
            query_parameters['monitorCondition'] = self._serialize.query("monitor_condition", monitor_condition, 'str')
        if severity is not None:
            query_parameters['severity'] = self._serialize.query("severity", severity, 'str')
        if alert_state is not None:
            query_parameters['alertState'] = self._serialize.query("alert_state", alert_state, 'str')
        if alert_rule is not None:
            query_parameters['alertRule'] = self._serialize.query("alert_rule", alert_rule, 'str')
        if time_range is not None:
            query_parameters['timeRange'] = self._serialize.query("time_range", time_range, 'str')
        if custom_time_range is not None:
            query_parameters['customTimeRange'] = self._serialize.query("custom_time_range", custom_time_range, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AlertsSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_summary.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alertsSummary'}
