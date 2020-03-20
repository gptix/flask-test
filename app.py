from flask import Flask, request, json

app = Flask(__name__)


def recommend_time(JSON_doc):
    """Return a JSON document holding a recommended tweet time
    based on contents of a JSON document."""
    dummy_return = json.jsonify(recommended_time="01:30")
    return dummy_return


@app.route('/recommend', methods=['POST'])
def return_recommendation():
    """Return a JSON document based on a JSON document that is
    the 'data' in a POST request."""
    JSON_in_POST_request = request.get_json(force=True)
    # return f'Return from route /recommender via POST'
    return recommend_time(JSON_in_POST_request)

# Below here are routes defined for testing only


@app.route('/')
def any():
    return 'Return from GET request (POST should not work)'


@app.route('/post_only', methods=['POST'])
def post_only():
    return f'Return from route /post_only'


@app.route('/get_only', methods=['GET'])
def get_only():
    return 'Return from route /get_only'


@app.route('/post_or_get', methods=['POST', 'GET'])
def post_or_get():
    return json.jsonify(method=request.method)

if __name__ == '__main__':
    app.run()
