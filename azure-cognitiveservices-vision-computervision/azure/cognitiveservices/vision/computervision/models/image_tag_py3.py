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


class ImageTag(Model):
    """An entity observation in the image, along with the confidence score.

    :param name: Name of the entity.
    :type name: str
    :param confidence: The level of confidence that the entity was observed.
    :type confidence: float
    :param hint: Optional hint/details for this tag.
    :type hint: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'confidence': {'key': 'confidence', 'type': 'float'},
        'hint': {'key': 'hint', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, confidence: float=None, hint: str=None, **kwargs) -> None:
        super(ImageTag, self).__init__(**kwargs)
        self.name = name
        self.confidence = confidence
        self.hint = hint
