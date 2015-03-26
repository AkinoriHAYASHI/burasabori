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
from metro.station.metro_api.api_executor import StationApiExecutor
from metro.station.metro_api.station import Station

class StationManager(BaseModelManager):

    __metro_stations = {'AoyamaItchome':'青山一丁目','Akasaka':'赤坂','AkasakaMitsuke':'赤坂見附','AkabaneIwabuchi':'赤羽岩淵','Akihabara':'秋葉原','Asakusa':'浅草','AzabuJuban':'麻布十番','Ayase':'綾瀬','Awajicho':'淡路町','Iidabashi':'飯田橋','Ikebukuro':'池袋','Ichigaya':'市ケ谷','Inaricho':'稲荷町','Iriya':'入谷','Ueno':'上野','UenoHirokoji':'上野広小路','Urayasu':'浦安','Edogawabashi':'江戸川橋','Ebisu':'恵比寿','Oji':'王子','OjiKamiya':'王子神谷','Otemachi':'大手町','Ogikubo':'荻窪','Oshiage':'押上<スカイツリー前>','Ochiai':'落合','Ochanomizu':'御茶ノ水','OmoteSando':'表参道','Gaiemmae':'外苑前','Kagurazaka':'神楽坂','Kasai':'葛西','Kasumigaseki':'霞ケ関','Kanamecho':'要町','Kamiyacho':'神谷町','Kayabacho':'茅場町','Kanda':'神田','KitaAyase':'北綾瀬','KitaSando':'北参道','KitaSenju':'北千住','Kiba':'木場','Gyotoku':'行徳','Kyobashi':'京橋','KiyosumiShirakawa':'清澄白河','Ginza':'銀座','GinzaItchome':'銀座一丁目','Kinshicho':'錦糸町','Kudanshita':'九段下','Kojimachi':'麴町','Korakuen':'後楽園','Gokokuji':'護国寺','KotakeMukaihara':'小竹向原','KokkaiGijidomae':'国会議事堂前','Kodemmacho':'小伝馬町','Komagome':'駒込','Sakuradamon':'桜田門','Shibuya':'渋谷','Shimo':'志茂','Shirokanedai':'白金台','ShirokaneTakanawa':'白金高輪','ShinOtsuka':'新大塚','ShinOchanomizu':'新御茶ノ水','ShinKiba':'新木場','ShinKoenji':'新高円寺','Shinjuku':'新宿','ShinjukuGyoemmae':'新宿御苑前','ShinjukuSanchome':'新宿三丁目','Shintomicho':'新富町','ShinNakano':'新中野','Shimbashi':'新橋','Jimbocho':'神保町','Suitengumae':'水天宮前','Suehirocho':'末広町','Sumiyoshi':'住吉','Senkawa':'千川','Sendagi':'千駄木','Zoshigaya':'雑司が谷','Takadanobaba':'高田馬場','Takebashi':'竹橋','Tatsumi':'辰巳','TameikeSanno':'溜池山王','Tawaramachi':'田原町','ChikatetsuAkatsuka':'地下鉄赤塚','ChikatetsuNarimasu':'地下鉄成増','Tsukiji':'築地','Tsukishima':'月島','Tokyo':'東京','Todaimae':'東大前','Toyocho':'東陽町','Toyosu':'豊洲','Toranomon':'虎ノ門','NakaOkachimachi':'仲御徒町','Nagatacho':'永田町','Nakano':'中野','NakanoSakaue':'中野坂上','NakanoShimbashi':'中野新橋','NakanoFujimicho':'中野富士見町','NakaMeguro':'中目黒','NishiKasai':'西葛西','Nishigahara':'西ケ原','NishiShinjuku':'西新宿','NishiNippori':'西日暮里','NishiFunabashi':'西船橋','NishiWaseda':'西早稲田','Nijubashimae':'二重橋前','Nihombashi':'日本橋','Ningyocho':'人形町','Nezu':'根津','Nogizaka':'乃木坂','Hatchobori':'八丁堀','BarakiNakayama':'原木中山','Hanzomon':'半蔵門','HigashiIkebukuro':'東池袋','HigashiGinza':'東銀座','HigashiKoenji':'東高円寺','HigashiShinjuku':'東新宿','Hikawadai':'氷川台','Hibiya':'日比谷','HiroO':'広尾','Heiwadai':'平和台','Honancho':'方南町','HongoSanchome':'本郷三丁目','HonKomagome':'本駒込','Machiya':'町屋','Mitsukoshimae':'三越前','MinamiAsagaya':'南阿佐ケ谷','MinamiGyotoku':'南行徳','MinamiSunamachi':'南砂町','MinamiSenju':'南千住','Minowa':'三ノ輪','Myogadani':'茗荷谷','Myoden':'妙典','MeijiJingumae':'明治神宮前<原宿>','Meguro':'目黒','MonzenNakacho':'門前仲町','Yurakucho':'有楽町','Yushima':'湯島','Yotsuya':'四ツ谷','YotsuyaSanchome':'四谷三丁目','YoyogiUehara':'代々木上原','YoyogiKoen':'代々木公園','Roppongi':'六本木','RoppongiItchome':'六本木一丁目','Wakoshi':'和光市','Waseda':'早稲田'}
    __other_stations = {"odpt.Station:JR-East.Joban.Abiko":"我孫子","odpt.Station:JR-East.Joban.Toride":"取手","odpt.Station:JR-East.Joban.Kashiwa":"柏","odpt.Station:JR-East.Joban.Matsudo":"松戸","odpt.Station:JR-East.Chuo.Mitaka":"三鷹","odpt.Station:JR-East.ChuoChikatetsuTozai.Tsudanuma":"津田沼","odpt.Station:Toei.Mita.Onarimon":"御成門","odpt.Station:Toei.Mita.Takashimadaira":"高島平","odpt.Station:Toei.Mita.ShinTakashimadaira":"新高島平","odpt.Station:Toei.Mita.NishiTakashimadaira":"西高島平","odpt.Station:SaitamaRailway.SaitamaRailway.UrawaMisono":"浦和美園","odpt.Station:SaitamaRailway.SaitamaRailway.Hatogaya":"鳩ヶ谷","odpt.Station:ToyoRapidRailway.ToyoRapid.ToyoKatsutadai":"東葉勝田台","odpt.Station:ToyoRapidRailway.ToyoRapid.YachiyoMidorigaoka":"八千代緑が丘","odpt.Station:Odakyu.Tama.Karakida":"唐木田","odpt.Station:Odakyu.Odawara.HonAtsugi":"本厚木","odpt.Station:Odakyu.Odawara.HakoneYumoto":"箱根湯本","odpt.Station:Odakyu.Odawara.Ebina":"海老名","odpt.Station:Tobu.Nikko.MinamiKurihashi":"南栗橋","odpt.Station:Tobu.Isesaki.Kuki":"久喜","odpt.Station:Tobu.Isesaki.Takenotsuka":"竹ノ塚","odpt.Station:Tobu.Isesaki.KitaKasukabe":"北春日部","odpt.Station:Tobu.Isesaki.KitaKoshigaya":"北越谷","odpt.Station:Tobu.Isesaki.TobuDoubutuKouen":"東武動物公園","odpt.Station:Tobu.Tojo.Kawagoeshi":"川越市","odpt.Station:Tobu.Tojo.Asaka":"朝霞","odpt.Station:Tobu.Tojo.Asakadai":"朝霞台","odpt.Station:Tobu.Tojo.Shiki":"志木","odpt.Station:Tobu.Tojo.Yanasegawa":"柳瀬川","odpt.Station:Tobu.Tojo.Mizuhodai":"みずほ台","odpt.Station:Tobu.Tojo.Tsuruse":"鶴瀬","odpt.Station:Tobu.Tojo.Fujimino":"ふじみ野","odpt.Station:Tobu.Tojo.KamiFukuoka":"上福岡","odpt.Station:Tobu.Tojo.Shingashi":"新河岸","odpt.Station:Tobu.Tojo.Kawagoe":"川越","odpt.Station:Tobu.Tojo.Kasumigaseki":"霞ヶ関","odpt.Station:Tobu.Tojo.Tsurugashima":"鶴ヶ島","odpt.Station:Tobu.Tojo.Wakaba":"若葉","odpt.Station:Tobu.Tojo.Sakado":"坂戸","odpt.Station:Tobu.Tojo.KitaSakado":"北坂戸","odpt.Station:Tobu.Tojo.Takasaka":"高坂","odpt.Station:Tobu.Tojo.HigashiMatsuyama":"東松山","odpt.Station:Tobu.Tojo.ShinrinKoen":"森林公園","odpt.Station:Tokyu.DenEnToshi.ChuoRinkan":"中央林間","odpt.Station:Tokyu.DenEnToshi.FutakoTamagawa":"二子玉川","odpt.Station:Tokyu.DenEnToshi.Nagatsuta":"長津田","odpt.Station:Tokyu.DenEnToshi.Saginuma":"鷺沼","odpt.Station:Tokyu.Toyoko.MusashiKosugi":"武蔵小杉","odpt.Station:Tokyu.Toyoko.Yokohama":"横浜","odpt.Station:Tokyu.Toyoko.Kikuna":"菊名","odpt.Station:Tokyu.Toyoko.Motosumiyoshi":"元住吉","odpt.Station:Tokyu.Meguro.Hiyoshi":"日吉","odpt.Station:Tokyu.Meguro.Okusawa":"奥沢","odpt.Station:Tokyu.Meguro.Motosumiyoshi":"元住吉","odpt.Station:Tokyu.Meguro.MusashiKosugi":"武蔵小杉","odpt.Station:Minatomirai.Minatomirai.MotomachiChukagai":"元町・中華街","odpt.Station:Seibu.Ikebukuro.ShinSakuradai":"新桜台","odpt.Station:Seibu.Ikebukuro.Nerima":"練馬","odpt.Station:Seibu.Ikebukuro.Nakamurabashi":"中村橋","odpt.Station:Seibu.Ikebukuro.Fujimidai":"富士見台","odpt.Station:Seibu.Ikebukuro.NerimaTakanodai":"練馬高野台","odpt.Station:Seibu.Ikebukuro.ShakujiiKoen":"石神井公園","odpt.Station:Seibu.Ikebukuro.OizumiGakuen":"大泉学園","odpt.Station:Seibu.Ikebukuro.Hoya":"保谷","odpt.Station:Seibu.Ikebukuro.Hibarigaoka":"ひばりヶ丘","odpt.Station:Seibu.Ikebukuro.HigashiKurume":"東久留米","odpt.Station:Seibu.Ikebukuro.Kiyose":"清瀬","odpt.Station:Seibu.Ikebukuro.Akitsu":"秋津","odpt.Station:Seibu.Ikebukuro.Tokorozawa":"所沢","odpt.Station:Seibu.Ikebukuro.NishiTokorozawa":"西所沢","odpt.Station:Seibu.Ikebukuro.Kotesashi":"小手指","odpt.Station:Seibu.Ikebukuro.Sayamagaoka":"狭山ヶ丘","odpt.Station:Seibu.Ikebukuro.MusashiFujisawa":"武蔵藤沢","odpt.Station:Seibu.Ikebukuro.InariyamaKoen":"稲荷山公園","odpt.Station:Seibu.Ikebukuro.Irumashi":"入間市","odpt.Station:Seibu.Ikebukuro.Bushi":"仏子","odpt.Station:Seibu.Ikebukuro.Motokaji":"元加治","odpt.Station:Seibu.Ikebukuro.Hanno":"飯能"}

    _api_executor = StationApiExecutor()

    @classmethod
    def get_metro_englishes(cls):
        englishes = []
        for key in cls.__metro_stations.keys():
            englishes.append(key)
        return englishes

    @classmethod
    def get_other_station_ids(cls):
        ids =[]
        for key in cls.__other_stations.keys():
            ids.append(key)
        return ids

    @classmethod
    def get_japanese(cls, metro_id):
        for key in cls.__metro_stations.keys():
            if metro_id.split('.')[-1] == key:
                return cls.__metro_stations[key], True

        for key in cls.__other_stations:
            if metro_id == key:
                return cls.__other_stations[key], False

    @classmethod
    def is_metro(cls, metro_id):
        for key in cls.__metro_stations.keys():
            if metro_id.split('.')[-1] == key:
                return True

        for key in cls.__other_stations:
            if metro_id == key:
                return False

    @classmethod
    def get_station_detail_by_metro_id(cls, metro_id):
        for station in cls._api_json_data:
            if station['owl:sameAs'] == metro_id:
                return Station(station)
        for key in cls.__other_stations.keys():
            if key == metro_id:
                return Station({'owl:sameAs':key, 'dc:title': cls.__other_stations[key]})

    @classmethod
    def get_station_detail_by_railway_metro_id(cls, railway_metro_id, station_english):
        from metro.railway.metro_api.railway_manager import RailwayManager
        station_metro_id = 'odpt.Station:TokyoMetro.' + \
                           RailwayManager.get_english(railway_metro_id) + '.' + station_english
        for station in cls._api_json_data:
            if station['owl:sameAs'] == station_metro_id:
                return Station(station)
        raise Exception('station %s does not exists.' % (station_metro_id))

    @classmethod
    def get_station_details_by_english(cls, english):
        stations = []
        for station in cls._api_json_data:
            if station['owl:sameAs'].split('.')[-1] == english:
                stations.append(Station(station))
        return stations

    @classmethod
    def get_english_by_metro_id(cls, metro_id):
        return metro_id.split('.')[-1]