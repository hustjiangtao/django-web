# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


import os
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.httpserver

# from django.core.wsgi import get_wsgi_application
from okweb.wsgi import application
from okweb.settings import STATIC_ROOT


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "okweb.settings")
settings = {
    "static_path": STATIC_ROOT,
    # "debug": True,
    # "xsrf_cookies": False,
}


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def main():
    # wsgi_app = get_wsgi_application()
    wsgi_app = application
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    tornado_app = tornado.web.Application(
        [
            ('/hello-tornado', HelloHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ], **settings)

    http_server = tornado.httpserver.HTTPServer(tornado_app)
    http_server.listen(8881)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()