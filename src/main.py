#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request
from flask_restful import Api
from flask_cors import *
import configparser
from views.user import user_blue
from dbAlchemy import postdb
import config

app = Flask(__name__)
app.config.from_object(config)
# 需要在此处初始化数据库连接
postdb.init_app(app)
# 解决跨域问题
CORS(app, resource=r'/')
api = Api(app)
# 注册模块
app.register_blueprint(user_blue)
# 钩子函数
# @app.before_request
# def my_before_request():
#     pass
#
#
# @app.context_processor
# def my_context_processor():
#     pass

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        print(e)
