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

__author__ = 'Junya Kaneko'

from copy import deepcopy

class JsonModel:
    def __init__(self, json_data):
        self.__json_data = json_data

    @property
    def _json_data(self):
        return self.__json_data

class JsonModelManager:
    def __init__(self, json_data):
        self.__json_data = json_data

    @property
    def _json_data(self):
        return self.__json_data