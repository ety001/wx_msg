#!/usr/bin/python
import urllib, urllib2, json, os, time, sys

# You need to edit from here
tmpl_id = 'your template id'
appid = 'your app id'
secret = 'your app secret'
user_id = 'your user id'

tmpl_data = {
    'touser':user_id,
    'template_id':tmpl_id,
    'url': 'http://www.domyself.me',
    'topcolor': '#ff0000',
    'data': {
        'first': {
            'value': '',
            'color': '#173177'
        },
        'send': {
            'value': '',
            'color': '#173177'
        },
        'text': {
            'value': '',
            'color': '#173177'
        },
        'time': {
            'value': '',
            'color': '#173177'
        },
        'remark': {
            'value': '',
            'color': '#173177'
        }
    }
}
# You need to edit end this

access_url = 'https://api.weixin.qq.com/cgi-bin/token'
access_url += '?grant_type=client_credential&appid='
access_url += appid+'&secret='+secret

tmpl_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
tmpl_url += '?access_token='

realpath = os.path.split(os.path.realpath(__file__))[0]
cachepath = realpath + r'/cache.log'

def get_access_token():
    if os.path.exists(cachepath):
        f = open(cachepath, 'r')
        data = f.readline().split('|')
        f.close()
        if len(data) == 2:
            if (int(data[1]) + 7100) > int( time.time() ):
                access_token = data[0]
            else:
                access_token = ''
        else:
            access_token = ''
    else:
        access_token = ''

    if access_token == '':
        req = urllib2.Request(access_url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        decodejson = json.loads(res)
        access_token = decodejson['access_token']
        f = file(cachepath,"w+")
        cache_str = [access_token + r'|' + str( int( time.time() ) )]
        f.writelines(cache_str)
        f.close()
    return access_token

def get_tmpl_url():
    return tmpl_url + get_access_token();

def send(params):
    param_arr = params.split('|')
    for v in param_arr:
        v = v.split('::')   # using :: to avoid conflicting
        tmpl_data['data'][v[0]]['value'] = v[1]
    request = urllib2.Request(get_tmpl_url() , json.dumps(tmpl_data))
    response = urllib2.urlopen(request)
    res = response.read()
    print res
    if json.loads(res)['errcode'] == 40001:
        f = file(cachepath,"w+")
        f.writelines([''])
        f.close()
        send(sys.argv[1])

if len(sys.argv) == 3:
    user_id = sys.argv[2]
if len(sys.argv) == 2:
    send(sys.argv[1])