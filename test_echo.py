# -*- coding: utf-8 -*-
from echo_client import client

def test_message():
    message = u'This is the message to send to the server'
    cmessage = client(message)
    assert message == cmessage

def test_unicode_message():
    message = u'I like the café that is down the street'
    cmessage = client(message)
    assert message == cmessage
