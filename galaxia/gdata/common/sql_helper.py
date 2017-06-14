# Copyright 2016 - Wipro Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Helper module to create engine, create connection
"""

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

engine = None


def init_db(db_type, username, password, host, db, db_location):
    """
    Creates database engine
    :param db_type: database type
    :param username: database username
    :param password: database password
    :param host: database host
    :param db: database name
    :return:
    """
    global engine
    url = None
    if db_type == 'mysql':
        url = URL(db_type, username, password, host, database=db)
    elif db_type == 'sqlite':
        url = "sqlite:///" + db_location
    engine = create_engine(url)
