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


class Author(object):
    def __init__(self, id=None, name=None, avatar_url=None):
        """
        Author - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'id': 'int',
            'name': 'str',
            'avatar_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'avatar_url': 'avatar_url'
        }

        self._id = id
        self._name = name
        self._avatar_url = avatar_url


    @property
    def id(self):
        """
        Gets the id of this Author.
        A unique identification for the author

        :return: The id of this Author.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Author.
        A unique identification for the author

        :param id: The id of this Author.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Author.
        The extracted author full name

        :return: The name of this Author.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Author.
        The extracted author full name

        :param name: The name of this Author.
        :type: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this Author.
        A URL which points to the author avatar

        :return: The avatar_url of this Author.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this Author.
        A URL which points to the author avatar

        :param avatar_url: The avatar_url of this Author.
        :type: str
        """

        self._avatar_url = avatar_url

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
