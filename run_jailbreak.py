# Seestar/ASIAIR jailbreak by @joshumax
# Licensed in the public domain

import socket
import os
import hashlib
import sys

JAILBREAK_FILE = 'jailbreak.tar.bz2'


def recv_all(sock):
    text = ''

    while True:
        chunk = sock.recv(1024)
        text += chunk.decode()

        if not chunk or chunk.decode().endswith('\n'):
            break

    return text


def begin_update(address, file):
    s = socket.socket()
    s_ota = socket.socket()

    file_contents = open(file,'rb').read()
    json_str = '{{"id":1,"method":"begin_recv","params":[{{"file_len":{file_len},"file_name":"air","run_update":true,"md5":"{md5}"}}]}}\r\n'
    fsize = os.path.getsize(file)
    fmd5 = hashlib.md5(file_contents).hexdigest()
    json_str = json_str.format(file_len = fsize, md5 = fmd5)

    # Connect to OTA file socket first
    s_ota.connect((address, 4361))

    # Then connect to OTA command socket
    s.connect((address, 4350))

    print('Got: ' + recv_all(s))

    print('Sending RPC: {rpc}'.format(rpc = json_str))
    s.sendall(json_str.encode())

    print('Got back: ' + recv_all(s))

    s_ota.sendall(file_contents)

    s_ota.close()
    s.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {name} [ASIAIR_IP]'.format(name = sys.argv[0]))
        sys.exit(1)

    begin_update(sys.argv[1], JAILBREAK_FILE)
