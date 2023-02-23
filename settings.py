# -*- coding:utf-8 -*-
import os
base_path = os.path.dirname(__file__)
setting = {
    "debug": True,
    "static_path": os.path.join(base_path, "static"),
    "template_path": os.path.join(base_path, "templates")
}
