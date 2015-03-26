#
#    (c) 2014 Morning Project Samurai
#
#    This file is part of Burasabori.
#    Burasabori is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    Burasabori is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'Akinori Hayashi, Junya Kaneko'

from core import exceptions

from urllib import parse, request
import json, xmltodict

class ApiExecutor:
    JSON_FORMAT = 0
    XML_FORMAT = 1

    def __init__(self, base_url, parameters):
        self.__base_url = base_url
        self.__parameters = parameters

    @property
    def _base_url(self):
        return self.__base_url

    @property
    def _parameters(self):
        return self.__parameters

    def _get_default_query(self):
        default_query = {}
        for key in self._parameters.keys():
            if self._parameters[key] != None:
                default_query[key] = self._parameters[key]
        return default_query

    def _update_query(self, parameters, default_query):
        for key in parameters.keys():
            if key in self._parameters.keys():
                default_query[key] = parameters[key]
            else:
                raise KeyError
        return default_query

    def _get_query(self, parameters):
        default_query = self._get_default_query()
        query = self._update_query(parameters, default_query)
        return query

    def _get_response(self, parameters):
        query = self._get_query(parameters)
        query_string = parse.urlencode(query)
        url = self._base_url + '?' + query_string
        response = request.urlopen(url)
        response_code = response.getcode()
        if response_code == 200 or response_code == 304:
            return response
        else:
            raise exceptions.ApiExecutionFailureException(self.__class__.__name__)

    def _check_data_format(self, response):
        content_type = response.info()['Content-Type']
        if content_type.find('json') != -1:
            return self.JSON_FORMAT
        elif content_type.find('xml') != -1:
            return self.XML_FORMAT
        else:
            Exception('Received data is unknown format....')

    def _convert_xml_to_json(self, byte_data):
        return xmltodict.parse(byte_data)
    
    def get_data(self, parameters = {}):
        response = self._get_response(parameters)
        data_format = self._check_data_format(response)
        byte_data = response.read()
        
        byte_data = byte_data.decode('utf-8')
        
        if data_format == self.JSON_FORMAT:
            return json.loads(byte_data)
        else:
            return self._convert_xml_to_json(byte_data)