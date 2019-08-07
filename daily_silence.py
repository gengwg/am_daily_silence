#!/usr/bin/env python

"""
Silence all DB blocking alerts for site 8888 daily 3pm - 3:45pm PST.
"""
import requests
from datetime import datetime
import sys
import json

API_ENDPOINT = "http://example.com:9093/api/v2/silences"

today = datetime.utcnow().strftime('%Y-%m-%d')
data = '''{{
  "matchers": [
    {{
      "name": "alertname",
      "value": ".*DbBlock.*",
      "isRegex": true
    }},
    {{
      "name": "site",
      "value": "8888",
      "isRegex": false
    }}
  ],
  "createdBy": "Jack Ma",
  "startsAt": "{0}T22:00:13.455Z",
  "endsAt": "{0}T22:45:50.000Z",
  "comment": "Daily Silence for Defrag Job"
}}
'''.format(today)

#print json.dumps(data)
print data

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

r = requests.post(url = API_ENDPOINT, data = data, headers = headers)
print r.text
