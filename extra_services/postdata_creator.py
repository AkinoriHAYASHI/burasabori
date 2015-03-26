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

__author__ = 'Akinori Hayashi'

from core import exceptions
import copy, sys, random, pytz
from enum import Enum
from django.utils import timezone

class PostdataCreator:
    
    __key_access_count = 'access_count'
    __key_data_num = 'data_num'
    __key_data = 'data'
    __key_option_key = 'search_option'
    
    # data format
    # { 'station' : {
    #                'option_key' : data
    #                'access_count' : data,
    #                'data_num' : data,
    #                'data' : [{post data},{post_data}]
    #                },
    #   'station' : {...            
    #}
    
    def __init__(self, station_limit, get_data_method):  
        self.__station_limit = station_limit
        self.__get_data_method = get_data_method
        self._dataDictionary = {}
    
    def __get_random_data(self, area, option):
        station_data = self._dataDictionary[area]
        data_num = station_data[PostdataCreator.__key_data_num]
        data = station_data[PostdataCreator.__key_data]
        
        result = None
        if data_num > 0:
            station_data[PostdataCreator.__key_access_count] = station_data[PostdataCreator.__key_access_count] + 1
            data_num = int(data_num) - 1
            index = random.randint(0, data_num)
            result = data[index]
        return result
    
    def __add_data_dictionary(self, area, option, data_num, data):
        
        if len(self._dataDictionary) >= self.__station_limit:
            min = sys.maxsize
            delete_key = None
            for key, value in self._dataDictionary.items():
                access = value[PostdataCreator.__key_access_count]
            
                if access < min:
                    delete_key = key
                    min = access
            del self._dataDictionary[delete_key]
        self._dataDictionary[area] = {
                                      PostdataCreator.__key_access_count : 0,
                                      PostdataCreator.__key_data_num : data_num,
                                      PostdataCreator.__key_data : data,
                                      PostdataCreator.__key_option_key : option
                                      }
    
    def __update_data_dictionary(self, area, option):
        data_num, add_data = self.__get_data_method(option)
        self._dataDictionary[area][PostdataCreator.__key_data_num] = data_num
        self._dataDictionary[area][PostdataCreator.__key_data] = add_data
        self._dataDictionary[area][PostdataCreator.__key_option_key] = option
        
    def get_data(self, parameters):
        raise Exception('undefined get_data API')
    
    def _get_add_data(self, latitude, longitude):
        raise Exception('undefined _get_add_data API')
    
    def _get_timetable(self):
        d = timezone.now().astimezone(pytz.timezone('Asia/Tokyo'))
        return TimeTable.get_timetable(d.hour)
    
    def _get_station_data(self, area, option):
        data = None
        
        if ((area in self._dataDictionary) and
            (self._dataDictionary[area][PostdataCreator.__key_option_key] != option)):
            self.__update_data_dictionary(area, option)
        elif area not in self._dataDictionary:
            data_num, add_data = self.__get_data_method(option)
            self.__add_data_dictionary(area, option, data_num, add_data)
            
            if data_num == 0:
                return None
        
        data = self.__get_random_data(area, option)
        return data
    
class TimeTable(Enum):
    Morning = 12
    Noon = 15
    AfterNoon = 18
    Night = 21
    MidNight = 24
        
    @classmethod
    def get_timetable(cls, hour):
        if hour < TimeTable.Morning.value:
            return TimeTable.Morning
        elif hour < TimeTable.Noon.value:
            return TimeTable.Noon
        elif hour < TimeTable.AfterNoon.value:
            return TimeTable.AfterNoon
        elif hour < TimeTable.Night.value:
            return TimeTable.Night
        else:
            return TimeTable.MidNight