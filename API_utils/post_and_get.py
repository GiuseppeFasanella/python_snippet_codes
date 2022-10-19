#### NICE TRICK HERE:
"""
Immagina che hai le istruzioni fatte così: 
curl --location --request POST 'https://gate.eos.com/api/gdw/api?api_key=<you_api_key>' \
--header 'Content-Type: application/json' \
--data-raw '{
"type":"mt_stats",
"params": {
    "bm_type":"NDVI",
    "date_start":"2020-01-01",
    "date_end":"2020-09-20",
    "geometry":
        {
        "coordinates": [
                          [
                              [-86.86718,41.317464],
                              [-86.86718,41.331596],
                              [-86.862631,41.331596],
                              [-86.862631,41.317464],
                              [-86.86718,41.317464]
                            ]
                        ],
        "type":"Polygon"
        },
    "reference":"ref_20200924-00-00",
    "sensors":["sentinel2"],
    "limit":10
   
    }
} '

E MO? come lo trascrivo in Python???
--> Così: https://reqbin.com/req/python/c-xgafmluu/convert-curl-to-python-requests
--> ZAC e diventa Python-like
"""

#### POST request 
# importing the requests library
import requests
  
# defining the api-endpoint 
API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"
  
# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''
  
# data to be sent to api
data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':source_code,
        'api_paste_format':'python'}
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
  
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

#### GET request
# importing the requests library
import requests
  
# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
  
  
# extracting latitude, longitude and formatted address 
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
  
# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))
