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

from metro.railway.metro_constant.rail_direction import RailDirection

rail_directions = {
    'odpt.RailDirection:TokyoMetro.Asakusa': '浅草',
    'odpt.RailDirection:TokyoMetro.Shibuya': '渋谷',
    'odpt.RailDirection:TokyoMetro.Ikebukuro': '池袋',
    'odpt.RailDirection:TokyoMetro.Ogikubo': '荻窪',
    'odpt.RailDirection:TokyoMetro.NakanoSakaue': '中野坂上',
    'odpt.RailDirection:TokyoMetro.Honancho': '方南町',
    'odpt.RailDirection:TokyoMetro.KitaSenju': '北千住',
    'odpt.RailDirection:TokyoMetro.NakaMeguro': '中目黒',
    'odpt.RailDirection:TokyoMetro.Nakano': '中野',
    'odpt.RailDirection:TokyoMetro.NishiFunabashi': '西船橋',
    'odpt.RailDirection:TokyoMetro.Ayase': '綾瀬',
    'odpt.RailDirection:TokyoMetro.YoyogiUehara': '代々木上原',
    'odpt.RailDirection:TokyoMetro.KitaAyase': '北綾瀬',
    'odpt.RailDirection:TokyoMetro.Wakoshi': '和光市',
    'odpt.RailDirection:TokyoMetro.ShinKiba': '新木場',
    'odpt.RailDirection:TokyoMetro.KotakeMukaihara': '小竹向原',
    'odpt.RailDirection:TokyoMetro.Oshiage': '押上',
    'odpt.RailDirection:TokyoMetro.Meguro': '目黒',
    'odpt.RailDirection:TokyoMetro.AkabaneIwabuchi': '赤羽岩淵',
    'odpt.RailDirection:TokyoMetro.ShirokaneTakanawa': '白金高輪'
}


class RailDirectionManager:

    __rail_directions = rail_directions

    @classmethod
    def get_direction_by_metro_id(cls, metro_id):
        for key in cls.__rail_directions.keys():
            if key == metro_id:
                return RailDirection({'metro_id': key, 'japanese': rail_directions[key]})
        raise KeyError('The direction %s does not exist.' % (metro_id))