#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : test_login.py
# @Author  : mykaneki

import allure
import pytest
from VAR.BOOK_VAR import *

from logic.login import LoginPage


@allure.epic("会员中心（Memebers）")
@allure.feature("登陆(Login)")
@allure.story("典型场景")
@allure.testcase(__file__)
@allure.issue("issue_link")
def test_01(browser):
    """

    :param browser:
    :return:
    """
    url = BASE_URL + LOGIN_API
    username = USERNAME
    passwd = PASSWD
    login = LoginPage(browser)
    login.login(url, username, passwd)
