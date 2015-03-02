import pytest
import echo_server
import echo_client

# @pytest.yield_fixture(scope='session')
# def start_server():
#     import threading
#     target = echo_server.server()
#     server_thread = threading.Thread(target=target)
#     server_thread.daemon = True
#     server_thread.start()
#     yield

def test_response_ok():
    response = '200 OK'
    content_type = 'text/plain'
    actual = echo_server.response_ok()
    assert response in actual
    assert content_type in actual

def test_response_error():
    error_code = '404'
    reason = 'Not Found'
    actual = echo_server.response_error(error_code, reason)
    assert error_code in actual
    assert reason in actual

def test_parse_request():
    request = "GET /index.html HTTP/1.1 \
                Host: www.example.com \
                <CRLF>"
    uri = echo_server.parse_request(request)
    assert uri == "/index.html"

def test_server():
    request = "GET /index.html HTTP/1.1 \
                Host: www.example.com \
                <CRLF>"
    actual = echo_client.client(request)
    assert '/index.html' in actual
    assert '200' in actual
    assert 'OK' in actual

def test_error_server():
    request = "POST /index.html HTTP/1.1 \
                Host: www.example.com \
                <CRLF>"
    actual = echo_client.client(request)
    assert '405' in actual
    assert 'Method Not Allowed' in actual
