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

from contrib.api_executor.api_executor import ApiExecutor

class LandmarkSearchApiExecuter(ApiExecutor) : 
    
    __base_url = 'https://api.loctouch.com/v1/spots/search'
    
    __parameters = {
                      'lat' : None,
                      'lng' : None,
                      'category_id' : None,
                      'limit' : None
                      }
    
    def __init__(self) : 
        super(LandmarkSearchApiExecuter, self).__init__(LandmarkSearchApiExecuter.__base_url, LandmarkSearchApiExecuter.__parameters) 