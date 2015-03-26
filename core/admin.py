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

from django.contrib import admin

from core import models

# Register your models here.
class RailwayAdmin(admin.ModelAdmin):
    model = models.Railway

    list_display = ('japanese', 'metro_id')

class StationAdmin(admin.ModelAdmin):
    model = models.Station

    list_display = ('id', 'japanese', 'metro_id', 'railway')

class PostInline(admin.TabularInline):
    model = models.Post


class AvatarAdmin(admin.ModelAdmin):
    model = models.Avatar

    inlines = [PostInline, ]

    list_display = ('id', 'ip_address', 'key', 'start_station', 'created_time')

class PostAdmin(admin.ModelAdmin):
    model = models.Post

    list_display = ('decoded_attributes', 'pub_time', 'avatar_id')

    def avatar_id(self, instance):
        return instance.avatar.id
    avatar_id.short_description = 'アバターID'

    def decoded_attributes(self, instance):
        from urllib.parse import unquote
        return unquote(instance.attrubites)
    decoded_attributes.short_description = '投稿データ'

admin.site.register(models.Railway, RailwayAdmin)
admin.site.register(models.Station, StationAdmin)
admin.site.register(models.Avatar, AvatarAdmin)
admin.site.register(models.Post, PostAdmin)