#!/usr/bin/env python
# -*- coding:utf-8 -*-


from views.user import user_blue
from flask import request, render_template


@user_blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('user_name')
        password = request.form.get('user_password')
        save_pass = request.form.get('save_password')

        print(username)
        print(password)
        print(save_pass)
        return render_template('main.html')


@user_blue.route('/getpass/', methods=["GET", "POST"])
def getpass():
    if request.method == 'GET':
        return render_template('getpass.html')


@user_blue.route('/regist/', methods=["GET", "POST"])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
