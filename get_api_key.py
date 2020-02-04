#
# Copyright © 2019 Maestro Creativescape
#
# SPDX-License-Identifier: GPL-3.0
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
import re
from os import remove
from os import environ
from dotenv import load_dotenv

load_dotenv("config.env")

# Run Chrome Headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)

# Grab the current window
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle


driver.get("http://api.xda-developers.com/explorer/")
que=driver.find_element_by_id('login_btn')
que.click()

# Swap to signin window
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)


username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_id("signin-submit")
username.send_keys(environ.get("XDA_USERNAME"))
password.send_keys(environ.get("XDA_PASSWORD"))
submit.click()
driver.implicitly_wait(3)
confirm_btn = driver.find_element_by_id("authorize")
confirm_btn.click()

# Come back to main window
driver.switch_to.window(main_window_handle)
driver.implicitly_wait(3)

#Scrape out the API Key
page = driver.page_source
f = open("page_sauce.txt", "w")
f.write(page)
f.close()

for line in open("page_sauce.txt", 'r'):
    if re.search("Access token:", line):
        token_line = line
        break

remove("page_sauce.txt")
token = token_line.split(" ")[5]
token = token[:40]
environ["XDA_API_TOKEN"] = str(token)

# close the browser window
driver.quit()
