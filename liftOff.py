#!/usr/bin/python

#LiftOff - Pull newest images from interfacelift.com and download them into my personal Wallpaper folder

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys, os, urllib

if len(sys.argv) > 1:
	i = sys.argv[1]
else:
	i = 4039

index_num = str(i)
driver = webdriver.Firefox()
driver.get("http://interfacelift.com/wallpaper/downloads/date/any")
assert "InterfaceLIFT" in driver.title, "InterfaceLIFT title doesn't match"

try:
	dropdown_click = driver.find_element_by_name('resolution').click()
	resolution = driver.find_element_by_xpath("//select/optgroup[@label='Widescreen 16:10']/option[@id='res_1440x900_1']").click()

	item_to_dl = "//div[@id='download_" + index_num + "']/a"
	download = driver.find_element_by_xpath(item_to_dl)

	download.click()

	download.click()

	pull_url = driver.current_url
	#file_url_from_pull = pull_url[44:]

	file_name = index_num + ".jpg"
	urllib.urlretrieve(pull_url, file_name)
	driver.close()
	
except NoSuchElementException:
	print "Could not find", index_num, "on site. Might be too soon, check back when new file is uploaded"
	driver.close()
	exit()








