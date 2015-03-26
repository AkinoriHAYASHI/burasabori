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

class Post:
    _avatar_id = None
    _template_name = None
    _attributes = None
    _pub_time = None

    def set_values(self, avatar_id, template_name, attributes, pub_time):
        self._avatar_id = avatar_id
        self._template_name = template_name
        self._attributes = attributes
        self._pub_time = pub_time

    @property
    def avatar_id(self):
        return self._avatar_id

    @property
    def template_name(self):
        return self._template_name

    @property
    def attributes(self):
        return self._attributes

    @property
    def pub_time(self):
        return self._pub_time

    def clear(self):
        self._avatar_id = None
        self._template_name = None
        self._attributes = None