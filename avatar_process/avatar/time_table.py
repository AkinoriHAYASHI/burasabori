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

from datetime import timedelta
import pytz

class TimeTable:
    @classmethod
    def get_timedelta(cls, plan):
        return timedelta(seconds = 5 * 60)

    @classmethod
    def get_plan(cls):
        from avatar_process.avatar.avatar import Avatar

        now = timezone.now().astimezone(pytz.timezone('Asia/Tokyo')).hour

        if now < 10:
            return Avatar.BREAKFAST
        elif now < 12:
            return Avatar.LOOK_AROUND
        elif now < 14:
            return Avatar.LUNCH
        elif now < 15:
            return Avatar.LOOK_AROUND
        elif now < 17:
            return Avatar.TEA
        elif now < 18:
            return Avatar.LOOK_AROUND
        elif now < 20:
            return Avatar.DINNER
        elif now < 21:
            return Avatar.LOOK_AROUND
        elif now < 23:
            return Avatar.ALCOHOL
        else:
            return Avatar.LOOK_AROUND