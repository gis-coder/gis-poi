#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import configparser
import psycopg2


def post_conn():
    cfg_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../..")), 'service.cfg')
    print(cfg_path)

    postgre_cfg = configparser.ConfigParser()
    postgre_cfg.read(cfg_path)

    db_name = postgre_cfg.get('PostgreSQL', 'DB_Name')
    db_user = postgre_cfg.get('PostgreSQL', 'DB_User')
    db_pass = postgre_cfg.get('PostgreSQL', 'DB_Pass')
    db_host = postgre_cfg.get('PostgreSQL', 'DB_Host')
    db_port = postgre_cfg.get('PostgreSQL', 'DB_Port')
    return psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)


def __select(sql, type):
    if sql is None or str.strip(sql) == '':
        raise Exception('查询语句为空')
    db_conn = post_conn()
    try:
        if db_conn is None:
            raise Exception('数据库连接失败')
        db_cursor = db_conn.cursor()
        db_cursor.excute(sql)
        if type == 0:
            row = db_cursor.fecthone()
            if row is None:
                raise Exception('查询结果为空')
            return row
        elif type == 1:
            rows = db_cursor.fecthall()
            if rows is None:
                raise Exception('查询结果为空')
            return rows
        else:
            raise Exception('')
    finally:
        db_conn.close()


def post_select(sql):
    row = __select(sql, 0)
    if row is None:
        raise Exception('查询结果为空')
    return row[0]


def post_select_all(sql):
    rows = __select(sql, 1)
    if rows is None:
        raise Exception('查询结果为空')
    return rows


if __name__ == '__main__':
    try:
        print('1')
    except Exception as e:
        print(e)
