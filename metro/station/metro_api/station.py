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

from metro.base_model import BaseModel

class Station(BaseModel):

    @property
    def metro_id(self):
        return self._json_data['owl:sameAs']

    @property
    def japanese(self):
        return self._json_data['dc:title'] + '駅'

    @property
    def english(self):
        return self.metro_id.split('.')[-1]

    @property
    def pub_date(self):
        try:
            return self._json_data['dc:date']
        except KeyError:
            return None

    @property
    def longitude(self):
        return self._json_data['geo:long']

    @property
    def latitude(self):
        return self._json_data['geo:lat']

    @property
    def region(self):
        try:
            return self._json_data['ug:region']
        except KeyError:
            return None

    @property
    def operator(self):
        return self._json_data['odpt:operator']

    @property
    def railway(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        return RailwayManager.get_railway_detail_by_metro_id(self._json_data['odpt:railway'])

    @property
    def connections(self):
        connections = []
        try:
            railways = self._json_data['odpt:connectingRailway']
        except:
            return connections

        from metro.railway.metro_api.railway_manager import RailwayManager
        for railway in railways:
            connections.append(RailwayManager.get_railway_detail_by_metro_id(railway))
        return connections

    @property
    def facilities(self):
        return self._json_data['odpt:facility']

    @property
    def passenger_surveys(self):
        return self._json_data['odpt:passengerSurvey']

    @property
    def code(self):
        return self._json_data['odpt:stationCode']

    @property
    def exits(self):
        return self._json_data['exit']

    @property
    def index(self):
        ordered_stations = self.railway.ordered_stations
        count = 0
        for ordered_station in ordered_stations:
            if ordered_station.metro_id == self.metro_id:
                return count
            else:
                count = count + 1

    @property
    def is_edge(self):
        ordered_stations = self.railway.ordered_stations
        count = 0
        for ordered_station in ordered_stations:
            if ordered_station.metro_id == self.metro_id:
                if count == 0 or len(ordered_stations) -1 == count:
                    return True
            else:
                count = count + 1
        return False