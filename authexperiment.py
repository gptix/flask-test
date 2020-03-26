# import something about auth
from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# test_user = 'jud'
app.config['SECRET_KEY'] = 'mickeymouse'
test_token = ''
# exp_string = datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)
# test_token = jwt.encode({'user' : test_user, 'exp' :  10000000}, app.config['SECRET_KEY'])
# decoded_token = jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoianVkIiwiZXhwIjoxMDAwMDAwMH0.MRd2BuEjL4mUtwBzRymI_R3Tf67_1COhwbxAMFpysd4', app.config['SECRET_KEY'])
 
def token_required(func_to_wrap):
    @wraps(func_to_wrap)
    def decorated(*args, **kwargs):
        # token = request.args.get('Authorization')
        token = request.headers['Authorization']
        if not token:
            return jsonify({'message' : 'Token is missing.'}), 403

        elif token != 'access_token myToken':
            return jsonify({'message' : 'Token is invalid.'}), 403        
        #     data = jwt.decode(token, app.config['SECRET_KEY'])
        # except:
        #     return jsonify({'message' : 'Token is invalid.'}), 403
        
        return func_to_wrap(*args, **kwargs)

    return decorated




@app.route('/')
def index():
    return jsonify({'message' : 'Index page.'})

@app.route('/header_test', methods=['POST'])
def header_test():
    token_received = request.headers['Authorization']
    print(f'token received: {token_received}')
    return jsonify({'token received' : token_received})

@app.route('/unprotected', methods=['POST','GET'])
def unprotected():
    return jsonify({'message' : 'You have reached an unprotected endpoint.'})

@app.route('/protected', methods=['POST','GET'])
@token_required
def protected():
    token = request.headers['Authorization']
    return jsonify({'message' : f'PROTECTED endpoint, token received = "{token}".'})

# @app.route('/login')
# def login():

#     auth = request.authorization
    
#     if auth and auth.password == 'password':

#         exp_string = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

#         token = jwt.encode({'user' : auth.username, 'exp' :  exp_string}, app.config['SECRET_KEY'])
#         # test_token = token # obvs use for testing

#         return jsonify({'token' : token.decode('UTF-8')})

#     return ('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})



if __name__ == "__main__":
        app.run(debug=True)