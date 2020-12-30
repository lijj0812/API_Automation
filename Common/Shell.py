#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time    : 2020/12/30 13:18
# @Author  : Gavin


"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o