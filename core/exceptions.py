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

class ApiExecutionFailureException(Exception):
    def __init__(self, value):
        self.value = 'Api %s fails to execute.' % (value)
    def __str__(self):
        return repr(self.value)

class AvatarDoesNotWaitForAnyTrain(Exception):
    def __init__(self, value):
        self.value = 'Avatar %s does not wait for any train.' % (value)
    def __str__(self):
        return repr(self.value)

class UserHasMaximumNumberOfAvatars(Exception):
    def __init__(self, value):
        self.value = 'User %s has maximum number of avatars.' % (value)
    def __str__(self):
        return repr(self.value)

class StationDoesNotExist(Exception):
    def __str__(self):
        return repr('The specified station does not exist.')

class InvalidIpAddress(Exception):
    def __str__(self):
        return repr('GIven IP address is invalid.')
    
class PostDataCreatorPageNotFound(Exception):
    def __str__(self):
        return repr('PostData Page not found.')