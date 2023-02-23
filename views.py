# -*- coding:utf-8 -*-
import tornado.web
from tornado import gen
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
# create your views hear
class DemoHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(32)
    @gen.coroutine
    def get(self, *args, **kwargs):
        result = yield self.demo()
        self.write(result)
        self.finish()
    @run_on_executor
    def demo(self):
        return "hello world!"
