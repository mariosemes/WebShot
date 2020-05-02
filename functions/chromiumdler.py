from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import etree
import re
import os
from os import path
import wget
import zipfile

def chromium_downloader():
    url = "https://chromedriver.chromium.org/"

    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)

    stable_release = tree.xpath("//*[@id='sites-canvas-main-content']/table/tbody/tr/td/div/div[4]/ul/li[1]/a/text()")
    print("ChromeDriver version: " + stable_release[0].replace("ChromeDriver ", ""))
    stable_release = stable_release[0].replace("ChromeDriver ", "")
    final_url = f"https://chromedriver.storage.googleapis.com/{stable_release}/chromedriver_win32.zip"
    print("ChromeDriver URL: " + final_url)

    if wget.download(final_url):
        with zipfile.ZipFile("chromedriver_win32.zip", 'r') as zip_ref:
            zip_ref.extractall()
    else:
        print("Somethings wrong downloading file")

    if path.exists("chromedriver.exe"):
        os.remove("chromedriver_win32.zip")
        print("chromedriver_win32.zip Removed!")
    else:
        print("Somethings wrong with deleting")
