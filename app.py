from flask import Flask, request
# import json


app = Flask(__name__)


@app.route('/recommend')
def return_recommendation():
    return f'Return from route /recommend:  "1 AM"'

@app.route('/best')
def return_best_time():
    return f'Return from route /best:  "JSON message"'


@app.route('/')
def hello():
    return  f'Hello World {request.form}!'


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
