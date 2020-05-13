#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid, re
from io import BytesIO
from views.user import user_blue
from flask import request, render_template, redirect, url_for, make_response, session
from models.user_model import User
from dbAlchemy import postdb
import captchaImg


# 用户登录
@user_blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('user_name')
        password = request.form.get('user_password')
        save_pass = request.form.get('save_password')
        if username is None or password is None:
            return render_template('login.html', login_error='用户名或密码为空')
        user = User.query.filter(User.f_name == username, User.f_pass == password).first()
        if user is None:
            return render_template('login.html', login_error='不存在当前用户')
        else:
            if save_pass is 'on':
                session['username'] = username
                session['password'] = password
            user = {
                'username': username
            }
            return render_template('main.html', user=user)


# 用户注册
@user_blue.route('/regist/', methods=["GET", "POST"])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        password = request.form.get('pass')
        repassword = request.form.get('repass')
        captcha = request.form.get('captcha')
        if username is None or re.search('^[a-zA-Z]([a-zA-Z0-9_]{5,20})$', username) is None:
            return render_template('regist.html', name_error='*用户名是由字母、数字和下划线组成，长度为6-21个字符且首字母只能是字母')
        user = User.query.filter(User.f_name == username).first()
        if user is not None:
            return render_template('regist.html', name_error='*当前用户已经被注册了')
        if password is None or re.search('^[a-zA-Z0-9_]{6,12}$', password) is None:
            return render_template('regist.html', username=username, pass_error='用户密码必须是数字、字母和下划线组成的6-12位长度的字符')
        if repassword is None or password != repassword:
            return render_template('regist.html', username=username, password=password, repass_error='两次输入的密码不同')
        captcha_code = session['captcha_code']
        if captcha is None or captcha.lower() != captcha_code.lower():
            return render_template('regist.html', username=username, password=password, repassword=repassword,
                                   captcha_error='输入的验证码错误')
        user = User(f_id=uuid.uuid1(), f_name=username, f_pass=password)
        postdb.session.add(user)
        postdb.session.commit()
        return redirect(url_for('user.login'))


# 用户查询密码
@user_blue.route('/getpass/', methods=["GET", "POST"])
def getpass():
    if request.method == 'GET':
        return render_template('getpass.html')


# 生成验证码图片
@user_blue.route('/captcha/', methods=["GET"])
def captcha():
    image, code = captchaImg.generate_captcha()
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/png'
    session['captcha_code'] = code
    return response


@user_blue.route('/user_info/', methods=["GET"])
def user_info():
    if request.method == 'GET':
        a = session
        username = session['username']
        user = {
            'username': username
        }
        return render_template('user_info.html', user=user)
