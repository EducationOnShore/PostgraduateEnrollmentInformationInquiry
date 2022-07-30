#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: Lambert
@file: main_mysql.py
@time: 2022/7/30 13:28
"""

# 全部专业专硕
import os

from other.api import professional_degree_category, academic_master_category, academic_master_category_second


def all_professional_degree():
    """
    专业硕士全部内容写入数据库
    :return:
    """
    result = professional_degree_category()
    for index,yjxk in enumerate(result):
        commod ='python -m yzwspider  -ssdm 0 -yjxk '+yjxk['dm']+ " mysql -u root -p 123456 -db yzw -table t_specialty_"+str(index)
        os.system(commod)


def all_academic_master():
    """
    全部专业硕士信息
    :return:
    """
    amc = academic_master_category()
    for index,value in enumerate(amc):
        # print(value['dm'])
        amcs = academic_master_category_second(value['dm'])
        for index_1,value_1 in enumerate(amcs):
            commod = 'python -m yzwspider  -ssdm 0 -yjxk ' + value_1[
                'dm'] + " mysql -u root -p 123456 -db yzw -table t_academic_" + str(index)
            os.system(commod)
            pass
    pass

if __name__ == '__main__':
    all_academic_master()
    pass
