from selenium import webdriver

import time

browser = webdriver.Firefox()
browser.get("https://www.twitter.com/")
time.sleep(2)

login = browser.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[1]/a')
login.click()
time.sleep(2)



browser.close()