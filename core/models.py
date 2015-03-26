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

from django.db import models
from jsonfield import JSONField

# Create your models here.
class Railway(models.Model):
    metro_id = models.CharField('固有識別子', max_length = 90, db_index = True)
    code = models.CharField('路線コード', max_length = 5)
    japanese = models.CharField('日本語名', max_length = 90)

    pub_date = models.DateTimeField('情報登録日')

    def __str__(self):
        return self.japanese

    class Meta:
        ordering = ['metro_id']

        verbose_name = '路線'
        verbose_name_plural = '路線リスト'

class Station(models.Model):
    metro_id = models.CharField('固有識別子', max_length = 90, db_index = True)
    code = models.CharField('駅コード', max_length = 10)
    japanese = models.CharField('日本語名', max_length = 90)

    railway = models.ForeignKey(Railway, related_name='railway', db_index = True, null = True)
    index = models.IntegerField('駅順')

    connections = models.ManyToManyField(Railway, related_name = '乗り換え可能路線')

    pub_date = models.DateTimeField('情報発行日')

    def __str__(self):
        return self.japanese

    @property
    def english_name(self):
        return self.metro_id.split('.')[-1]

    class Meta:
        ordering = ['railway', 'index']

        verbose_name = '駅'
        verbose_name_plural = '駅リスト'

class Avatar(models.Model):
    ip_address = models.GenericIPAddressField('生成したIPアドレス')
    key = models.CharField('オーナー判別用キー', max_length = 90)
    created_time = models.DateTimeField('作成日時')

    start_station = models.ForeignKey(Station)

    def __str__(self):
        return '%s - %s' % (self.ip_address, self.key)

    class Meta:
        verbose_name = 'アバター'
        verbose_name_plural = 'アバターリスト'

class Post(models.Model):
    avatar = models.ForeignKey(Avatar, db_index = True)

    template_name = models.CharField('投稿の表示用テンプレートのファイル名', max_length = 255)

    pub_time = models.DateTimeField('投稿日時')

    attributes = models.TextField('投稿に使用するデータ')

    def __str__(self):
        from urllib.parse import unquote
        return unquote(self.attributes)

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿リスト'
