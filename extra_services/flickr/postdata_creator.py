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

from extra_services.postdata_creator import PostdataCreator as CreatorBase
from core.exceptions import PostDataCreatorPageNotFound
from extra_services.flickr.data_providers import SearchDataProvider
from extra_services.flickr.data_providers import PhotoDataProvider
from extra_services.landmark.data_providers import LandmarkDataProvider


class FlickrPostdataCreator(CreatorBase):
    
    __station_limit_num = 100
    __data_num = 3
    
    def __init__(self):
        super(FlickrPostdataCreator, self).__init__(
                                                      FlickrPostdataCreator.__station_limit_num,
                                                      self._get_add_data
                                                      )

    def __get_userdata(self, photo_id):
        parameter = PhotoDataProvider.get_request_photo_id(photo_id)
        json_data = PhotoDataProvider.get_json_data(parameter)
        
        username = PhotoDataProvider.get_username(json_data)
        user_url = PhotoDataProvider.get_user_url(json_data)
        
        return username, user_url
    
    def __get_format_data(self,
                          user,
                          userurl,
                          photo_url,
                          landmark
                          ):
        
        return {
                'user' : user,
                'user_url' : userurl,
                'photo_url' : photo_url,  
                'landmark' : landmark,
                }
        
    
    def get_data(self, area, latitude, longitude):
        try:
            area = LandmarkDataProvider.get_landmark(latitude, longitude)
            request_option = SearchDataProvider.get_request_text(area)
            return self._get_station_data(area, request_option)
        except:
            raise PostDataCreatorPageNotFound()
    
    
    
    def _get_add_data(self, option):
        searched_data = SearchDataProvider.get_json_data(option)
        total = SearchDataProvider.get_total(searched_data)
        request_text = SearchDataProvider.search_request_text(option)
        
        if total != None:
            total = int(total)
        
        if total == None or total == 0 :
            data = self.__get_format_data(
                                          None,
                                          None, 
                                          None,
                                          None)
            return 0, data
        elif total == 1:
            photo = SearchDataProvider.get_photo(searched_data)
            photo_id = SearchDataProvider.get_photo_id(photo)
            photo_url = SearchDataProvider.get_photo_url(photo)
            user, userurl = self.__get_userdata(photo_id)
            
            data = self.__get_format_data(user, userurl, photo_url, request_text)
            
            return 1, [data]
        else:
            photo = SearchDataProvider.get_photo(searched_data)
            
            if total < FlickrPostdataCreator.__data_num:
                end = total
            else:
                end = FlickrPostdataCreator.__data_num
                
            all_data = []
            for i in range(0, end):
                photo_id = SearchDataProvider.get_photo_id(photo[i])
                photo_url = SearchDataProvider.get_photo_url(photo[i])
                user, userurl = self.__get_userdata(photo_id)
                data = self.__get_format_data(user, userurl, photo_url, request_text)
                all_data.append(data)
            return end, all_data
            
        