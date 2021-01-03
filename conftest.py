# -*-coding:utf-8 -*-
# File : conftest.py
# @Time : 2020/12/25 18:47
# @Author : Sf
# version : python 3.7.8
import pytest
from selenium import webdriver
from py._xmlgen import html

_driver = None


# 测试失败时添加截图和测试用例描述(用例的注释信息)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop(2)
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop()  #删除最后links列的表头内容


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop(2)
    cells.insert(2, html.td(report.nodeid))
    cells.pop()  #删除最后links列的内容


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()


# 这里我设置的级别是模块级别，也就是每个测试文件运行一次
# 可以设置为session，全部用例执行一次，但是针对126邮箱的话
# 登录次数太多会叫你验证，如果验证就没法执行用例了，我没有对验证处理（处理比较复杂）
@pytest.fixture(scope='module')
def driver():
    global _driver
    print('------------open browser------------')
    # _driver = webdriver.Firefox()
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Dpapp\Chrome\ChromePortable\ChromePortable.exe"
    chromedriver = "D:\dev_env\driver\chromedriver.exe"
    _driver = webdriver.Chrome(chromedriver, options=options)
    _driver.maximize_window()
    yield _driver
    print('------------close browser------------')
    _driver.quit()