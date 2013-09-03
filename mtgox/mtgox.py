#!/usr/bin/env python

from datetime import datetime
import json
import socket
import time

out = open('ticker.json', 'a', 0)

def on_ticker(data):
    data['timestamp'] = time.mktime(datetime.now().timetuple())
    out.write(json.dumps(data) + '\n')

def on_trade(data):
    print data

def on_depth(data):
    print data['depth']['price_int']

host = "websocket.mtgox.com"
host_ip = socket.gethostbyname(host)
port = 80
path = "/mtgox?Currency=USD"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host_ip, port))
msg = "GET {0} HTTP/1.1\nUpgrade: WebSocket\nConnection: Upgrade\nHost: localhost\nOrigin: http://localhost\nWebSocket-Protocol: sample\n\n".format(path)

sock.sendall(msg)
sock.recv(4096)

packet = []
depth = 0
while 1:
    char = sock.recv(1).decode('utf-8', 'ignore')

    packet.append(char)

    if char == '{':
        depth += 1
    elif char == '}':
        depth -= 1

    if depth == 0:
        if len(packet) > 2:
            data = json.loads("".join(packet))
            if data['channel_name'] == 'ticker.BTCUSD':
                on_ticker(data)

        packet = []
