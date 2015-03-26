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

__author__ = 'Ak\inori Hayashi'

from extra_services.flickr.api_executers import SearchPhotoApiExecutor as SearchPhotoAPI
from extra_services.flickr.api_executers import GetInfoPhotoApiExecutor as GetInfoAPI

class SearchDataProvider():
    
    __search_api = SearchPhotoAPI()
    
    __key_rsp = 'rsp'
    __key_photos = 'photos'
    __key_pages = '@pages'
    __key_total = '@total'
    __key_photo = 'photo'
    __key_photo_id = '@id'
    __key_owner = '@owner'
    __key_secret = '@secret'
    __key_server = '@server'
    
    __request_text = 'text'
    __request_page = 'page'
    __request_longitude = 'lon'
    __request_latitude = 'lat'
    
    __photo_url = 'https://farm1.staticflickr.com/%s/%s_%s.jpg'
    
    def __get_photo(json_data):
        return json_data[SearchDataProvider.__key_rsp][SearchDataProvider.__key_photos]
    
    def get_request_text(value):
        return {SearchDataProvider.__request_text : value}
    
    def get_request_page(value):
        return {SearchDataProvider.__request_page : value}
    
    def get_request_longitude(value):
        return {SearchDataProvider.__request_longitude : value}
    
    def get_request_latitude(value):
        return {SearchDataProvider.__request_latitude : value}
    
    def get_json_data(parameter):
        return SearchDataProvider.__search_api.get_data(parameter)
    
    def get_pages(json_data):
        result = None
        try:
            photos = SearchDataProvider.__get_photo(json_data)
            result = photos[SearchDataProvider.__key_pages]
        except:
            pass
        return result
    
    def get_total(json_data):
        result = None
        try:
            photos = SearchDataProvider.__get_photo(json_data)
            result = photos[SearchDataProvider.__key_total]
        except:
            pass
        return result
    
    def get_photo(json_data):
        result = None
        try:
            photos = SearchDataProvider.__get_photo(json_data)
            result = photos[SearchDataProvider.__key_photo]
        except:
            pass
        return result

    def get_photo_id(photo):
        result = None
        try:
            result = photo[SearchDataProvider.__key_photo_id]
        except:
            pass
        return result
        
    def get_photo_url(photo):
        result = None
        try:
            photo_id = photo[SearchDataProvider.__key_photo_id]
            secret = photo[SearchDataProvider.__key_secret]
            server = photo[SearchDataProvider.__key_server]
            result = SearchDataProvider.__photo_url % (server, photo_id, secret)
        except:
            pass
        return result
    
    def search_request_text(option):
        result = None
        if SearchDataProvider.__request_text in option:
            result = option[SearchDataProvider.__request_text]
        return result

class PhotoDataProvider():
    
    __getinfo_api = GetInfoAPI()
    
    __key_rsp = 'rsp'
    __key_photo= 'photo'
    __key_owner = 'owner'
    __key_nsid = '@nsid'
    __key_username = '@username'
    __key_urls = 'urls'
    __key_url = 'url'
    __key_text = '#text'
    
    __request_photo_id = 'photo_id'
     
    __user_url = 'https://www.flickr.com/people/%s/'
    
    def __get_photo(json_data):
        return json_data[PhotoDataProvider.__key_rsp][PhotoDataProvider.__key_photo]
    
    def get_request_photo_id(value):
        return {PhotoDataProvider.__request_photo_id : value}
    
    def get_json_data(parameter):
        try:
            result = PhotoDataProvider.__getinfo_api.get_data(parameter)
        except:
            pass
        return result
    
    def get_username(json_data):
        try:
            photo = PhotoDataProvider.__get_photo(json_data)
            result =  photo[PhotoDataProvider.__key_owner][PhotoDataProvider.__key_username]
        except:
            pass
        return result
    
    def get_user_url(json_data):
        try:
            photo = PhotoDataProvider.__get_photo(json_data)
            nsid = photo[PhotoDataProvider.__key_owner][PhotoDataProvider.__key_nsid]
            result = PhotoDataProvider.__user_url % (nsid)
        except:
            pass
        return result
    
    