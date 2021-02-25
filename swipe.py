from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from security import security

"""
    @author: Suleyman Eminov
    @date: 2/20/2021
    Description: This script swipes 100 people right on Tinder
    This program runs in 5 minutes 22 seconds overall

"""

data = security()

EMAIL = data.get_email()
PASSWORD = data.get_password()


#set up chromedriver path and webdriver 

chromedriver_path = 'C:\Program Files (x86)/chromedriver.exe' #change this to your local computer's chromdriver path
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

allow_location = webdriver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') #Change modal-manager (Inspect button, copy and paste the xPath)
allow_location.click()

sleep(3)
notifications = webdriver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]') #Change modal-manager (Inspect button, copy and paste the xPath)
notifications.click()


sleep(3)
cookies = webdriver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button') #change "content" ^^
cookies.click()

# hit like till there is an exception
# takes 5 minutes to hit 100 likes 
for n in range(100):
    
    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = webdriver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button') # change "content"
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = webdriver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)


raise Exception("stop") # to not close the tab