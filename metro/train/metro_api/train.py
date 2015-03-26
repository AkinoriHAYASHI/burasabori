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

from datetime import datetime
import pytz

class Train(BaseModel):

    @property
    def metro_id(self):
        return self._json_data['owl:sameAs']

    @property
    def number(self):
        return self._json_data['odpt:trainNumber']

    @property
    def type(self):
        return self._json_data['odpt:trainType']

    @property
    def pub_date(self):
        return self._json_data['dc:date']

    @property
    def is_valid(self):
        deadline =  datetime.strptime(self._json_data['dct:valid'], '%Y-%m-%dT%H:%M:%S+09:00').\
            replace(tzinfo = pytz.timezone('Asia/Tokyo'))
        if deadline > datetime.now().astimezone(pytz.timezone('Asia/Tokyo')):
            return True
        else:
            return False

    @property
    def frequency(self):
        return int(self._json_data['odpt:frequency'])

    @property
    def railway(self):
        return self._json_data['odpt:railway']

    @property
    def owner(self):
        return self._json_data['odpt:trainOwner']

    @property
    def direction(self):
        from metro.railway.metro_constant.rail_direction_manager import RailDirectionManager
        return RailDirectionManager.get_direction_by_metro_id(self._json_data['odpt:railDirection'])

    @property
    def delay(self):
        return self._json_data['odpt:delay']

    @property
    def starting_station(self):
        from metro.station.metro_api.station_manager import StationManager
        return StationManager.get_station_detail_by_metro_id(self._json_data['odpt:startingStation'])

    @property
    def terminal_station(self):
        from metro.station.metro_api.station_manager import StationManager
        return StationManager.get_station_detail_by_metro_id(self._json_data['odpt:terminalStation'])

    @property
    def from_station(self):
        from metro.station.metro_api.station_manager import StationManager
        return StationManager.get_station_detail_by_metro_id(self._json_data['odpt:fromStation'])

    @property
    def to_station(self):
        station = self._json_data['odpt:toStation']
        if station == 'null':
            return None
        else:
            from metro.station.metro_api.station_manager import StationManager
            return StationManager.get_station_detail_by_metro_id(station)

    @property
    def is_at_station(self):
        if self.to_station == None:
            return True
        else:
            return False

    @property
    def detail_str(self):
        str = self.__str__() + '\n'
        if self.starting_station != None:
            str = str + '始発駅: ' + self.starting_station.japanese + '\n'
        if self.terminal_station != None:
            str = str + '終点: ' + self.terminal_station.japanese + '\n'
        if self.from_station != None:
            str = str + '出発駅: ' + self.from_station.japanese + '\n'
        if self.to_station != None:
            str = str + '次駅: ' + self.to_station.japanese + '\n'
        str = str + '方面' + self.direction.english + '\n'
        return str


    def __str__(self):
        return '%s %s' % (self.railway, self.number)

