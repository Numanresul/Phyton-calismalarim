# -*- coding: utf-8 -*-
import socket

target_host = "0.0.0.0"
target_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,))