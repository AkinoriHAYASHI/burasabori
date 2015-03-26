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

from metro.api_executor import MetroApiExecutor, METRO_KEY

class TrainApiExecutor(MetroApiExecutor):
    def __init__(self):
        parameters = {
            'rdf:type': 'odpt:Train',
            'acl:consumerKey': METRO_KEY,
            '@id': None,
            'owl:sameAs': None,
            'odpt:trainNumber': None,
            'odpt:trainType': None,
            'odpt:railway': None,
            'odpt:trainOwner': None,
            'odpt:railDirection': None,
            'odpt:delay': None,
            'odpt:startingStation': None,
            'odpt:terminalStation': None,
            'odpt:fromStation': None,
            'odpt:toStation': None
        }
        super(TrainApiExecutor, self).__init__(parameters)