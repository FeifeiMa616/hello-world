# -*- coding: utf-8 -*-
# @Time    : 2025/9/25 10:18
# @Author  : FayeMa
# @File    : helloWorld.py
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Baidu:
    driver=webdriver.Chrome()

    def helloworld(self):
        self.driver.get("https://www.baidu.com/")
        time.sleep(1)
        input_text=self.driver.find_element(By.ID,'chat-textarea')
        input_text.send_keys('Hello World')
        sleep(10)





if __name__=='__main__':
    Baidu().helloworld()