import os
from flask import Flask, jsonify, request
from flask_httpauth import HTTPDigestAuth
import random
from crypt import methods 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'welcome home '
auth = HTTPDigestAuth()

users = {
    'vcu': 'rams'
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None



@app.route('/pong', methods=['GET'])
@auth.login_required
def pongApp():
    pongApp =random.randint(0, 500)
    
    return jsonify(str(pongApp))


if __name__ == '__main__':
    app.run()