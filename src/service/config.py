#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

DEBUG = True
SECRET_KEY = os.urandom(24)

# DIALECT = 'postgresql'
# DRIVER = 'psycopg2'
# HOSTNAME = '127.0.0.1'
# PORT = '5432'
# DATABASE = 'gis_poi'
# USERNAME = 'rex'
# PASSWORD = '123456'
# MySql连接字符串
DB_URI = '{}+{}://{}:{}@{}:{}/{}'.format('postgresql', 'psycopg2', 'rex', '123456', '127.0.0.1', '5432', 'gis_poi')
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
