#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Float, create_engine
from geoalchemy2 import Geometry
from postdb import postdb


# 引入模型时注意循环引入
# 兴趣点模型
class Poi(postdb.Model):
    __tablename__ = 'tb_poi'
    f_gid = Column(Integer, primary_key=True)
    f_name = Column(String(100))
    f_pname = Column(String(50))
    f_cname = Column(String(50))
    f_dname = Column(String(50))
    f_dcode = Column(String(10))
    f_tel = Column(String(50))
    f_address = Column(String(200))
    f_area = Column(String(50))
    f_b = Column(String(50))
    f_s = Column(String(50))
    f_x = Column(Float(10, 6))
    f_y = Column(Float(10, 6))


# 行政区模型
class Region(postdb.Model):
    __tablename__ = 'tb_region'
    f_gid = Column(Integer, primary_key=True)
    f_name = Column(String(100))
    f_level = Column(Integer)
    f_code = Column(String(10))
    f_pcode = Column(String(10))
    f_east = Column(Float(10, 6))
    f_west = Column(Float(10, 6))
    f_north = Column(Float(10, 6))
    f_south = Column(Float(10, 6))
    f_geom = Column(Geometry('MULTIPOLYGON', 4326))
