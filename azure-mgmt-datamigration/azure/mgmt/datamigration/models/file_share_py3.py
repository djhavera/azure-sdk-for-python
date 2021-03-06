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


class FileShare(Model):
    """File share information with Path, Username, and Password.

    All required parameters must be populated in order to send to Azure.

    :param user_name: User name credential to connect to the share location
    :type user_name: str
    :param password: Password credential used to connect to the share
     location.
    :type password: str
    :param path: Required. The folder path for this share.
    :type path: str
    """

    _validation = {
        'path': {'required': True},
    }

    _attribute_map = {
        'user_name': {'key': 'userName', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, *, path: str, user_name: str=None, password: str=None, **kwargs) -> None:
        super(FileShare, self).__init__(**kwargs)
        self.user_name = user_name
        self.password = password
        self.path = path
