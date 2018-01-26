#!/usr/bin/env python
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
b = webdriver.Firefox()
b.get('https://web.whatsapp.com')
input()
elem = b.find_element_by_xpath('//span[contains(text(),"")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
while True:
	elem1[1].send_keys('  ')
	b.find_element_by_class_name('compose-btn-send').click()

