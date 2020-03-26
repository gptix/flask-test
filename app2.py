from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mickeymouse'
test_token = '' # this will be used to hold test token during testing


# A decorator used to abstract 'requirement to have a token for authorization to 
# proceed'. To be used to modify route definitions.
# Takes, as a value via parameter, to 
def token_required(func_to_wrap):
    @wraps(func_to_wrap)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return jsonify({'message' : 'Token is missing.'}), 403

        # try:
        #     data = jwt.decode(token, app.config['SECRET_KEY'])
        # except:
        #     return jsonify({'message' : 'Token is invalid.'}), 403
        
        return func_to_wrap(*args, **kwargs)

    return decorated





def recommend_time(JSON_doc):
    """Return a JSON document holding a recommended tweet time
    based on contents of a JSON document."""
    dummy_return = jsonify(recommended_time="01:30")
    return dummy_return


@app.route('/recommend', methods=['POST'])
def return_recommendation():
    """Return a JSON document based on a JSON document that is
    the 'data' in a POST request."""
    JSON_in_POST_request = request.get_json(force=True)

    answer = recommend_time(JSON_in_POST_request)

    post_request_back = make_request.put(data = answer)
    
    return 

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
