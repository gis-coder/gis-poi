#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from postdb import postdb
from sqlalchemy import Column, String, Integer, Text, orm


# engine = create_engine('postgresql://rex:123456@127.0.0.1:5432/gis_poi', echo=True)
# class Region(db.Model):
#     __tablename__ = 'tb_region1'
#     f_id = Column(Integer, primary_key=True)
#     f_name = Column(String)
#     f_geom = Column(Geometry('POLYGON', 4326))

class User(postdb.Model):
    __tablename__ == 'user'
    f_id = Column(Integer, primary_key=True)
    f_name = Column(String)
