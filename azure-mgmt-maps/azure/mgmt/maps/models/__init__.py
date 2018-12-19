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

try:
    from .error_details_item_py3 import ErrorDetailsItem
    from .error_py3 import Error, ErrorException
    from .resource_py3 import Resource
    from .sku_py3 import Sku
    from .maps_account_properties_py3 import MapsAccountProperties
    from .maps_account_py3 import MapsAccount
    from .maps_account_create_parameters_py3 import MapsAccountCreateParameters
    from .maps_account_update_parameters_py3 import MapsAccountUpdateParameters
    from .maps_accounts_move_request_py3 import MapsAccountsMoveRequest
    from .maps_key_specification_py3 import MapsKeySpecification
    from .maps_account_keys_py3 import MapsAccountKeys
    from .maps_operations_value_item_display_py3 import MapsOperationsValueItemDisplay
    from .maps_operations_value_item_py3 import MapsOperationsValueItem
except (SyntaxError, ImportError):
    from .error_details_item import ErrorDetailsItem
    from .error import Error, ErrorException
    from .resource import Resource
    from .sku import Sku
    from .maps_account_properties import MapsAccountProperties
    from .maps_account import MapsAccount
    from .maps_account_create_parameters import MapsAccountCreateParameters
    from .maps_account_update_parameters import MapsAccountUpdateParameters
    from .maps_accounts_move_request import MapsAccountsMoveRequest
    from .maps_key_specification import MapsKeySpecification
    from .maps_account_keys import MapsAccountKeys
    from .maps_operations_value_item_display import MapsOperationsValueItemDisplay
    from .maps_operations_value_item import MapsOperationsValueItem
from .maps_account_paged import MapsAccountPaged
from .maps_operations_value_item_paged import MapsOperationsValueItemPaged
from .maps_management_client_enums import (
    KeyType,
)

__all__ = [
    'ErrorDetailsItem',
    'Error', 'ErrorException',
    'Resource',
    'Sku',
    'MapsAccountProperties',
    'MapsAccount',
    'MapsAccountCreateParameters',
    'MapsAccountUpdateParameters',
    'MapsAccountsMoveRequest',
    'MapsKeySpecification',
    'MapsAccountKeys',
    'MapsOperationsValueItemDisplay',
    'MapsOperationsValueItem',
    'MapsAccountPaged',
    'MapsOperationsValueItemPaged',
    'KeyType',
]
