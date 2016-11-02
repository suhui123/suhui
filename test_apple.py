from selenium import webdriver
import apple
import time

browser = webdriver.Firefox()
#打开浏览器并输入网址
apple.open_browser(browser,"http://www.baidu.com")
#最大化浏览器
apple.max_browser(browser)
#清除输入框内容
apple.by_xpath_clear(browser,"//input[@id='kw']")
#输入selenium
apple.by_xpath_input(browser,"//input[@id='kw']","selenium")
#点击搜索那妞
apple.by_xpath_click(browser,"//input[@id='su']")

time.sleep(2)
#退出浏览器
apple.close_browser(browser)