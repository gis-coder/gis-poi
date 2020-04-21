#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request
from flask_restful import Api
from flask_cors import *
import configparser

app = Flask(__name__)
CORS(app, resource=r'/')
api = Api(app)

if __name__ == '__main__':
    try:
        cfg = configparser.ConfigParser()
        cfg.read('service.cfg')

        db_host = cfg.get('poi_service', 'S_Host')
        db_port = cfg.get('poi_service', 'S_Port')
        db_debug = cfg.get('poi_service', 'S_Debug')
        app.run(host=db_host, port=db_port, debug=db_debug)
        # app.run(debug=True)
    except Exception as e:
        print(e)
