from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

EMAIL = 'suleyman.eminov22@gmail.com'
PASSWORD = '7U4KM3n!'
"""
set up chromedriver path and webdriver 
"""
chromedriver_path = 'C:\Program Files (x86)/chromedriver.exe'
webdriver = webdriver.Chrome(chromedriver_path)

# now we can start navigating

# login to the tinder account
webdriver.get("http://www.tinder.com")

sleep(2)  # to not brake the program

login_button = webdriver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')

login_button.click()

sleep(2)

FB_login = webdriver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
FB_login.click()

sleep(2)
# Switch to FB login window
base_window = webdriver.window_handles[0]
fb_login_window = webdriver.window_handles[1]
webdriver.switch_to.window(fb_login_window)
print(webdriver.title)

# Login and hit enter
email_input = webdriver.find_element_by_xpath('//*[@id="email"]')
password_input = webdriver.find_element_by_xpath('//*[@id="pass"]')
email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

# Switch back to Tinder window

webdriver.switch_to.window(base_window)
print(webdriver.title)

sleep(10)

allow_location = webdriver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

sleep(3)
notifications = webdriver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[2]')
notifications.click()


sleep(3)
cookies = webdriver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# hit like till there is an exception
# takes 5 minutes to hit 100 likes 
for n in range(100):
    
    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = webdriver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = webdriver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)





raise Exception("stop")