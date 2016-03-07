#!/usr/bin/python

import sys
import os
import urllib
import requests
from bs4 import BeautifulSoup
import pickle


index_num = str(4034)
r = requests.get("https://interfacelift.com/wallpaper/downloads/date/any")
ifl = r.text

soup = BeautifulSoup(ifl, "html.parser")
list_num = "list_" + index_num
div_element = soup.find("div", {"id": list_num})
div_content = div_element.contents

##if element == None:
	# print("Your images are up to date. Try again when a new image might be uploaded.")
	# exit()
##else:




print(div_content)