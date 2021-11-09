# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:22:17 2020

@author: itssh
"""
from selenium import webdriver
driver=webdriver.Chrome('C:\\Program Files\\chromedriver')
driver.get('http:\\youtube.com')
searchbox = driver.find_element_by_xpath('/html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[3]/div[2]/ytd-searchbox[1]/form[1]/div[1]/div[1]/input[1]')
searchbox.send_keys('Raashifal')
searchbutton = driver.find_element_by_xpath('/html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[3]/div[2]/ytd-searchbox[1]/form[1]/button[1]')
searchbutton.click()