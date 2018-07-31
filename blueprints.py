from flask import current_app, Blueprint, request, json
from .settings import TOKEN, APPID, APP_SECRET
import hashlib

import requests
admin = Blueprint('admin', __name__, url_prefix=None)

@admin.route('/')
def index():
    signature = request.args.get('signature', None)
    timestamp = request.args.get('timestamp', None)
    nonce = request.args.get('nonce', None)
    echostr = request.args.get('echostr', None)
    if check_signature(signature, timestamp, nonce):
        return echostr
    return 'hello'

def check_signature(signature, timestamp, nonce):
    token = TOKEN
    if hashlib.sha1(''.join(sorted([token, timestamp, nonce])).encode()).hexdigest() == signature:
        return True
    return False

@admin.route('/get_access_token')
def get_access_token():
    token_response = requests.request('GET','https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(APPID, APP_SECRET))
    access_token, expires_in = "", 0
    if token_response.status_code == 200:
        access_token = token_response.json()['access_token']
        expires_in = token_response.json()['expires_in']

    return json.dumps({'access_token': access_token, 'expires_in': expires_in})
