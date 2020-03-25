# import something about auth
from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# test_user = 'jud'
app.config['SECRET_KEY'] = 'mickeymouse'
# exp_string = datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)
# test_token = jwt.encode({'user' : test_user, 'exp' :  10000000}, app.config['SECRET_KEY'])
# decoded_token = jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoianVkIiwiZXhwIjoxMDAwMDAwMH0.MRd2BuEjL4mUtwBzRymI_R3Tf67_1COhwbxAMFpysd4', app.config['SECRET_KEY'])
 
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






@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'You have reached an unprotected endpoint.'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'You have reached an PROTECTED endpoint with a valid token.'})

@app.route('/login')
def login():

    auth = request.authorization
    
    if auth and auth.password == 'password':

        exp_string = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

        token = jwt.encode({'user' : auth.username, 'exp' :  exp_string}, app.config['SECRET_KEY'])

        # return {'user' : auth.username, 'exp' :  exp_string}
        return jsonify({'token' : token.decode('UTF-8')})
        # return jsonify({'token' : test_token.decode('UTF-8')})
    
    return jsonify(auth)
    return ('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})



if __name__ == "__main__":
        app.run(debug=True)