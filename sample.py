#-*- coding: utf-8 -*-
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#def jsonformat (r):
 #   q = json.dumps (r, indent = 4)
  #  return q.encode ('utf-8').decode ('unicode_escape')

def hitokoto (c, encode, charset, callback):
    payload = {
        'c': c,
        'encode': encode,
        'charset': charset,
        'callback':callback
    }
    r = requests.get ('https://v1.hitokoto.cn/', params = payload)
    #print(jsonformat(r.json()))
    return r.json ()

def test_1 ():
    c = ''
    encode = ''
    charset = ''
    callback = ''
    result = hitokoto (c, encode, charset, callback)
    return result['hitokoto']

def test_2 ():
    c = ''
    encode = ''
    charset = ''
    callback = ''
    result = hitokoto (c, encode, charset, callback)
    if result['type'] == 'a':
        result['type'] = '动画'
    if result['type'] == 'b':
        result['type'] = '漫画'
    if result['type'] == 'c':
        result['type'] = '游戏'
    if result['type'] == 'd':
        result['type'] = '小说'
    if result['type'] == 'e':
        result['type'] = '原创'
    if result['type'] == 'f':
        result['type'] = '网络'
    if result['type'] == 'g':
        result['type'] = '其他'
    return result['type']

def test_3 ():
c = ''
encode = ''
charset = ''
callback = ''
result = hitokoto (c, encode, charset, callback)
return result['from']

def test_4 ():
c = ''
encode = ''
charset = ''
callback = ''
result = hitokoto (c, encode, charset, callback)
return result['creator']

str1 = test_1 ()
str2 = '类型:' + test_2 ()
str3 = '出自:' + test_3 ()
str4 = '创建者:' + test_4 ()
str = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4

def onQQMessage (bot, contact, member, content):
if content == '一言':
    bot.SendTo (contact, str)
elif content == '-stop':
    bot.SendTo (contact, 'QQ机器人已关闭')
    bot.Stop ()
