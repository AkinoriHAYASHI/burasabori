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

import random

from extra_services.postdata_creator import PostdataCreator as CreatorBase
from extra_services.postdata_creator import TimeTable
from core.exceptions import PostDataCreatorPageNotFound
from extra_services.gurunavi.data_providers import RestDataProvider
from extra_services.gurunavi.data_providers import PhotoDataProvider


class GurunaviPostdataCreator(CreatorBase):
    
    __freeword_table = {
                        TimeTable.Morning : '朝,モーニング',
                        TimeTable.Noon : '昼,ランチ',
                        TimeTable.AfterNoon : 'デザート,スイーツ',
                        TimeTable.Night : '夕,ディナー',
                        TimeTable.MidNight : '晩,バー,カクテル',
                        }
    
    __morning_shop_name_length = 10
    
    __station_limit_num = 100
    __data_num = 3
    
    def __init__(self):
        super(GurunaviPostdataCreator, self).__init__(
                                                      GurunaviPostdataCreator.__station_limit_num,
                                                      self._get_add_data
                                                      )
    
    def __get_freeword(self):
        timetable = self._get_timetable()
        freeword = GurunaviPostdataCreator.__freeword_table[timetable]
        return freeword
    
    def __get_photo_data(self, shop_id):
        parameter = PhotoDataProvider.get_request_shop_id(shop_id)
        
        response = PhotoDataProvider.get_json_data(parameter)
        photo_data = PhotoDataProvider.get_photo(response)
        hit_page = PhotoDataProvider.get_total_hit_count(response)
        
        nickname = None
        meal_name = None
        image_url = None
        comment = None
        eval_average = None
        
        if photo_data != None:
            hit_page = int(hit_page)
            if hit_page > 1:
                index = random.randint(0, hit_page - 1)
                photo = photo_data[index]
            else:
                photo = photo_data
            nickname = PhotoDataProvider.get_nickname(photo)
            meal_name = PhotoDataProvider.get_menu_name(photo)
            image_url = PhotoDataProvider.get_image_url(photo)
            comment = PhotoDataProvider.get_comment(photo)
            eval_average = PhotoDataProvider.get_score_average(response)
        
        return nickname, meal_name, image_url, comment, eval_average
    
    def __get_format_data(self,
                          name,
                          address,
                          shop_url,
                          meal_category,
                          eval_average,
                          image_url,
                          related_urls
                          ):
        return {
                'name' : name,
                'address' : address,
                'shop_url' : shop_url,
                'meal_category' : meal_category,
                'eval_average' : eval_average,
                'image_url' : image_url,
                'related_urls' : related_urls
                }
        
    def __get_related_data(self,
                           meal_name,
                           meal_url,
                           comment,
                           committer
                           ):
        return {
                'meal_name' : meal_name,
                'meal_url' : meal_url,
                'comment' : comment,
                'committer' : committer
                }
    
    def __create_data_from_restdata(self, rest):
        name = RestDataProvider.get_name(rest)
        address = RestDataProvider.get_address(rest)
        shop_url = RestDataProvider.get_shop_url(rest)
        category = RestDataProvider.get_category(rest)
        image_url = RestDataProvider.get_image_url(rest)
        shop_id = RestDataProvider.get_shop_id(rest)
        
        nickname, meal_name, meal_url, comment, eval_average = self.__get_photo_data(shop_id)
        
        related = self.__get_related_data(meal_name, meal_url, comment, nickname)
        
        return self.__get_format_data(
                                      name,
                                      address, 
                                      shop_url, 
                                      category, 
                                      eval_average, 
                                      image_url, 
                                      related)
    
    def __is_accept_shop_name_length(self, timetable, rest):
        result = True
        if timetable == TimeTable.Morning:
            name = RestDataProvider.get_name(rest)
            if GurunaviPostdataCreator.__morning_shop_name_length < len(name):
                result = False
        return result
    
    def __get_None_data(self):
        related = self.__get_related_data(None, None, None, None)
        data = self.__get_format_data(
                                      None,
                                      None, 
                                      None, 
                                      None, 
                                      None, 
                                      None, 
                                      related)
        return data        
    
    def get_data(self, area, latitude, longitude):
        try:
            request_option = {}
            request_area = RestDataProvider.get_request_latitude(latitude)
            request_area.update(RestDataProvider.get_request_longitude(longitude))
            request_option = RestDataProvider.get_request_freeword(self.__get_freeword())
            request_option.update(request_area)
    
            return self._get_station_data(area, request_option)
        except:
            raise PostDataCreatorPageNotFound()
            
    def _get_add_data(self, option):
        
        json_data = RestDataProvider.get_json_data(option)

        # first search
        hit = RestDataProvider.get_total_hit_count(json_data)
        
        timetable = self._get_timetable()
        
        if hit != None:
            hit = int(hit)
        
        if hit == None or hit == 0 :
            data = self.__get_None_data()
            return 0, data
        elif hit == 1:
            rest = RestDataProvider.get_rest(json_data)
            
            if self.__is_accept_shop_name_length(timetable, rest):    
                return 1, [self.__create_data_from_restdata(rest)]
            else:
                data = self.__get_None_data()
                return 0, data
        else:
            rest = RestDataProvider.get_rest(json_data)
            
            add_num = 0
            all_data = []
            for i in range(0, len(rest)):
                if self.__is_accept_shop_name_length(timetable, rest[i]):
                    all_data.append(self.__create_data_from_restdata(rest[i]))
                    add_num = add_num + 1
                    if add_num >= GurunaviPostdataCreator.__data_num:
                        break
            
            return add_num, all_data