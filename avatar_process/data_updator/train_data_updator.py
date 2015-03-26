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

import threading
import time

class TrainDataUpdator(threading.Thread):
    def __init__(self, lock):
        super(TrainDataUpdator, self).__init__()
        self.__lock = lock
        self.__updated_time = timezone.now()

    @property
    def updated_time(self):
        return self.__updated_time

    def run(self):
        from metro.train.metro_api.train_manager import TrainManager
        while True:
            with self.__lock:
                TrainManager.update()
                self.__updated_time = timezone.now()
            frequency = TrainManager.get_frequency()
            time.sleep(frequency)