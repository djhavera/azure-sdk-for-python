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
    from .intent_model_py3 import IntentModel
    from .entity_model_py3 import EntityModel
    from .composite_child_model_py3 import CompositeChildModel
    from .composite_entity_model_py3 import CompositeEntityModel
    from .sentiment_py3 import Sentiment
    from .luis_result_py3 import LuisResult
    from .entity_with_score_py3 import EntityWithScore
    from .entity_with_resolution_py3 import EntityWithResolution
    from .api_error_py3 import APIError, APIErrorException
except (SyntaxError, ImportError):
    from .intent_model import IntentModel
    from .entity_model import EntityModel
    from .composite_child_model import CompositeChildModel
    from .composite_entity_model import CompositeEntityModel
    from .sentiment import Sentiment
    from .luis_result import LuisResult
    from .entity_with_score import EntityWithScore
    from .entity_with_resolution import EntityWithResolution
    from .api_error import APIError, APIErrorException

__all__ = [
    'IntentModel',
    'EntityModel',
    'CompositeChildModel',
    'CompositeEntityModel',
    'Sentiment',
    'LuisResult',
    'EntityWithScore',
    'EntityWithResolution',
    'APIError', 'APIErrorException',
]
