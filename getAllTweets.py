from selenium import webdriver
browser = webdriver.Firefox(executable_path = '/home/fako/geckodriver')


browser.get("https://www.twitter.com/")
time.sleep(2)

login = browser.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[1]/a')
login.click()
time.sleep(2)

username = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
password = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

#Enter username instead of #
username.send_keys("#")
#Enter password instead of #
password.send_keys("#")

loginButton = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
loginButton.click()

searchArea = browser.find_element_by_xpath('//*[@id="search-query"]')
searchButton = browser.find_element_by_xpath('//*[@id="global-nav-search"]/span/button')

#enter hashtag insted of # you want to search
searchArea.send_keys("#")
searchButton.click()





browser.close()