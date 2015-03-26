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

from extra_services.landmark.api_executers import LandmarkSearchApiExecuter as LandSearchAPI


class LandmarkDataProvider():
      
    __land_api = LandSearchAPI()
    
    __key_spots = 'spots'
    __key_name = 'name'
    
    __request_lat = 'lat'
    __request_lng = 'lng'
    
    def get_landmark(latitude, longitude):
        request_parameter = {
                             LandmarkDataProvider.__request_lat : latitude,
                             LandmarkDataProvider.__request_lng : longitude
                             }
        
        json_data = LandmarkDataProvider.__land_api.get_data(request_parameter)
        
        spots = json_data[LandmarkDataProvider.__key_spots]
        
        if len(spots) > 0:
            return spots[0][LandmarkDataProvider.__key_name]
                
        return None