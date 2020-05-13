#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# 服务器配置信息
HOSTNAME = '127.0.0.1'
PORT = '8888'
SERVER_NAME = '{}:{}'.format(HOSTNAME, PORT)
DEBUG = True
# 如果使用cookie必须设置SECRET_KEY
SECRET_KEY = os.urandom(24)

# 数据库配置信息
DB_DIALECT = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_HOSTNAME = '127.0.0.1'
DB_PORT = '5432'
DB_DATABASE = 'poi'
DB_USERNAME = 'rex'
DB_PASSWORD = '123456'
# 数据库连接字符串
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DB_DIALECT, DB_DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOSTNAME,
                                                          DB_PORT,
                                                          DB_DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
