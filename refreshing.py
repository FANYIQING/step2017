# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:02:08 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:10:22 2017

@author: Administrator
"""

from selenium import webdriver
import hazwordz as hw
import time

highest = 0
c_Seed = 0
c_Started = 0
h_Seed = 0
h_Started = 0
dic_in_order = hw.ini()
executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"   
driver = webdriver.Chrome(executable_path)
for _ in xrange(1000):
    
    driver.get(r'https://icanhazwordz.appspot.com/')
    total = 0
    c_Seed = driver.find_element_by_xpath("//input[@name='Seed' and @type='hidden']").get_attribute("value")
    c_Started = driver.find_element_by_xpath("//input[@name='Started' and @type='hidden']").get_attribute("value")
    for _ in xrange(10):
        table = driver.find_element_by_xpath('/html/body/table/tbody/tr/td').text
        table = table.replace('\n', '').encode('ascii')
        letters = list(table.lower())
        result, score = hw.run(letters, dic_in_order)
        if score == 0:
            driver.find_element_by_xpath("//input[@value='Submit' and @type='submit']").click()
            continue
        total += score
        driver.find_element_by_id('MoveField').send_keys(result)
        driver.find_element_by_xpath("//input[@value='PASS' and @type='submit']").click()
    if total > highest:
        highest = total        
        h_Seed = c_Seed
        h_Started = c_Started     
        
    print highest    
    print h_Seed
    print h_Started
    
    
