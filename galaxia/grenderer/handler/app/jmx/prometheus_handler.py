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

import datetime
import os

from galaxia.common.prometheus import response_parser
from galaxia.gmiddleware.handler import client

query_url = "query"
dashboard_url = "dashboard"
headers = {
        "Accept": "application/json"
    }


def get_names_list(message):

    if not "names_list" in message.keys() or message['names_list'] is None:
        prom_request_url = client.concatenate_url(os.getenv
                                                  ("aggregator_endpoint"),
                                                  query_url)
        current_time = str(datetime.datetime.now().isoformat())+"Z"
        if "exclude" in message.keys() and message['exclude']:
            query = "jmx_scrape_error{"+message["search_type"]+"!~"+'"' +\
                message["search_string"]+'"'+"}"
        else:
            query = "jmx_scrape_error{"+message["search_type"]+"=~"+'"' +\
                message["search_string"]+'"'+"}"

        payload = {"query": query, "time": current_time}
        resp = client.http_request("GET", prom_request_url, headers, payload,
                                   None, None)
        instance_list, job_list = response_parser.get_jmx_names_list(resp.text)
        return instance_list, job_list
    else:
        return message['names_list'], ""
