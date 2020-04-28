#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request
from flask_restful import Api
from flask_cors import *
import configparser
from views.user import user_blue

app = Flask(__name__)
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
        cfg = configparser.ConfigParser()
        cfg.read('service.cfg')

        db_host = cfg.get('poi_service', 'S_Host')
        db_port = cfg.get('poi_service', 'S_Port')
        db_debug = cfg.get('poi_service', 'S_Debug')
        app.run(host=db_host, port=db_port, debug=db_debug)
    except Exception as e:
        print(e)
