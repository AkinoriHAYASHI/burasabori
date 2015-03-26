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

from multiprocessing import Process
import time

class PeriodicApiExecutor(Process):
    def __init__(self, api_executor, interval, shared_json_data, lock):
        super(PeriodicApiExecutor, self).__init__(name = self.__class__.__name__)
        self.__api_executor = api_executor
        self.__json_data = shared_json_data
        self.__interval = interval
        self.__lock = lock

    @property
    def _api_executor(self):
        return self.__api_executor

    @property
    def _json_data(self):
        return self.__json_data

    @_json_data.setter
    def _json_data(self, json_data):
        with self._lock:
            while len(self.__json_data) > 0:
                self.__json_data.pop()
            for element in json_data:
                self.__json_data.append(element)

    @property
    def _interval(self):
        return self.__interval

    @_interval.setter
    def _interval(self, value):
        self.__interval = value

    @property
    def _lock(self):
        return self.__lock

    def _update(self):
        self._json_data = self._api_executor.get_data()

    def _continuous_update(self):
        self._update()
        while(True):
            time.sleep(self._interval)
            self._update()
            print('updated... (%s)' % (self.pid))


    def run(self):
        self._continuous_update()