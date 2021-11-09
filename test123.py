# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:22:18 2020

@author: itssh
"""
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
#C:\Users\itssh\Downloads\chromedriver_win32.zip
#PATH="C:\\Users\\itssh\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome('C:\\Program Files\\chromedriver')

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Di"'

# Replace the below string with your own message 
string ="hi!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
for i in range(100): 
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(1) 
