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


from django.utils import timezone

from core import models

class DBInitializer:
    def __init__(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        RailwayManager.update()

        from metro.station.metro_api.station_manager import StationManager
        StationManager.update()

        from metro.station.metro_api.station_facility_manager import StationFacilityManager
        StationFacilityManager.update()

    def register_railway(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        for railway_id in RailwayManager.get_metro_railway_ids():
            railway = RailwayManager.get_railway_detail_by_metro_id(railway_id)
            metro_id = railway.metro_id
            if railway.metro_id == 'odpt.Railway:TokyoMetro.MarunouchiBranch':
                japanese = '丸ノ内線（分岐線）'
            else:
                japanese = railway.japanese
            code = railway.code

            models.Railway.objects.get_or_create(metro_id = metro_id,
                                                 japanese = japanese,
                                                 code = code,
                                                 pub_date = timezone.now())

        for railway_id in RailwayManager.get_other_railway_ids():
            railway = RailwayManager.get_railway_detail_by_metro_id(railway_id)
            metro_id = railway.metro_id
            japanese = railway.japanese
            code = ''
            models.Railway.objects.get_or_create(metro_id = metro_id,
                                                 japanese = japanese,
                                                 code = code,
                                                 pub_date = timezone.now())

    def register_station(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        from metro.station.metro_api.station_manager import StationManager

        for railway_db_obj in models.Railway.objects.all():
            print(railway_db_obj.metro_id, railway_db_obj.japanese)
            railway = RailwayManager.get_railway_detail_by_metro_id(railway_db_obj.metro_id)
            for station in railway.ordered_stations:
                metro_id = station.metro_id
                japanese = station.japanese
                code = station.code
                railway_metro_id = station.railway.metro_id
                index = station.index

                station_db_obj, created = models.Station.objects.get_or_create(
                    metro_id = metro_id,
                    japanese = japanese,
                    code = code,
                    railway = models.Railway.objects.get(metro_id = railway_metro_id),
                    index = index,
                    pub_date = timezone.now())

                for connection in station.connections:
                    station_db_obj.connections.add(models.Railway.objects.get(metro_id = connection.metro_id))

            for station_metro_id in StationManager.get_other_station_ids():
                station = StationManager.get_station_detail_by_metro_id(station_metro_id)
                metro_id = station.metro_id
                japanese = station.japanese
                code =''
                railway = None
                index = 0
                pub_date = timezone.now()

                station_db_obj, created = models.Station.objects.get_or_create(
                    metro_id = metro_id,
                    japanese = japanese,
                    code = code,
                    railway = railway,
                    index = index,
                    pub_date = pub_date
                )