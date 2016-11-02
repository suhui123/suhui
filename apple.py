from selenium import webdriver

#打开浏览器
def open_browser(driver,url):
	return driver.get(url)
#退出浏览器
def close_browser(driver):
	return driver.quit()
#最大化浏览器
def max_browser(driver):
	return driver.maximize_window()


#xpath定位
def by_xpath(driver,xpath):
	return driver.find_element_by_xpath(xpath)
#xpath定位后并点击
def by_xpath_click(driver,xpath):
	return driver.find_element_by_xpath(xpath).click()
#xpath定位后清除内容
def by_xpath_clear(driver,xpath):
	return driver.find_element_by_xpath(xpath).clear()
#xpath定位输入框、清除里面内容，后并输入
def by_xpath_input(driver,xpath,shuru):
	return driver.find_element_by_xpath(xpath).send_keys(shuru)

