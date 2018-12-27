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

from msrest.serialization import Model


class TargetProperties(Model):
    """Group specific to the update configuration.

    :param azure_queries: List of Azure queries in the software update
     configuration.
    :type azure_queries:
     list[~azure.mgmt.automation.models.AzureQueryProperties]
    :param non_azure_queries: List of non Azure queries in the software update
     configuration.
    :type non_azure_queries:
     list[~azure.mgmt.automation.models.NonAzureQueryProperties]
    """

    _attribute_map = {
        'azure_queries': {'key': 'azureQueries', 'type': '[AzureQueryProperties]'},
        'non_azure_queries': {'key': 'nonAzureQueries', 'type': '[NonAzureQueryProperties]'},
    }

    def __init__(self, *, azure_queries=None, non_azure_queries=None, **kwargs) -> None:
        super(TargetProperties, self).__init__(**kwargs)
        self.azure_queries = azure_queries
        self.non_azure_queries = non_azure_queries
