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


from burasabori.settings import FLICKR_KEY
from contrib.api_executor.api_executor import ApiExecutor

class FlickrApiExecutor(ApiExecutor) : 
    def __init__(self, parameters) : 
        base_url = 'https://api.flickr.com/services/rest'
        parameters = parameters
        super(FlickrApiExecutor, self).__init__(base_url, parameters)        

class SearchPhotoApiExecutor(FlickrApiExecutor) : 
    def __init__(self) : 
        parameters = {
                      'method' : 'flickr.photos.search',
                      'api_key' : FLICKR_KEY,
                      'user_id' : None,
                      'tags' : None,
                      'tag_mode' : None,
                      'text' : None,
                      'min_upload_date' : None,
                      'max_upload_date' : None,
                      'min_taken_date' : None,
                      'max_taken_date' : None,
                      'license' : '4,7',
                      'sort' : 'interestingness-desc',
                      'privacy_filter' : 1,
                      'bbox' : None,
                      'accuracy' : None,
                      'safe_search' : None,
                      'content_type' : None,
                      'machine_tags' : None,
                      'machine_tag_mode' : None,
                      'group_id' : None,
                      'contacts' : None,
                      'woe_id' : None,
                      'place_id' : None,
                      'media' : None,
                      'has_geo' : None,
                      'geo_context' : None,
                      'lat' : None,
                      'lon' : None,
                      'radius' : None,
                      'radius_units' : None,
                      'is_commons' : None,
                      'in_gallery' : None,
                      'is_getty' : None,
                      'extras' : None,
                      'per_page' : 5,
                      'page' : None
                      }
        
        super(SearchPhotoApiExecutor, self).__init__(parameters)

class GetInfoPhotoApiExecutor(FlickrApiExecutor) : 
    def __init__(self) : 
        parameters = {
                      'method' : 'flickr.photos.getInfo',
                      'api_key' : FLICKR_KEY,
                      'photo_id' : None,
                      'secret' : None
                      }
        super(GetInfoPhotoApiExecutor, self).__init__(parameters)

