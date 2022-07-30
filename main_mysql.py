#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: Lambert
@file: main_mysql.py
@time: 2022/7/30 13:28
"""

# 全部专业专硕
import os

from other.api import professional_degree_category

result = professional_degree_category()
for index,yjxk in enumerate(result):
    commod ='python -m yzwspider  -ssdm 0 -yjxk '+yjxk['dm']+ " mysql -u root -p 123456 -db yzw -table t_specialty_"+str(index)
    os.system(commod)
if __name__ == '__main__':
    pass
