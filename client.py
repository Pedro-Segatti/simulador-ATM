# -- coding: utf-8 --

import socket
import struct
import time

server_address = ('192.168.0.108', 12345)

# VPI, VCI e PT para a célula a ser enviada
vpi = 0 
vci = 1
pt = 1 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cell = (
    struct.pack('>H', vpi) +
    struct.pack('>H', vci) +
    struct.pack('B', pt & 0b111) + 
    b'Dados da célula ATM'
)

    client_socket.sendto(cell, server_address)
    time.sleep(0.10)