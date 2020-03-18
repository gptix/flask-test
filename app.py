from flask import Flask, request
# import json


app = Flask(__name__)


@app.route('/recommend')
def return_recommendation():
    return request


@app.route('/')
def hello():
    return request # "Hello World!"


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
