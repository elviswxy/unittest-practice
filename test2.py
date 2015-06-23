from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BrowserObj_dirver = webdriver.Firefox()

BrowserObj_dirver.get("http://www.google.com")

BrowserObj_dirver.implicitly_wait(10)

EditObj_element = BrowserObj_dirver.find_element_by_name('q')


EditObj_element.send_keys("Hello WebDriver!")
EditObj_element.send_keys(Keys.RETURN)

print BrowserObj_dirver.title

BrowserObj_dirver.close()
