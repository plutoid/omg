# coding:utf8
import os,bottle
from bottle import route, run, default_app, error, template, view, request, response
from bottle import install 
from bottle_sqlite import SQLitePlugin
from bottle import static_file


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./bootstrap')



@route('/')
def main():
    data = [1,2,3,4,5]
    return template('content',data=data)

@error(404)
def error404(error):
    return template('error')

class StripPathMiddleware(object):
  def __init__(self, app):
    self.app = app
  def __call__(self, e, h):
    e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
    return self.app(e,h)

if __name__ == "__main__":
    # Interactive mode
    run(app=myapp)
    
else:
    # Mod WSGI launch
    bottle.debug(True)
    os.chdir(os.path.dirname(__file__))
    application = StripPathMiddleware(default_app())

