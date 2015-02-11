from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://verify-email.org/")
#assert "Python" in driver.title
elem = driver.find_element_by_name("check")
elem.send_keys("rejeeshchandran037@gmail.com")
elem.send_keys(Keys.RETURN)
time.sleep(10)
print(driver.page_source)
pagesource = driver.page_source
if "The email account that you tried to reach does not exist" in pagesource:
    print("email doesnot exist")
else:
    print("email exists")
driver.close()
