import requests

endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint, params={"product_id" : 123})
print(get_response.headers)
#print(get_response.text) # print raw text response
print(get_response.status_code)
print(get_response.json())