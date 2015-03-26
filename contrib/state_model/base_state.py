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

class BaseState:
    STATE_ATTRIBUTES = {'key1': None, 'key2': None}

    def __init__(self):
        for key in self.STATE_ATTRIBUTES.keys():
            setattr(self, key, self.STATE_ATTRIBUTES[key])

    def _transition_function(self):
        raise Exception('_transition_function should return the instance of the next state.')

    def transition(self):
        new_state = self._transition_function()
        return new_state

    def __str__(self):
        str = 'State: %s\n' % (self.__class__.__name__)
        attributes_str = ''
        for key in self.STATE_ATTRIBUTES:
            attributes_str = attributes_str + '%s: %s\n' % (key, getattr(self, key))

        return str + attributes_str