# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:53:20 2020

@author: itssh
"""
from selenium import webdriver
import time
driver=webdriver.Chrome('C:\\Program Files\\chromedriver')
driver.get('http:\\instagram.com')
time.sleep(2)
searchbox = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]')

searchbox.send_keys('theripped_soul')
password = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/label[1]/input[1]')

password.send_keys('07081999')
searchbutton = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]')
searchbutton.click()
time.sleep(2)
notnow = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/button[1]')
notnow.click()
noti= driver.find_element_by_xpath('')
time.sleep(2)
search = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[2]/input[1]')
search.send_keys('')
