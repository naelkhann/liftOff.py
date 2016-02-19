#!/usr/bin/python

#LiftOff - Pull newest images from interfacelift.com and downlod them into my personal Wallpaper folder

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, os


driver = webdriver.Firefox()
driver.get("http://interfacelift.com/wallpaper/downloads/date/any")
assert "InterfaceLIFT" in driver.title, "InterfaceLIFT title doesn't match"

i = 4012
x = 6
dropdown_click = driver.find_element_by_name('resolution').click()
resolution = driver.find_element_by_xpath("//select/optgroup[@label='Widescreen 16:10']/option[@id='res_1680x1050_1']")

resolution.click()
resolution.click()


# driver.implicitly_wait(1)

# pull_url = driver.current_url

# pull = requests.get(pull_url)

# imageFile = open(os.path.join('intfl', os.path.basename(pull_url)), 'wb')
# for each in pull.iter_content(100000):
# 	imageFile.write(each)
# imageFile.close()

# driver.close()






