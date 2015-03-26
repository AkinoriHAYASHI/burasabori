__author__ = 'Junya Kaneko'

from datetime import datetime, timedelta
import random
import math

from django.utils import timezone
import pytz

from extra_services.gurunavi.postdata_creator import GurunaviPostdataCreator
from extra_services.flickr.postdata_creator import FlickrPostdataCreator
from avatar_process.avatar.visits_count_table import VisitsCountTable
from avatar_process.avatar.time_table import TimeTable
from avatar_process.post.post import Post
from avatar_process.post.post_updator import PostUpdator


class Avatar:

    CONSIDER_NEXT_TRAIN = 0
    WAIT_FOR_NEXT_TRAIN = 1
    IS_IN_TRAIN = 2
    WAIT_SIGHTSEEING = 3
    DO_SIGHTSEEING = 4
    FINISH_SIGHTSEEING = 5
    IS_BACK_TO_STATION = 6
    IS_BACK_TO_HOME = 7

    LOOK_AROUND = 0
    BREAKFAST = 1
    LUNCH = 2
    TEA = 3
    DINNER = 4
    ALCOHOL = 5

    def __init__(self, id, state, updated_time, station_metro_id):
        from metro.station.metro_api.station_manager import StationManager

        self.__id = id
        self.__state = state
        self.__previous_state = None
        self.__updated_time = updated_time

        # Avatar's train trip state
        self.__visits_count_table = VisitsCountTable()
        self.__latest_station = StationManager.get_station_detail_by_metro_id(station_metro_id)
        self.__take_higher_indexed_direction = False
        self.__target_train = None
        self.__current_train = None
        self.__planed_riding_time = 15 * 60

        # Avatar's gourmet state
        self.__finish_breakfast = False
        self.__finish_lunch = False
        self.__finish_tea = False
        self.__finish_dinner = False
        self.__finish_alcohol= False

        # Sightseeing state and its outcome
        self.__current_sightseeing_state = None
        self.__current_sightseeing_memory = None

        # Extra services' PostDataCreators
        self.__gurunavi_postdata_creator = GurunaviPostdataCreator()
        self.__flickr_postdata_creator = FlickrPostdataCreator()

        # Post
        self.__post = Post()

    @property
    def _visits_count_table(self):
        return self.__visits_count_table

    @property
    def id(self):
        return self.__id

    @property
    def state(self):
        return self.__state

    @property
    def updated_time(self):
        return self.__updated_time

    @property
    def latest_station(self):
        return self.__latest_station

    @property
    def current_train(self):
        return self.__current_train

    @property
    def current_sightseeing_state(self):
        return self.__current_sightseeing_state

    @property
    def current_sightseeing_memory(self):
        return self.__current_sightseeing_memory

    def decide_next_railway(self):
        from metro.station.metro_api.station_manager import StationManager
        from metro.railway.metro_api.railway_manager import RailwayManager

        english = self.__latest_station.english
        stations = StationManager.get_station_details_by_english(english)

        railway_metro_ids = [station.railway.metro_id for station in stations]
        distributions = []
        for railway_metro_id in railway_metro_ids:
            distributions.append(
                self.__visits_count_table.get_cumulative_unvisits_distribution(english, [railway_metro_id]))
        print('distributions: %s' % (distributions))

        threshold = random.random()
        next_railway = None
        is_high_indexed = False

        for railway in distributions[random.randint(0, len(distributions) - 1)]:
            if railway[1][0] > threshold:
                next_railway = RailwayManager.get_railway_detail_by_metro_id(railway[0])
                break
            elif railway[1][1] > threshold:
                next_railway = RailwayManager.get_railway_detail_by_metro_id(railway[0])
                is_high_indexed = True
                break
        next_station = StationManager.get_station_detail_by_railway_metro_id(next_railway.metro_id, english)

        self.__latest_station = next_station
        self.__take_higher_indexed_direction = is_high_indexed
        self.__state = self.WAIT_FOR_NEXT_TRAIN
        self.__updated_time = timezone.now()

    def decide_next_train(self):
        from metro.train.metro_api.train_manager import TrainManager
        trains = TrainManager.get_incoming_trains_by_station_metro_ids([self.__latest_station.metro_id])

        for train in trains:
            if train.to_station == None:
                if train.from_station.metro_id == self.__latest_station.metro_id and \
                        train.direction.english != self.__latest_station.english:
                    self.__target_train = train
                    self.__planed_riding_time = random.gauss(15, math.sqrt(10)) * 60
                    self.__state = self.WAIT_FOR_NEXT_TRAIN
                    self.__updated_time = timezone.now()
                    break
            elif train.direction.english == self.__latest_station.english:
                pass
            elif train.from_station.index < train.to_station.index and self.__take_higher_indexed_direction:
                self.__target_train = train
                self.__planed_riding_time = random.gauss(15, math.sqrt(10)) * 60
                self.__state = self.WAIT_FOR_NEXT_TRAIN
                self.__updated_time = timezone.now()
                break
            elif train.from_station.index > train.to_station.index and not self.__take_higher_indexed_direction:
                self.__target_train = train
                self.__planed_riding_time = random.gauss(15, math.sqrt(10)) * 60
                self.__state = self.WAIT_FOR_NEXT_TRAIN
                self.__updated_time = timezone.now()
                break

    def wait_for_next_train(self):
        from metro.train.metro_api.train_manager import TrainManager
        train = TrainManager.get_target_train_by_metro_id(self.__target_train.metro_id)

        if train == None or timezone.now() - self.__updated_time > timedelta(seconds = 20 * 60):
            self.__target_train = None
            self.__state = self.CONSIDER_NEXT_TRAIN
            self.__updated_time = timezone.now()
        elif train.to_station == None or train.to_station.metro_id != self.__latest_station:
            self.__current_train = train
            self.__state = self.IS_IN_TRAIN
            self.__updated_time = timezone.now()


    def get_off_from_train(self):
        from metro.train.metro_api.train_manager import TrainManager
        elapsed = timezone.now() - self.__updated_time

        train = TrainManager.get_target_train_by_metro_id(self.__current_train.metro_id)

        if elapsed.total_seconds() > self.__planed_riding_time or train == None:
            if self.__current_train.to_station != None:
                self.__latest_station = self.__current_train.to_station
            else:
                self.__latest_station = self.__current_train.from_station
            self.__visits_count_table.increment(self.__latest_station.english)
            self.__current_train = None
            self.__target_train = None
            self.__state = self.WAIT_SIGHTSEEING
            self.__updated_time = timezone.now()
        else:
            self.__current_train = train

    def _look_around(self):
        self.__current_sightseeing_state = self.LOOK_AROUND
        try:
            self.__current_sightseeing_memory = \
                self.__flickr_postdata_creator.get_data(
                    self.__latest_station.japanese, self.__latest_station.latitude, self.__latest_station.longitude)
        except Exception as e:
            print(e,  '_look_around')

    def _have_meal(self):
        try:
            self.__current_sightseeing_memory = \
                self.__gurunavi_postdata_creator.get_data(self.__latest_station.japanese,
                                                          self.__latest_station.latitude,
                                                          self.__latest_station.longitude)
            if self.__current_sightseeing_memory == None:
                print('No grunavi data. %s' % (self.id))
            elif self.__current_sightseeing_state == self.BREAKFAST:
                self.__finish_breakfast = True
            elif self.__current_sightseeing_state == self.LUNCH:
                self.__finish_lunch = True
            elif self.__current_sightseeing_state == self.TEA:
                self.__finish_tea = True
            elif self.__current_sightseeing_state == self.DINNER:
                self.__finish_dinner = True
            elif self.current_sightseeing_state == self.ALCOHOL:
                self.__finish_alcohol = True
            else:
                self._look_around()
        except Exception as e:
            print(e, '_have_meal', self.id)
            self._look_around()

    def do_sightseeing(self):
        self.__current_sightseeing_memory = None

        if TimeTable.get_plan() == self.BREAKFAST and not self.__finish_breakfast:
            self.__current_sightseeing_state = self.BREAKFAST
        elif TimeTable.get_plan() == self.LUNCH and not self.__finish_lunch:
            self.__current_sightseeing_state = self.LUNCH
        elif TimeTable.get_plan() == self.TEA and not self.__finish_tea:
            self.__current_sightseeing_state = self.TEA
        elif TimeTable.get_plan() == self.DINNER and not self.__finish_dinner:
            self.__current_sightseeing_state = self.DINNER
        elif TimeTable.get_plan() == self.ALCOHOL and not self.__finish_alcohol:
            self.__current_sightseeing_state = self.ALCOHOL
        else:
            self.__current_sightseeing_state = self.LOOK_AROUND

        if self.__current_sightseeing_state == self.LOOK_AROUND:
            self._look_around()
        else:
            self._have_meal()

        time_taken = TimeTable.get_timedelta(self.__current_sightseeing_state)
        self.__sleeping_time = self.__updated_time + time_taken - timezone.now()
        self.__updated_time = timezone.now()
        self.__state = self.FINISH_SIGHTSEEING

    def go_back_to_station(self):
        if self.__sleeping_time + self.__updated_time < timezone.now():
            self.__state = self.IS_BACK_TO_STATION
            self.__updated_time = timezone.now()

    def go_back_to_home(self):
        self.__state = self.IS_BACK_TO_HOME

    def consider_next_train(self):
        self.__state = self.CONSIDER_NEXT_TRAIN
        self.__updated_time = timezone.now()

    def transit_state(self):
        if self.__state == self.CONSIDER_NEXT_TRAIN:
            self.decide_next_railway()
        elif self.__state == self.WAIT_FOR_NEXT_TRAIN:
            if self.__target_train == None:
                self.decide_next_train()
            else:
                self.wait_for_next_train()
        elif self.__state == self.IS_IN_TRAIN:
            self.get_off_from_train()
        elif self.__state == self.WAIT_SIGHTSEEING:
            self.do_sightseeing()
        elif self.__state == self.FINISH_SIGHTSEEING:
            self.go_back_to_station()
        elif self.__state == self.IS_BACK_TO_STATION:
            if timezone.now().astimezone(pytz.timezone('Asia/Tokyo')).hour > 22:
                self.go_back_to_home()
            else:
                self.consider_next_train()
        elif self.__state == self.IS_BACK_TO_HOME:
            pass

        if self.__previous_state != self.__state:
            post = PostUpdator.update(self, self.__post)
        else:
            post = None

        self.__previous_state = self.__state

        return post

    def __str__(self):
        from metro.train.metro_api.train_manager import TrainManager
        if self.__state == self.CONSIDER_NEXT_TRAIN:
            state = '電車決定中'
        elif self.__state == self.WAIT_FOR_NEXT_TRAIN:
            state = '列車待ち'
        elif self.__state == self.IS_IN_TRAIN:
            state = '乗車中'
        elif self.__state == self.WAIT_SIGHTSEEING:
            state = '観光前'
        elif self.__state == self.WAIT_SIGHTSEEING:
            state = '観光待ち'
        elif self.__state == self.DO_SIGHTSEEING:
            state = '観光中'
        elif self.__state == self.FINISH_SIGHTSEEING:
            state = '観光終了(駅戻り待ち)'
        elif self.__state == self.IS_BACK_TO_STATION:
            state = '駅に戻った'
        elif self.__state == self.IS_BACK_TO_HOME:
            state = '家に戻った'
        else:
            state = '未確定なアバター状態'

        str = 'id %s (状態: %s)\n' % (self.__id, state)
        if self.__take_higher_indexed_direction:
            direction = '上り'
        else:
            direction = '下り'
        str = str + '現在の駅: %s (%s)\n' % (self.__latest_station.metro_id, direction)
        incoming_train_str = ''
        for train in TrainManager.get_incoming_trains_by_station_metro_ids([self.__latest_station.metro_id]):
            incoming_train_str = incoming_train_str + train.detail_str
        str = str + '現在の駅に入ってくる電車:\n%s' % (incoming_train_str)

        if self.__target_train != None:
            if self.__take_higher_indexed_direction:
                direction = '上り'
            else:
                direction = '下り'
            str = str + '予定の列車: %s (%s)\n' % (self.__target_train.metro_id, direction)
            train = TrainManager.get_target_train_by_metro_id(self.__target_train.metro_id)
            if train != None:
                str = str + '予定の列車の追跡:\n%s\n' % (train.detail_str)
            else:
                str = str + '予定の列車の追跡:\n喪失\n'

        if self.__current_train != None:
            str = str + '乗車中の列車 %s (%s)\n' % (self.__current_train.metro_id, self.__current_train.direction.metro_id)
            str = str + '予定乗車時間 %s\n' % (self.__planed_riding_time)
            str = str + '乗車中の電車の追跡 %s\n' % (self.__current_train.detail_str)
        return str