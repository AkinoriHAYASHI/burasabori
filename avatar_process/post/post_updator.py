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

from avatar_process.post.template_manager import TemplateManager

class PostUpdator:
    @classmethod
    def get_template(cls, avatar):
        return TemplateManager.get_template(avatar)

    @classmethod
    def update(cls, avatar, post):
        template_name = cls.get_template(avatar)

        if template_name == None:
            return None

        if avatar.current_train != None:
            direction = avatar.current_train.direction.japanese
        else:
            direction = None

        attributes = {'station': avatar.latest_station.japanese,
                      'railway': avatar.latest_station.railway.japanese,
                      'direction': direction,
                      'memory': avatar.current_sightseeing_memory
        }

        post.set_values(avatar.id, template_name, attributes, avatar.updated_time)
        return post
