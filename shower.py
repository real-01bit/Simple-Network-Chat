import json
import requests
import os
server = input('server link:')
data = []
while True:
    r = requests.get(os.path.join(server, 'get'))
    data1 = json.loads(r.text)
    if data1 != data:
        print('\a')
        os.system('cls')
        os.system('clear')
        data = data1
        for i in data:
            print('[%s][%s] : %s' % (i['time'], i['name'], i['msg']))
