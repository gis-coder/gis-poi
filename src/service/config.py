#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

DIALECT = 'postgresql'
DRIVER = 'psycopg2'
HOSTNAME = '127.0.0.1'
PORT = '5432'
DATABASE = 'gis_poi'
USERNAME = 'rex'
PASSWORD = '123456'
# MySql连接字符串
# DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf-8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
DB_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# DB_URI = 'postgresql://rex:123456@127.0.0.1/gis_poi'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
