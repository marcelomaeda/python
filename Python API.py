#Python API

import requests
response = requests.get('https://google.com/')
print(response)

if response:
  print('Request is successful.')
else:
  print('Request returned an error.')

#Python API Pull Data
  
import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
data = response_API.text
#print(data)
parse_json = json.loads(data)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman:", active_case)