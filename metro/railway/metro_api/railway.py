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

class TravelTime(BaseModel):
    @property
    def from_station(self):
        from metro.station.metro_api.station_manager import StationManager
        return StationManager.get_station_detail_by_metro_id(self._json_data['odpt:fromStation'])

    @property
    def to_station(self):
        from metro.station.metro_api.station_manager import StationManager
        return StationManager.get_station_detail_by_metro_id(self._json_data['odpt:toStation'])

    @property
    def necessary_time(self):
        return self._json_data['odpt:necessaryTime']

    @property
    def train_type(self):
        return self._json_data['odpt:trainType']

    def __str__(self):
        return '%s -> %s (%s分, %s)' % (self.from_station, self.to_station, self.necessary_time, self.train_type)

class Railway(BaseModel):

    @property
    def metro_id(self):
        return self._json_data['owl:sameAs']

    @property
    def pub_date(self):
        return self._json_data['dc:date']

    @property
    def japanese(self):
        return self._json_data['dc:title'] + '線'

    @property
    def english(self):
        return self.metro_id.split('.')[-1]

    @property
    def region(self):
        return self._json_data['ug:region']

    @property
    def operator(self):
        return self._json_data['odpt:operator']

    @property
    def ordered_stations(self):
        stations = []
        from metro.station.metro_api.station_manager import StationManager

        if not 'odpt:stationOrder' in self._json_data.keys():
            return stations

        for order in self._json_data['odpt:stationOrder']:
            stations.append(StationManager.get_station_detail_by_metro_id(order['odpt:station']))
        return stations

    @property
    def travel_times(self):
        times = []
        for travel_time in self._json_data['odpt:travelTime']:
            times.append(TravelTime(travel_time))
        return times

    @property
    def code(self):
        return self._json_data['odpt:lineCode']

    @property
    def women_only_car(self):
        return self._json_data['odpt:womenOnlyCar']

    def compare_station_indexes(self, station1_metro_id, station2_metro_id):
        if station1_metro_id == station2_metro_id:
            return 0

        for station in self.ordered_stations:
            if station1_metro_id == station:
                return 1
            elif station2_metro_id == station:
                return 2
