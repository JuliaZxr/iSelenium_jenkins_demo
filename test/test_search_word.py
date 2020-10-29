#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSearch:

    def setup(self):
        # 实例化driver
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        # 设置隐式等待，使用后无需在方法中每句代码后再去添加sleep()方法；而是自行每步等待5s，使之可以有时间找到元素继续测试，避免网速慢等原因导致元素未被加载，从而导致用例执行失败
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 回收driver
        self.driver.quit()


    def test_webui_1(self):
        """ 测试用例1，验证'今日头条'关键词在百度上的搜索结果
        """

        self._test_baidu('今日头条', 'test_webui_1')

    def test_webui_2(self):
        """ 测试用例2， 验证'王者荣耀'关键词在百度上的搜索结果
        """

        self._test_baidu('王者荣耀', 'test_webui_2')

    def _test_baidu(self, search_keyword, testcase_name):
        """ 测试百度搜索子函数

        :param search_keyword: 搜索关键词 (str)
        :param testcase_name: 测试用例名 (str)
        """

        self.driver.get("https://ww.baidu.com")
        # print('打开浏览器，访问 www.baidu.com')
        # time.sleep(5)
        # assert f'百度一下' in self.driver.title

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        print(f'搜索关键词~{search_keyword}')
        time.sleep(5)
        assert f'{search_keyword}' in self.driver.title
        # self.assertTrue(f'{search_keyword}' in self.driver.title, msg=f'{testcase_name}校验点 pass')