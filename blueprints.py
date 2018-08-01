from flask import current_app, Blueprint, request, json
from .settings import TOKEN, APPID, APP_SECRET
import hashlib
import requests
import xmltodict
admin = Blueprint('admin', __name__, url_prefix=None)

@admin.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        signature = request.args.get('signature', None)
        timestamp = request.args.get('timestamp', None)
        nonce = request.args.get('nonce', None)
        echostr = request.args.get('echostr', None)
        if signature or timestamp or nonce:

            if check_signature(signature, timestamp, nonce):
                return echostr
        return 'hello'
    if request.method == 'POST':

        data = request.data.decode()
        to_user_name = xmltodict.parse(data)['xml']['ToUserName']
        from_user_name = xmltodict.parse(data)['xml']['FromUserName']
        create_time = xmltodict.parse(data)['xml']['CreateTime']
        msg_type = xmltodict.parse(data)['xml']['MsgType']
        content = xmltodict.parse(data)['xml']['Content']
        msg_id = xmltodict.parse(data)['xml']['MsgId']
        print(data)
        req = {
            'xml':{
            'ToUserName': from_user_name,
            'FromUserName': 'WahChiYu',
            'CreateTime': create_time,
            'MsgType': msg_type,
            'Content': 'bye'
            }
        }
        req_data = xmltodict.unparse(req)
        print(req_data)
        return req_data
    return 'helo'
        # print(data)

def check_signature(signature, timestamp, nonce):
    token = TOKEN
    if hashlib.sha1(''.join(sorted([token, timestamp, nonce])).encode()).hexdigest() == signature:
        return True
    return False

@admin.route('/get_access_token')
def get_access_token():
    '''获取access_token '''
    token_response = requests.request('GET','https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(APPID, APP_SECRET))
    access_token, expires_in = "", 0
    if token_response.status_code == 200:
        access_token = token_response.json()['access_token']
        expires_in = token_response.json()['expires_in']

    return json.dumps({'access_token': access_token, 'expires_in': expires_in})

def get_wechat_server_ip():
    '''获取微信服务器IP地址'''
    pass

def verify_messages():
    '''验证消息真实性'''
    pass

def receive_messages():
    '''接收普通消息'''

    pass

def receive_events_pass():
    '''接收事件推送'''
    pass

def receive_voice_verify():
    '''接收语音识别结果'''
    pass

def auto_reply():
    '''自动回复'''
    pass

def support_jsapi():
    '''判断当前客户端版本是否支持指定JS接口'''
    pass

def get_jsapi_ticket():
    '''获取jsapi_ticket'''
    pass

def get_img():
    '''拍照或从手机相册中选图接口'''
    pass

def preview_img():
    '''预览图片接口'''
    pass

def upload_img():
    '''上传图片接口'''
    pass

def download_img():
    '''下载图片接口'''
    pass

def start_record():
    '''开始录音接口'''
    pass

def stop_record():
    '''停止录音接口'''
    pass

def play_voice():
    '''播放语音接口'''
    pass

def stop_play():
    '''暂停播放接口'''
    pass

def end_play():
    '''停止播放接口'''
    pass

def upload_voice():
    ''''上传语音接口'''
    pass

def download_voice():
    '''下载语音接口'''
    pass

def verify_voice():
    '''识别音频并返回识别结果接口'''
    pass

def get_net_status():
    '''获取网络状态接口'''
    pass

def get_location():
    '''获取地理位置接口'''
    pass

def use_map():
    '''使用微信内置地图查看位置接口'''
    pass

def hide_right_corner():
    '''隐藏右上角菜单接口'''
    pass

def show_right_corner():
    '''显示右上角菜单接口'''
    pass

def close_current_webpage():
    '''关闭当前网页窗口接口'''
    pass

def batch_hide_buttons():
    '''批量隐藏功能按钮接口'''
    pass

def batch_show_buttons():
    '''批量显示功能按钮接口'''
    pass

def hide_all_buttons():
    '''隐藏所有非基础按钮接口'''
    pass

def show_all_buttons():
    '''显示所有功能按钮接口'''
    pass

def use_scan():
    '''调起微信扫一扫接口'''
    pass