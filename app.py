from flask import Flask, request
# import json


app = Flask(__name__)


#@app.route('/recommend', methods=['POST', 'GET'])
#def return_recommendation():
#    return request


@app.route('/')
def hello():
    return "Hello World!"


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
