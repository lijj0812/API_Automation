#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 17:10
# @Author  : Gavin

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urls = "https://dev.recloud.com.cn:5202/token"
datas = {
    "grant_type": "xrm",
    "username": r"CRM\Administrator",
    "password": "siri7181"
}
header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 "
                  "Safari/537.36"}

re = requests.post(urls, datas, headers=header, verify=False)
# print(re.text.encode("GBK", "ignore").decode())
print(re.text)
