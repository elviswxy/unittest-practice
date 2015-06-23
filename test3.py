from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BrowserObj_dirver = webdriver.Firefox()

BrowserObj_dirver.get("http://yutong91.github.io")

#BrowserObj_dirver.implicitly_wait(10)

BrowserObj_dirver.execute_script("p = document.getElementById('gotop');" + "p.focus();")
BrowserObj_dirver.implicitly_wait(10)
BrowserObj_dirver.close()
