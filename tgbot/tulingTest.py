import requests

appkey ='8nrDneDzeK8GovFJ'
s = input()
resp = requests.post("http://www.tuling123.com/openapi/api", data={
    "app_id": "2138941863",
    "info": s,
    "userid": "Nyako"
})





# while 1:
#     s = input()
#     resp = requests.post("http://www.tuling123.com/openapi/api", data={
#         "key": "d59c41e816154441ace453269ea08dba",
#         "info": s,
#         "userid": "Nyako"
#     })
#     resp = resp.json()
#     print(resp['text'])