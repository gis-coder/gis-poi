#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

# 指定模板文件位置、静态文件位置
# user_blue = Blueprint('user', __name__, static_folder='static_user', template_folder='templates_user')
user_blue = Blueprint('user', __name__, template_folder='templates_user')
# 注册视图函数
from ..user import user
