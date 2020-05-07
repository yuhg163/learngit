from django.apps import AppConfig


class ApitestConfig(AppConfig):
     name = 'apitest'
     
# import requests
# results = requests.get('http://192.168.0.92:7090/actProcess/start?userId=7A738A45C60524D98685838D18AFD4B6&actKey=KET_41607E303E7448EAF6219A5580C794D7&busId=001',None).text
# print(results)