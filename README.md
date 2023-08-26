# WebAuto
Web自动化框架

## 架构



## 环境搭建

1. java > 8

2. selenium

3. webdriver_manager [webdriver-manager · PyPI](https://pypi.org/project/webdriver-manager/)

4. pytest

5. allure

   https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.23.1/allure-commandline-2.23.1.zip

   配置Allure到环境变量，到path里面，E:\\<ALLURE_PATH>\bin

   验证： `allure --version`

6. allure-pytest

   allure测试报告是基于pytest运行的，运行之后生成一个json报告数据源，来实现结果

   的展示，以一个工程的形态展示本次测试的所有测试结果

   需要集成pytest实现allure的展示，需要安装：`pip install allure-pytest`





## 框架搭建过程笔记

### 报告层

#### Allure用例描述

| @allure.epic()            | epic描述           | 敏捷里面的概念，对用例或用例集进行描述分类 |
| ------------------------- | ------------------ | ------------------------------------------ |
| @allure.feature()         | 模块名称           | 与epic类似，只是比epic级别低               |
| @allure.story()           | 用户故事           | 与epic类似，只是比feature级别低            |
| @allure.title(用例的标题) | 用例的标题         | 重命名html报告的用例名称                   |
| @allure.testcase()        | 测试用例的链接地址 | 与link类似                                 |
| @allure.issue()           | 缺陷               | 与link类似                                 |
| @allure.description()     | 用例描述           | 进行测试用例的描述                         |
| @allure.step()            | 操作步骤           | 进行测试用例的步骤                         |
| @allure.severity()        | 用例等级           | blocker，critical，normal，minor，trivial  |
| @allure.link()            | 链接               | 定义一个链接，在测试报告展现（推荐使用）   |

#### 启动命令 （可以根据用例描述筛选需要运行的命令）

> Pycharm也需要重启，否则可能系统变量没更新，导致找不到命令

1. `pytest.main(['-v', '--alluredir','./result','--clean-alluredir'])`

   - `-v`: 运行测试时输出详细信息。
   - `--alluredir`: 指定Allure结果文件的生成目录。在这个例子中，结果文件会被生成在当前目录的`result`子目录中。
   - `--clean-alluredir`: 在生成新的结果文件之前清除旧的结果文件。

2. `os.system('allure generate ./result/ -o ./report_allure/ --clean')`

   使用Allure命令行工具将结果文件转换为**HTML报告**：

   - `./result/`: 指定结果文件的位置。这应该和上面`pytest.main`函数中的`--alluredir`选项相匹配。
   - `-o ./report_allure/`: 指定HTML报告的生成目录
   - `--clean`: 在生成新的HTML报告之前清除旧的HTML报告。

3. `allure serve ./result/` 

   作为web服务启动Allure报告。

Allure报告添加失败截图

使用pytest_runtest_makereport钩子函数实现allure报告添加用例失败截图

```python
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

```

### 封装层

#### 关键字封装（目录KeyWord）

1. 打开浏览器
2. 元素定位
3. 显性等待
4. 发送文本并回车
5. 切换窗口
6. 切换标签
7. 热键



### BUG

**NameError: name 'driver' is not defined** 

在截图的时候报错

解决：browser 设置 autouse=True
