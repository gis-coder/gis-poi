#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dbAlchemy import postdb
from sqlalchemy import Column, String, Integer, Text, orm


class User(postdb.Model):
    __tablename__ = 'tb_user'
    f_id = Column(String(50), primary_key=True)
    f_name = Column(String(50), nullable=False)
    f_pass = Column(String(20), nullable=False)
