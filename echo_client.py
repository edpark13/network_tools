# -*- coding: utf-8 -*-
import socket
import sys

def client(message):
    message = message.encode('utf-8')
    client_socket = socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(message)
    client_socket.shutdown(socket.SHUT_WR)
    bsize = 32
    done = False
    message_received = ''
    while not done:
        piece = client_socket.recv(bsize)
        message_received = '{}{}'.format(message_received, piece)
        if len(piece) < bsize:
            done = True
            client_socket.close()
    # sys.stdout.write('{}'.format(message_received))
    return message_received.decode('utf-8') 

if __name__ == '__main__':
    message = sys.argv[1]
    client(message)
