import requests
print("你好，我是图灵机器人")
while 1:
    s = input()
    resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "d59c41e816154441ace453269ea08dba",
        "info": s,
        "userid": "Nyako"
    })
    resp = resp.json()
    print(resp['text'])