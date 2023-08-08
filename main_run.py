#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : main_run.py
# @Author  : mykaneki

import os
import pytest


def run_tests(file_name=None, marker=None, parallel=None, reruns=None):
    """
    使用allure运行pytest测试。

    参数:
    file_name: str, 可选。要运行的测试文件的名称。如果为None，运行所有测试。
    marker: str, 可选。要运行的测试的标记。如果为None，运行所有测试。
    parallel: int, 可选。用于并行测试的CPU核心数量。如果为None，顺序运行测试。
    reruns: int, 可选。失败测试重跑的次数。如果为None，不重跑失败的测试。
    """

    # 开始基本的命令
    cmd = ['-v', '--alluredir=./result', '--clean-alluredir']

    # 如果指定了文件名，添加文件名
    if file_name is not None:
        cmd.append(file_name)

    # 如果指定了标记，添加标记
    if marker is not None:
        cmd.append('-m')
        cmd.append(marker)

    # 如果指定了并行选项，添加并行选项
    if parallel is not None:
        cmd.append('-n')
        cmd.append(str(parallel))

    # 如果指定了重跑选项，添加重跑选项
    if reruns is not None:
        cmd.append('--reruns')
        cmd.append(str(reruns))

    # 运行测试
    pytest.main(cmd)


def generate_report():
    """
    从测试结果生成allure报告。
    """
    os.system('allure generate ./result/ -o ./report_allure/ --clean')


def run_all():
    """
    运行测试并生成报告。
    """
    run_tests()
    generate_report()


def serve_report():
    """
    作为web服务启动Allure报告。
    """
    os.system('allure serve ./result/')


if __name__ == '__main__':
    """
    运行测试，生成报告，并启动报告服务。
    """
    file_name = None
    run_tests(file_name=file_name, marker=None, parallel=None, reruns=None)
    generate_report()
    serve_report()
