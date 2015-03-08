from gevent.server import StreamServer
from gevent.monkey import patch_all
from echo_server import response_ok, parse_request, resolve_uri

def handle(conn, addr):
    bsize = 32
    try:
        while True:
            message = ''
            done = False
            while not done:
                piece = conn.recv(bsize)
                message = '{}{}'.format(message, piece)
                if len(piece) < bsize:
                    done = True
            first_line = message.splitlines()[0]
            first_line = first_line.split(' ')
            uri = first_line[1]
            if str(uri) == str(parse_request(message)):
                t = resolve_uri(uri)
                response = "{}{}".format(response_ok(t), parse_request(message))
            else:
                response = parse_request(message)
            conn.sendall(response)
            conn.close()
    except KeyboardInterrupt:
        print '{}: {}'.format('Message received', message)
        conn.close()

def start():
    patch_all()
    server = StreamServer(('127.0.0.1', 50000), handle)
    print('Starting server on port 50000')
    server.serve_forever()

if __name__ == '__main__':
    start()
