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

from burasabori.settings import GURUNAVI_KEY
from contrib.api_executor.api_executor import ApiExecutor

class PhotoSearchApiExecuter(ApiExecutor):
    def __init__(self):
        base_url = 'http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/'
        
        parameters = {
                      'keyid':GURUNAVI_KEY,
                      'format' : None,
                      'callback' : None,
                      'shop_id' : None,
                      'latitude' : None,
                      'longitude' : None,
                      'range' : None,
                      'shop_name' : None,
                      'area' : None,
                      'comment' : None,
                      'first_shop_message' : None,
                      'menu_name' : None,
                      'photo_scene_id' : None,
                      'hit_per_page' : 50,
                      'offset_page' : None,
                      'offset' : None,
                      'order' : None,
                      'sort' : None,
                      'vote_date' : None,
                      'photo_genre_id' : None,
                      }
        super(PhotoSearchApiExecuter, self).__init__(base_url, parameters) 
            
class RestSearchApiExecuter(ApiExecutor):
    def __init__(self):
        base_url = 'http://api.gnavi.co.jp/ver1/RestSearchAPI/'
        
        parameters = {
                       'keyid':GURUNAVI_KEY,
                       'id':None,
                       'format':None,
                       'callback':None,
                       'name':None,
                       'name_kana':None,
                       'tel':None,
                       'address':None,
                       'area':None,
                       'pref':None,
                       'category_l':None,
                       'category_s':None,
                       'input_coordinates_mode':None,
                       'equipment':None,
                       'coordinates_mode':None,
                       'latitude':None,
                       'longitude':None,
                       'range':3,
                       'sort':None,
                       'offset':None,
                       'hit_per_page':None,
                       'offset_page':None,
                       'freeword':None,
                       'freeword_condition': 2
                       }
        super(RestSearchApiExecuter, self).__init__(base_url, parameters) 
        