"""
In version 1,
I will show the basic usage of WSGI.
At its simplest WSGI is an interface between web servers and web applications

Reference: http://pythonpaste.org/do-it-yourself-framework.html
"""

from paste import httpserver
# WSGI have lots of implemented in python. Here we use paste for example.
# In Openstack the WSGI implemented is eventlet.wsgi.server


def app(environ, start_respones):
    status = '200 OK'
    header = [('content-type', 'text/html'),
              ('request-id', 'blablabla')]
    start_respones(status, header)
    return ['hello']


httpserver.serve(app, host='127.0.0.1', port='8888')

# $python version_1.py
# $ curl 127.0.0.1:8888
# you will see the response like below
# **********************************
#* Connected to localhost (127.0.0.1) port 8888 (#0)
#> GET / HTTP/1.1
#> User-Agent: curl/7.30.0
#> Host: localhost:8888
#> Accept: */*
#>
#< HTTP/1.0 200 OK
#< Server: PasteWSGIServer/0.5 Python/2.7.3
#< Date: Sat, 27 Apr 2013 07:39:47 GMT
#< content-type: text/html
#< request-id: blablabla
#< Connection: close
#<
# hello
