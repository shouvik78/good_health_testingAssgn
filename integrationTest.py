from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome("C:\\Users\\Shouvik\\Desktop\\webdriver\\chromedriver.exe")
    return driver

browser =  get_browser()

browser.get("C:\\Users\\Shouvik\\Desktop\\Register page\\index.html")

username = browser.find_element_by_id("username")
email = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
number = browser.find_element_by_id("number")

username.send_keys("Shouvik Ghosh")                                       
email.send_keys("shouvikghosh206@gmail.com")
password.send_keys("Atapur2020")
number.send_keys("7541064484")

time.sleep(4)

browser.find_element_by_xpath("//button").click()
time.sleep(4)

if 'invalid details' in browser.page_source:
    print('Testing Fail')
else:
    print('Testing Pass')    

browser.close()

