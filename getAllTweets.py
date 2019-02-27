from selenium import webdriver
browser = webdriver.Firefox(executable_path = '/home/fako/geckodriver')


browser.get("https://www.twitter.com/")
time.sleep(2)

login = browser.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[1]/a')
login.click()
time.sleep(2)



browser.close()