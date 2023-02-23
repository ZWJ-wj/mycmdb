# -*- coding:utf-8 -*-
from tornado.options import define, options
from tornado.ioloop import IOLoop
from urls import Applications
define("port", default=8888, type=int)
define("address", default="127.0.0.1", type=str)
if __name__ == '__main__':
    options.parse_command_line()
    app = Applications()
    app.listen(port=options.port, address=options.address)
    IOLoop.current().start()
