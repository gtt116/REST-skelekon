"""
In version 2, I will show use `Webob` to wrap request and response, which lead
to better readable.

Compared with version_1.py, version 2 is decorated by webob.dec.wsgify, which
wrap `environ, start_response` into a solid object `webob.Request`. And we dont
need to invoke `start_response` before return the body of response. webob
Request will do the work for us.

So, with webob we can write app more gracefull.

Reference: http://docs.webob.org/en/latest/reference.html
"""

from paste import httpserver

# the new package we used.
import webob.dec
import webob


@webob.dec.wsgify
def app(req):
    """
    In these app, I will introduce a app which receive all request to /hello,
    and reject other requests.
    """
    if req.path_info == '/hello':
        body = 'hello world'
        status = '200 OK'
    else:
        body = 'go away'
        status = '404 Not Found'
    resp = webob.Response(body, status)
    return resp


httpserver.serve(app, host='127.0.0.1', port='8888')

# run the script like below
# $ python version_2.py
# $ curl localhost:8888/hello
# you will get response like 'hello'
# $ curl localhost:8888/other
# you will get `go away`.
