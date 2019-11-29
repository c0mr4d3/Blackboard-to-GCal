# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 03:07:21 2019

@author : Siddharth
"""

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
def blackboardlogin():
    options = Options()
    options.add_experimental_option("prefs", {
  "download.default_directory": os.getcwd(),
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
      })
    browser = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    blackboard_link = 'http://learn.bu.edu'
    browser.get(blackboard_link)
    username = browser.find_element_by_id("j_username")
    password = browser.find_element_by_id("j_password")
    
    with open("secret.txt",'r') as file:
        for dets in file:
            uname,passw = dets.split(':')
#            print(uname)
#            print(passw)
    username.send_keys(uname)
    password.send_keys(passw)
    browser.find_element_by_name("_eventId_proceed").click()
    #click on the agree t&c button
    time.sleep(3)
    browser.find_element_by_id('agree_button').click()
#    browser.find_element_by_class("button-1").click()
    #Click on calendar button
    browser.find_element_by_link_text("Calendar").click()
    #Get icalendar link
    time.sleep(3)
    browser.find_element_by_id('ical').click()
    time.sleep(3)
    icalurl = browser.find_element_by_id('icalurlid').text
    browser.get(icalurl)    
