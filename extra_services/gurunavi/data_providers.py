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

from extra_services.gurunavi.api_executers import PhotoSearchApiExecuter as PhotoAPI
from extra_services.gurunavi.api_executers import RestSearchApiExecuter as RestAPI


class RestDataProvider():
    
    __rest_api = RestAPI()
    
    __key_response = 'response'
    __key_rest = 'rest'
    __key_total_hit = 'total_hit_count' 
    __key_name = 'name'
    __key_category = 'category'
    __key_image_url = 'image_url'
    __key_shop_image1 = 'shop_image1'
    __key_address = 'address'
    __key_mobile_url = 'url_mobile'
    __key_shop_url = 'url'
    __key_latitude = 'latitude'
    __key_longitude = 'longitude'
    __key_id = 'id'
    __key_hit_per_page = 'hit_per_page'
    __key_page_offset = 'page_offset'
    __request_offset = 'offset'
    __request_freeword = 'freeword'
    __request_address = 'address'
    __request_latitude = 'latitude'
    __request_longitude = 'longitude'
    
    def get_request_freeword(value):
        return {RestDataProvider.__request_freeword : value}
        
    def get_request_offset(value):
        return {RestDataProvider.__request_offset : value}
    
    def get_request_address(value):
        return {RestDataProvider.__request_address : value}
    
    def get_request_latitude(value):
        return {RestDataProvider.__request_latitude : value}
    
    def get_request_longitude(value):
        return {RestDataProvider.__request_longitude : value}
    
    def get_json_data(parameter):
        return RestDataProvider.__rest_api.get_data(parameter)
    
    def get_total_hit_count(json_data):
        result = None
        try:
            result = json_data[RestDataProvider.__key_response][RestDataProvider.__key_total_hit]
        except:
            pass
        return result
    
    def get_hit_per_page(json_data):
        result = None
        try:
            result = json_data[RestDataProvider.__key_response][RestDataProvider.__key_hit_per_page]
        except:
            pass
        return result
    
    def get_page_offset(json_data):
        result = None
        try:
            result = json_data[RestDataProvider.__key_response][RestDataProvider.__key_page_offset]
        except:
            pass
        return result
        
    def get_rest(json_data):
        result = None
        try:
            result = json_data[RestDataProvider.__key_response][RestDataProvider.__key_rest]
        except:
            pass
        return result
        
    def get_name(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_name]
        except:
            pass
        return result
    
    def get_category(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_category]
        except:
            pass
        return result
    
    def get_image_url(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_image_url][RestDataProvider.__key_shop_image1]
        except:
            pass
        return result
    
    def get_address(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_address]
        except:
            pass
        return result
    
    def get_shop_url(rest_data):
        result = None
        try:
            if RestDataProvider.__key_mobile_url in rest_data:
                result = rest_data[RestDataProvider.__key_mobile_url]
            else:
                result = rest_data[RestDataProvider.__key_shop_url]            
        except:
            pass
        return result
        
    def get_latitude(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_latitude]
        except:
            pass
        return result
    
    def get_longitude(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_longitude]
        except:
            pass
        return result
    
    def get_shop_id(rest_data):
        result = None
        try:
            result = rest_data[RestDataProvider.__key_id]
        except:
            pass
        return result

class PhotoDataProvider():
    __photo_api = PhotoAPI()
    
    __key_response = 'response'
    __key_total_hit_count = 'total_hit_count'
    __key_photo = 'photo'
    __key_nickname = 'nickname' 
    __key_image_url = 'image_url'
    __key_imgage_size = 'url_250'
    __key_comment = 'comment'
    __key_total_score = 'total_score'
    __key_menu_name = 'menu_name'
    
    __request_shop_id = 'shop_id'
    
    def get_request_shop_id(value):
        return {PhotoDataProvider.__request_shop_id : value}
        
    def get_json_data(parameter):
        return PhotoDataProvider.__photo_api.get_data(parameter)
    
    def get_photo(json_data):
        result = None
        try:
            result = json_data[PhotoDataProvider.__key_response][PhotoDataProvider.__key_photo]
        except:
            pass
        return result
    
    def get_total_hit_count(json_data):
        result = None
        try:
            result = json_data[PhotoDataProvider.__key_response][PhotoDataProvider.__key_total_hit_count]
        except:
            pass
        return result
            
    def get_nickname(photo_data):
        result = None
        try:
            result = photo_data[PhotoDataProvider.__key_nickname]
        except:
            pass
        return result
    
    def get_image_url(photo_data):
        result = None
        try:
            result = photo_data[PhotoDataProvider.__key_image_url][PhotoDataProvider.__key_imgage_size]
        except:
            pass
        return result
    
    def get_menu_name(photo_data):
        result = None
        try:
            result = photo_data[PhotoDataProvider.__key_menu_name]
        except:
            pass
        return result
    
    def get_comment(photo_data):
        result = None
        try:
            result = photo_data[PhotoDataProvider.__key_comment]
        except:
            pass
        return result
    
    def get_score_average(json_data):
        result = None
        try:
            hit_page = PhotoDataProvider.get_hit_per_page(json_data)
            hit_page = int(hit_page)
            photos = PhotoDataProvider.get_photo(json_data)
            
            if hit_page > 1:
                total_count = 0
                total_score = 0
                for i in range(0, hit_page):
                    photo = photos[i]
                    total_count = total_count + 1
                    score = photo[PhotoDataProvider.__key_total_score]
                    total_score = total_score + float(score)                    
                result = total_score / total_count
            else:
                total_score = photos[PhotoDataProvider.__key_total_score]
                result = float(total_score)
            
            result = round(result, 1)
        except:
            pass
        return result
    
        