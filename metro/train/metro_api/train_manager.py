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

from metro.base_model_manager import BaseModelManager
from metro.train.metro_api.api_executor import TrainApiExecutor
from metro.train.metro_api.train import Train

class TrainManager(BaseModelManager):
    _api_executor = TrainApiExecutor()

    @classmethod
    def update(cls):
        cls._api_json_data = cls._api_executor.get_data()

    @classmethod
    def get_frequency(cls):
        if len(cls._api_json_data) > 0:
            return cls._api_json_data[0]['odpt:frequency']
        else:
            return 90

    @classmethod
    def get_incoming_trains_by_station_metro_ids(cls, metro_ids):
        trains = []
        for train in cls._api_json_data:
            if train['odpt:toStation'] in metro_ids or \
                            train['odpt:fromStation'] in metro_ids and train['odpt:toStation'] == None:
                trains.append(Train(train))
        return trains

    @classmethod
    def get_target_train_by_metro_id(cls, metro_id):
        for train in cls._api_json_data:
            if train['owl:sameAs'] == metro_id:
                return Train(train)
        return None