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

metro_railways = [
    {'metro_id': 'odpt.Railway:TokyoMetro.Ginza', 'japanese': '銀座線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Marunouchi', 'japanese': '丸ノ内線（本線）'},
    {'metro_id': 'odpt.Railway:TokyoMetro.MarunouchiBranch', 'japanese': '丸ノ内線（支線）'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Hibiya', 'japanese': '日比谷線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Tozai', 'japanese': '東西線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Chiyoda', 'japanese': '千代田線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Yurakucho', 'japanese': '有楽町線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Hanzomon', 'japanese': '半蔵門線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Namboku', 'japanese': '南北線'},
    {'metro_id': 'odpt.Railway:TokyoMetro.Fukutoshin', 'japanese': '副都心線'}]

other_railways = [
    {'metro_id': 'odpt.Railway:JR-East', 'japanese': 'JR線'},
    {'metro_id': 'odpt.Railway:JR-East.Chuo', 'japanese': '中央線'},
    {'metro_id': 'odpt.Railway:JR-East.ChuoKaisoku', 'japanese': '中央線快速'},
    {'metro_id': 'odpt.Railway:JR-East.ChuoSobu', 'japanese': '中央・総武線各駅停車'},
    {'metro_id': 'odpt.Railway:JR-East.Joban', 'japanese': '常磐線'},
    {'metro_id': 'odpt.Railway:JR-East.KeihinTohoku', 'japanese': '京浜東北線'},
    {'metro_id': 'odpt.Railway:JR-East.Keiyo', 'japanese': '京葉線'},
    {'metro_id': 'odpt.Railway:JR-East.Musashino', 'japanese': '武蔵野線'},
    {'metro_id': 'odpt.Railway:JR-East.NaritaExpress', 'japanese': '成田エクスプレス'},
    {'metro_id': 'odpt.Railway:JR-East.Saikyo', 'japanese': '埼京線'},
    {'metro_id': 'odpt.Railway:JR-East.ShonanShinjuku', 'japanese': '湘南新宿ライン'},
    {'metro_id': 'odpt.Railway:JR-East.Sobu', 'japanese': '総武線'},
    {'metro_id': 'odpt.Railway:JR-East.Takasaki', 'japanese': '高崎線'},
    {'metro_id': 'odpt.Railway:JR-East.Tokaido', 'japanese': '東海道線'},
    {'metro_id': 'odpt.Railway:JR-East.Utsunomiya', 'japanese': '宇都宮線'},
    {'metro_id': 'odpt.Railway:JR-East.Yamanote', 'japanese': '山手線'},
    {'metro_id': 'odpt.Railway:JR-East.Yokosuka', 'japanese': '横須賀線'},
    {'metro_id': 'odpt.Railway:Keio.Inokashira', 'japanese': '井の頭線'},
    {'metro_id': 'odpt.Railway:Keio.Keio', 'japanese': '京王線'},
    {'metro_id': 'odpt.Railway:Keio.New', 'japanese': '京王新線'},
    {'metro_id': 'odpt.Railway:Keisei.KeiseiMain', 'japanese': '京成本線'},
    {'metro_id': 'odpt.Railway:Keisei.KeiseiOshiage', 'japanese': '押上線'},
    {'metro_id': 'odpt.Railway:MIR.TX', 'japanese': 'つくばエクスプレス線'},
    {'metro_id': 'odpt.Railway:Odakyu.Odawara', 'japanese': '小田原線'},
    {'metro_id': 'odpt.Railway:SaitamaRailway.SaitamaRailway', 'japanese': '埼玉高速鉄道線'},
    {'metro_id': 'odpt.Railway:Seibu.Ikebukuro', 'japanese': '池袋線'},
    {'metro_id': 'odpt.Railway:Seibu.SeibuYurakucho', 'japanese': '西武有楽町線'},
    {'metro_id': 'odpt.Railway:Seibu.Shinjuku', 'japanese': '新宿線'},
    {'metro_id': 'odpt.Railway:TWR.Rinkai', 'japanese': 'りんかい線'},
    {'metro_id': 'odpt.Railway:Tobu.Isesaki', 'japanese': '伊勢崎線'},
    {'metro_id': 'odpt.Railway:Tobu.Tojo', 'japanese': '東上線'},
    {'metro_id': 'odpt.Railway:Toei.Asakusa', 'japanese': '浅草線'},
    {'metro_id': 'odpt.Railway:Toei.Mita', 'japanese': '三田線'},
    {'metro_id': 'odpt.Railway:Toei.NipporiToneri', 'japanese': '日暮里・舎人ライナー'},
    {'metro_id': 'odpt.Railway:Toei.Oedo', 'japanese': '大江戸線'},
    {'metro_id': 'odpt.Railway:Toei.Shinjuku', 'japanese': '新宿線'},
    {'metro_id': 'odpt.Railway:Toei.TodenArakawa', 'japanese': '都電荒川線'},
    {'metro_id': 'odpt.Railway:Tokyu.DenEnToshi', 'japanese': '田園都市線'},
    {'metro_id': 'odpt.Railway:Tokyu.Meguro', 'japanese': '目黒線'},
    {'metro_id': 'odpt.Railway:Tokyu.Toyoko', 'japanese': '東横線'},
    {'metro_id': 'odpt.Railway:ToyoRapidRailway.ToyoRapidRailway', 'japanese': '東葉高速線'},
    {'metro_id': 'odpt.Railway:Yurikamome.Yurikamome', 'japanese': 'ゆりかもめ'},
]