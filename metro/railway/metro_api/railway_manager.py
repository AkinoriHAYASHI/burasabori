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

from metro.base_model_manager import BaseModelManager
from metro.railway.metro_api.api_executor import RailwayApiExecutor
from metro.railway.metro_constant.railway import metro_railways, other_railways
from metro.railway.metro_api.railway import Railway


class RailwayManager(BaseModelManager):
    __metro_railways = metro_railways
    __other_railways = other_railways

    _api_executor = RailwayApiExecutor()

    @classmethod
    def get_metro_raliway_ids_with_japanese(cls):
        railways = []
        for metro_railway in cls.__metro_railways:
            railways.append([metro_railway['metro_id'], metro_railway['japanese']])
        return railways


    @classmethod
    def get_metro_railway_ids(cls):
        railways = []
        for metro_railway in cls.__metro_railways:
            railways.append(metro_railway['metro_id'])
        return railways

    @classmethod
    def get_other_railway_ids(cls):
        railways = []
        for metro_railway in cls.__other_railways:
            railways.append(metro_railway['metro_id'])
        return railways

    @classmethod
    def get_japanese(cls, metro_id):
        for railway in cls.__metro_railways:
            if metro_id == railway['metro_id']:
                return railway['japanese'], True

        for railway in cls.__other_railways:
            if metro_id == railway['metro_id']:
                return railway['japanese'], False

    @classmethod
    def get_metro_id(cls, english):
        for railway in metro_railways:
            if railway['metro_id'].split('.')[-1] == english:
                return railway['metro_id'], True
        for railway in other_railways:
            if railway['metro_id'].split('.')[-1] == english:
                return railway['metro_di'], False

    @classmethod
    def get_english(cls, metro_id):
        return metro_id.split('.')[-1]

    @classmethod
    def is_metro(cls, metro_id):
        for railway in cls.__metro_railways:
            if metro_id == railway['metro_id']:
                return True

    @classmethod
    def get_railway_detail_by_metro_id(cls, metro_id):
        for railway in cls._api_json_data:
            if railway['owl:sameAs'] == metro_id:
                return Railway(railway)
        for railway in other_railways:
            if railway['metro_id'] == metro_id:
                return Railway({'owl:sameAs': railway['metro_id'], 'dc:title': railway['japanese']})

def test():
    print(RailwayManager.get_metro_railway_ids())

    for metro_id in RailwayManager.get_metro_railway_ids():
        japanese, is_metro = RailwayManager.get_japanese(metro_id)
        print('%s, %s' % (japanese, is_metro))

    for metro_id in RailwayManager.get_other_railway_ids():
        japanese, is_metro = RailwayManager.get_japanese(metro_id)
        print('%s, %s' % (japanese, is_metro))