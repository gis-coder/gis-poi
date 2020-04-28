#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request, render_template, session
from datetime import timedelta
from flask_restful import Api
import config
import models
from postdb import postdb
from views.user import user_blue

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# 在不设置session的存活时间时，默认是一个月
# session.permanent = True
# 设置session的存活时间为7天
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
# app.config.from_object(config)
# postdb.init_app(app)
api = Api(app)

app.register_blueprint(user_blue)

# db = SQLAlchemy(app)
# engine = create_engine('postgresql://rex:123456@127.0.0.1:5432/gis_poi', echo=True)


# class Region(db.Model):
#     __tablename__ = 'tb_region1'
#     f_id = Column(Integer, primary_key=True)
#     f_name = Column(String)
#     f_geom = Column(Geometry('POLYGON', 4326))


# @app.route('/')
# def index():
#     regions = Region.query.filter(Region.f_level == 1).order_by('f_gid')
#     return render_template('index.html', regions=regions)

# @app.route('/')
# def hello_world():
#     session['username'] = 'rex'
#     # 在不设置session的存活时间时，默认是一个月
#     session.permanent = True
#     # return 'Hello World!'
#     return render_template('main.html')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)
