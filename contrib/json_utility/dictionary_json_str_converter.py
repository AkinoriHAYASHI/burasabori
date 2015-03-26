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

__author__ = 'Jynya Kaneko'

from urllib.parse import quote, unquote
import json

class DictionaryJsonStrConverter:
    @classmethod
    def get_quoted_json_str(cls, dictionary_data):
        json_str = json.dumps(dictionary_data, ensure_ascii=False).encode('utf-8')
        quoted_json_str = quote(json_str)
        return quoted_json_str

    @classmethod
    def get_dictionary(cls, quoted_json_str):
        unquoted_json_str = unquote(quoted_json_str)
        try:
            dictionary = json.loads(unquoted_json_str)
            return dictionary
        except TypeError:
            return None