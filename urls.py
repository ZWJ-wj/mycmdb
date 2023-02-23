# -*- coding:utf-8 -*-
from tornado.web import Application
from views import *
from settings import setting
from tornado.routing import ReversibleRuleRouter
from tornado.web import url
class Applications(Application, ReversibleRuleRouter):
    def __init__(self):
        handlers = [
            url(r'/', DemoHandler, name="demo"),
        ]
        super(Applications, self).__init__(handlers=handlers, **setting)
