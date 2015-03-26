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

from metro.api_executor import MetroApiExecutor
from metro.api_executor import METRO_KEY

class RailwayApiExecutor(MetroApiExecutor):
    def __init__(self):
        parameters = {
            'rdf:type': 'odpt:Railway',
            'acl:consumerKey': METRO_KEY,
            '@id': None,
            'owl:sameAs': None,
            'dc:title': None,
            'odpt:operator': None,
            'odpt:lineCode': None
        }
        super(RailwayApiExecutor, self).__init__(parameters)