#!/usr/bin/python

#LiftOff - Pull newest images from interfacelift.com and downlod them into my personal Wallpaper folder

import webbrowser, bs4, requests, sys

soup = bs4.BeautifulSoup()