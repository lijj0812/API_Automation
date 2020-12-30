#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 13:25
# @Author  : Gavin


import allure

from Params.params import Login
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert
import urllib3
import requests


class TestLogin:
    @allure.feature('serviceCould')
    @allure.severity('blocker')
    @allure.story('login')
    def test_login_01(self, action):
        """
            用例描述：用户登录
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        conf = Config()
        data = Login()
        test = Assert.Assertions()
#        request = Request.Request(action)

        host = conf.host_release
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        datas = params[0][0]
#        print("api_url==========", api_url)
#        print("params==========", params[0][0])
        r = requests.post(api_url, data=datas, verify=False)
        re_time = r.elapsed.total_seconds()
#        print("接口响应时间==========", r.elapsed.total_seconds())
        print("text==========", r.text)
        rep_code = r.status_code
        assert test.assert_code(rep_code, 200)
        assert test.assert_in_text(r.text, "access_token")
        Consts.STRESS_LIST.append(re_time)
        Consts.RESULT_LIST.append('True')
