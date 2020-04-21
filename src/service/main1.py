#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from geoalchemy2 import Geometry
import config

app = Flask(__name__)
# app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rex:123456@127.0.0.1:5432/gis_poi'
api = Api(app)

db = SQLAlchemy(app)

engine = create_engine('postgresql://rex:123456@127.0.0.1:5432/gis_poi', echo=True)


class Region(db.Model):
    __tablename__ = 'tb_region1'
    f_id = Column(Integer, primary_key=True)
    f_name = Column(String)
    f_geom = Column(Geometry('POLYGON'))


db.create_all()


@app.route('/')
def index():
    return 're'


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)
