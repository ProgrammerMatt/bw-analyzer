from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import time
import os

def run2v2Crawler(players=None, maps=["투혼+1.3"]):
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory":os.path.abspath("./DownloadedReplays")}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)
    

    driver.get("https://repmastered.app/login")
    driver.find_element('id', 'email').send_keys("mattwilfert93@gmail.com")
    driver.find_element('id', 'entryCode').send_keys("b781e397d6758528")
    driver.find_element('name', 'submitEntryCode').click()
    url = 'https://repmastered.app/?format=2v2'
    if players:
        url = url + "&players="+','.join(players)
    # driver.get(url)
    # time.sleep(10) 
    elems = driver.find_elements("xpath","//a[@href]")
    for map in maps:
        for i in range(1, 5):
            driver.get(f"{url}&map={map}&page={i}")
            time.sleep(5) 
            elems = driver.find_elements("xpath","//a[@href]")
            for elem in elems:
                if "Get" in elem.text:
                    elem.click()
                    time.sleep(3)

    driver.close()

def cleanupRedundantFiles():
    for filename in os.listdir('./DownloadedReplays'):
        path = "./DownloadedReplays/" + filename
        if filename.endswith('(1).rep'):
            os.remove(path)

if __name__=="__main__":
    run2v2Crawler()
    cleanupRedundantFiles()