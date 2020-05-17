import requests


def bot1(s):
        resp=requests.get("http://api.qingyunke.com/api.php",{
            'key':'free',
            'appid':0,
            'msg':s
        })
        resp.encoding='utf8'
        resp=resp.json()
        r=resp['content']
        print('bot1:'+r)
        bot2(r)
        return r

def bot2(s):
        resp = requests.post("http://www.tuling123.com/openapi/api", data={
            "key": "d59c41e816154441ace453269ea08dba",
            "info": s,
            "userid": "123456"
        })
        resp.encoding='utf8'
        resp=resp.json()
        r=resp['text']
        print('bot2:'+r)
        bot1(r)
        return r

s=input()
bot1(s)