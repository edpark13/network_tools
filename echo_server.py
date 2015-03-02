# -*- coding: utf-8 -*-
import socket

def server():
    server_socket = socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    server_socket.bind(('127.0.0.1', 50000))
    server_socket.listen(1)
    bsize = 32
    try:
        while True:
            message = ''
            done = False
            conn, addr = server_socket.accept()
            while not done:
                piece = conn.recv(bsize)
                message = '{}{}'.format(message, piece)
                if len(piece) < bsize:
                    done = True
                    conn.sendall(message)
                    conn.shutdown(socket.SHUT_WR)
                    conn.close()
    except KeyboardInterrupt:
        print '{}: {}'.format('Message received', message)
        server_socket.close()
        
if __name__ == '__main__':
    server()
