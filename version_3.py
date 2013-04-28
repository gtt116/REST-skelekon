"""
version 3, I will show a upgrade from version 2, which use `paste` to
dymaticlly load the app.

In version 1 and 2, we write app logic in only on file. Now I want to
put these app into config, and dymaticly load them if I need them.
"""
import os
PWD = os.path.dirname(__file__)

from paste import deploy

import webob.dec
import webob

from paste import deploy


config_name = PWD + 'version_3.ini'
app = deploy.appconfig('config:%s')
httpserver.serve(app, host='127.0.0.1', port='8888')
