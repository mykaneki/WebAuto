#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : login.py
# @Author  : mykaneki
import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from key_word.web_keys import WebKeys
from locate.locator import *


# 以页面或页面组件为单位，封装常用的行为操作代码和元素定位代码
class LoginPage(WebKeys):
    # 登陆操作
    @allure.step("登陆")
    def login(self, url, username, passwd):
        with allure.step("打开登陆页"):
            wk = WebKeys(self.driver)
            wk.open(url)
            wk.text_wait(page_login_title, "登陆读书屋")
        with allure.step(f"输入用户名{username}"):
            wk.locator_with_wait(page_login_user).send_keys(username)
        with allure.step(f"输入密码{passwd}"):
            wk.locator_with_wait(page_login_indexPwd).send_keys(passwd)
        with allure.step("点击登陆按钮"):
            wk.locator_with_wait(page_login_loginBtn).click()
        with allure.step(f"结果检查，用户名：{username}在首页正常出现"):
            result = WebDriverWait(wk.driver, 5).until(
                ec.text_to_be_present_in_element((By.LINK_TEXT, str(username)), str(username)))
            assert result is True
