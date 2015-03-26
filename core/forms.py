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

from django import forms
from core import models

from metro.railway.metro_api.railway_manager import RailwayManager

class RailwaySelectForm(forms.Form):
    railway = forms.ModelChoiceField(label = '路線選択',
                                     queryset = models.Railway.objects.filter(metro_id__contains = 'TokyoMetro'),
                                     empty_label = '-- はじめる路線を選択するケロ ^ ^ --')

class StationSelectForm(forms.Form):
    def __init__(self, railway, *args, **kwargs):
        super(StationSelectForm, self).__init__(*args, **kwargs)
        self.fields['station'] = \
          forms.ModelChoiceField(label = '駅選択',
              queryset = models.Station.objects.filter(railway = railway),
              empty_label = '-- はじめる駅を選択するケロ ^ ^ --')

class StationForm(forms.Form):
    station = forms.ModelChoiceField(queryset = models.Station.objects.all())

class IpAddressForm(forms.Form):
    ip_address = forms.GenericIPAddressField()

class AvatarForm(forms.Form):
    avatar = forms.ModelChoiceField(label = 'アバター選択',
                                    queryset = models.Avatar.objects.all(),
                                    empty_label = '-- アバター選択 --')

class UserVerificationFrom(forms.Form):
    avatar = forms.ModelChoiceField(label = 'アバター選択',
                                    queryset = models.Avatar.objects.all(),
                                    empty_label = '-- アバター選択 --')

    key = forms.CharField(label = 'キー', max_length = 32)