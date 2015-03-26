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

class VisitsCountTable:
    def __init__(self):
        from metro.railway.metro_api.railway_manager import RailwayManager
        self.__count_table = {}
        for railway_metro_id in RailwayManager.get_metro_railway_ids():
            self.__count_table[railway_metro_id] = []
            ordered_stations = RailwayManager.get_railway_detail_by_metro_id(railway_metro_id).ordered_stations
            for station in ordered_stations:
                self.__count_table[railway_metro_id].append([station.metro_id, 0])

    def increment(self, current_station_english):
        from metro.station.metro_api.station_manager import StationManager

        stations = StationManager.get_station_details_by_english(current_station_english)

        for station in stations:
            for element in self.__count_table[station.railway.metro_id]:
                if StationManager.get_english_by_metro_id(element[0]) == current_station_english:
                    element[1] = element[1] + 1

    def _get_count_table(self):
        return self.__count_table

    def _get_visits_rate(self, current_station_english, railway_metro_id):
        stations = self.__count_table[railway_metro_id]
        station_num = len(stations)
        lower_count = 0
        higher_count = 0
        num_of_lower_indexed = 0
        num_of_higher_indexed = 0
        is_higher = False
        for i in range(0, station_num):
            if stations[i][0].split('.')[-1] == current_station_english:
                is_higher = True
            elif is_higher == False:
                lower_count = lower_count + stations[i][1]
                num_of_lower_indexed = num_of_lower_indexed + 1
            elif is_higher == True:
                higher_count = higher_count + stations[i][1]
                num_of_higher_indexed = num_of_higher_indexed + 1

        lower_indexed_visits_rate = 100000
        higher_indexed_visits_rate = 100000
        if num_of_lower_indexed != 0:
            lower_indexed_visits_rate = lower_count/num_of_lower_indexed
        if num_of_higher_indexed != 0:
            higher_indexed_visits_rate = higher_count/num_of_higher_indexed
        print('lower_indexed:%s, higher_indexed:%s' % (num_of_lower_indexed, num_of_higher_indexed))
        return lower_indexed_visits_rate, higher_indexed_visits_rate

    def get_visits_rates(self, current_station_english, railway_metro_ids):
        visits_rates = []
        total = 0
        for metro_id in railway_metro_ids:
            lower_indexed_rate, higher_indexed_rate = self._get_visits_rate(current_station_english, metro_id)
            visits_rates.append([metro_id, [lower_indexed_rate, higher_indexed_rate]])

            total = total + lower_indexed_rate + higher_indexed_rate
        return visits_rates, total

    def get_cumulative_unvisits_distribution(self, current_station_english, railway_metro_ids):
        visits_rates, denominator = self.get_visits_rates(current_station_english, railway_metro_ids)

        if denominator == 0:
            previous_cumulative_visits_value = 0
            for visits_rate in visits_rates:
                for i in range(0, len(visits_rate[1])):
                    visits_rate[1][i] = 1 / (2 * len(visits_rates)) + previous_cumulative_visits_value
                    previous_cumulative_visits_value = visits_rate[1][i]
            return visits_rates

        total = 0
        for visits_rate in visits_rates:
            for i in range(0, len(visits_rate[1])):
                visits_rate[1][i] = 1 - visits_rate[1][i]/denominator
                total = total + visits_rate[1][i]

        previous_cumulative_visits_value = 0
        for visits_rate in visits_rates:
            for i in range(0, len(visits_rate[1])):
                visits_rate[1][i] = visits_rate[1][i]/total + previous_cumulative_visits_value
                previous_cumulative_visits_value = visits_rate[1][i]

        return visits_rates