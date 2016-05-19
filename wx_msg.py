#!/usr/bin/python
import urllib, urllib2, json, os, time

tmpl_id = 'PT0X_93niu22Ti3CYqEL0bXPkflJ06zUK5Yt3_KCF_g'
appid = 'wx54602a12c477c961'
secret = 'dde1ceb8fb98cb3ec0a70e9f0849221b'
user_id = 'oUeGNtz41L35y49a_xqXGjWeBazU'

access_url = 'https://api.weixin.qq.com/cgi-bin/token'
access_url += '?grant_type=client_credential&appid='
access_url += appid+'&secret='+secret

tmpl_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send'
tmpl_url += '?access_token='

def get_access_token():
    realpath = os.path.split(os.path.realpath(__file__))[0]
    cachepath = realpath + r'/cache.log'

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

print get_access_token()
