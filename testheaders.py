import requests
import json

url = 'http://localhost:5000/unprotected'
url = 'https://gt-wordcount-pro.herokuapp.com/'


payload = {"message" : "POST request for test"}
headers = {'Authorization' : 'access_token myToken'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.text)

def test():
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.text)
    return r.text
