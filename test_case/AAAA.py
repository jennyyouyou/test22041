#@coding=utf-8
#@TIME:2023/5/24 7:06
#@author:SX
from flask import Flask
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
auth = HTTPBasicAuth()
users = [
   {'username': 'haha', 'password': '123456'},
   {'username': 'qianfeng', 'password': '123456'}
]
@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None
@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.run(port=8887, debug=True,host='0.0.0.0')