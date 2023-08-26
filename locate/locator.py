#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : locator.py
# @Author  : mykaneki


"""
读书屋登陆页
http://novel.hctestedu.com/user/login.html
page_login
"""
# 登陆页标题
page_login_title = ('xpath', "//*[@id='form1']/h3")
# 用户名
page_login_user = ('xpath', "//input[@placeholder='手机号码']")
# 密码
page_login_indexPwd = ('xpath', "//input[@placeholder='密码']")
# 登陆按钮
page_login_loginBtn = ('xpath', "//input[@name='btnLogin']")


