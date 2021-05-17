import requests
import socket
import os
_local_ip = None


def get_host_ip():
    global _local_ip
    s = None
    try:
        if not _local_ip:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            _local_ip = s.getsockname()[0]
        return _local_ip
    finally:
        if s:
            s.close()


get_host_ip()
server = input('server link:')
while True:
    msg = input('enter to send:')
    r = requests.post(os.path.join(server, 'chat'), {
                      'name': _local_ip, 'msg': msg})
