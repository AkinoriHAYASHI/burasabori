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

from django.http.request import QueryDict
from django.utils import timezone
from django.template.loader import get_template
from django.template import Context

from core import models, exceptions, forms

from urllib.parse import unquote
from random import random
from hashlib import md5
from datetime import datetime
import pytz
import json

class User:
    MAX_AVATAR_NUM = 3

    def __init__(self, request):
        self.__request = request
        self.__ip_address = self._get_ip_address(self._request)

    @property
    def _request(self):
        return self.__request

    @property
    def _ip_address(self):
        return self.__ip_address

    @property
    def _can_create_avatar(self):
        ip_address = self._ip_address
        max_avatar_num = self.MAX_AVATAR_NUM

        if ip_address == None:
            return False

        now = timezone.now().astimezone(pytz.timezone('Asia/Tokyo'))
        year = now.year
        month = now.month
        day = now.day
        start_today = datetime(year, month, day, 0, 0, 0)

        avatar_num = models.Avatar.objects.filter(ip_address = ip_address,
                                                  created_time__gt = start_today).count()
        if avatar_num >= max_avatar_num:
            return False
        else:
            return True

    def _get_ip_address(self, request):
        try:
            ip_address = request.META.get('REMOTE_ADDR')
        except KeyError:
            return None

        ip_address_form = forms.IpAddressForm(QueryDict('ip_address=%s' % (ip_address)))
        if ip_address_form.is_valid():
            return ip_address_form.cleaned_data['ip_address']
        else:
            return None

    def _generate_key(self):
        text = 'IP address is %s and seed = %s for burasabori.' % (self._ip_address, random())
        return md5(text.encode()).hexdigest()

    def create_avatar(self):
        ip_address = self._ip_address
        request = self._request

        if not self._can_create_avatar:
            raise exceptions.UserHasMaximumNumberOfAvatars(ip_address)

        if ip_address == None:
            raise exceptions.InvalidIpAddress()

        station_form = forms.StationForm(request.GET)
        if station_form.is_valid():
            station = station_form.cleaned_data['station']
            key = self._generate_key()

            avatar = models.Avatar(ip_address = ip_address, key = key,
                                   start_station = station, created_time = timezone.now())
            avatar.save()

            models.Post(avatar = avatar,
                        template_name = 'core/comments/starting_journey.html',
                        pub_time = timezone.now(),
                        attributes = json.dumps({})).save()

            return avatar.id, key
        else:
            raise exceptions.StationDoesNotExist()

class PostsCreator:
    @classmethod
    def create_comment(cls, template_name, attributes):
        context = {}

        if 'memory' in attributes.keys() and attributes['memory'] != None:
            for key in attributes['memory'].keys():
                attributes[key] = attributes['memory'][key]
            attributes.pop('memory')

        return get_template(template_name).render(Context(attributes))

    @classmethod
    def unquote_attributes(cls, attributes):
        return json.loads(unquote(attributes))

    @classmethod
    def create_comment_for(cls, post, posted_to):
        try:
            template_name = post.template_name
            attributes = {'posted_to': posted_to}
            posted_attributes = cls.unquote_attributes(post.attributes)
            attributes.update(posted_attributes)
            return cls.create_comment(template_name, attributes)
        except ValueError:
            return None

    @classmethod
    def create_comment_for_burasabori(cls, post):
        return cls.create_comment_for(post, 'burasabori')

    @classmethod
    def create_comment_for_twitter(cls, post):
        return cls.create_comment_for(post, 'twitter')

    @classmethod
    def create_posts(cls, avatar):
        posts = []
        for post in avatar.post_set.all():
            burasabori_comment = cls.create_comment_for_burasabori(post)
            twitter_comment = cls.create_comment_for_twitter(post)

            if burasabori_comment != None and twitter_comment != None:
                posts.append({
                    'avatar_id': avatar.id,
                    'post_id': post.id,
                    'pub_time': post.pub_time,
                    'burasabori_comment': burasabori_comment,
                    'twitter_comment': twitter_comment
                    })
        return posts
