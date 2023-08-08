#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : WebKeys.py
# @Author  : mykaneki
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class WebKeys:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        # 等待网页加载完成
        self.wait.until(ec.url_contains(url))

    # 显示定位的地方，方便确认定位位置
    def locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid red;"  # 边框，green绿色
        )

    def locator(self, locator):
        """

        :param locator: 元组类型，如(By.ID,"kw")
        :return: 返回元素
        """
        el = self.driver.find_element(*locator)
        self.locator_station(el)
        return el

    def locator_with_wait(self, locator, wait_type=None):
        """

        :param locator: 元组类型，如(By.ID,"kw")
        :param wait_type: 等待类型，如：presence_of_element_located（默认）
        :return: 返回元素
        """
        el = None
        if wait_type is None:
            el = self.wait.until(ec.presence_of_element_located(locator))
        else:
            el = eval("self.wait.until(ec." + wait_type + "(locator))")
        self.locator_station(el)
        return el

    def text_wait(self, locator, text):
        """
        等待文本出现
        :param locator:  元组类型，如(By.ID,"kw")
        :param text:  文本
        :return:  返回布尔值
        """
        return self.wait.until(ec.text_to_be_present_in_element(locator, text))

    def change_windows(self, index):
        """
        切换窗口
        :param index: 窗口索引
        :return: 无
        """
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def send_keys_and_enter(self, locator, text):
        """
        输入文本
        :param locator: 元组类型，如(By.ID,"kw")
        :param text: 文本
        :return: 无
        """
        self.locator(locator).send_keys(text + Keys.ENTER)

    def select(self, locator, index=None, value=None, text=None):
        """
        根据索引、value、文本选择列表元素
        :param locator:  元组类型，如(By.ID,"kw")
        :param index:   索引
        :param value:  value值
        :param text:  文本
        :return: None
        """
        if index is not None:
            Select(self.locator(locator)).select_by_index(index)
        elif value is not None:
            Select(self.locator(locator)).select_by_value(value)
        elif text is not None:
            Select(self.locator(locator)).select_by_visible_text(text)
        else:
            print("参数错误")
