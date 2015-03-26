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

class TemplateManager:
    @classmethod
    def get_template(cls, avatar):
        template_name = None

        if avatar.state == avatar.IS_IN_TRAIN:
            template_name = 'core/comments/riding_train.html'
        elif avatar.state == avatar.WAIT_SIGHTSEEING:
            template_name = 'core/comments/starting_sightseeing.html'
        elif avatar.state == avatar.DO_SIGHTSEEING:
            pass
        elif avatar.state == avatar.IS_BACK_TO_STATION:
            if avatar.current_sightseeing_memory == None:
                template_name = 'core/comments/nothing_found.html'
            elif avatar.current_sightseeing_state == avatar.LOOK_AROUND:
                template_name = 'core/comments/flickr0.html'
            elif avatar.current_sightseeing_state == avatar.BREAKFAST:
                template_name = 'core/comments/gurunavi_breakfast0.html'
            elif avatar.current_sightseeing_state == avatar.LUNCH:
                template_name = 'core/comments/gurunavi_lunch0.html'
            elif avatar.current_sightseeing_state == avatar.TEA:
                template_name = 'core/comments/gurunavi_tea0.html'
            elif avatar.current_sightseeing_state == avatar.DINNER:
                template_name = 'core/comments/gurunavi_dinner0.html'
            elif avatar.current_sightseeing_state == avatar.ALCOHOL:
               template_name = 'core/comments/gurunavi_alcohol0.html'
        elif avatar.state == avatar.IS_BACK_TO_HOME:
            template_name = 'core/comments/sleep.html'

        return template_name
