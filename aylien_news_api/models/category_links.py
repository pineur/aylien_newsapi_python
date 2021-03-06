# coding: utf-8

# Copyright 2016 Aylien, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pprint import pformat
from six import iteritems
import re


class CategoryLinks(object):
    def __init__(self, _self=None, parent=None):
        """
        CategoryLinks - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            '_self': 'str',
            'parent': 'str'
        }

        self.attribute_map = {
            '_self': 'self',
            'parent': 'parent'
        }

        self.__self = _self
        self._parent = parent


    @property
    def _self(self):
        """
        Gets the _self of this CategoryLinks.
        A URL pointing to the category

        :return: The _self of this CategoryLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this CategoryLinks.
        A URL pointing to the category

        :param _self: The _self of this CategoryLinks.
        :type: str
        """

        self.__self = _self

    @property
    def parent(self):
        """
        Gets the parent of this CategoryLinks.
        A URL pointing to the parent category

        :return: The parent of this CategoryLinks.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this CategoryLinks.
        A URL pointing to the parent category

        :param parent: The parent of this CategoryLinks.
        :type: str
        """

        self._parent = parent

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.api_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
