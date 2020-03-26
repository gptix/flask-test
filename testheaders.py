import requests
import json

url = 'http://localhost:5000/header_test'
payload = {"message" : "POST request for test"}
headers = {'token' : '12345'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.text)

def test():
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.text)
    return r.text
