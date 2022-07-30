#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: Lambert
@file: mysql_table_merge.py
@time: 2022/7/30 16:59
"""
import pymysql

db = pymysql.connect(host='47.98.105.28',
                     user='root',
                     password='MOsXo6m%auCcfTTM',
                     database='yzw')

cursor = db.cursor()

cursor.execute("SELECT table_name from information_schema.columns where table_name like 't_specialty\_%' group by table_name;")
data = cursor.fetchall()

for i,v in enumerate(data):
    if (v[0]=="t_specialty_info"):
        continue
    sql = "insert into yzw.t_specialty_info select * from "+v[0]+";"
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    print(data)


if __name__ == '__main__':
    pass
