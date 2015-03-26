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



from datetime import datetime
import threading
import multiprocessing
import time

from django.utils import timezone
from django.db.models import Q
import pytz

from core import models
from avatar_process.avatar.avatar import Avatar
from avatar_process.post.post_writer import PostWriter

class Process:
    __database = 'burasabori'
    __user = 'burasabori'

    def __init__(self):
        self.__avatars = []

    def _load_avatars(self):
        now = timezone.now().astimezone(pytz.timezone('Asia/Tokyo'))
        today = datetime(now.year, now.month, now.day, 0, 0, 0).replace(tzinfo = pytz.timezone('Asia/Tokyo'))

        new_avatar_objs = models.Avatar.objects.exclude(Q(id__in = [avatar.id for avatar in self.__avatars]) | \
                                                        Q(created_time__lt = today))
        for avatar_obj in new_avatar_objs:
            self.__avatars.append(Avatar(avatar_obj.id,
                                         Avatar.CONSIDER_NEXT_TRAIN,
                                         avatar_obj.created_time,
                                         avatar_obj.start_station.metro_id))

    def _write_posts(self, posts):
        post_writer = PostWriter()
        post_writer.connect()
        for avatar_id, template_name, pub_time, attributes in posts:
            post_writer.write(avatar_id, template_name, pub_time, attributes)
        post_writer.close()

    def _conduct_sightseeing(self, avatars):
        for avatar in avatars:
            avatar.transit_state()

    def run(self):
        from metro.station.metro_api.station_manager import StationManager
        from metro.railway.metro_api.railway_manager import RailwayManager
        from avatar_process.data_updator.train_data_updator import TrainDataUpdator

        StationManager.update()
        RailwayManager.update()

        test()

        train_data_lock = threading.Lock()
        train_data_updator = TrainDataUpdator(train_data_lock)
        train_data_updator.start()

        train_data_updated_time = train_data_updator.updated_time

        while True:
            start_time = timezone.now()

            self._load_avatars()

            sightseeing_waiting_list = []
            posts = []

            for avatar in self.__avatars:
                print(avatar)

                post = None
                with train_data_lock:
                    if avatar.state != Avatar.WAIT_SIGHTSEEING and avatar.DO_SIGHTSEEING:
                        post = avatar.transit_state()

                    if post != None and avatar.state == Avatar.WAIT_SIGHTSEEING:
                        sightseeing_waiting_list.append(avatar)

                    if post != None:
                        print('ポストされる内容:')
                        print(post.avatar_id, post.template_name, post.pub_time)
                        print(post.attributes)

                        posts.append([post.avatar_id, post.template_name, post.pub_time, post.attributes])

                if len(sightseeing_waiting_list) >= 1000:
                    sightseeing_process = threading.Thread(target = self._conduct_sightseeing,
                                                           args = (sightseeing_waiting_list, ))
                    sightseeing_process.start()
                    sightseeing_waiting_list = []

                if len(posts) >= 1000:
                    writing_process = multiprocessing.Process(target = self._write_posts, args = (posts,))
                    writing_process.start()
                    writing_process.join()
                    posts = []

            if len(sightseeing_waiting_list) != 0:
                sightseeing_process = threading.Thread(target = self._conduct_sightseeing,
                                                       args = (sightseeing_waiting_list, ))
                sightseeing_process.start()

            if len(posts) != 0:
                self._write_posts(posts)

            end_time = timezone.now()

            if end_time.astimezone(pytz.timezone('Asia/Tokyo')).hour == 4:
                self.__avatars = []

            elapsed_time = end_time - start_time

            print('Number of avatars: %s' % len(self.__avatars))
            print('start_time: %s' % (start_time.astimezone(pytz.timezone('Asia/Tokyo'))))
            print('end_time: %s' % (end_time.astimezone(pytz.timezone('Asia/Tokyo'))))
            print('elapsed_time: %s' % (elapsed_time))

            while True:
                if train_data_updator.updated_time == train_data_updated_time:
                    time.sleep(10)
                else:
                    train_data_updated_time = train_data_updator.updated_time
                    break


def test():
    from metro.railway.metro_api.railway_manager import RailwayManager
    from hashlib import md5
    import random

    for railway_id in RailwayManager.get_metro_railway_ids():
        for station in RailwayManager.get_railway_detail_by_metro_id(railway_id).ordered_stations:
            models.Avatar(ip_address = '192.168.0.100',
                          key = md5(str(random.random()).encode()),
                          created_time = timezone.now(),
                          start_station = models.Station.objects.get(metro_id = station.metro_id)).save()