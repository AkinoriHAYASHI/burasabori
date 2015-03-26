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

from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'burasabori.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^user_verification/', views.UserVerificationView.as_view(), name='user_verification'),
    url(r'^railway_select/', views.RailwaySelectView.as_view(), name = 'railway_select'),
    url(r'^station_select/', views.StationSelectView.as_view(), name = 'station_select'),
    url(r'^create_avatar/', views.CreateAvatarView.as_view(), name = 'create_avatar'),
    url(r'^posts/', views.PostsView.as_view(), name = 'posts'),
    url(r'^journey_report/', views.JourneyReportView.as_view(), name = 'journey_report'),
    url(r'^licence/', views.LicenceView.as_view(), name = 'licence'),
    url(r'^', views.StartJourneyView.as_view(), name = 'start_journey'),
)