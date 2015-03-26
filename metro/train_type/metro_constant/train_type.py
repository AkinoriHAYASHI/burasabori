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

from metro.base_model import BaseModel
from metro.base_manager import BaseModelManager

train_types = [
    {'metro_id': 'odpt.TrainType:Local', 'japanese': '普通'},
    {'metro_id': 'odpt.TrainType:Rapid', 'japanese': '快速'},
    {'metro_id': 'odpt.TrainType:Express', 'japanese': '急行'},
    {'metro_id': 'odpt.TrainType:LimitedExpress', 'japanese': '特急'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.Unknown', 'japanese': '不明'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.Local', 'japanese': '各停'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.Express', 'japanese': '急行'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.Rapid', 'japanese': '快速'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.SemiExpress', 'japanese': '準急'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.TamaExpress', 'japanese': '多摩急行'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.HolidayExpress', 'japanese': '土休急行'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.CommuterSemiExpress', 'japanese': '通勤準急'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.Extra', 'japanese': '臨時'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.RomanceCar', 'japanese': '特急ロマンスカー'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.RapidExpress', 'japanese': '快速急行'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.CommuterExpress', 'japanese': '通勤急行'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.LimitedExpress', 'japanese': '特急'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.CommuterLimitedExpress', 'japanese': '通勤特急'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.CommuterRapid', 'japanese': '通勤快速'},
    {'metro_id': 'odpt.TrainType:TokyoMetro.ToyoRapid', 'japanese': '東葉快速'},
]

class TrainType(BaseModel):
    @property
    def metro_id(self):
        return self._json_data['metro_id']

    @property
    def japanese(self):
        return self._json_data['japanese']

    @property
    def english(self):
        return self.metro_id.split('.')[-1]

class TrainTypeManager(BaseModelManager):
    __train_types = train_types

    def __init__(self):
        super(TrainTypeManager, self).__init__(self.__train_types)

    @classmethod
    def get_train_type_by_metro_id(cls, metro_id):
        for train_type in cls.__train_types:
            if train_type['metro_id'] == metro_id:
                return TrainType(train_type)
        return None

def test():
    for train_type in train_types:
        type = TrainTypeManager.get_train_type_by_metro_id(train_type['metro_id'])
        print(type.metro_id, type.japanese, type.english)