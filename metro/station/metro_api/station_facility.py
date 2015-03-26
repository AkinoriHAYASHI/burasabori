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

class TransferInformation(BaseModel):

    @property
    def railway(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        return RailwayManager.get_railway_detail_by_metro_id(self._json_data['odpt:railway'])

    @property
    def rail_direction(self):
        #from metro.railway.metro_constant.rail_direction_manager import RailDirectionManager
        #if 'odpt:railDirection' in self._json_data:
        #    return RailDirectionManager.get_direction_by_metro_id(self._json_data['odpt:railDirection'])
        #else:
        #    return None
        return self._json_data['odpt:railDirection']

    @property
    def necessary_time(self):
        return self._json_data['odpt:necessaryTime']

    def __str__(self):
        str = self.railway + ' '
        if self.rail_direction != None:
            str = str + '(%s) ' % (self.rail_direction)
        str = str + '%s' % (self.necessary_time)
        return str

class PlatformInformation(BaseModel):
    @property
    def railway(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        return RailwayManager.get_railway_detail_by_metro_id(self._json_data['odpt:railway'])

    @property
    def composition(self):
        return self._json_data['odpt:carComposition']

    @property
    def car_number(self):
        return self._json_data['odpt:carNumber']

    @property
    def rail_direction(self):
        from metro.railway.metro_constant.rail_direction_manager import RailDirectionManager
        return RailDirectionManager.get_direction_by_metro_id(self._json_data['odpt:railDirection'])

    @property
    def transfer_informations(self):
        transfers = []
        if 'odpt:transferInformation' in self._json_data.keys():
            for transfer in self._json_data['odpt:transferInformation']:
                transfers.append(TransferInformation(transfer))
        return transfers

    @property
    def metro_transfer_informations(self):
        transfers = []
        if 'odpt:transferInformation' in self._json_data.keys():
            for transfer in self._json_data['odpt:transferInformation']:
                if transfer['odpt:railway'].split('.')[-2] == 'Railway:TokyoMetro':
                    transfers.append(TransferInformation(transfer))
        return transfers

    @property
    def barrier_free_facility(self):
        return None

    @property
    def surrounding_area(self):
        if 'odpt:surroundingArea' in self._json_data:
            return self._json_data['odpt:surroundingArea']
        return []


class BarrierFreeFacility(BaseModel):
    @property
    def metro_id(self):
        return self._json_data['owl:sameAs']

    @property
    def japanese(self):
        return self.category_name

    @property
    def category_name(self):
        return self._json_data['ugsrv:categoryName']

    def get_service_details(self):
        pass

    @property
    def place_name(self):
        return self._json_data['odpt:placeName']

    @property
    def located_area_name(self):
        return self._json_data['odpt:locatedAreaName']

    @property
    def remark(self):
        return self._json_data['ugsrv:remark']

    @property
    def has_assistant(self):
        return None

    @property
    def has_available_to(self):
        return None

class StationFacility(BaseModel):

    @property
    def metro_id(self):
        return self._json_data['owl:sameAs']

    @property
    def pub_date(self):
        return self._json_data['dc:date']

    @property
    def barrier_free_facilities(self):
        facilities = []
        for facility in self._json_data['odpt:barrierfreeFacility']:
            facilities.append(BarrierFreeFacility(facility))
        return facilities

    @property
    def platform_informations(self):
        platforms = []
        for platform in self._json_data['odpt:platformInformation']:
            platforms.append(PlatformInformation(platform))
        return platforms

