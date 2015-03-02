# -*- coding: utf-8 -*-
import socket

def response_ok():
    return u"HTTP/1.1 200 OK\r\n \
    Content-Type: text/plain\r\n\r\n".encode('utf-8')

def response_error(error_code, reason):
    return u"HTTP/1.1 {} {}\r\n \
    Content-Type: text/plain\r\n\r\n".format(error_code, reason).encode('utf-8')

def parse_request(request):
    first_line = request.splitlines()[0]
    first_line = first_line.split(' ')
    method = first_line[0]
    uri = first_line[1]
    protocol = first_line[2]

    if method != 'GET':
        return response_error('405', 'Method Not Allowed')
    elif protocol != 'HTTP/1.1':
        return response_error('505', 'HTTP Version Not Supported')
    else:
        return uri

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
            first_line = message.splitlines()[0]
            first_line = first_line.split(' ')
            uri = first_line[1]
            if str(uri) == str(parse_request(message)):
                response = "{}{}".format(response_ok(), parse_request(message))
            else:
                response = parse_request(message)
            conn.sendall(response)
            conn.shutdown(socket.SHUT_WR)
            conn.close()

    except KeyboardInterrupt:
        print '{}: {}'.format('Message received', message)
        server_socket.close()

if __name__ == '__main__':
    server()
