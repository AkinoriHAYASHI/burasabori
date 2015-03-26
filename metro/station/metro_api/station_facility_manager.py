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
from metro.station.metro_api.api_executor import StationFacilityApiExecutor
from metro.station.metro_api.station_facility import StationFacility

class StationFacilityManager(BaseModelManager):

    _api_executor = StationFacilityApiExecutor()

    @classmethod
    def get_facility_detail_by_station_metro_id(cls, metro_id):
        for facility in cls._api_json_data:
            if facility['owl:sameAs'] == 'odpt.StationFacility:TokyoMetro.' + metro_id.split('.')[-1]:
                return StationFacility(facility)
        return None

    @classmethod
    def get_facility_detail_by_station_english(cls, english):
        for facility in cls._api_json_data:
            if facility['owl:sameAs'].split('.')[-1] == english:
                return StationFacility(facility)
        return None