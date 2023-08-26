#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : conftest.py
# @Author  : mykaneki

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# scope为session，整个项目只会启动一次浏览器，关闭一次浏览器

@pytest.fixture(autouse=True, scope='session')
def browser():
    # 初始化浏览器
    # 定义全局变量driver
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # 移动窗口
    driver.set_window_position(1900, -200)
    driver.set_window_size(1550, 1000)

    yield driver

    # 用例后置，关闭浏览器
    driver.quit()


# scope为function，每个用例都会启动和关闭浏览器


"""
    装饰器@pytest.hookimpl(hookwrapper=True)等价于 @pytest.mark.hookwrapper
    作用：
    a:可以获取测试用例的信息，比如用例函数的描述
    b.可以获取测试用例的执行结果，yield，返回一个result对象
"""


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 获取测试用例的执行结果，yield，返回一个result对象
    out = yield
    """
        从result对象out获取调用结果的测试报告，返回一个report对象, 
        report对象的属性
        包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、
        outcome(用例的执行结果，passed,failed)
    """
    report = out.get_result()

    # 仅仅获取用例call阶段的执行结果，不包含 setup/teardown
    if report.when == "call":
        # 获取用例call执行结果为失败的情况
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败截图"):
                # 使用Allure自带的添加附件的方法，三个参数分别为：源文件、文件名、文件类型
                allure.attach(driver.get_screenshot_as_png(),
                              "失败截图", allure.attachment_type.PNG)
