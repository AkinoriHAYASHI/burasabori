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

from metro.base_model import BaseModel
from metro.base_model_manager import BaseModelManager

class PassengerSurvey(BaseModel):
    @property
    def metro_id(self):
        return self._json_data['owl:sameAs']

    @property
    def operator(self):
        return self._json_data['odpt:operator']

    @property
    def survey_year(self):
        return self._json_data['odpt:surveyYear']

    @property
    def passenger_journeys(self):
        return self._json_data['odpt:passengerJourneys']


class PassengerSurveyManager(BaseModelManager):
    def get_surveys_by_station_english(self, english):
        surveys = []
        for survey in self._json_data:
            if survey['owl:sameAs'].split('.')[-2] == english:
                surveys.append(PassengerSurvey(survey))
        return surveys