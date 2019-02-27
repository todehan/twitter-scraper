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

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
tweets = []

elements = browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")

for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1
                   





browser.close()