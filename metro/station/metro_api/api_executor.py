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

class StationApiExecutor(MetroApiExecutor):
    def __init__(self):
        parameters = {
            'rdf:type': 'odpt:Station',
            'acl:consumerKey': METRO_KEY,
            '@id': None,
            'owl:sameAs': None,
            'dc:title': None,
            'odpt:operator': None,
            'odpt:railway': None,
            'odpt:stationCode': None
        }
        super(StationApiExecutor, self).__init__(parameters)

class StationFacilityApiExecutor(MetroApiExecutor):
    def __init__(self):
        parameters = {
            'rdf:type': 'odpt:StationFacility',
            'acl:consumerKey': METRO_KEY,
            '@id': None,
            'owl:sameAs': None
        }
        super(StationFacilityApiExecutor, self).__init__(parameters)

class PassengerSurveyApiExecutor(MetroApiExecutor):
    def __init__(self):
        parameters = {
            'rdf:type': 'odpt:PassengerSurvey',
            'acl:consumerKey': METRO_KEY,
            '@id': None,
            'owl:sameAs': None,
            'odpt:operator': None,
            'odpt:surveyYear': None
        }
        super(PassengerSurveyApiExecutor, self).__init__(parameters)
