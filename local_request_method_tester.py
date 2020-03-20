# Test a combination of routes that specify different sets of methods,
# Using POST and GET request methods.
# Run in or passing to REPL

import requests
import json

URL_base = "http://localhost:5000/"

# Define routes to test
routes = ['recommend']
# routes = ['', 'post_only', 'get_only', 'post_or_get', 'recommend']

URLs = [URL_base + r for r in routes]

# Dummy data to pass via request
data = {}

for u in URLs:
    response_test = requests.post(url=u, data=data).text
    print(f"The response is: {response_test}")
    response_test = requests.get(url=u, data=data).text
    print(f"The response is: {response_test}")

print("Done")

# Log on local server - as expected
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "POST / HTTP/1.1" 405 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "POST /post_only HTTP/1.1" 200 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "GET /post_only HTTP/1.1" 405 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "POST /get_only HTTP/1.1" 405 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "GET /get_only HTTP/1.1" 200 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "POST /post_or_get HTTP/1.1" 200 -
# 127.0.0.1 - - [19/Mar/2020 19:36:56] "GET /post_or_get HTTP/1.1" 200 -


# Test '/recommender' route
u = 'http://localhost:5000/recommend'
data = json.dumps({'name': 'test', 'description': 'some test repo'}) # data gets ingnored anyway
response_test = requests.post(url=u, data=data).text
print(response_test)

# As expected
# {"recommended_time":"01:30"}
