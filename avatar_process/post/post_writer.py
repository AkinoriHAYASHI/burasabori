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

from contrib.json_utility.dictionary_json_str_converter import DictionaryJsonStrConverter
import psycopg2

class PostWriter:
    __cnx = None
    __cursor = None

    __dbname = 'burasabori'
    __user = 'burasabori'
    __password = 'burasabori'

    def connect(self):
        self.__cnx = psycopg2.connect(dbname = self.__dbname, user = self.__user, password = self.__password)
        self.__cursor = self.__cnx.cursor()

    def write(self, avatar_id, template_name, pub_time, attributes):
        quoted_attributes_str = DictionaryJsonStrConverter.get_quoted_json_str(attributes)
        print('書き込まれるデータ: %s' % (quoted_attributes_str))
        query = ('insert into core_post(avatar_id, template_name, pub_time, attributes)'
                 "values(%s, '%s', '%s', '%s')")
        self.__cursor.execute(query % (avatar_id, template_name, pub_time, quoted_attributes_str))

    def close(self):
        self.__cnx.commit()
        self.__cursor.close()
        self.__cnx.close()