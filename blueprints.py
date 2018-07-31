from flask import current_app, Blueprint, request
from .settings import TOKEN
import hashlib
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