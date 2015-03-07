import echo_server
import echo_client

def test_response_ok():
    t = ('text/plain', 'sample')
    response = '200 OK'
    content_type = 'text/plain'
    actual = echo_server.response_ok(t)
    assert response in actual
    assert content_type in actual

# def test_response_error():
#     error_code = '404'
#     reason = 'Not Found'
#     actual = echo_server.response_error(error_code, reason)
#     assert error_code in actual
#     assert reason in actual

# def test_parse_request():
#     request = "GET /index.html HTTP/1.1 \
#                 Host: www.example.com \
#                 <CRLF>"
#     uri = echo_server.parse_request(request)
#     assert uri == "/index.html"

def test_server():
    request = "GET / HTTP/1.1\r\n \
                Host: www.example.com \
                <CRLF>"
    actual = echo_client.client(request)
    assert '200' in actual
    assert 'OK' in actual

# def test_error_server():
#     request = "POST /index.html HTTP/1.1 \
#                 Host: www.example.com \
#                 <CRLF>"
#     actual = echo_client.client(request)
#     assert '405' in actual
#     assert 'Method Not Allowed' in actual

def test_resolve_uri_file():
    uri = "/sample.txt"
    result = echo_server.resolve_uri(uri)
    assert 'text/plain' in result
    assert 'This is a very simple text file.' in result[1]

def test_resolve_uri_dir():
    result = echo_server.resolve_uri('/')
    assert 'text/html' in result
