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

from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from django.utils import timezone

from core import forms, controllers, exceptions

from datetime import datetime, timedelta
import pytz

# Create your views here.
class StartJourneyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/html/start_journey.html', {})

class CreateAvatarView(View):
    def get_context_data(self, request):
        user = controllers.User(request)
        try:
            avatar_id, key = user.create_avatar()
            return {'state': 'success',
                    'avatar_id': avatar_id,
                    'key': key}
        except exceptions.UserHasMaximumNumberOfAvatars:
            return {'state': 'user_has_maximum_number_of_avatars'}
        except exceptions.InvalidIpAddress:
            return {'state': 'invalid_ipaddress'}
        except exceptions.StationDoesNotExist:
            return {'state': 'station_does_not_exist'}

    def set_cookie(self, response, context):
        if context['state'] == 'success':
            path = '/burasabori'
            year = timezone.now().astimezone(pytz.timezone('Asia/Tokyo')).year
            month = timezone.now().astimezone(pytz.timezone('Asia/Tokyo')).month
            day = timezone.now().astimezone(pytz.timezone('Asia/Tokyo')).day

            expires_datetime = datetime(year, month, day + 1, 4, 0, 0).replace(tzinfo = pytz.timezone('Asia/Tokyo')).\
                astimezone(timezone.utc)
            expires = expires_datetime.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
            response.set_cookie('avatar_id', value = context['avatar_id'], path = path, expires = expires)
            response.set_cookie('key', value = context['key'], path = path, expires = expires)
        return response

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        response = render(request, 'core/html/create_avatar.html', context)
        return self.set_cookie(response, context)

class RailwaySelectView(View):
    def get_context_data(self):
        railway_select_form = forms.RailwaySelectForm()
        context = {'railway_select_form': railway_select_form}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'core/html/railway_select.html', context)


class StationSelectView(View):
    def get_railway(self, request):
        railway_select_form = forms.RailwaySelectForm(request.GET)
        if railway_select_form.is_valid():
            return railway_select_form.cleaned_data['railway']
        else:
            raise Http404

    def get_context_data(self, request):
        railway = self.get_railway(request)
        station_select_form = forms.StationSelectForm(railway)
        context = {'station_select_form': station_select_form}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, 'core/html/station_select.html', context)

class JourneyReportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/html/journey_report.html', {})

class PostsView(View):
    def get_context_data(self, request):
        avatar_form = forms.AvatarForm(request.GET)
        if avatar_form.is_valid():
            avatar = avatar_form.cleaned_data['avatar']
            posts = controllers.PostsCreator.create_posts(avatar)
            context = {'posts': posts}
            return context
        else:
            raise Http404

    def get(self,request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, 'core/html/posts.html', context)

class UserVerificationView(View):
    def get_context_data(self, request):
        user_verification_form = forms.UserVerificationFrom(request.GET)
        if user_verification_form.is_valid():
            avatar = user_verification_form.cleaned_data['avatar']
            key = user_verification_form.cleaned_data['key']

            if avatar.key == key:
                context = {'avatar_id': avatar.id}
                return context
        context = {'avatar_id': None}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, 'core/html/user_verification.html', context)

class LicenceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/html/licence.html', {})


